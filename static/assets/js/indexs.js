let roadMapSwiperSetting = {
    slidesPerView: 4,
    spaceBetween: 30,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
}
let roadMapSwiper;

function slidesPerViewController() {
    if (window.innerWidth <= 1200 && window.innerWidth >= 768) {

        roadMapSwiperSetting.slidesPerView = 3;
        roadMapSwiper = new Swiper(".road-map-swiper", roadMapSwiperSetting);

    } else if (window.innerWidth <= 768 && window.innerWidth > 556) {

        roadMapSwiperSetting.slidesPerView = 2;
        roadMapSwiper = new Swiper(".road-map-swiper", roadMapSwiperSetting);

    } else if (window.innerWidth <= 576) {

        roadMapSwiperSetting.slidesPerView = 1.3;
        roadMapSwiper = new Swiper(".road-map-swiper", roadMapSwiperSetting);

    } else {
        
        roadMapSwiperSetting.slidesPerView = 4;
        roadMapSwiper = new Swiper(".road-map-swiper", roadMapSwiperSetting);

    }
}

window.addEventListener("resize", slidesPerViewController)
slidesPerViewController()