(function () {
    function initPortfolioCarousel() {
        const carousel = document.getElementById("about-photo-carousel");

        const slides = Array.from(
            document.querySelectorAll(
                "#about-carousel-track .about-carousel-slide"
            )
        );

        const prev = document.getElementById("about-carousel-prev");
        const next = document.getElementById("about-carousel-next");

        const dots = Array.from(
            document.querySelectorAll(
                "#about-photo-carousel .about-carousel-dot"
            )
        );

        if (!carousel || slides.length !== 4 || !prev || !next) {
            console.warn("Portfolio carousel: required elements not found.");
            return;
        }

        let current = 0;
        let autoPlayTimer = null;

        function show(index) {
            current = (index + slides.length) % slides.length;

            slides.forEach(function (slide, i) {
                slide.style.opacity = i === current ? "1" : "0";
            });

            dots.forEach(function (dot, i) {
                dot.style.opacity = i === current ? "1" : "0.35";
                dot.setAttribute(
                    "aria-current",
                    i === current ? "true" : "false"
                );
            });
        }

        function startAutoPlay() {
            clearInterval(autoPlayTimer);

            autoPlayTimer = setInterval(function () {
                show(current + 1);
            }, 4000);
        }

        function restartAutoPlay() {
            startAutoPlay();
        }

        prev.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();
            show(current - 1);
            restartAutoPlay();
        });

        next.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();
            show(current + 1);
            restartAutoPlay();
        });

        dots.forEach(function (dot, i) {
            dot.addEventListener("click", function (event) {
                event.preventDefault();
                event.stopPropagation();
                show(i);
                restartAutoPlay();
            });
        });

        let startX = null;

        carousel.addEventListener(
            "touchstart",
            function (event) {
                startX = event.changedTouches[0].clientX;
            },
            { passive: true }
        );

        carousel.addEventListener(
            "touchend",
            function (event) {
                if (startX === null) return;

                const endX = event.changedTouches[0].clientX;
                const distance = endX - startX;

                if (Math.abs(distance) > 45) {
                    show(
                        distance < 0
                            ? current + 1
                            : current - 1
                    );

                    restartAutoPlay();
                }

                startX = null;
            },
            { passive: true }
        );

        show(0);
        startAutoPlay();

        console.log(
            "Portfolio carousel initialized with autoplay."
        );
    }

    if (document.readyState === "loading") {
        document.addEventListener(
            "DOMContentLoaded",
            initPortfolioCarousel
        );
    } else {
        initPortfolioCarousel();
    }
})();
