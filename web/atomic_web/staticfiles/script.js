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
    const widthImg = document.querySelector('.result-img').width;
    const heigthImg = document.querySelector('.result-img').height;

    frames.forEach((frame) => {
        let width = frame.getAttribute('data-width');
        let height = frame.getAttribute('data-height');
        let x = frame.getAttribute('data-x');
        let y = frame.getAttribute('data-y');

        // frame.style.width = `${width * widthImg}px`;
        // frame.style.height = `${height * heigthImg}px`;
        // frame.style.left = `${x * widthImg}px`;
        // frame.style.top = `${y * heigthImg}px`;
        frame.style.width = `calc(${width * widthImg}px )`;
        frame.style.height = `calc(${height * heigthImg}px )`;
        frame.style.left = `calc((${x * widthImg}px) + (${widthImg / 2}px))`;
        frame.style.top = `calc((${y * heigthImg}px)  + (${heigthImg / 2}px))`;

    })

})