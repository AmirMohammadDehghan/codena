const audio = document.getElementById("audio");
const playPauseButton = document.getElementById("playPauseButton");
const progressEl = document.querySelector(".progress")
const progressBar = document.getElementById("progress-bar");
const currentTimeDisplay = document.getElementById("currentTime");
const totalTimeDisplay = document.getElementById("totalTime");
const plusSecondButton = document.getElementById("plusSecond")
const minusSecondButton = document.getElementById("minusSecond")
var descriptionsContianer = document.getElementById("descriptionsContainer");
var showMoreBtn = document.getElementById("showMore");

audio.addEventListener("loadedmetadata", () => {
    let currentTime = audio.currentTime;
    let duration = audio.duration;
    const totalMinutes = Math.floor(duration / 60);
    const totalSeconds = Math.floor(duration % 60);
    totalTimeDisplay.textContent = `${totalMinutes}:${totalSeconds < 10 ? '0' : ''}${totalSeconds}`;

    let isPlaying = false;
    playPauseButton.addEventListener("click", () => {
        if (isPlaying) {
            audio.pause();
            playPauseButton.innerHTML = `
                <svg width="30px" height="30px" viewBox="0 0 11 14">
                    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <g transform="translate(-753.000000, -955.000000)">
                            <g transform="translate(100.000000, 852.000000)">
                                <g transform="translate(646.000000, 98.000000)">
                                    <g>
                                        <rect x="0" y="0" width="24" height="24">
                                        </rect>
                                        <path
                                            d="M7,6.82 L7,17.18 C7,17.97 7.87,18.45 8.54,18.02 L16.68,12.84 C17.3,12.45 17.3,11.55 16.68,11.15 L8.54,5.98 C7.87,5.55 7,6.03 7,6.82 Z"
                                            fill="#fff"></path>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </svg>
                `;
        } else {
            audio.play();
            playPauseButton.innerHTML = `
                <svg fill="#fff" width="30px" height="30px" viewBox="0 0 32 32">
                    <path d="M5.92 24.096q0 0.832 0.576 1.408t1.44 0.608h4.032q0.832 0 1.44-0.608t0.576-1.408v-16.16q0-0.832-0.576-1.44t-1.44-0.576h-4.032q-0.832 0-1.44 0.576t-0.576 1.44v16.16zM18.016 24.096q0 0.832 0.608 1.408t1.408 0.608h4.032q0.832 0 1.44-0.608t0.576-1.408v-16.16q0-0.832-0.576-1.44t-1.44-0.576h-4.032q-0.832 0-1.408 0.576t-0.608 1.44v16.16z"></path>
                </svg>
                `;
        }
        isPlaying = !isPlaying;
    });

    audio.addEventListener("timeupdate", () => {
        currentTime = audio.currentTime;
        duration = audio.duration;

        var isFinished = currentTime >= duration;
        if (isFinished) {
            playPauseButton.innerHTML = `
                <svg width="30px" height="30px" viewBox="0 0 11 14">
                    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <g transform="translate(-753.000000, -955.000000)">
                            <g transform="translate(100.000000, 852.000000)">
                                <g transform="translate(646.000000, 98.000000)">
                                    <g>
                                        <rect x="0" y="0" width="24" height="24">
                                        </rect>
                                        <path
                                            d="M7,6.82 L7,17.18 C7,17.97 7.87,18.45 8.54,18.02 L16.68,12.84 C17.3,12.45 17.3,11.55 16.68,11.15 L8.54,5.98 C7.87,5.55 7,6.03 7,6.82 Z"
                                            fill="#fff"></path>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </svg>
                `
            isPlaying = !isPlaying;
        }

        const currentMinutes = Math.floor(currentTime / 60);
        const currentSeconds = Math.floor(currentTime % 60);

        currentTimeDisplay.textContent = `${currentMinutes}:${currentSeconds < 10 ? '0' : ''}${currentSeconds}`;

        const progress = (currentTime / duration) * 100;
        progressBar.style.width = `${progress}%`;
    });

    plusSecondButton.addEventListener("click", function () {
        audio.currentTime += 15
        if (audio.currentTime >= audio.duration && isPlaying === true) {
            isPlaying = false;
        }
    })

    minusSecondButton.addEventListener("click", function () {
        audio.currentTime -= 15
        if (audio.currentTime >= audio.duration && isPlaying === true) {
            isPlaying = false;
        }
    })

    function getProgressFromMouseEvent(event) {
        var progressBarOffset = progressEl.getBoundingClientRect();
        var clickX = event.clientX - progressBarOffset.left;
        var progress = clickX / progressEl.offsetWidth;
        return progress;
    }
    progressEl.addEventListener("click", function (event) {
        var progress = getProgressFromMouseEvent(event);
        audio.currentTime = progress * audio.duration;
        progressBar.style.width = progress * progressEl.offsetWidth + "px";
    });
})

showMoreBtn.onclick = function () {
    if (descriptionsContianer.className == "container open") {
        //shrink the box
        descriptionsContianer.className = "container position-relative";
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