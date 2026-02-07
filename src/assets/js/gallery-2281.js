class GalleryFilter {
    constructor() {
        this.filtersSelector = '#gallery-2281 .cs-button';
        this.imagesSelector = '#gallery-2281 .cs-gallery';
        this.activeClass = 'cs-active';
        this.hiddenClass = 'cs-hidden';

        const filters = document.querySelectorAll(this.filtersSelector);
        if (!filters.length) return;

        this.$activeFilter = filters[0];
        this.$images = document.querySelectorAll(this.imagesSelector);

        this.$activeFilter.classList.add(this.activeClass);

        for (const filter of filters) {
            filter.addEventListener('click', () => this.onClick(filter));
        }
    }

    onClick(filter) {
        this.filter(filter.dataset.filter);
        this.$activeFilter.classList.remove(this.activeClass);
        filter.classList.add(this.activeClass);
        this.$activeFilter = filter;
    }

    filter(filter) {
        const showAll = filter === 'all';
        for (const image of this.$images) {
            const show = showAll || image.dataset.category === filter;
            image.classList.toggle(this.hiddenClass, !show);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new GalleryFilter();
});
