// // 슬라이드쇼 관련 스크립트
// let pages = 0;
// let positionValue = 0;
// const IMAGE_WIDTH = 1000;

// // 다음으로 가는 기능
// function next(images, backBtn, nextBtn) {
//     for (let i = 0; i < images.length; i++) {
//         let positionValue = parseInt(getComputedStyle(images[i]).transform.split(',')[4]);
//         images[i].style.transform = `translateX(${positionValue - IMAGE_WIDTH}px)`;
//     }

//     backBtn.removeAttribute('disabled');
//     const positionValue = parseInt(getComputedStyle(images[0]).transform.split(',')[4]);
//     if (positionValue - IMAGE_WIDTH <= -IMAGE_WIDTH * (images.length - 4)) {
//         nextBtn.setAttribute('disabled', 'true');
//     }
// }

// // 이전으로 가는 기능
// function back(images, backBtn, nextBtn) {
//     for (let i = 0; i < images.length; i++) {
//         let positionValue = parseInt(getComputedStyle(images[i]).transform.split(',')[4]);
//         images[i].style.transform = `translateX(${positionValue + IMAGE_WIDTH}px)`;
//     }

//     nextBtn.removeAttribute('disabled');
//     const positionValue = parseInt(getComputedStyle(images[0]).transform.split(',')[4]);
//     if (positionValue + IMAGE_WIDTH >= 0) {
//         backBtn.setAttribute('disabled', 'true');
//     }
// }

// function init() {
//     const backBtns = document.querySelectorAll(".back");
//     const nextBtns = document.querySelectorAll(".next");
//     const recomDisplays = document.querySelectorAll(".recom_display");

//     backBtns.forEach((backBtn, index) => {
//         const nextBtn = nextBtns[index];
//         const images = recomDisplays[index].querySelectorAll(".recom_item");

//         backBtn.setAttribute('disabled', 'true');
//         backBtn.addEventListener("click", () => back(images, backBtn, nextBtn));
//         nextBtn.addEventListener("click", () => next(images, backBtn, nextBtn));
//     });
// }

// init();