<?php

$servername = "localhost";

$username = "root";

$password = "";

$dbname = "cadastros";


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Falha na conexão" . $conn->connect_error);
}


$nome = $_POST["nome"];
$email = $_POST["email"];
$senha = $_POST["senha"];


$sql = "INSERT INTO pessoas (nome, email, senha) VALUES ('$nome', '$email', '$senha')";



if($conn->query($sql) === TRUE){
    ?>
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cadastro realizado com sucesso</title>
        <style>
            /* Estilo para o corpo da página */
            body {
                display: flex;             /* Flexbox para centralizar o conteúdo */
                justify-content: center;   /* Centraliza horizontalmente */
                align-items: center;       /* Centraliza verticalmente */
                height: 100vh;            /* Altura da viewport */
                background-color: #003366; /* Fundo azul escuro */
                color: white;              /* Texto branco */
                font-family: Arial, sans-serif; /* Fonte simples */
            }

            /* Estilo para o botão de voltar */
            button {
                background-color: white;   /* Fundo branco para o botão */
                color: #003366;            /* Texto azul escuro */
                padding: 10px 20px;       /* Espaçamento interno */
                border: none;              /* Remove a borda padrão */
                border-radius: 4px;       /* Bordas levemente arredondadas */
                cursor: pointer;           /* Muda o cursor ao passar sobre o botão */
                margin-top: 20px;         /* Espaçamento acima do botão */
            }

            /* Efeito hover no botão */
            button:hover {
                background-color: #003366; /* Fundo azul escuro ao passar o mouse */
                color: white;               /* Texto branco ao passar o mouse */
            }
        </style>
    </head>
    <body>
        <div>
            <h2>Cadastro realizado com sucesso!</h2>
            <button onclick="window.location.href='index.html'">Voltar ao Cadastro</button>
        </div>
    </body>
    </html>
   
    <?php
} else {
    echo "Erro ao inserir os dados: " . $conn->error;
}

// Fecha a conexão com o banco de dados
$conn->close();
?>