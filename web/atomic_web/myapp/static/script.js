document.addEventListener('DOMContentLoaded', () => {
    // file input
    previewImage = (event) => {
        const input = event.target;
        const wrapper = document.getElementById("form-input-wrapper");
        const label = document.querySelector(".form-label");
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.onload = function (e) {
                wrapper.style.backgroundImage = `url(${e.target.result})`;
                label.classList.add("hidden");
            };
            reader.readAsDataURL(input.files[0]);
        }
    };

    document
        .getElementById("form-input-wrapper")
        .addEventListener("click", () => {
            document.getElementById("photo").click();
        });
})