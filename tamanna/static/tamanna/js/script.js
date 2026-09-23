document.addEventListener("DOMContentLoaded", function () {

    const openPortfolio =
        document.getElementById("openPortfolio");

    const openPortfolioText =
        document.getElementById("openPortfolioText");

    const closePortfolio =
        document.getElementById("closePortfolio");

    const portfolioModal =
        document.getElementById("portfolioModal");


    // ==========================================
    // OPEN PORTFOLIO
    // ==========================================

    function openMenu() {

        portfolioModal.classList.add("active");

        document.body.style.overflow = "hidden";

    }


    // ==========================================
    // CLOSE PORTFOLIO
    // ==========================================

    function closeMenu() {

        portfolioModal.classList.remove("active");

        document.body.style.overflow = "";

    }


    // Photo click

    if (openPortfolio) {

        openPortfolio.addEventListener(
            "click",
            openMenu
        );

    }


    // Text click

    if (openPortfolioText) {

        openPortfolioText.addEventListener(
            "click",
            openMenu
        );

    }


    // Close button

    if (closePortfolio) {

        closePortfolio.addEventListener(
            "click",
            closeMenu
        );

    }


    // ==========================================
    // CLICK OUTSIDE MODAL
    // ==========================================

    if (portfolioModal) {

        portfolioModal.addEventListener(
            "click",
            function (event) {

                if (
                    event.target === portfolioModal ||
                    event.target.classList.contains(
                        "modal-background"
                    )
                ) {

                    closeMenu();

                }

            }
        );

    }


    // ==========================================
    // ESC KEY
    // ==========================================

    document.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Escape" &&
                portfolioModal.classList.contains("active")
            ) {

                closeMenu();

            }

        }
    );


    // ==========================================
    // CARD HOVER EFFECT
    // ==========================================

    const cards =
        document.querySelectorAll(".menu-card");


    cards.forEach(function (card) {

        card.addEventListener(
            "mouseenter",
            function () {

                card.style.zIndex = "20";

            }
        );


        card.addEventListener(
            "mouseleave",
            function () {

                card.style.zIndex = "";

            }
        );

    });

});