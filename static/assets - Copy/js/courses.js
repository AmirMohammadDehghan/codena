document.addEventListener("DOMContentLoaded", () => {
    var srcChangerEle = document.querySelectorAll("a[data-video-target-src]"),
        videoPlayer = document.querySelector("#videoCourse")
    if (srcChangerEle) {
        srcChangerEle.forEach(function (e) {
            e.addEventListener("click", function (r) {
                r.preventDefault()
                if (videoPlayer) {
                    videoPlayer.setAttribute('primary-src', e.getAttribute("data-video-target-src"))
                    videoPlayer.play()
                }
                videoPlayer.poster = e.getAttribute("data-img-target-src")
                document.getElementById('videoContainer').scrollIntoView({ behavior: 'smooth' });
            })
        });
    }
})