class Slideshow {
    constructor() {
        this.slides = Array.from(document.querySelectorAll('.cs-slide'));
        this.nextButton = document.querySelector('.cs-slideshow-next');
        this.prevButton = document.querySelector('.cs-slideshow-prev');
        this.currentIndex = 0;
        this.isMoving = false;
        this.init();
    }

    init() {
        if (this.slides.length === 0) return;
        this.nextButton?.addEventListener('click', () => this.moveSlide('next'));
        this.prevButton?.addEventListener('click', () => this.moveSlide('prev'));
        this.updateSlideStates();
    }

    updateSlideStates() {
        this.slides.forEach((slide, index) => {
            slide.classList.remove('active', 'prev', 'next', 'initial');
            if (index === this.currentIndex) {
                slide.classList.add('active');
            } else if (index === this.getAdjacentIndex('prev')) {
                slide.classList.add('prev');
            } else if (index === this.getAdjacentIndex('next')) {
                slide.classList.add('next');
            }
        });
    }

    getAdjacentIndex(direction) {
        const totalSlides = this.slides.length;
        if (direction === 'next') {
            return (this.currentIndex + 1) % totalSlides;
        }
        return (this.currentIndex - 1 + totalSlides) % totalSlides;
    }

    moveSlide(direction) {
        if (this.isMoving) return;
        this.isMoving = true;
        this.currentIndex = this.getAdjacentIndex(direction);
        this.updateSlideStates();
        setTimeout(() => {
            this.isMoving = false;
        }, 300);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new Slideshow();
});
