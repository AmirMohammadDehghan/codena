const navbarCollapse = document.querySelector('.navbar-collapse');
const toggleNav = document.querySelector('#toggleNav');
const closeNav = document.querySelector('#closeNav');
const dimmer = document.querySelector('.dimmer')

if (navbarCollapse) {
    toggleNav.addEventListener('click', toggleNavFunc)
    closeNav.addEventListener('click', toggleNavFunc)
    dimmer.addEventListener('click', toggleNavFunc)
}

function toggleNavFunc() {
    toggleNav.classList.toggle('opened');
    toggleNav.setAttribute('aria-expanded', toggleNav.classList.contains('opened'))

    if (navbarCollapse.style.right === '0px') {
        navbarCollapse.style.right = '-333px'
        dimmer.style.opacity = '0'
        setTimeout(() => {
            dimmer.style.display = 'none'
        }, 400)
    } else {
        navbarCollapse.style.right = '0px'
        dimmer.style.display = 'block'
        setTimeout(() => {
            dimmer.style.opacity = '1'
        }, 400)
    }
}


//light and dark mode toggle
const dayNightCheckBox = document.querySelectorAll('#dayNightCheckBox')
const textLight = document.querySelectorAll('.text-light')
const textSecondary = document.querySelectorAll('.text-secondary')
const btnLight = document.querySelectorAll('.btn-light')
const btnOutlineLight = document.querySelectorAll('.btn-outline-light')
const borderLight = document.querySelectorAll('.border-light')
const logo = document.querySelectorAll('.navbar-brand img')
const linkLight = document.querySelectorAll('.link-light')
const bgDark = document.querySelectorAll('.bg-dark')
const wordFromCodnaImage = document.getElementById('wordFromCodnaImage')
let isNight = true;
if (dayNightCheckBox) {
    dayNightCheckBox.forEach(el => {
        el.addEventListener('change', () => {
            if (isNight) {
                document.body.classList.add('light-mode')
                isNight = false
            } else {
                document.body.classList.remove('light-mode')
                isNight = true
            }

            if (textLight) {
                textLight.forEach(el => {
                    el.classList.toggle('text-light')
                    el.classList.toggle('text-dark')
                })
            }
            if (textSecondary) {
                textSecondary.forEach(el => {
                    el.classList.toggle('text-secondary')
                    el.classList.toggle('text-muted')
                })
            }
            if (btnLight) {
                btnLight.forEach(el => {
                    el.classList.toggle('btn-light')
                    el.classList.toggle('btn-dark')
                })
            }
            if (btnOutlineLight) {
                btnOutlineLight.forEach(el => {
                    el.classList.toggle('btn-outline-light')
                    el.classList.toggle('btn-outline-dark')
                })
            }
            if (borderLight) {
                borderLight.forEach(el => {
                    el.classList.toggle('border-light')
                    el.classList.toggle('border-dark')
                })
            }
            if (logo) {
                logo.forEach(el => {
                    if (el.src === `${location.origin}/assets/img/logo-light.png`) {
                        el.src = './assets/img/logo.png'
                    } else {
                        el.src = './assets/img/logo-light.png'
                    }
                })
            }
            if (linkLight) {
                linkLight.forEach(el => {
                    el.classList.toggle('link-light')
                    el.classList.toggle('link-dark')
                })
            }
            if (bgDark) {
                bgDark.forEach(el => {
                    el.classList.toggle('bg-dark')
                    el.classList.toggle('bg-light')
                })
            }
            if (wordFromCodnaImage) {
                if (wordFromCodnaImage.src === `${location.origin}/assets/img/bg-semicircular.png`) {
                    wordFromCodnaImage.src = './assets/img/bg-semicircular-light.png'
                } else {
                    wordFromCodnaImage.src = './assets/img/bg-semicircular.png'
                }
            }
        })
    })
}

//
// var element = document.getElementById("pyCourse");

// window.addEventListener('scroll', () => {
//     var elementOffsetTop = element.offsetTop * 1.5;

//     var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

//     var windowHeight = window.innerHeight || document.documentElement.clientHeight;

//     if (scrollTop >= elementOffsetTop - windowHeight) {
//         element.style.transform = 'scale(1)'
//     } else {

//     }
// })

//back to top btn
const backToTopBtn = document.querySelector('.back-to-top-btn')
const backToTopContainer = document.getElementById('backToTopContainer')
const showOnPx = 100;

if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
        document.body.scrollIntoView({
            behavior: "smooth",
        });
    })

    const scrollContainer = () => {
        return document.documentElement || document.body;
    };

    document.addEventListener("scroll", () => {
        if (scrollContainer().scrollTop > showOnPx) {
            backToTopContainer.style.bottom = '0'
        } else {
            backToTopContainer.style.bottom = '-70px'
        }
    })
}

//search
const searchInput = document.getElementById('searchInput')
searchInput.addEventListener('keyup', searchHandler)
function searchHandler() {
    let filter, searchList, searchItems, a, i, txtValue;
    filter = searchInput.value.toUpperCase();
    searchList = document.getElementById("searchList");
    searchItems = searchList.getElementsByTagName("li");
    for (i = 0; i < searchItems.length; i++) {
        a = searchItems[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            searchItems[i].style.display = "";
        } else {
            searchItems[i].style.display = "none";
        }
    }
}

//video src change
const srcChangerEle = document.querySelectorAll('a[data-video-target-src]')
const videoPlayer = document.querySelector('video')
const vjsPoster = document.querySelector('.vjs-poster img')
if (srcChangerEle) {
    srcChangerEle.forEach(el => {
        el.addEventListener('click', e => {
            e.preventDefault();
            document.body.scrollIntoView({
                behavior: "smooth",
            });
            if (videoPlayer) {
                videoPlayer.src = el.getAttribute('data-video-target-src')
                vjsPoster.src = el.getAttribute('data-img-target-src')
            }
        })
    })
}

//symbol
const root = document.documentElement;
const symbolElementsDisplayed = getComputedStyle(root).getPropertyValue("--symbol-elements-displayed");
const symbolContent = document.querySelector("ul.symbol-content");

if (symbolContent) {
    root.style.setProperty("--symbol-elements", symbolContent.children.length);

    for (let i = 0; i < symbolElementsDisplayed; i++) {
        symbolContent.appendChild(symbolContent.children[i].cloneNode(true));
    }
}

(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()