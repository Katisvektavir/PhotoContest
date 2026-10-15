const imageModalEl = document.getElementById('carousel_modal_window');
const imageModal = document.getElementById('modal_image')
const textModal = document.getElementById('modal_text')
const imageModalWindow = new bootstrap.Modal(imageModalEl);


function ClickHandler(event) {
    obj = event.target.closest('.post_photo');
    if (!obj) {
        return;
    }

    imageModal.src = obj.src;
    imageModalWindow.show();
    if (obj.alt.trim() && obj.alt != "None") {
        textModal.hidden = false;
        textModal.textContent = obj.alt;
    }
    else {
        textModal.hidden = true;
    }
}

let HandlerBox = document.querySelectorAll('.post_box');

HandlerBox.forEach((item) =>{
    item.addEventListener('click', ClickHandler);
}) ;
