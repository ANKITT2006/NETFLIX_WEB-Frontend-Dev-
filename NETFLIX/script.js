// ==========================================
// FAQ ACCORDION INTERACTION
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
    const faqBoxes = document.querySelectorAll(".faq-box");

    faqBoxes.forEach((box) => {
        box.addEventListener("click", () => {
            const answer = box.nextElementSibling;
            const isOpen = answer.classList.contains("show");

            // Close all answers first (Accordion style)
            document.querySelectorAll(".faq-answer").forEach((ans) => {
                ans.classList.remove("show");
            });
            document.querySelectorAll(".faq-box").forEach((b) => {
                b.classList.remove("active");
            });

            // If it wasn't open, open it
            if (!isOpen) {
                answer.classList.add("show");
                box.classList.add("active");
            }
        });
    });

    // ==========================================
    // EMAIL FORM VALIDATION & INTERACTION
    // ==========================================
    const forms = document.querySelectorAll(".cta-form");

    forms.forEach((form) => {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            const input = form.querySelector(".email-input");
            const email = input.value.trim();

            if (email && validateEmail(email)) {
                alert(`Welcome to Netflix! We've sent a sign-up link to: ${email}`);
                input.value = "";
            } else {
                alert("Please enter a valid email address.");
                input.focus();
            }
        });
    });

    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }
});

