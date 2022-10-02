window.onload = function () {
    window.addEventListener('scroll', function (e) {
        if(window.pageYOffset >100) {
            this.document.querySelector("header").classList.add('is-scrolling');
        } else {
            this.document.querySelector("header").classList.remove('is-scrolling');
        }
    });

const hamburger = document.querySelector('.hamburger');
const mobile_menu = document.querySelector('.navmenu');

hamburger.addEventListener('click', function() {
    hamburger.classList.toggle('active');
    mobile_menu.classList.toggle('active');
});

}


