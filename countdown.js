

function updateCountdown() {
    const eventDate = new Date('2025-05-10T00:00:00'); // Data evenimentului
    const now = new Date();
    const timeDifference = eventDate - now;

    if (timeDifference < 0) {
        // Dacă evenimentul a trecut
        document.getElementById('days').querySelector('.countdown-number').textContent = '0';
        document.getElementById('hours').querySelector('.countdown-number').textContent = '0';
        document.getElementById('minutes').querySelector('.countdown-number').textContent = '0';
        document.getElementById('seconds').querySelector('.countdown-number').textContent = '0';
        return;
    }

    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    document.getElementById('days').querySelector('.countdown-number').textContent = days;
    document.getElementById('hours').querySelector('.countdown-number').textContent = hours;
    document.getElementById('minutes').querySelector('.countdown-number').textContent = minutes;
    document.getElementById('seconds').querySelector('.countdown-number').textContent = seconds;
}

// Actualizează countdown-ul la fiecare secundă
setInterval(updateCountdown, 1000);

// Inițializare countdown la încărcarea paginii
updateCountdown();
