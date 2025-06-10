import pandas as pd

def transformar_para_horizontal(caminho_arquivo_excel, nome_aba=0):
    # Lê a planilha
    df = pd.read_excel(caminho_arquivo_excel, sheet_name=nome_aba, header=None)

    # Inicializa os dados finais
    dados_formatados = {}

    # Identifica onde estão os blocos e reorganiza os dados
    for i in range(len(df)):
        linha = df.iloc[i]
        if linha.str.contains("MEDIÇÕES", case=False, na=False).any():
            colunas = linha.dropna().tolist()
            atual_categoria = ""
            for j in range(i+1, i+5):  # supõe até 4 linhas abaixo do título
                if j >= len(df): break
                tipo_linha = df.iloc[j].dropna()
                if len(tipo_linha) == 0: continue
                atual_categoria = tipo_linha.iloc[0]
                valores = tipo_linha.iloc[1:].tolist()
                if atual_categoria not in dados_formatados:
                    dados_formatados[atual_categoria] = []
                dados_formatados[atual_categoria].extend(valores)

    # Converte para DataFrame
    df_final = pd.DataFrame.from_dict(dados_formatados, orient='index')
    df_final.columns = [f"{i+1}ª MP" for i in range(df_final.shape[1])]

    return df_final

# Uso:
caminho = "seuarquivo.xlsx"  # substitua pelo seu caminho
df_horizontal = transformar_para_horizontal(caminho)

# Salvar em novo Excel
df_horizontal.to_excel("tabela_horizontal.xlsx")
