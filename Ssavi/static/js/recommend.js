// 앨범 위에 정보 띄우는 스크립트
function displayAlbumInfo(albumElement) {
    var albumInfo = albumElement.querySelector('.album_info');
    albumInfo.style.display = 'block';
    }

    function hideAlbumInfo(albumElement) {
    var albumInfo = albumElement.querySelector('.album_info');
    albumInfo.style.display = 'none';
    }

    function likeAlbum(albumElement) {
    // 좋아요 처리 로직 추가
    alert('좋아요가 클릭되었습니다.');
    }

    var albums = document.querySelectorAll('.recom_item');

    albums.forEach(function(albumElement) {
    albumElement.addEventListener('mouseover', function() {
        displayAlbumInfo(albumElement);
    });

    albumElement.addEventListener('mouseout', function() {
        hideAlbumInfo(albumElement);
    });
    });


// "recommend.js" 파일 내에서 수정된 슬라이드 스크립트
// 각 슬라이드 그룹을 식별하기 위해 클래스를 사용합니다.
const recomGroups = document.querySelectorAll(".recom-group");

recomGroups.forEach(group => {
    let pages = 0;
    let positionValue = 0;
    const IMAGE_WIDTH = 1000;
    const backBtn = group.querySelector(".back"); // 현재 그룹 내의 버튼 선택
    const nextBtn = group.querySelector(".next"); // 현재 그룹 내의 버튼 선택
    const images = group.querySelectorAll(".recom_item"); // 현재 그룹 내의 이미지 선택
    const all_page = images.length;

    // 다음으로 가는 기능
    function next() {
        if (pages < all_page) {
            backBtn.removeAttribute('disabled');
            for (let i = 0; i < images.length; i++) {
                images[i].style.transform = `translateX(${positionValue - 1000}px)`;
            }
            positionValue -= IMAGE_WIDTH;
            pages += 1;
            if (pages === all_page) {
                nextBtn.setAttribute('disabled', 'true');
            }
        }
    };

    // 이전으로 가는 기능
    function back() {
        if (pages > 0) {
            nextBtn.removeAttribute('disabled');
            for (let i = 0; i < images.length; i++) {
                images[i].style.transform = `translateX(${positionValue + 1000}px)`;
            }
            positionValue += IMAGE_WIDTH;
            pages -= 1;
            if (pages === 0) {
                backBtn.setAttribute('disabled', 'true');
            }
        }
    };

    function init() {
        backBtn.setAttribute('disabled', 'true');
        backBtn.addEventListener("click", back);
        nextBtn.addEventListener("click", next);
    };

    init();
});