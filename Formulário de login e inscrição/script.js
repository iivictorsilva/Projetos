const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});



// Seleciona o formulário e adiciona um evento para quando o botão de enviar for clicado
document.querySelector('form').addEventListener('submit', function(event) {
    // Seleciona os campos do formulário
    var nome = document.getElementById('nome').value;
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;

    // Verifica se todos os campos estão preenchidos
    if (nome === ''  || email === '' || senha === '') {
        alert('Por favor, preencha todos os campos.'); // Exibe um alerta se houver campos vazios
        event.preventDefault(); // Evita o envio do formulário até que os campos sejam preenchidos
    } else {
        form.reset();
    }
});