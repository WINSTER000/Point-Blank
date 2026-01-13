// State Management
let cart = [];
let currentPage = '/';
let selectedProductId = null;
let filters = {
    category: 'all',
    priceRange: 'all',
    search: ''
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    checkAgeVerification();
    loadCart();
    updateCartCount();
});

// Age Verification
function checkAgeVerification() {
    const verified = sessionStorage.getItem('ageVerified');
    if (verified === 'true') {
        document.getElementById('ageVerificationModal').classList.add('hidden');
    }
}

function success() {
    const verified = sessionStorage.getItem('ageVerified');
    if (verified === 'true') {
        document.getElementById('ageVerificationModal').classList.add('hidden');
    }
}

function verifyAge(isOver21) {
    if (isOver21) {
        sessionStorage.setItem('ageVerified', 'true');
        document.getElementById('ageVerificationModal').classList.add('hidden');
    } else {
        document.getElementById('ageError').style.display = 'block';
        setTimeout(() => {
            window.location.href = 'https://www.youtube.com/watch?v=OgKl0DK4Bc4';
        }, 1000);
    }
}



// 404 Page JavaScript

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateCurrentTime();
    startAutoRedirect();
    addGlitchEffect();
});

// Update current time
function updateCurrentTime() {
    const now = new Date();
    const timeString = now.toLocaleString('en-US', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
    });
    
    document.getElementById('currentTime').textContent = timeString;
}

// Auto redirect countdown
let redirectTimer = null;
let redirectCountdown = 10;

function startAutoRedirect() {
    // Show redirect notice after 3 seconds
    setTimeout(() => {
        const notice = document.getElementById('redirectNotice');
        notice.style.display = 'flex';
        
        // Start countdown
        redirectTimer = setInterval(() => {
            redirectCountdown--;
            document.getElementById('countdown').textContent = redirectCountdown;
            
            if (redirectCountdown <= 0) {
                clearInterval(redirectTimer);
                window.location.href = 'index.html';
            }
        }, 1000);
    }, 3000);
}

function cancelRedirect() {
    if (redirectTimer) {
        clearInterval(redirectTimer);
        redirectTimer = null;
    }
    
    const notice = document.getElementById('redirectNotice');
    notice.style.display = 'none';
    
    // Show confirmation
    const confirmation = document.createElement('div');
    confirmation.style.cssText = `
        position: fixed;
        top: 2rem;
        right: 2rem;
        background-color: var(--color-zinc-900);
        border: 1px solid var(--color-green-600);
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        color: #86efac;
        font-size: 0.875rem;
        z-index: 1000;
        animation: slideIn 0.3s ease-out;
    `;
    confirmation.textContent = 'Auto-redirect canceled';
    document.body.appendChild(confirmation);
    
    // Remove after 3 seconds
    setTimeout(() => {
        confirmation.remove();
    }, 3000);
}

// Handle search
function handleSearch(event) {
    event.preventDefault();
    
    const searchInput = document.getElementById('searchInput');
    const query = searchInput.value.trim();
    
    if (!query) {
        alert('Please enter a search term');
        return;
    }
    
    // In production, this would search the site
    // For demo, redirect to products page
    alert(`Searching for: "${query}"\n\nIn production, this would search the product catalog.`);
    
    // Redirect to main site
    window.location.href = 'index.html';
}

// Add glitch effect to error code
function addGlitchEffect() {
    const errorCode = document.querySelector('.error-code');
    
    // Random glitch effect every 5-10 seconds
    setInterval(() => {
        if (Math.random() > 0.5) {
            errorCode.classList.add('glitch');
            setTimeout(() => {
                errorCode.classList.remove('glitch');
            }, 1000);
        }
    }, Math.random() * 5000 + 5000);
}

// Log 404 error (for analytics)
function log404Error() {
    const errorData = {
        timestamp: new Date().toISOString(),
        url: window.location.href,
        referrer: document.referrer || 'Direct',
        userAgent: navigator.userAgent
    };
    
    console.log('404 Error Logged:', errorData);
    
    // In production, send to analytics service
    // sendToAnalytics(errorData);
}

// Call on load
log404Error();

// Easter egg - Konami code
let konamiCode = [];
const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

document.addEventListener('keydown', (e) => {
    konamiCode.push(e.key);
    konamiCode = konamiCode.slice(-10);
    
    if (konamiCode.join(',') === konamiSequence.join(',')) {
        activateEasterEgg();
    }
});

function activateEasterEgg() {
    const errorCode = document.querySelector('.error-code');
    errorCode.style.animation = 'rainbow 2s linear infinite';
    
    const style = document.createElement('style');
    style.textContent = `
        @keyframes rainbow {
            0% { color: #dc2626; }
            16% { color: #ea580c; }
            33% { color: #ca8a04; }
            50% { color: #16a34a; }
            66% { color: #2563eb; }
            83% { color: #7c3aed; }
            100% { color: #dc2626; }
        }
    `;
    document.head.appendChild(style);
    
    alert('🎯 Easter egg activated! You found the secret!');
}
