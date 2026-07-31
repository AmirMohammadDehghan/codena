const timelineContents = document.querySelectorAll(".timeline_content");

    function onScroll() {
        for (const timelineContent of timelineContents) {
            const timelineItemTop = timelineContent.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;

            if (timelineItemTop < windowHeight) {
                timelineContent.style.opacity = 1;
            } else {
                timelineContent.style.opacity = 0;
            }
        }
    }

    window.addEventListener("scroll", onScroll);


var futureTime = document.querySelector(".discount-card").getAttribute("data-future-time");
    var countDownDate = new Date(futureTime).getTime();
    function convertEnNumberToPersian(number) {
        const persian = {
            0: "۰",
            1: "۱",
            2: "۲",
            3: "۳",
            4: "۴",
            5: "۵",
            6: "۶",
            7: "۷",
            8: "۸",
            9: "۹",
        };
        number = number.toString().split("");
        let persianNumber = "";
        for (let i = 0; i < number.length; i++) {
            number[i] = persian[number[i]];
        }
        for (let i = 0; i < number.length; i++) {
            persianNumber += number[i];
        }
        return persianNumber;
    };
    var countdownfunction = setInterval(function () {
        var now = new Date().getTime();
        var distance = countDownDate - now;
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        document.querySelector(".days").innerHTML = convertEnNumberToPersian(days);
        document.querySelector(".hours").innerHTML = convertEnNumberToPersian(hours);
        document.querySelector(".minutes").innerHTML = convertEnNumberToPersian(minutes);
        document.querySelector(".seconds").innerHTML = convertEnNumberToPersian(seconds);
    }, 1000);

