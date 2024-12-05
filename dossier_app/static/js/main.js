// main.js

// Function to handle a click event for navigation
document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        link.addEventListener("click", (event) => {
            console.log(`Navigating to: ${event.target.href}`);
        });
    });
});

// Function to confirm deletion in admin panel
function confirmDeletion() {
    return confirm("Are you sure you want to delete this item?");
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("Dossier Application Ready!");
});
