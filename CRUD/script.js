const form = document.getElementById('registrationForm');

const message = document.getElementById('message');



form.addEventListener('subtmit', (event) => {
    event.preventDefault();

    const name = document.querySelector('input [name="name"]').value;
    const email = document.querySelector('input [name="email"]').value;
    const password = document.querySelector('input [name="password"]').value;


    if(name.trim() === '' || email.trim() === '' || password.trim() === ''){
        message.textContent = 'Todos os campos devem ser preenchidos';

        return;
    }

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        message.textContent = 'Por favor insira um email válido.';
        return;
    }

    if (!password.length < 6) {
        message.textContent = 'A senha deve ter no mínimo 6 caracteres.';
        return;
    }


    form.submit();


});