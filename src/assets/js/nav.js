// add classes for mobile navigation toggling
document.addEventListener('DOMContentLoaded', function() {
    var CSbody = document.querySelector("body");
    const CSnavbarMenu = document.querySelector("#cs-navigation");
    const CShamburgerMenu = document.querySelector("#cs-navigation .cs-toggle");
    const csUL = document.querySelector('#cs-expanded');

    // Initialize aria-expanded attribute
    if (csUL && !csUL.hasAttribute('aria-expanded')) {
        csUL.setAttribute('aria-expanded', 'false');
    }

    if (CShamburgerMenu) {
        CShamburgerMenu.addEventListener('click', function() {
            CShamburgerMenu.classList.toggle("cs-active");
            CSnavbarMenu.classList.toggle("cs-active");
            CSbody.classList.toggle("cs-open");
            ariaExpanded();
        });
    }

    function ariaExpanded() {
        if (!csUL) return;
        const csExpanded = csUL.getAttribute('aria-expanded');
        if (csExpanded === 'false') {
            csUL.setAttribute('aria-expanded', 'true');
        } else {
            csUL.setAttribute('aria-expanded', 'false');
        }
    }

    // mobile nav toggle code
    const dropDowns = Array.from(document.querySelectorAll('#cs-navigation .cs-dropdown'));
    for (const item of dropDowns) {
        const onClick = () => item.classList.toggle('cs-active');
        item.addEventListener('click', onClick);
    }

    // after scrolling down 100px, add .scroll class to the #cs-navigation
    document.addEventListener('scroll', function() {
        const scroll = document.documentElement.scrollTop;
        var nav = document.querySelector('#cs-navigation');
        if (nav) {
            if (scroll >= 100) nav.classList.add('scroll');
            else nav.classList.remove('scroll');
        }
    }, { passive: true });
});

// Remove preload after load so transitions run (prevents menu flash on refresh)
window.addEventListener('load', function() {
    document.body.classList.remove('preload');
});
