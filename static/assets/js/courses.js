document.addEventListener("DOMContentLoaded",()=>{var e,t=document.querySelectorAll("a[data-video-target-src]"),r=document.querySelector("#videoCourse"),o=document.querySelector(".part-name"),n=document.getElementById("videoContainer"),_=document.getElementById("downloadLinkAttached");function i(e){let t={0:"۰",1:"۱",2:"۲",3:"۳",4:"۴",5:"۵",6:"۶",7:"۷",8:"۸",9:"۹"};e=e.toString().split("");let r="";for(let o=0;o<e.length;o++)e[o]=t[e[o]];for(let n=0;n<e.length;n++)r+=e[n];return r}t&&t.forEach(function(e){e.addEventListener("click",function(t){if(t.preventDefault(),r){r.setAttribute("src",e.getAttribute("data-video-target-src")),r.setAttribute("primary-src",e.getAttribute("data-video-target-src"));let i=e.querySelector(".accordion-course__part-name").innerHTML;o.innerHTML=i,n.scrollIntoView({behavior:"smooth",block:"start"}),r.play()}r.poster=e.getAttribute("data-img-target-src");var l=e.getAttribute("data-attached-url");l&&_&&_.setAttribute("href",l)})});var l=document.querySelector(".discount-card").getAttribute("data-future-time");if(l)var a=new Date(l).getTime(),$=setInterval(function(){var e=new Date().getTime(),t=a-e;document.querySelector(".days").innerHTML=i(Math.floor(t/864e5)),document.querySelector(".hours").innerHTML=i(Math.floor(t%864e5/36e5)),document.querySelector(".minutes").innerHTML=i(Math.floor(t%36e5/6e4)),document.querySelector(".seconds").innerHTML=i(Math.floor(t%6e4/1e3))},1e3);var s=document.getElementById("descriptionsContianer"),c=document.getElementById("showMore");c&&(c.onclick=function(){"container open"==s.className?(s.className="container",c.innerHTML=`نمایش بیشتر
    <svg width="24px" height="24px" viewBox="0 0 24 24" fill="none" style="rotate: 180deg;">
        <path
            d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
            stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </svg>
`):(s.className="container open",c.innerHTML=`نمایش کمتر
    <svg width="24px" height="24px" viewBox="0 0 24 24" fill="none">
        <path
            d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
            stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </svg>
`)});let d=document.querySelectorAll(".comment-collapse");d.forEach(e=>{let t=e.id,r=document.querySelector(`[data-bs-target="#${t}"]`),o=r.getAttribute("data-num-replay");e.addEventListener("show.bs.collapse",function(e){r.innerHTML=`
پنهان کردن
<svg width="20px" height="20px" viewBox="0 0 24 24" fill="none">
<path
d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
stroke="#fff" stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"></path>
</svg>
`}),e.addEventListener("hide.bs.collapse",function(e){r.innerHTML=`
نمایش
<strong>${o}</strong>
پاسخ
<svg width="20px" height="20px" viewBox="0 0 24 24" fill="none"
style="rotate: 180deg;">
<path
d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
stroke="#fff" stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"></path>
</svg>
`})});let u=document.querySelectorAll(".replay-btn"),f=document.getElementById("massage");u.forEach(e=>{e.addEventListener("click",function(){f.focus()})});let g=document.querySelectorAll('[for="touch"]');g&&g.forEach(e=>{let t=!1;e.addEventListener("click",()=>{let r=e.parentElement,o=r.querySelector(".accordion-course__item"),n=o.querySelectorAll(".accordion-course__item-container"),_=0;n.forEach(e=>{_+=e.offsetHeight}),t?(o.style.height=0,t=!1):(o.style.height=`${_}px`,t=!0);let i=e.querySelector(".accordion-course__icon");i.classList.toggle("active")})})});