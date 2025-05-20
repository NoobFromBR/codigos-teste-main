<?php
// Comentário de uma linha com duas formas
# Comentário de uma linha também

# Criação de variáveis
$nome = "NoobFromBr";
$idade = 33;
$cpf = "111.222.333-44";

# Exibição das variáveis
echo "Nome: " . $nome . "<br>";
echo "Idade: " . $idade . "<br>";
echo "CPF: " . $cpf . "<br>";

# Estrutura de controle com exemplo real
if ($idade >= 33) {
    echo "Você tem mais que 33 anos.<br>";
} else {
    echo "Você tem menos que 33 anos.<br>";
}
echo "<hr>";

# Estrutura de repetição
for ($i = 0; $i < $idade; $i++) {
    echo "<p>O valor de i é $i</p>";
}
?>

