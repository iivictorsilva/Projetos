<?php
$servername = "localhost";
$username = "root"; // Altere para o seu usuário do MySQL
$password = ""; // Altere para a sua senha do MySQL
$dbname = "sistema_login";

// Cria a conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica a conexão
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Recebe os dados do formulário
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Prepara e executa a consulta
    $stmt = $conn->prepare("SELECT password FROM usuarios WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        $stmt->bind_result($hashed_password);
        $stmt->fetch();

        // Verifica a senha
        if (password_verify($password, $hashed_password)) {
            echo "Login realizado com sucesso!";
            // Aqui você pode iniciar a sessão do usuário ou redirecioná-lo
        } else {
            echo "Senha incorreta!";
        }
    } else {
        echo "Usuário não encontrado!";
    }

    $stmt->close();
}
$conn->close();
?>