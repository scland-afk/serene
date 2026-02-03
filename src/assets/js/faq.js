// FAQ functionality for all FAQ sections
(function() {
    function initFAQs() {
        const faqItems = Array.from(document.querySelectorAll('.cs-faq-item'));
        faqItems.forEach(function(item) {
            // Remove any existing active class to ensure all start closed
            item.classList.remove('active');
            
            const button = item.querySelector('.cs-button');
            if (button) {
                // Remove any existing event listeners by cloning the button
                const newButton = button.cloneNode(true);
                newButton.setAttribute('type', 'button');
                button.parentNode.replaceChild(newButton, button);
                
                newButton.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    item.classList.toggle('active');
                });
            } else {
                // Fallback: if no button, make the whole item clickable
                item.addEventListener('click', function(e) {
                    e.preventDefault();
                    item.classList.toggle('active');
                });
            }
        });
    }
    
    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFAQs);
    } else {
        initFAQs();
    }
})();
