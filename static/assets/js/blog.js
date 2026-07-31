const tables = document.querySelectorAll("table"); tables.forEach(e => { let t = document.createElement("div"); t.classList.add("table-wrapper"), e.parentNode.insertBefore(t, e), t.appendChild(e) }); var allTd = document.querySelectorAll("td"); allTd.forEach(e => { var t, o = e.querySelector("p"); o.offsetHeight > 140 && o.classList.add("w-200") }); const labelTouch = document.querySelectorAll('[for="touch"]'); function changeElementColorWithInlineStyle() { let e = document.querySelectorAll('[style*="color"]'); e.forEach(e => { e.style.color.includes("rgb(31, 55, 99)") && (e.style.color = "#9c5aff") }) } labelTouch && labelTouch.forEach(e => { let t = !1; e.addEventListener("click", () => { let o = e.parentElement, l = o.querySelector(".accordion-course__item"), n = l.querySelectorAll(".accordion-course__item-container"), r = 0; n.forEach(e => { r += e.offsetHeight }), t ? (l.style.height = 0, t = !1) : (l.style.height = `${r}px`, t = !0); let s = e.querySelector(".accordion-course__icon"); s.classList.toggle("active") }) }), changeElementColorWithInlineStyle(); const postLink = location.href, postLinkElement = document.getElementById("postLink"), copyLink = document.getElementById("copyLink"); postLinkElement.innerHTML = postLink; const copyLinkAlert = document.getElementById("copyLinkAlert"), toastBootstrap = bootstrap.Toast.getOrCreateInstance(copyLinkAlert); copyLink.addEventListener("click", () => { navigator.clipboard.writeText(postLink), toastBootstrap.show() }); const collapseElementList = document.querySelectorAll(".comment-collapse"); collapseElementList.forEach(e => {
    let t = e.id, o = document.querySelector(`[data-bs-target="#${t}"]`), l = o.getAttribute("data-num-replay"); e.addEventListener("show.bs.collapse", function (e) {
        o.innerHTML = `
    پنهان کردن
    <svg width="20px" height="20px" viewBox="0 0 24 24" fill="none">
        <path
            d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
            stroke="#fff" stroke-width="1.5" stroke-linecap="round"
            stroke-linejoin="round"></path>
    </svg>
`}), e.addEventListener("hide.bs.collapse", function (e) {
            o.innerHTML = `
    نمایش
    <strong>${l}</strong>
    پاسخ
    <svg width="20px" height="20px" viewBox="0 0 24 24" fill="none"
        style="rotate: 180deg;">
        <path
            d="M12 7V17M12 7L16 11M12 7L8 11M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
            stroke="#fff" stroke-width="1.5" stroke-linecap="round"
            stroke-linejoin="round"></path>
    </svg>
    `})
}); const replayBtn = document.querySelectorAll(".replay-btn"), massageTextArea = document.getElementById("massage"); replayBtn.forEach(e => { e.addEventListener("click", function () { massageTextArea.focus() }) });