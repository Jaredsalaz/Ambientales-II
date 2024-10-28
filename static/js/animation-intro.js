document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.getElementById("intro-animation").style.display = "none";
    }, 8000); // 5s delay + 3s animation duration

    // Crear hojas
    const leafContainer = document.getElementById('leaf-container');
    for (let i = 0; i < 10; i++) {
        let leaf = document.createElement('div');
        leaf.className = 'leaf';
        leafContainer.appendChild(leaf);
    }
});