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
        navbarCollapse.style.right = '-100vw'
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



//sticky header
window.onscroll = function () { myFunction() };

var header = document.querySelector("header");

function myFunction() {
    if (window.pageYOffset >= 100) {
        header.classList.add("sticky")
    } else {
        header.classList.remove("sticky");
    }
}