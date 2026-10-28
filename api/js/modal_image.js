const imageModalEl = document.getElementById('carousel_modal_window');
const imageModal = document.getElementById('modal_image');
const textModal = document.getElementById('modal_text');
const imageModalWindow = new bootstrap.Modal(imageModalEl);


function ClickHandler(event) {
    let obj = event.target.closest('.post_photo');
    if (!obj) {
        return;
    }

    imageModal.src = obj.src;
    imageModalWindow.show();
    if (obj.alt.trim() && obj.alt !== "None") {
        textModal.hidden = false;
        textModal.textContent = obj.alt;
    }
    else {
        textModal.hidden = true;
    }
}

let HandlerBox = document.getElementById('posts_container');

HandlerBox.addEventListener('click', ClickHandler);
