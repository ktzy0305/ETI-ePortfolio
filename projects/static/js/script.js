$(document).ready(function () {
    new WOW().init();
    $(".owl-carousel").owlCarousel(
        {
            loop: true,
            margin: 10,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                    nav: false,
                    loop: false,
                },
                768: {
                    items: 2,
                    nav: false,
                    loop: false,
                },
                1000: {
                    items: 3,
                    nav: false,
                    loop: false,
                }
            }
        }
    );
});