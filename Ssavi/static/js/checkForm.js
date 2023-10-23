// checkForm.js : 폼 유효성 확인

window.onload = function() {
    // 폼의 유효성 확인
    // 폼의 [회원가입] 버튼 눌렀을 때 : submit 이벤트 발생 / 처리
    document.getElementById('login-form').onsubmit = function() {
      
        // (2) id 확인
        let id = document.getElementById("id");

        // id의 value 값을 가져와서(반환) 비었는지 확인 (get)
        if(id.value == ""){
            alert("ID을 입력하지 않았습니다. \nID를 입력하세요.");
            id.focus(); //ID 입력창으로 커서 이동
            return false; //submit되어 다음 페이지로 넘어가지 않게함
        }

        

        // id 길이 확인 : 6~10
        // 입력한 값의 길이 확인 : value의 length 확인
        // if(id.value.length < 6 || id.value.length >10){
        //     alert("아이디를 6~10자로 입력하세요");
        //     id.value = ""; // id의 value 값 설정 (set)
        //     id.focus(); 
        //     return false; 
        // }

        // (3) 비밀번호 일치 확인
        let pw = document.getElementById("password");
        let pwChk = document.getElementById("passwordCheck");

        if(pw.value != pwChk.value){
            alert("비밀번호 확인이 일치하지 않습니다.");
            pwChk.value = "";
            pwChk.focus();
            return false;
        }

        // (1) 성명을 입력하지 않은 경우 알림창 출력
        let name = document.getElementById('name');

        if(name.value == "") { // 성명을 입력하지 않았으면
            alert("성명을 입력하세요");
            name.focus(); // 성명 입력란에 포커스
            return false; // 다음 페이지로 이동하지 않게 (submit 되지 않게)
        }

        let email = document.getElementById('email');

        if(email.value == "") { // 이메일을 입력하지 않았으면
            alert("이메일을 입력하세요");
            email.focus(); // 이메일 입력란에 포커스
            return false; // 다음 페이지로 이동하지 않게 (submit 되지 않게)
        }

        // (4) select 태그 : 직업 선택하지 않은 경우
        // let job = document.getElementById("job");
       
        // 방법1 : selectedIndex 속성 사용
        // if(job.selectedIndex == 0) {
        //     alert("직업을 선택하세요");
        //     return false;
        // }

        // 방법2 : value 속성 사용
        // if(job.value == "") {
        //     alert("직업을 선택하세요");
        //     return false;
        // }

        // (5) '이메일 수시 여부' 라디오 버튼 선택하지 않은 경우
        // 라디오 버튼의 경우에는 id 속성을 사용하지 않고 그룹 이름인 name 속성 사용
        // 동일 그룹에 속한 여러 라디오 객체는 name 동일
        // 그룹 내에 여러 개의 라디오 객체가 있으므로 배열로 처리 : for문 사용
        // let chk = false; // 체크 여부 확인하는 변수. false로 초기화
        // for(let i=0; i<joinForm.emailRcv.length; i++){
        //     if(joinForm.emailRcv[i].checked == true) {
        //         chk = true; // 하나라도 체크되면 true로 설정
        //     }
        // }

        // 하나도 선택되지 않으면 false 값 그대로 있음
        // if(chk == false){
        //     alert("이메일  수신 여부를 선택하세요");
        //     return false;
        // }

        //(6) 체크박스 checkbox
        //여러 개 선택 가능
        // checked 속성이 true면 체크된 상태
        // false면 체크되지 않은 상태
        // 각 체크박스의 id 다르게 설정해서 id로 확인하면
        
        let agreement1 = document.getElementById("agreement1");
        let agreement2 = document.getElementById("agreement2");

        // 둘 다 체크해야 하는 경우 : 하나라도 체크하지 않은 경우
        if(agreement1.checked == false || agreement2.checked == false) {
            alert("모두 동의해야 합니다");
            return false;
        }

    }; // onsubmit 끝


}; // window.onload 끝