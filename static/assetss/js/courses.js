document.addEventListener("DOMContentLoaded", () => {
    var srcChangerEle = document.querySelectorAll("a[data-video-target-src]"),
        videoPlayer = document.querySelector("#videoCourse_html5_api"),
        vjsPoster = document.querySelector('picture.vjs-poster img');

    if (srcChangerEle) {
        console.log(srcChangerEle)
        srcChangerEle.forEach(function (e) {
            console.log(e)
            e.addEventListener("click", function (r) {
                r.preventDefault()
                if (videoPlayer) {
                    videoPlayer.src = e.getAttribute("data-video-target-src")
                    console.log(videoPlayer.src)
                }
                vjsPoster.src = e.getAttribute("data-img-target-src")

                document.getElementById('videoContainer').scrollIntoView({behavior: 'smooth'});
            })
        });
    }
})

function seeVideo(link) {
    let video = document.querySelector("#videoCourse")
    video.src = link
}