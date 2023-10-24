    // 페이지가 로드될 때 실행될 함수

    // 'liketrack' 변수는 Python에서 전달된 변수로 JavaScript에서 사용 가능
    var likealbum = {{ likealbum|safe }};

    // 페이지가 로드될 때 실행될 함수
    window.addEventListener('load', function() {
        var heartIcons = document.querySelectorAll(".like-button");

        heartIcons.forEach(function(heartIcon) {
        
        var albumId = heartIcon.getAttribute("data-album-id");

        if (likealbum.includes(albumId)) {
            heartIcon.src = "{% static '/image/heart_icon2.png' %}";
        } else {
            heartIcon.src = "{% static '/image/heart_icon1.png' %}";
        }

        });   
    });

    function displayAlbumInfo(albumElement) {
        var albumInfo = albumElement.querySelector('.album_info');
        if (albumInfo) {
            albumInfo.style.display = 'block';
        }
    }
    
    function hideAlbumInfo(albumElement) {
        var albumInfo = albumElement.querySelector('.album_info');
        if (albumInfo) {
            albumInfo.style.display = 'none';
        }
    }

    function likeAlbum(heartIcon, albumId) {
        var currentImageSrc = heartIcon.src;
        var currentImageFileName = currentImageSrc.substr(currentImageSrc.lastIndexOf('/') + 1);
        
        if (currentImageFileName === 'heart_icon1.png') {
            heartIcon.src = '{% static "/image/heart_icon2.png" %}';
            likeTrack(albumId, true);
        } else {
            heartIcon.src = '{% static "/image/heart_icon1.png" %}';
            likeTrack(albumId, false);
        }
        
        event.preventDefault();
        event.stopPropagation();
    }

    function likeTrack(albumId, isLiked) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", '/like_album/', true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
        
        xhr.onreadystatechange = function() {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                console.log(this.responseText);
            }
        }
        
        if ({{ request.user.is_authenticated|lower }}) {
            xhr.send("id={{ request.user.id|default:'null' }}&album_id=" + albumId);
        } else {
            alert('로그인이 필요합니다.');
        }
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

// 장르별 페이지 버튼 클릭하면 넘기는 자바스크립트.
// 슬라이드쇼 기능은 css에 들어있다. transition: transform 0.5s ease
const recomGroups = document.querySelectorAll(".recom-group");

recomGroups.forEach(group => {
    let pages = 0;
    const IMAGE_WIDTH = 1000;
    const backBtn = group.querySelector(".back");
    const nextBtn = group.querySelector(".next");
    const images = group.querySelectorAll(".recom_item");
    const all_page = images.length;

    console.log(all_page)

    function slideShow() {
        const positionValue = -pages * IMAGE_WIDTH;
        for (let i = 0; i < images.length; i++) {
            images[i].style.transform = `translateX(${positionValue}px)`;
        }
    }

    function next() {
        if (pages < all_page - 1) {
            pages += 1;
            slideShow();
            backBtn.removeAttribute('disabled');
            if (pages === all_page - 1) {
                nextBtn.setAttribute('disabled', 'true');
            }
        }
    }

    function back() {
        if (pages > 0) {
            pages -= 1;
            slideShow();
            nextBtn.removeAttribute('disabled');
            if (pages === 0) {
                backBtn.setAttribute('disabled', 'true');
            }
        }
    }

    function init() {
        backBtn.setAttribute('disabled', 'true');
        backBtn.addEventListener("click", back);
        nextBtn.addEventListener("click", next);
    }

    init();
});
