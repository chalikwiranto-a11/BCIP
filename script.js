document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.getElementById('navbar');
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const dropdowns = document.querySelectorAll('.dropdown');

    // Sticky navbar effect on scroll
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.padding = '15px 50px';
            navbar.style.background = 'rgba(255, 255, 255, 1)';
            navbar.style.boxShadow = '0 5px 20px rgba(0,0,0,0.1)';
        } else {
            navbar.style.padding = '20px 50px';
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    });

    // Mobile menu toggle
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Mobile dropdown toggle
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                dropdown.classList.toggle('active');
            }
        });
    });

    // E-Induction Modal logic
    const eInductionBtns = document.querySelectorAll('.e-induction-btn');
    const modal = document.getElementById('e-induction-modal');
    const closeModalBtn = document.querySelector('.close-modal');

    if (modal) {
        eInductionBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                modal.classList.add('show');
            });
        });

        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', () => {
                modal.classList.remove('show');
            });
        }

        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('show');
            }
        });
    }
});
