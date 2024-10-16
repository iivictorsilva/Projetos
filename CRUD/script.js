// Obtém o formulário pelo ID
const form = document.getElementById('registrationForm');
// Obtém o elemento onde a mensagem será exibida
const message = document.getElementById('message');

// Adiciona um evento ao formulário para tratar o envio
form.addEventListener('submit', function(event) {
    // Impede o envio padrão do formulário
    event.preventDefault();

    // Obtém os valores dos campos
    const name = document.querySelector('input[name="name"]').value;
    const email = document.querySelector('input[name="email"]').value;
    const password = document.querySelector('input[name="password"]').value;

    // Valida se os campos não estão vazios
    if (name.trim() === '' || email.trim() === '' || password.trim() === '') {
        message.textContent = 'Todos os campos são obrigatórios.'; // Exibe mensagem de erro
        return; // Interrompe a execução se houver erro
    }

    // Valida o formato do email
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; // Regex para validar email
    if (!email.match(emailPattern)) {
        message.textContent = 'Por favor, insira um email válido.'; // Exibe mensagem de erro
        return; // Interrompe a execução se houver erro
    }

    // Valida a senha (mínimo de 6 caracteres)
    if (password.length < 6) {
        message.textContent = 'A senha deve ter pelo menos 6 caracteres.'; // Exibe mensagem de erro
        return; // Interrompe a execução se houver erro
    }

    // Se todas as validações passarem, o formulário é enviado
    form.submit(); // Envia o formulário
});