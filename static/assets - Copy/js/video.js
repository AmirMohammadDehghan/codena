"use strict";

function createVideoPlayer(videoContainerSelector) {

  //elements
  const videoContainer = document.querySelector(videoContainerSelector)
  const video = videoContainer.querySelector('.video')
  const screenshot = videoContainer.querySelector("#screenshot")
  const grayVideoToggle = videoContainer.querySelector("#grayVideoToggle")
  const playPause = videoContainer.querySelector("#playPause")
  const setPlaybackRate = videoContainer.querySelector("#setPlaybackRate")
  const pictureInPicture = videoContainer.querySelector("#pictureInPicture")
  const controllers = videoContainer.querySelector(".controllers")
  const progress = videoContainer.querySelector(".progress-video")
  const progressHidden = videoContainer.querySelector(".progress-hidden")
  const progressMarker = videoContainer.querySelector("#progressMarker")
  const plusSecond = videoContainer.querySelector("#plusSecond")
  const minusSecond = videoContainer.querySelector("#minusSecond")
  const fullscreen = videoContainer.querySelector("#fullscreen")
  const volumeRange = videoContainer.querySelector("#volumeRange");
  const volumeContainer = videoContainer.querySelector("#volumeContainer")
  const volumeBtn = videoContainer.querySelector("#volumeBtn")
  const loading = videoContainer.querySelector(".loading")



  //screenshot of video frame
  screenshot.addEventListener("click", () => {

    const canvas = document.createElement("canvas");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const dataURL = canvas.toDataURL();

    const a = document.createElement("a");
    a.href = dataURL;
    a.download = "screenshot.png";
    a.click();


     const userInformation = videoContainer.querySelector(".user-information")
    //user information move
    let randomNum;
    setInterval(() => {
        randomNum = Math.random() * 100
        if (userInformation) {
            if (randomNum < 75) {
                userInformation.style.right = `${randomNum}%`
                userInformation.style.top = `${randomNum - (randomNum / 10)}%`
            } else {
                userInformation.style.right = `${randomNum - 20}%`
                userInformation.style.top = `${randomNum - 20 - (randomNum / 2)}%`
            }
        }
    }, 10000)

  })


  //grayscale video toggle
  let isGray = false;
  grayVideoToggle.addEventListener("click", () => {
    if (isGray) {
      video.style.filter = 'grayscale(0)'
      isGray = false
    } else {
      video.style.filter = 'grayscale(1)'
      isGray = true
    }
  })




  //play && pause video
  let isPlay = false;
  playPause.addEventListener("click", () => {
    const isVideoFinished = video.currentTime >= video.duration;

    if (isVideoFinished) {
      playVideo()
    } else {
      if (isPlay) {
        pauseVideo()
      } else {
        playVideo()
      }
    }
  })

  function playVideo() {
    video.play()
  }

  function pauseVideo() {
    video.pause()
  }

  video.addEventListener('play', () => {
    playPause.innerHTML = `
                                            <svg fill="#fff" width="21px" height="21px" viewBox="0 0 32 32">
                                                <path d="M5.92 24.096q0 0.832 0.576 1.408t1.44 0.608h4.032q0.832 0 1.44-0.608t0.576-1.408v-16.16q0-0.832-0.576-1.44t-1.44-0.576h-4.032q-0.832 0-1.44 0.576t-0.576 1.44v16.16zM18.016 24.096q0 0.832 0.608 1.408t1.408 0.608h4.032q0.832 0 1.44-0.608t0.576-1.408v-16.16q0-0.832-0.576-1.44t-1.44-0.576h-4.032q-0.832 0-1.408 0.576t-0.608 1.44v16.16z"></path>
                                            </svg>
                                            `
    isPlay = true

    isShowController = false
  })

  video.addEventListener('pause', () => {
    playPause.innerHTML = `
                                            <svg width="21px" height="21px" viewBox="0 0 11 14">
                                                <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                                                    <g transform="translate(-753.000000, -955.000000)">
                                                        <g transform="translate(100.000000, 852.000000)">
                                                            <g transform="translate(646.000000, 98.000000)">
                                                                <g>
                                                                    <rect x="0" y="0" width="24" height="24"></rect>
                                                                    <path d="M7,6.82 L7,17.18 C7,17.97 7.87,18.45 8.54,18.02 L16.68,12.84 C17.3,12.45 17.3,11.55 16.68,11.15 L8.54,5.98 C7.87,5.55 7,6.03 7,6.82 Z" fill="#fff"></path>
                                                                </g>
                                                            </g>
                                                        </g>
                                                     </g>
                                                </g>
                                            </svg>
                                            `
    isPlay = false
  })


  //show && hide controller
  let isShowController = true
  videoContainer.addEventListener("mouseover", () => {
    controllers.style.opacity = '1'
    isShowController = true
  })

  videoContainer.addEventListener("mouseleave", () => {
    if (isShowController) {
      controllers.style.opacity = '0'
      isShowController = false
    }
  })

  videoContainer.addEventListener("click", () => {
    if (isShowController) {
      controllers.style.opacity = '0'
      isShowController = false
    } else {
      controllers.style.opacity = '1'
      isShowController = true
    }
  })

  //playback rate
  setPlaybackRate.addEventListener("click", e => {
    if (video.playbackRate === 1) {
      video.playbackRate = 1.5
      e.target.innerHTML = 1.5
    } else if (video.playbackRate === 1.5) {
      video.playbackRate = 2
      e.target.innerHTML = 2
    } else if (video.playbackRate === 2) {
      video.playbackRate = .5
      e.target.innerHTML = 0.5
    } else if (video.playbackRate === .5) {
      video.playbackRate = 1
      e.target.innerHTML = 1
    }
  })


  //picture in picture
  if (navigator.userAgent.indexOf("Firefox") != -1) {
    pictureInPicture.remove()
  } else {
    pictureInPicture.addEventListener("click", () => {
      if (document.pictureInPictureElement) {
        document
          .exitPictureInPicture()
          .then(() => {
            console.log("Document Exited from Picture-in-Picture mode")
          })
          .catch((err) => console.error(err));
      } else {
        video.requestPictureInPicture();
      }
    });
  }


  //progress bar
  function getProgressFromMouseEvent(event) {
    const progressBarOffset = progressHidden.getBoundingClientRect();
    const clickX = event.clientX - progressBarOffset.left;

    const progress = clickX / progressHidden.offsetWidth;

    return progress;

  }

  progress.addEventListener("click", (event) => {
    const progress = getProgressFromMouseEvent(event);

    video.currentTime = progress * video.duration;
    progressMarker.style.width = progress * progressHidden.offsetWidth + "px";
  });

  function getProgressFromTime(currentTime) {
    const progress = currentTime / video.duration;

    return progress;
  }

  video.addEventListener("timeupdate", () => {
    const progress = getProgressFromTime(video.currentTime);

    progressMarker.style.width = progress * progressHidden.offsetWidth + "px";

    let isVideoFinished = video.currentTime >= video.duration;
    if (isVideoFinished) {
      playPause.innerHTML = `
        <svg width="21px" height="21px" viewBox="0 0 11 14">
        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
            <g transform="translate(-753.000000, -955.000000)">
                <g transform="translate(100.000000, 852.000000)">
                    <g transform="translate(646.000000, 98.000000)">
                        <g>
                            <rect x="0" y="0" width="24" height="24"></rect>
                            <path d="M7,6.82 L7,17.18 C7,17.97 7.87,18.45 8.54,18.02 L16.68,12.84 C17.3,12.45 17.3,11.55 16.68,11.15 L8.54,5.98 C7.87,5.55 7,6.03 7,6.82 Z" fill="#fff"></path>
                        </g>
                    </g>
                </g>
             </g>
        </g>
        </svg>
        `
    }
  });


  //fullscreen
  let isFullscreen = false

  fullscreen.addEventListener("click", () => {
    if (isFullscreen) {
      document.exitFullscreen();
      isFullscreen = false
    } else {
      videoContainer.requestFullscreen();
      isFullscreen = true
    }
  })

  //plusSecond && d minusSecond
  plusSecond.addEventListener("click", () => {
    video.currentTime += 5
  })

  minusSecond.addEventListener("click", () => {
    video.currentTime -= 5
  })

  //volume
  volumeContainer.addEventListener("mousemove", () => {
    volumeContainer.style.width = '100%'
    volumeRange.style.opacity = '1'
  })

  volumeContainer.addEventListener("mouseleave", () => {
    volumeContainer.style.width = '26px'
    volumeRange.style.opacity = '0'
  })

  video.volume = volumeRange.value / 100;

  volumeRange.onchange = function () {
    video.volume = volumeRange.value / 100;
  }

  //loading
  video.addEventListener('waiting', function () {
    loading.style.display = "block";
  });

  video.addEventListener('playing', function () {
    loading.style.display = "none";
  });

  //intro video to primary video
  video.addEventListener('ended', function () {
    video.src = video.getAttribute("primary-src");
    playVideo()
  });
}