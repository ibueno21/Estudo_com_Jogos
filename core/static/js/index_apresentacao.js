document.addEventListener("DOMContentLoaded", () => {

    // Dados para a troca dinâmica no Card Interativo
    const initialData = {
        imgSrc: "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=1000&q=80",
        alt: "Estudo Tradicional",
        title: "Estudo Tradicional",
        desc: "Livros, anotações e teoria prontos para se tornarem desafios práticos.",
        hintText: "Passe o mouse para ver o modo de jogo",
        hintBg: "rgba(43, 37, 35, 0.85)"
    };

    const transformedData = {
        imgSrc: "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1000&q=80",
        alt: "Aprendizado Gamificado",
        title: "Aprendizado Interativo",
        desc: "Quizzes, perguntas com pontuação e acompanhamento de desempenho!",
        hintText: "Modo Gamificado! (Afastar mouse para voltar)",
        hintBg: "rgba(25, 94, 140, 0.9)"
    };

    const interactiveCard = document.getElementById("interactiveCard");
    const interactiveImg = document.getElementById("interactiveImg");
    const interactiveTitle = document.getElementById("interactiveTitle");
    const interactiveDesc = document.getElementById("interactiveDesc");
    const hoverHint = document.getElementById("hoverHint");
    const hintTextNode = hoverHint.querySelector(".hint-text");

    const allCards = [
        document.getElementById("headerBox"),
        document.getElementById("dishCard"),
        interactiveCard
    ];

    // Efeito de sombra
    allCards.forEach(card => {
        if (!card) return;

        card.addEventListener("mouseenter", () => {
            card.classList.add("card-hover-shadow");
        });

        card.addEventListener("mouseleave", () => {
            card.classList.remove("card-hover-shadow");
        });
    });

    // Troca de estado ao passar o mouse
    if (interactiveCard) {
        interactiveCard.addEventListener("mouseenter", () => {
            interactiveImg.src = transformedData.imgSrc;
            interactiveImg.alt = transformedData.alt;
            interactiveTitle.textContent = transformedData.title;
            interactiveDesc.textContent = transformedData.desc;
            hintTextNode.textContent = transformedData.hintText;
            hoverHint.style.backgroundColor = transformedData.hintBg;
        });

        interactiveCard.addEventListener("mouseleave", () => {
            interactiveImg.src = initialData.imgSrc;
            interactiveImg.alt = initialData.alt;
            interactiveTitle.textContent = initialData.title;
            interactiveDesc.textContent = initialData.desc;
            hintTextNode.textContent = initialData.hintText;
            hoverHint.style.backgroundColor = initialData.hintBg;
        });
    }
});