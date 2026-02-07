// Improve touch interactions for services and gallery sections on mobile
(function() {
    function initTouchInteractions() {
        // Services section - ensure links are clickable
        const serviceItems = document.querySelectorAll('#services-1749 .cs-item');
        serviceItems.forEach(function(item) {
            const link = item.querySelector('.cs-link');
            if (link) {
                // Ensure the link covers the entire item area
                link.style.position = 'absolute';
                link.style.top = '0';
                link.style.left = '0';
                link.style.width = '100%';
                link.style.height = '100%';
                link.style.zIndex = '10';
                
                // Prevent background from blocking touches
                const background = item.querySelector('.cs-background');
                if (background) {
                    background.style.pointerEvents = 'none';
                }
            }
        });

        // Gallery section - improve touch responsiveness
        const galleryItems = document.querySelectorAll('#gallery-2281 .cs-image');
        galleryItems.forEach(function(item) {
            // Ensure the link is fully clickable
            item.style.cursor = 'pointer';
            item.style.webkitTapHighlightColor = 'transparent';
            
            // Show hover box on touch
            let touchStartTime = 0;
            item.addEventListener('touchstart', function(e) {
                touchStartTime = Date.now();
                item.classList.add('touched');
            }, { passive: true });
            
            item.addEventListener('touchend', function(e) {
                const touchDuration = Date.now() - touchStartTime;
                // If it was a quick tap (not a scroll), show the hover box
                if (touchDuration < 200) {
                    item.classList.add('touched');
                    // Remove the class after animation
                    setTimeout(function() {
                        item.classList.remove('touched');
                    }, 300);
                } else {
                    item.classList.remove('touched');
                }
            }, { passive: true });
        });
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTouchInteractions);
    } else {
        initTouchInteractions();
    }
})();
