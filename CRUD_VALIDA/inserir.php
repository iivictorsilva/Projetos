<?

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "dados_pessoas";



$conn = new mysqli($servername, $username, $password, $dbname);


if($conn->connect_error){
    die("Conexão falhou: " . $conn->$connect_error);
}


$nome = $_POST['nome'];
$telefone = $_POST['telefone'];
$email = $_POST['email'];
$senha = $_POST['senha'];


$sql = "INSERT INTO pessoas (nome, telefone, email, senha) VALUES ('$nome', '$telefone', '$email', '$senha')";


if($conn->query($sql) === TRUE){
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cadastro realizado com sucesso</title>
        <style>
        
        body{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #003366;
            color: white;
            font-family: Arial, sans-serif;
        }

        button{
            background-color: white;
            color: #003366;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top:20px ;
        }

        button:hover{
            background-color: #003366;
            color: white;
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
    <?
}else{
    echo "Erro ao inserir os dados" . $conn->error;
}

$conn->close();

?>