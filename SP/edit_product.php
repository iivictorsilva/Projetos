<?php
// Conectar ao banco de dados
$mysqli = new mysqli("localhost", "root", "", "produtos");

// Verificar conexão
if ($mysqli->connect_error) {
    die("Falha na conexão: " . $mysqli->connect_error);
}

// Receber os dados do formulário e o ID do produto
$id = $_GET['id'];
$name = $_POST['name'];
$price = $_POST['price'];
$description = $_POST['description'];

// Atualizar o produto no banco de dados
$stmt = $mysqli->prepare("UPDATE produtos SET nome = ?, price = ?, description = ? WHERE id = ?");
$stmt->bind_param("sdsi", $name, $price, $description, $id);

if ($stmt->execute()) {
    echo "Produto atualizado com sucesso!";
} else {
    echo "Erro: " . $stmt->error;
}

// Redirecionar para a página principal
header("Location: index.html");
?>