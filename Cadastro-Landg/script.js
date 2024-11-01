var btnSignin = document.querySelector("#signin");
var btnSignup = document.querySelector("#signup");

var body = document.querySelector("body");


btnSignin.addEventListener("click", function () {
   body.className = "sign-in-js"; 
});

btnSignup.addEventListener("click", function () {
    body.className = "sign-up-js";
})


document.querySelector('form').addEventListener('submit',function(event){
    
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;

    if(email === '' || senha === ''){
        alert('Por favor, Preencha todos os campos.');
        event.preventDefault();
    }else{
        form.reset();
    }

});