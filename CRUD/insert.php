<?
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "dados_usuarios";


$conn = new mysqli($servername, $username, $password, $dbname);

if($conn->connect_error){
    die("Conexão Falhou: " . $conn->connect_error);
}

if($_SERVER["REQUEST_METHOD"] == "POST"){
    $nome = $_POST['name'];
    $email = $_POST['email'];
    $senha = $_POST['password'];

    $stmt = $conn->prepare("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $nome, $email, $senha);

    if($stmt->execute()){
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

    $stmt->close();
    $conn->close();
    
}else{
    echo "Método não suportado.";
}
?>