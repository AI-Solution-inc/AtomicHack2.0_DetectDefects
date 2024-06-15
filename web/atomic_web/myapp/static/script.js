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


    // frame
    const frames = document.querySelectorAll('.result-frame');

    frames.forEach((frame) => {
        let width = frame.getAttribute('data-width');
        let height = frame.getAttribute('data-height');
        let x = frame.getAttribute('data-x');
        let y = frame.getAttribute('data-y');

        frame.style.width = `calc(${width} * 1000px)`;
        frame.style.height = `calc(${height} * 1000px)`;
        frame.style.left = `calc((${x} * 100px) - (${width / 2} * 100px))`;
        frame.style.top = `calc((${y} * 100px) - (${height / 2} * 100px))`;
    })
})