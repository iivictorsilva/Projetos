<?php
// Configurações do banco de dados
$servername = "localhost"; // Normalmente 'localhost'
$username = "root";  // Substitua pelo seu usuário do banco
$password = 'P@$$w0rd';     // Substitua pela sua senha do banco
$dbname = "dados_usuarios";   // Nome do banco de dados

// Cria conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica a conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// Verifica se o método de requisição é POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtém os dados do formulário
    $nome = $_POST['name'];
    $email = $_POST['email'];
    $senha = $_POST['password'];

    // Prepara e executa a inserção
    $stmt = $conn->prepare("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $nome, $email, $senha); // 'sss' indica que os parâmetros são strings

    if ($stmt->execute()) {
        // Exibe a mensagem personalizada com fundo azul-marinho e letra branca
        echo '
        <html>
        <head>
            <style>
                body {
                    background-color: #1f3a93; /* Azul marinho */
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .message {
                    text-align: center;
                    padding: 20px;
                    border-radius: 10px;
                    background-color: #34495e; /* Cor de destaque */
                }
                .message h1 {
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>
            <div class="message">
                <h1>Cadastro realizado com sucesso!</h1>
                <p>Você será redirecionado em instantes...</p>
            </div>
        </body>
        </html>
        ';

        // Redireciona para a página index.html após 5 segundos
        header("refresh:5;url=index.html");
    } else {
        echo "Erro: " . $stmt->error;
    }

    // Fecha a declaração e a conexão
    $stmt->close();
    $conn->close();
} else {
    echo "Método não suportado.";
}
?>