(() => {
    const gallery = document.querySelector('#gallery-2281');
    const lightbox = document.querySelector('#gallery-2281-lightbox');
    if (!gallery || !lightbox) return;

    const imageEl = lightbox.querySelector('.cs-lightbox__image');
    const captionEl = lightbox.querySelector('.cs-lightbox__caption');
    const countEl = lightbox.querySelector('.cs-lightbox__count');
    const panel = lightbox.querySelector('.cs-lightbox__panel');

    let items = [];
    let currentIndex = 0;

    const getVisibleItems = (clicked) => {
        const galleryEl = clicked.closest('.cs-gallery');
        const visibleGallery = galleryEl && !galleryEl.classList.contains('cs-hidden') ? galleryEl : null;
        const scope = visibleGallery || gallery;
        return Array.from(scope.querySelectorAll('.cs-image'))
            .filter((item) => !item.closest('.cs-gallery')?.classList.contains('cs-hidden'));
    };

    const updateView = () => {
        const item = items[currentIndex];
        if (!item) return;

        const img = item.querySelector('img');
        const href = item.getAttribute('href');
        const tag = item.querySelector('.cs-tag')?.textContent?.trim();
        const project = item.querySelector('.cs-project')?.textContent?.trim();

        imageEl.src = href || img?.src || '';
        imageEl.alt = img?.alt || project || 'Gallery image';
        captionEl.textContent = [tag, project].filter(Boolean).join(' • ');
        countEl.textContent = `${currentIndex + 1} / ${items.length}`;
    };

    const open = (item) => {
        items = getVisibleItems(item);
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

    gallery.addEventListener('click', (event) => {
        const item = event.target.closest('.cs-image');
        if (!item) return;
        event.preventDefault();
        open(item);
    });

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
