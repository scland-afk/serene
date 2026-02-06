// FAQ functionality for all FAQ sections
(function() {
    function initFAQs() {
        const faqItems = Array.from(document.querySelectorAll('.cs-faq-item'));
        faqItems.forEach(function(item, index) {
            // Remove any existing active class to ensure all start closed
            item.classList.remove('active');
            
            const button = item.querySelector('.cs-button');
            const answer = item.querySelector('.cs-item-p');
            const answerId = answer && answer.id ? answer.id : ('faq-answer-' + index);
            if (answer && !answer.id) answer.id = answerId;

            if (button) {
                // Remove any existing event listeners by cloning the button
                const newButton = button.cloneNode(true);
                newButton.setAttribute('type', 'button');
                newButton.setAttribute('aria-expanded', 'false');
                if (answer) newButton.setAttribute('aria-controls', answerId);
                button.parentNode.replaceChild(newButton, button);
                
                newButton.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    const isOpen = item.classList.toggle('active');
                    newButton.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
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
