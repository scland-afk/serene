(() => {
    const lightbox = document.querySelector('#gallery-48-lightbox');
    const galleries = document.querySelectorAll('[data-lightbox-gallery]');
    if (!lightbox || !galleries.length) return;

    const imageEl = lightbox.querySelector('.cs-lightbox__image');
    const captionEl = lightbox.querySelector('.cs-lightbox__caption');
    const countEl = lightbox.querySelector('.cs-lightbox__count');
    const panel = lightbox.querySelector('.cs-lightbox__panel');

    let items = [];
    let currentIndex = 0;

    const updateView = () => {
        const item = items[currentIndex];
        if (!item) return;
        const full = item.getAttribute('data-full') || '';
        const caption = item.getAttribute('data-caption') || '';

        imageEl.src = full;
        imageEl.alt = caption || 'Gallery image';
        captionEl.textContent = caption;
        countEl.textContent = `${currentIndex + 1} / ${items.length}`;
    };

    const open = (gallery, item) => {
        items = Array.from(gallery.querySelectorAll('.cs-lightbox-trigger'));
        currentIndex = Math.max(0, items.indexOf(item));
        lightbox.classList.add('is-open');
        lightbox.setAttribute('aria-hidden', 'false');
        updateView();
        panel.focus({ preventScroll: true });
    };

    const close = () => {
        lightbox.classList.remove('is-open');
        lightbox.setAttribute('aria-hidden', 'true');
        imageEl.src = '';
    };

    const next = () => {
        if (!items.length) return;
        currentIndex = (currentIndex + 1) % items.length;
        updateView();
    };

    const prev = () => {
        if (!items.length) return;
        currentIndex = (currentIndex - 1 + items.length) % items.length;
        updateView();
    };

    for (const gallery of galleries) {
        gallery.addEventListener('click', (event) => {
            const item = event.target.closest('.cs-lightbox-trigger');
            if (!item) return;
            event.preventDefault();
            open(gallery, item);
        });
    }

    lightbox.addEventListener('click', (event) => {
        const action = event.target.getAttribute('data-action');
        if (action === 'close') {
            close();
        } else if (action === 'next') {
            next();
        } else if (action === 'prev') {
            prev();
        }
    });

    document.addEventListener('keydown', (event) => {
        if (!lightbox.classList.contains('is-open')) return;
        if (event.key === 'Escape') close();
        if (event.key === 'ArrowRight') next();
        if (event.key === 'ArrowLeft') prev();
    });
})();
