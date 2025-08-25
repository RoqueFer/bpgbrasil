document.addEventListener("DOMContentLoaded", () => {
  // Função genérica para inicializar um carrossel
  function initializeCarousel(
    containerSelector,
    trackSelector,
    slideSelector,
    dotsContainerSelector,
    getSlidesPerView,
    autoPlayInterval = 3000
  ) {
    const carouselContainer = document.querySelector(containerSelector);
    if (!carouselContainer) return;

    const carouselTrack = carouselContainer.querySelector(trackSelector);
    const slides = Array.from(carouselTrack.querySelectorAll(slideSelector));
    const prevButton = carouselContainer.querySelector(".carousel-button.prev");
    const nextButton = carouselContainer.querySelector(".carousel-button.next");
    const dotsContainer = document.querySelector(dotsContainerSelector);

    let currentIndex = 0;
    let autoPlayTimer;
    let slidesPerView = 1; // Default, will be updated by getSlidesPerView()

    // Cria ou atualiza os dots de navegação
    function createDots() {
      slidesPerView =
        typeof getSlidesPerView === "function"
          ? getSlidesPerView()
          : getSlidesPerView;
      dotsContainer.innerHTML = "";
      const numDots = Math.ceil(slides.length / slidesPerView);
      for (let i = 0; i < numDots; i++) {
        const dot = document.createElement("span");
        dot.classList.add("carousel-dot");
        dot.dataset.index = i; // Armazena o índice no dataset
        dot.addEventListener("click", () => {
          currentIndex = i;
          updateCarousel();
          resetAutoPlay();
        });
        dotsContainer.appendChild(dot);
      }
    }

    function adjustSlideWidthForMultipleViews() {
      slidesPerView =
        typeof getSlidesPerView === "function"
          ? getSlidesPerView()
          : getSlidesPerView;
      if (slides.length === 0) return;

      const trackContainerWidth = carouselContainer.querySelector(
        ".image-carousel-track-container, .icon-carousel-track-container"
      ).offsetWidth;
      const gapBetweenSlides = parseFloat(
        getComputedStyle(slides[0]).marginRight || 0
      );

      const slideCalculatedWidth =
        (trackContainerWidth - (slidesPerView - 1) * gapBetweenSlides) /
        slidesPerView;

      slides.forEach((slide) => {
        slide.style.minWidth = `${slideCalculatedWidth}px`;
      });
    }

    // Atualiza a posição do carrossel e o estado dos dots
    function updateCarousel() {
      slidesPerView =
        typeof getSlidesPerView === "function"
          ? getSlidesPerView()
          : getSlidesPerView;

      // Para o carrossel de imagens, a largura do slide é a largura do trackContainer
      // Para o carrossel de ícones, a largura do slide é a slideCalculatedWidth ajustada
      let effectiveSlideWidth;
      if (containerSelector === ".image-carousel-container") {
        effectiveSlideWidth = carouselContainer.querySelector(
          ".image-carousel-track-container"
        ).offsetWidth;
      } else {
        // icon-carousel-container
        // Re-calcula para garantir que está sempre certo
        const trackContainerWidth = carouselContainer.querySelector(
          ".icon-carousel-track-container"
        ).offsetWidth;
        const gapBetweenSlides = parseFloat(
          getComputedStyle(slides[0]).marginRight || 0
        );
        effectiveSlideWidth =
          (trackContainerWidth - (slidesPerView - 1) * gapBetweenSlides) /
          slidesPerView;
      }

      const offset =
        -currentIndex *
        effectiveSlideWidth *
        (containerSelector === ".image-carousel-container" ? 1 : slidesPerView);
      // Para o carrossel de imagens, move 1 slide por vez.
      // Para o carrossel de ícones, move um "grupo" de slides por vez.

      carouselTrack.style.transform = `translateX(${offset}px)`;

      // Atualiza os dots
      const dots = dotsContainer.querySelectorAll(".carousel-dot");
      dots.forEach((dot, index) => {
        if (index === currentIndex) {
          dot.classList.add("active");
        } else {
          dot.classList.remove("active");
        }
      });
    }

    // Navegação para o próximo slide
    function showNextSlide() {
      const maxIndex = Math.ceil(slides.length / slidesPerView) - 1;
      currentIndex = currentIndex < maxIndex ? currentIndex + 1 : 0;
      updateCarousel();
    }

    // Navegação para o slide anterior
    function showPrevSlide() {
      const maxIndex = Math.ceil(slides.length / slidesPerView) - 1;
      currentIndex = currentIndex > 0 ? currentIndex - 1 : maxIndex;
      updateCarousel();
    }

    // Inicializa o autoplay
    function startAutoPlay() {
      if (autoPlayInterval > 0) {
        autoPlayTimer = setInterval(showNextSlide, autoPlayInterval);
      }
    }

    // Reinicia o autoplay (útil após interação manual)
    function resetAutoPlay() {
      clearInterval(autoPlayTimer);
      startAutoPlay();
    }

    // Adiciona listeners para botões
    if (prevButton) {
      prevButton.addEventListener("click", () => {
        showPrevSlide();
        resetAutoPlay();
      });
    }
    if (nextButton) {
      nextButton.addEventListener("click", () => {
        showNextSlide();
        resetAutoPlay();
      });
    }

    // Observa o redimensionamento para ajustar o carrossel
    window.addEventListener("resize", () => {
      createDots(); // Recria dots (e recalcula slidesPerView)
      if (containerSelector === ".icon-carousel-container") {
        adjustSlideWidthForMultipleViews(); // Reajusta largura dos ícones
      }
      setTimeout(updateCarousel, 100); // Pequeno atraso para garantir que o layout terminou de ajustar
    });

    // Inicialização
    createDots(); // Chama createDots primeiro para definir slidesPerView
    if (containerSelector === ".icon-carousel-container") {
      adjustSlideWidthForMultipleViews(); // Apenas para o carrossel de ícones
    }
    updateCarousel(); // Chama uma vez para configurar a posição inicial
    startAutoPlay();
  }

  // --- Definindo a função getIconsPerView antes de ser usada ---
  function getIconsPerView() {
    if (window.innerWidth <= 400) return 2;
    if (window.innerWidth <= 768) return 3;
    if (window.innerWidth <= 1024) return 4;
    return 5;
  }

  // --- Inicializa o Carrossel de Imagens ---
  initializeCarousel(
    ".image-carousel-container",
    ".image-carousel-track",
    ".image-carousel-slide",
    ".image-dots",
    () => 1, // slidesPerView fixo em 1 para imagens
    4000
  );

  // --- Inicializa o Carrossel de Ícones ---
  initializeCarousel(
    ".icon-carousel-container",
    ".icon-carousel-track",
    ".icon-carousel-slide",
    ".icon-dots",
    getIconsPerView, // Passa a função para que slidesPerView seja dinâmico
    5000
  );
});
