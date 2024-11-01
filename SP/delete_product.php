<?php
// Conectar ao banco de dados
$mysqli = new mysqli("localhost", "root", "", "produtos");

// Verificar conexão
if ($mysqli->connect_error) {
    die("Falha na conexão: " . $mysqli->connect_error);
}



$id = $_GET['id'];


$stmt = $mysqli->prepare ("DELETE FROM produtos WHERE id = ?");


$stmt->bind_param("i", $id);


if($stmt->execute()){
    echo "Produto excluído com sucesso!";
}else{
    echo "Erro: " . $stmt->error;
}