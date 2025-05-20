<?php
$host = "localhost";
$user = "root";
$pass = "1234";
$db = "cadastro";
 
// Conexão
$conn = new mysqli($host, $user, $pass, $db);
 
// Verifica conexão
if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}
 
// Recebe dados
$nome = $_POST['nome'];
$email = $_POST['email'];
$senha = password_hash($_POST['senha'], PASSWORD_DEFAULT);//Deixar senha criptografada
 
// Prepara e executa
$sql = "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("sss", $nome, $email, $senha);
 
if ($stmt->execute()) {
    echo "Usuário cadastrado com sucesso!";
} else {
    echo "Erro: " . $stmt->error;
}
 
$conn->close();
?>