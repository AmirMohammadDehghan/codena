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
let themeMode;
if (!localStorage.getItem('themeMode')) {
    localStorage.setItem('themeMode', 'dark')
    themeMode = localStorage.getItem('themeMode')
}
themeMode = localStorage.getItem('themeMode')

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
let isNight;
if (themeMode === 'dark') {
    isNight = true;
} else {
    isNight = false;
}

if (dayNightCheckBox) {
    dayNightCheckBox.forEach(el => {
        el.addEventListener('change', () => {
            if (isNight) {
                themeLighter()
                if (bgDark) {
                    bgDark.forEach(el => {
                        el.classList.toggle('bg-dark')
                        el.classList.toggle('bg-light')
                    })
                }
            } else {
                themeDarker()
                if (bgDark) {
                    bgDark.forEach(el => {
                        el.classList.toggle('bg-dark')
                        el.classList.toggle('bg-light')
                    })
                }
            }
        })
    })
}

if (isNight) {
    themeDarker()
} else {
    themeLighter()
}

function themeDarker() {
    themeMode = localStorage.setItem('themeMode', 'dark')
    document.body.classList.remove('light-mode')
    isNight = true
    if (logo) {
        logo.forEach(el => {
            el.src = 'https://codena.org/static/assets/img/logo.png'
        })
    }
    if (wordFromCodnaImage) {
        wordFromCodnaImage.src = 'https://codena.org/static/assets/img/bg-semicircular.png'
    }

    if (textLight) {
        textLight.forEach(el => {
            el.classList.replace('text-dark', 'text-light')
        })
    }

    if (textSecondary) {
        textSecondary.forEach(el => {
            el.classList.replace('text-muted', 'text-secondary')
        })
    }

    if (btnLight) {
        btnLight.forEach(el => {
            el.classList.replace('btn-light', 'btn-dark')
        })
    }

    if (btnOutlineLight) {
        btnOutlineLight.forEach(el => {
            el.classList.replace('btn-outline-light', 'btn-outline-dark')
        })
    }

    if (borderLight) {
        borderLight.forEach(el => {
            el.classList.replace('border-dark', 'border-light')
        })
    }

    if (linkLight) {
        linkLight.forEach(el => {
            el.classList.replace('link-dark', 'link-light')
        })
    }
}

function themeLighter() {
    themeMode = localStorage.setItem('themeMode', 'light')
    document.body.classList.add('light-mode')
    isNight = false
    if (logo) {
        logo.forEach(el => {
            el.src = 'https://codena.org/static/assets/img/logo-light.png'
        })
    }
    if (wordFromCodnaImage) {
        wordFromCodnaImage.src = 'static' +
            'https://codena.org/static/assets/img/bg-semicircular-light.png'
    }
    if (textLight) {
        textLight.forEach(el => {
            el.classList.replace('text-light', 'text-dark')
        })
    }
    if (textSecondary) {
        textSecondary.forEach(el => {
            el.classList.replace('text-secondary', 'text-muted')
        })
    }

    if (btnLight) {
        btnLight.forEach(el => {
            el.classList.replace('btn-dark', 'btn-light')
        })
    }

    if (btnOutlineLight) {
        btnOutlineLight.forEach(el => {
            el.classList.replace('btn-outline-dark', 'btn-outline-light')
        })
    }

    if (borderLight) {
        borderLight.forEach(el => {
            el.classList.replace('border-light', 'border-dark')
        })
    }

    if (linkLight) {
        linkLight.forEach(el => {
            el.classList.replace('link-light', 'link-dark')
        })
    }
}

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
if (searchInput) {
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

if (document.querySelector('#specialDiscountModal')) {
    const specialDiscountModal = new bootstrap.Modal('#specialDiscountModal', {})
    specialDiscountModal.show()
}

    if (window.innerWidth > 992) {
        const dropdownToggle = document.querySelectorAll('.dropdown-toggle')
        const dimmer = document.querySelector('.dimmer')
        dropdownToggle.forEach(el => {
            el.addEventListener('show.bs.dropdown', event => {
                dimmer.style.display = 'block'
                setTimeout(() => {
                    dimmer.style.opacity = '1'
                }, 1)
            })

            el.addEventListener('hide.bs.dropdown', event => {
                dimmer.style.opacity = '0'
                setTimeout(() => {
                    dimmer.style.display = 'none'
                }, 400)
            })
        })
    }