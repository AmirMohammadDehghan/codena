"use strict";

function createVideoPlayer(videoContainerSelector) {
  //elements
  var videoContainer = document.querySelector(videoContainerSelector);
  var video = videoContainer.querySelector('.video');
  var screenshot = videoContainer.querySelector("#screenshot");
  var grayVideoToggle = videoContainer.querySelector("#grayVideoToggle");
  var playPause = videoContainer.querySelector("#playPause");
  var setPlaybackRate = videoContainer.querySelector("#setPlaybackRate");
  var pictureInPicture = videoContainer.querySelector("#pictureInPicture");
  var controllers = videoContainer.querySelector(".controllers");
  var progress = videoContainer.querySelector(".progress-video");
  var progressHidden = videoContainer.querySelector(".progress-hidden");
  var progressMarker = videoContainer.querySelector("#progressMarker");
  var timeProgress = videoContainer.querySelector("#timeProgress")
  var plusSecond = videoContainer.querySelector("#plusSecond");
  var minusSecond = videoContainer.querySelector("#minusSecond");
  var fullscreen = videoContainer.querySelector("#fullscreen");
  var volumeRange = videoContainer.querySelector("#volumeRange");
  var volumeContainer = videoContainer.querySelector("#volumeContainer");
  var volumeBtn = videoContainer.querySelector("#volumeBtn");
  var loading = videoContainer.querySelector(".loading");
  var userInformation = videoContainer.querySelector(".user-information");
  var buffered = videoContainer.querySelector(".buffered");
  var Times = videoContainer.querySelector(".times");
  var currentTimeText = videoContainer.querySelector(".current-time");
  var durationText = videoContainer.querySelector(".duration");
  var settingPanel = videoContainer.querySelector(".setting-panel");
  var setting = videoContainer.querySelector("#setting");
  var closeSetting = videoContainer.querySelector("#closeSetting");
  var controls = videoContainer.querySelectorAll(".control");

  //screenshot of video frame
  if (screenshot) {
    screenshot.addEventListener("click", function () {
      var canvas = document.createElement("canvas");
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      var ctx = canvas.getContext("2d");
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
      var dataURL = canvas.toDataURL();
      var a = document.createElement("a");
      a.href = dataURL;
      a.download = "screenshot.png";
      a.click();
    });
  }

  //grayscale video toggle
  var isGray = false;
  if (grayVideoToggle) {
    grayVideoToggle.addEventListener("click", function () {
      if (isGray) {
        video.style.filter = 'grayscale(0)';
        isGray = false;
      } else {
        video.style.filter = 'grayscale(1)';
        isGray = true;
      }
    });
  }

  //play && pause video
  var isPlay = false;
  if (playPause) {
    playPause.addEventListener("click", function () {
      var isVideoFinished = video.currentTime >= video.duration;
      if (isVideoFinished) {
        video.play();
      } else {
        if (isPlay) {
          video.pause();
        } else {
          video.play();
        }
      }
    });
  }
  video.addEventListener('play', function (event) {
    playPause.innerHTML = "\n                                            <svg fill=\"#fff\" width=\"21px\" height=\"21px\" viewBox=\"0 0 32 32\">\n                                                <path d=\"M5.92 24.096q0 0.832 0.576 1.408t1.44 0.608h4.032q0.832 0 1.44-0.608t0.576-1.408v-16.16q0-0.832-0.576-1.44t-1.44-0.576h-4.032q-0.832 0-1.44 0.576t-0.576 1.44v16.16zM18.016 24.096q0 0.832 0.608 1.408t1.408 0.608h4.032q0.832 0 1.44-0.608t0.576-1.408v-16.16q0-0.832-0.576-1.44t-1.44-0.576h-4.032q-0.832 0-1.408 0.576t-0.608 1.44v16.16z\"></path>\n                                            </svg>\n                                            " + '<span class="control-tooltip">پخش (K)</span>';
    isPlay = true;
  });
  video.addEventListener('pause', function () {
    playPause.innerHTML = "\n                                            <svg width=\"21px\" height=\"21px\" viewBox=\"0 0 11 14\">\n                                                <g stroke=\"none\" stroke-width=\"1\" fill=\"none\" fill-rule=\"evenodd\">\n                                                    <g transform=\"translate(-753.000000, -955.000000)\">\n                                                        <g transform=\"translate(100.000000, 852.000000)\">\n                                                            <g transform=\"translate(646.000000, 98.000000)\">\n                                                                <g>\n                                                                    <rect x=\"0\" y=\"0\" width=\"24\" height=\"24\"></rect>\n                                                                    <path d=\"M7,6.82 L7,17.18 C7,17.97 7.87,18.45 8.54,18.02 L16.68,12.84 C17.3,12.45 17.3,11.55 16.68,11.15 L8.54,5.98 C7.87,5.55 7,6.03 7,6.82 Z\" fill=\"#fff\"></path>\n                                                                </g>\n                                                            </g>\n                                                        </g>\n                                                     </g>\n                                                </g>\n                                            </svg>\n                                            " + '<span class="control-tooltip">پخش (K)</span>';
    isPlay = false;
  });

  //show && hide controller
  if (videoContainer) {
    videoContainer.addEventListener("click", function (event) {
      if (event.target.classList.contains("controllers")) {
        controllers.classList.toggle("show")
      }
    });
  }

  //playback rate
  if (setPlaybackRate) {
    setPlaybackRate.addEventListener("click", function (e) {
      if (video.playbackRate === 1) {
        video.playbackRate = 1.5;
        e.target.innerHTML = "<span>1.5</span>سرعت پخش";
      } else if (video.playbackRate === 1.5) {
        video.playbackRate = 2;
        e.target.innerHTML = "<span>2</span>سرعت پخش";
      } else if (video.playbackRate === 2) {
        video.playbackRate = .5;
        e.target.innerHTML = "<span>0.5</span>سرعت پخش";
      } else if (video.playbackRate === .5) {
        video.playbackRate = 1;
        e.target.innerHTML = "<span>1</span>سرعت پخش";
      }
    });
  }

  //picture in picture
  if (pictureInPicture) {
    if (navigator.userAgent.indexOf("Firefox") != -1) {
      pictureInPicture.remove();
    } else {
      pictureInPicture.addEventListener("click", function () {
        if (document.pictureInPictureElement) {
          document.exitPictureInPicture().then(function () {
            console.log("Document Exited from Picture-in-Picture mode");
          }).catch(function (err) {
            return console.error(err);
          });
        } else {
          video.requestPictureInPicture();
        }
      });
    }
  }

  //progress bar
  if (progress) {
    function getProgressFromMouseEvent(event) {
      var progressBarOffset = progressHidden.getBoundingClientRect();
      var clickX = event.clientX - progressBarOffset.left;
      var progress = clickX / progressHidden.offsetWidth;
      return progress;
    }
    progress.addEventListener("click", function (event) {
      var progress = getProgressFromMouseEvent(event);
      video.currentTime = progress * video.duration;
      progressMarker.style.width = progress * progressHidden.offsetWidth + "px";
    });
    progress.addEventListener("mousemove", e => {
      console.log(e.target);
      const progressPercent = (e.offsetX / progress.offsetWidth) * 100
      const time = formatTime(progressPercent * video.duration / 100)
      timeProgress.innerHTML = time;
      timeProgress.style.visibility = 'visible'
      if (Number(progressPercent) > 95) {
        timeProgress.style.left = `90%`
      } else if (Number(progressPercent) < 2) {
        timeProgress.style.left = `-5%`
      } else {
        timeProgress.style.left = `${progressPercent - 6}%`
      }
    })
    progress.addEventListener("mouseleave", () => {
      timeProgress.style.visibility = 'hidden'
    })
    function getProgressFromTime(currentTime) {
      var progress = currentTime / video.duration;
      return progress;
    }
    video.addEventListener("timeupdate", function () {
      var progress = getProgressFromTime(video.currentTime);
      progressMarker.style.width = progress * progressHidden.offsetWidth + "px";
      var isVideoFinished = video.currentTime >= video.duration;
      if (isVideoFinished) {
        playPause.innerHTML = "\n          <svg width=\"21px\" height=\"21px\" viewBox=\"0 0 11 14\">\n          <g stroke=\"none\" stroke-width=\"1\" fill=\"none\" fill-rule=\"evenodd\">\n              <g transform=\"translate(-753.000000, -955.000000)\">\n                  <g transform=\"translate(100.000000, 852.000000)\">\n                      <g transform=\"translate(646.000000, 98.000000)\">\n                          <g>\n                              <rect x=\"0\" y=\"0\" width=\"24\" height=\"24\"></rect>\n                              <path d=\"M7,6.82 L7,17.18 C7,17.97 7.87,18.45 8.54,18.02 L16.68,12.84 C17.3,12.45 17.3,11.55 16.68,11.15 L8.54,5.98 C7.87,5.55 7,6.03 7,6.82 Z\" fill=\"#fff\"></path>\n                          </g>\n                      </g>\n                  </g>\n               </g>\n          </g>\n          </svg>\n          ";
      }

      // محاسبه درصد پیشرفت
      var percentage = video.currentTime / video.duration * 100;

      // بررسی اینکه آیا کاربر به طور دستی به جلو رفته است
      if (video.currentTime > video.buffered.end(0)) {
        // محاسبه درصد آخرین بخش دانلود شده
        var lastBufferedPercentage = video.buffered.end(video.buffered.length - 1) / video.duration * 100;

        // تنظیم عرض نوار دانلود شده
        buffered.style.width = "".concat(lastBufferedPercentage, "%");
      } else {
        // محاسبه درصد دانلود شده
        var bufferedPercentage = video.buffered.end(0) / video.duration * 100;

        // تنظیم عرض نوار دانلود شده
        buffered.style.width = "".concat(bufferedPercentage, "%");
      }
      currentTimeText.textContent = formatTime(video.currentTime);
    });

    // آپدیت نوار دانلود شده زمانی که کاربر به طور دستی به جلو می رود
    video.addEventListener("seeking", function () {
      // محاسبه درصد آخرین بخش دانلود شده
      var lastBufferedPercentage = video.buffered.end(video.buffered.length - 1) / video.duration * 100;

      // تنظیم عرض نوار دانلود شده
      buffered.style.width = "".concat(lastBufferedPercentage, "%");
    });
  }

  //fullscreen
  var isFullscreen = false;
  if (fullscreen) {
    fullscreen.addEventListener("click", function () {
      if (isFullscreen) {
        document.exitFullscreen();
        isFullscreen = false;
      } else {
        videoContainer.requestFullscreen();
        isFullscreen = true;
      }
    });
  }

  //plusSecond && d minusSecond
  if (plusSecond) {
    plusSecond.addEventListener("click", function () {
      video.currentTime += 15;
    });
  }
  if (minusSecond) {
    minusSecond.addEventListener("click", function () {
      video.currentTime -= 15;
    });
  }

  //volume
  if (volumeContainer) {
    volumeContainer.addEventListener("mousemove", function () {
      volumeContainer.style.width = '100%';
      volumeRange.style.opacity = '1';
    });
    volumeContainer.addEventListener("mouseleave", function () {
      volumeContainer.style.width = '32px';
      volumeRange.style.opacity = '0';
    });
    volumeRange.addEventListener("input", function () {
      if (volumeRange.value === "0") {
        video.muted = true;
      } else {
        video.muted = false;
        video.volume = volumeRange.value;
      }
    });
    volumeBtn.addEventListener("click", function () {
      if (video.muted) {
        video.muted = false;
        volumeRange.value = 1;
      } else {
        video.muted = true;
        volumeRange.value = 0;
      }
    });
    video.addEventListener("volumechange", function () {
      if (video.muted) {
        volumeBtn.innerHTML = "\n        <svg viewBox=\"0 2 24 20\" width=\"21\" height=\"21\">\n          <g fill=\"currentcolor\" data-viewbox=\"0 0 24 24\">\n            <path d=\"M10.79 9.77a1 1 0 00.71.29.84.84 0 00.38-.08 1 1 0 00.62-.92V5a1 1 0 00-1.5-.84L8.48 5.74a1 1 0 00-.48.73 1 1 0 00.29.82zM19.57 4.72a1 1 0 10-1.44 1.39A8.5 8.5 0 0119 16.82a1 1 0 00.26 1.39 1 1 0 00.57.18 1 1 0 00.82-.44 10.5 10.5 0 00-1.08-13.23z\"></path><path d=\"M16.5 12a4.42 4.42 0 01-.5 2 1 1 0 00.44 1.34.93.93 0 00.45.11 1 1 0 00.9-.55 6.4 6.4 0 00.71-2.9 6.49 6.49 0 00-2-4.72 1 1 0 10-1.37 1.45A4.46 4.46 0 0116.5 12zM12.21 12.16L7.4 7.35 3.21 3.16a1 1 0 00-1.42 0 1 1 0 000 1.41L4.72 7.5H2.5a1 1 0 00-1 1v7a1 1 0 001 1h3.21L11 19.84a1 1 0 00.54.16 1 1 0 001-1v-3.72l6.43 6.43a1 1 0 001.42 0 1 1 0 000-1.42z\">\n            </path>\n          </g>\n        </svg>\n        " + '<span class="control-tooltip end-0">قطع و وصل صدا (M)</span>';
      } else {
        volumeBtn.innerHTML = "\n        <svg viewBox=\"0 2 24 20\" width=\"21\" height=\"21\">\n          <g fill=\"currentcolor\" data-viewbox=\"0 0 24 24\">\n            <path\n                d=\"M12 4.12a1 1 0 00-1 0L5.71 7.5H2.5a1 1 0 00-1 1v7a1 1 0 001 1h3.21L11 19.84a1 1 0 00.54.16 1 1 0 001-1V5a1 1 0 00-.54-.88zM19.57 4.72a1 1 0 10-1.44 1.39 8.5 8.5 0 010 11.78 1 1 0 000 1.42 1 1 0 00.7.27 1 1 0 00.72-.3 10.51 10.51 0 000-14.56z\">\n            </path>\n            <path\n                d=\"M16.46 7.28a1 1 0 10-1.37 1.45 4.5 4.5 0 010 6.54 1 1 0 101.37 1.45 6.48 6.48 0 000-9.44z\">\n            </path>\n          </g>\n        </svg>\n      " + '<span class="control-tooltip end-0">قطع و وصل صدا (M)</span>';
      }
    });
  }

  //formatTime
  function formatTime(time) {
    var hours = Math.floor(time / 3600);
    var minutes = Math.floor(time % 3600 / 60);
    var seconds = Math.floor(time % 60);
    return "".concat(hours, ":").concat(minutes.toString().padStart(2, "0"), ":").concat(seconds.toString().padStart(2, "0"));
  }

  //loading
  if (video) {
    video.addEventListener('waiting', function () {
      loading.style.display = "block";
    });
    video.addEventListener('playing', function () {
      loading.style.display = "none";
    });

    //intro video to primary video
    video.addEventListener('ended', function () {
      video.src = video.getAttribute("primary-src");
      video.play();
    });
  }

  //user information move
  if (userInformation) {
    var positionArr = [{
      right: 24,
      top: 22
    }, {
      right: 60,
      top: 10
    }, {
      right: 30,
      top: 70
    }, {
      right: 65,
      top: 50
    }];
    var currentNumber = 0;
    if (userInformation) {
      setInterval(function () {
        if (userInformation) {
          userInformation.style.right = "".concat(positionArr[currentNumber].right, "%");
          userInformation.style.top = "".concat(positionArr[currentNumber].top, "%");
          if (currentNumber < positionArr.length - 1) {
            currentNumber++;
          } else {
            currentNumber = 0;
          }
        }
      }, 10000);
    }
  }

  //time video
  video.addEventListener("loadedmetadata", function () {
    video.addEventListener("canplaythrough", function () {
      var currentTime = video.currentTime;
      var duration = video.duration;
      if (currentTimeText) {
        currentTimeText.textContent = formatTime(currentTime);
        durationText.textContent = formatTime(duration);
        Times.classList.add("show");
      }
    });
  });

  // setting
  if (settingPanel) {
    setting.addEventListener("click", function () {
      settingPanel.style.right = "0";
    });
    closeSetting.addEventListener("click", function () {
      settingPanel.style.right = "-300px";
    });
  }


  //context menu
  if (video) {
    video.addEventListener("contextmenu", e => {
      e.preventDefault();
    })
  }


  //keyboard controlling
  function isElementVisible(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= window.innerHeight &&
      rect.right <= window.innerWidth
    );
  }

  // document.addEventListener('keydown', (event) => {
  //   console.log(event.code);
  //   if (isElementVisible(videoContainer)) {
  //     event.preventDefault();
  //     if (event.code === 'KeyK') {
  //       var isVideoFinished = video.currentTime >= video.duration;
  //       if (isVideoFinished) {
  //         video.play();
  //       } else {
  //         if (isPlay) {
  //           video.pause();
  //         } else {
  //           video.play();
  //         }
  //       }
  //     } else if (event.code === 'KeyL') {
  //       video.currentTime += 15;
  //     } else if (event.code === 'KeyJ') {
  //       video.currentTime -= 15;
  //     } else if (event.code === 'KeyM') {
  //       if (video.muted) {
  //         video.muted = false;
  //         volumeRange.value = 1;
  //       } else {
  //         video.muted = true;
  //         volumeRange.value = 0;
  //       }
  //     } else if (event.code === 'KeyF') {
  //       if (isFullscreen) {
  //         document.exitFullscreen();
  //         isFullscreen = false;
  //       } else {
  //         videoContainer.requestFullscreen();
  //         isFullscreen = true;
  //       }
  //     }
  //   }
  // });

  //controllers tooltip
  controls.forEach(el => {
    el.addEventListener("mousemove", () => {
      var tooltip = el.querySelector(".control-tooltip")
      if (tooltip) {
        tooltip.style.visibility = 'visible'
      }
    })
    el.addEventListener("mouseleave", () => {
      var tooltip = el.querySelector(".control-tooltip")
      if (tooltip) {
        tooltip.style.visibility = 'hidden'
      }
    })
  })

}
