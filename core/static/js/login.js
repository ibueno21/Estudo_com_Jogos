// login.js - Validações e efeitos dinâmicos na interface de login
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.login-form');
    const submitBtn = document.querySelector('.btn-submit');

    form.addEventListener('submit', (e) => {
        // Altera o estado do botão para evitar cliques duplicados
        submitBtn.innerText = "Conectando...";
        submitBtn.style.opacity = "0.7";
        submitBtn.style.pointerEvents = "none";
    });
});