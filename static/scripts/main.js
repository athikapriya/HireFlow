document.addEventListener("DOMContentLoaded", function () {

    const toggleBtn = document.getElementById("sidebarToggle");
    const sidebar = document.getElementById("sidebar-wrapper");
    const mainContent = document.getElementById("main-content");

    let isCollapsed = false;

    toggleBtn.addEventListener("click", function () {
        isCollapsed = !isCollapsed;

        sidebar.classList.toggle("collapsed");
        mainContent.classList.toggle("expanded");

        document.body.classList.toggle("sidebar-collapsed");

        toggleBtn.innerHTML = isCollapsed
            ? '<i class="fa-solid fa-bars fs-5"></i>'
            : '<i class="fa-solid fa-xmark fs-5"></i>';
    });

});