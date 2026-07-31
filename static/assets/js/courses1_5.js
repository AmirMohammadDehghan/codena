document.addEventListener("DOMContentLoaded", () => {
    var srcChangerEle = document.querySelectorAll("a[data-video-target-src]"),
        videoPlayer = document.querySelector("#videoCourse")
    if (srcChangerEle) {
        srcChangerEle.forEach(function (e) {
            e.addEventListener("click", function (r) {
                r.preventDefault()
                if (videoPlayer) {
                    videoPlayer.setAttribute('src', e.getAttribute("data-video-target-src"))
                    videoPlayer.setAttribute('primary-src', e.getAttribute("data-video-target-src"))
                    function checkReadyState() {
					if (videoPlayer.readyState >= 2) {
						videoPlayer.play()
						} else {
						setTimeout(checkReadyState, 500);
						}
					}
					checkReadyState()
                }
                videoPlayer.poster = e.getAttribute("data-img-target-src")
            })
        });
    }

	//lazy avatar
    var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));

    if ("IntersectionObserver" in window) {
        let lazyImageObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    let lazyImage = entry.target;
                    lazyImage.src = lazyImage.dataset.src;
                    lazyImage.classList.remove("lazy");
                    lazyImageObserver.unobserve(lazyImage);
                }
            });
        });

        lazyImages.forEach(function (lazyImage) {
            lazyImageObserver.observe(lazyImage);
        });
    }

	//discount
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

	var discountCard = document.querySelector(".discount-card")
	if(discountCard){
		var futureTime = discountCard.getAttribute("data-future-time");
	}
	if(futureTime){
		var countDownDate = new Date(futureTime).getTime();

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

	}


	//show more
	var descriptionsContianer = document.getElementById("descriptionsContianer");
	var showMoreBtn = document.getElementById("showMore");

	if(showMoreBtn) {
		showMoreBtn.onclick = function () {
			if (descriptionsContianer.className == "container open") {
				//shrink the box
				descriptionsContianer.className = "container";
				showMoreBtn.innerHTML = "نمایش بیشتر" + `
							<svg width="24px" height="24px" viewBox="0 0 24 24" fill="none" style="rotate: 180deg;">
								<path
									d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
									stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
							</svg>
						`;
			} else {
				//expand the box
				descriptionsContianer.className = "container open";
				showMoreBtn.innerHTML = "نمایش کمتر" + `
							<svg width="24px" height="24px" viewBox="0 0 24 24" fill="none">
								<path
									d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
									stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
							</svg>
						`;
			}
		};
	}

	//replay
	const replayCollapse = document.getElementById("replayCollapse");
	const replayCollapseBtns = document.querySelectorAll('[data-kind="replayCollapseBtn"]')

	if(replayCollapseBtns) {
		replayCollapseBtns.forEach(el => {
			el.addEventListener("click", e => {
				if (e.target.getAttribute("data-mode") === "hide") {
					e.target.innerHTML = `
										پنهان کردن
										<svg width="20px" height="20px" viewBox="0 0 24 24" fill="none">
											<path
												d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
												stroke="#fff" stroke-width="1.5" stroke-linecap="round"
												stroke-linejoin="round"></path>
										</svg>
									`
					e.target.setAttribute("data-mode", "open")
				} else {
					e.target.innerHTML = `
							نمایش
							<strong>${e.target.getAttribute("data-num-replay")}</strong>
							پاسخ
							<svg width="20px" height="20px" viewBox="0 0 24 24" fill="none"
								style="rotate: 180deg;">
								<path
									d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
									stroke="#fff" stroke-width="1.5" stroke-linecap="round"
									stroke-linejoin="round"></path>
							</svg>
							`;
					e.target.setAttribute("data-mode", "hide")
				}
			})
		})
	}
})