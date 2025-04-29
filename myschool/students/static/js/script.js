document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelector('.slides');
    const slide = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    let index = 0;

    const nextButton = document.querySelector('.next');
    const prevButton = document.querySelector('.prev');

    if (!slides || slide.length === 0 || !nextButton || !prevButton || dots.length === 0) {
        console.error("Бир же бир нече элемент табылган жок! HTML кодун текшериңиз.");
        return;
    }

    nextButton.addEventListener('click', () => {
        index = (index + 1) % slide.length;
        updateSlider();
    });

    prevButton.addEventListener('click', () => {
        index = (index - 1 + slide.length) % slide.length;
        updateSlider();
    });

    function updateSlider() {
        slides.style.transform = `translateX(-${index * 100}%)`;
        dots.forEach(dot => dot.classList.remove("active"));
        dots[index].classList.add("active");
    }

    function goToSlide(n) {
        index = n;
        updateSlider();
    }

    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => {
            goToSlide(i);
        });
    });

    setInterval(() => {
        index = (index + 1) % slide.length;
        updateSlider();
    }, 4000);

    updateSlider();
});

                                                    //БУЛ ЖАНЫЛЫКТАРДЫ ТОЛУК ОКУУ КОДУ

// Модал терезени ачуу функциясы
function openModal(title, content, date, imageUrl) {
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalContent").innerText = content;
    document.getElementById("modalDate").innerText = "Дата: " + date;
    document.getElementById("modalImage").src = imageUrl;

    // Модал терезени көрсөтүү
    document.getElementById("newsModal").style.display = "flex";
}

// Модал терезени жабуу функциясы
function closeModal() {
    document.getElementById("newsModal").style.display = "none";
}

// Модалды сыртка басып жабуу функциясы (фонду басканда)
window.onclick = function(event) {
    if (event.target == document.getElementById("newsModal")) {
        closeModal();
    }
}

