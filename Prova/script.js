document.querySelector('form').addEventListener('submit', function(event){

    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;
    var nome = document.getElementById('nome').value;
    

    if(email == '' || senha == '' || nome == ''){
        alert('Por favor, preencha todos os campos');
        event.preventDefault();
    }else{
        form.reset();
    }


});