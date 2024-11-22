
const divNav = document.querySelector(".div-nav");
const navMenu = document.querySelector(".nav-menu");

divNav.addEventListener("click", () => {
    divNav.classList.toggle('active');
    navMenu.classList.toggle('active');
})
