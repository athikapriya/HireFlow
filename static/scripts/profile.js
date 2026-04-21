
document.addEventListener("DOMContentLoaded", function () {

    const input = document.getElementById('id_profile_image');
    const preview = document.getElementById('previewImg');
    const uploadBtn = document.getElementById('uploadBtn');
    const wrapper = document.getElementById('imageWrapper');

    if (!input || !preview) return;

    uploadBtn?.addEventListener('click', function (e) {
        e.preventDefault();
        input.click();
    });

    wrapper?.addEventListener('click', function () {
        input.click();
    });

    input.addEventListener('change', function () {
        const file = this.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                preview.src = e.target.result;
            };

            reader.readAsDataURL(file);
        }
    });

});