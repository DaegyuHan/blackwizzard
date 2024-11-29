
<img src="https://github.com/user-attachments/assets/2d3f3e29-44c0-4d64-9916-fbb35ac348f7" alt="검은마법사" width="210" height="250">


# 나의 해방일지 v1.8.3
### 🔗 서비스 링크
https://www.blackwizzard.net ( 서비스 종료로 인한 중지 )

### ⏲ 개발 기간
> 기간 2023.06 ~ 2023.11

### 👥 개발 인원
> 디자인,프론트,서버 개발 1인

### 사용 기술
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white)
---

## 🧙‍♂️ 프로젝트 소개
"메이플스토리" 라는 게임을 같이 하던 지인들의 고충을 해결해준 게임 일정 체크 및 기록 웹 서비스

## 🧙‍♂️ 주요 기능
### 🍄 캐릭터 정보
![image](https://github.com/user-attachments/assets/110e88c6-543d-4ca0-8236-ce8728642e01)

- 크롤링을 통해 게임 사이트로부터 캐릭터 아바타와 세부 능력치를 자동 업데이트

### 🍄 퀘스트 진행 및 보스 몬스터 처치 진행도 체크
![image](https://github.com/user-attachments/assets/9b3540de-5de1-48a6-9e8f-fab5e70c299d)

  
- 사용자가 진행한 퀘스트 및 어떤 보스 몬스터를 처치했는지 확인
- 클릭 시 명암처리로 진행 유무 확인

![image](https://github.com/user-attachments/assets/7d43c74f-3966-4f7a-a5e9-ea479c4aa758)

- 진행한 퀘스트 및 보스를 클릭함에 따라 진행도 쉽게 확인 가능

### 🍄 버프 아이템 사용 체크
![image](https://github.com/user-attachments/assets/be13f937-3b9f-422d-8629-d6fcde2f4318)

- 게임 플레이 전 잊은 버프 아이템이 있는지 확인
- 클릭 시 명암처리로 사용 유무 확인

### 🍄 모두가 함께 적는 공지사항
![image](https://github.com/user-attachments/assets/e8a1217b-e2c1-40e7-bdaa-fc96fff5bbf8)

- 함께 공유하면 좋을 공지사항을 모두가 자유롭게 공유하는 공간

### 🍄 이벤트 확인
![image](https://github.com/user-attachments/assets/ae648978-0d54-4653-a32e-d8321567a38f)

- 실제 이벤트 공지 페이지로 이동

---
## 💡 업데이트 내역
<details>
  <summary>업데이트 내역 펼쳐보기</summary>
  
2023.11.26 v1.8.3
union3 변수 제거

2023.10.28 v1.8.2
일일초기화 방식 롤백

2023.10.25 v1.8.1
web logo 적용, tab27 사용자 변경 (서버 주소 변경 URL27 삭제), 일일초기화 구현 코드 변경 ( localStorage 사용, 안정성 향상 ), 할로윈 이벤트 시작 ( 일일퀘스트 빨강단풍잎, 보물찾기 버튼 삭제, 레범몬 버튼 추가, 이벤트탭 펀치킹 제외 삭제)

2023.10.24 v1.7.9
tab45 서버 주소 변경, union 값 서버 유지, 졸업심볼 변경, 색상 변경, tab27 에스페라 심볼 추가

2023.10.21 v1.7.8
tab27 어센틱 지역 심볼 삭제, 일일퀘스트 최대 수량 변경

2023.10.13 v1.7.7
각 tab 재획 기능 버튼 에러 수정

2023.10.11 v1.7.6
tab35 환산 업데이트

2023.10.07 v1.7.5
서버 에러 디버깅

2023.10.04 v1.7.4
tab33 환산 업데이트

2023.10.03 v1.7.3
tab5 아케인지역 심볼 졸업, 로고 버튼에 새로고침 기능 추가

2023.10.01 v1.7.2
tab6 일일퀘스트 오디움 추가

2023.09.27 v1.7.1
tab8 아기새봉붕 추가, 스탯창 환산 추가, tab27 union 서버 주소 변경

2023.09.26 v1.6.3
v1.5.1로 backup(초기화 기능 구현 실패 사유), 함수 호출 위치 변경 실험 긍정적, 추가 보안 업데이트, tab00 보스도핑 container 장비제작 명장 버튼 추가, 각 tab 일일퀘스트 피크닉 버튼 이미지화, 보물찾기 버튼 수정

2023.09.25 v1.6.2
월요일, 목요일 자동 초기화 기능 회수, 함수 호출 위치 변경 실험 중

2023.09.24 v1.6.1
월요일, 목요일 자동 초기화 기능 추가(실패), 함수 호출 위치 변경 실험 (성능 향상 목적)

2023.09.22 v1.5.1
캐릭터 스탯창 이미지 자동 변경 기능 추가

2023.09.21 v1.4.1
각 tab 이벤트 container 활성화(추석이벤트), 각 tab 일일퀘스트 츄츄슬러시 버튼 삭제, 피크닉, 보물찾기 버튼 추가(추석이벤트), tab5 이미지 변경, 경험치 도핑, 보스 도핑 vip 버프 추가

2023.09.19 v1.3.5
tab7 스탯 정보 수정 tab1, tab4 이미지 변경

2023.09.18 v1.3.4
tab7 초기화 오류 수정, 무릉 층수 기능 추가, tab6, tab7 심볼 졸업 추가

2023.09.17 v1.3.3
tab 캐릭터 스탯 오류 수정, 업데이트 공지란 버전 숨김, tab27 union 값 고정

2023.09.12 v1.3.2
한정규 닉네임 변경으로 인한 서버 주소 변경, tab2~7 일일퀘스트 오디움 삭제, tab1 캐릭터 이미지 업데이트

2023.09.07 v1.3.1
주간퀘스트 주간초기화 → 월요일초기화 기능 수정, tab4 주간퀘스트 핑크빈버튼 오류 수정, 기존 [tab6], [tab7] 이름 → [tab99], [tab00] 변경, tab6,tab7 추가, label 디자인 간격 수정 로비 container 색상 입력

2023.09.06 v.1.2.1
tab2~5 재획 카운터 기능 추가, 수로,플래그 월요일 초기화 기능 추가 ( tab7 월요일 초기화 버튼 추가 ) 로비화면 업데이트 공지란 추가

2023.09.05 v.1.1.7
tab7 이름 [관리] → [version] 변경, tab2~5 일일퀘스트 츄츄,레헬른,아르카나 버튼 에러 수정 완료 tab1 재획 카운터 기능 추가

2023.09.04 v.1.1.6
사이트 이름 [검마 딱 대] → [나의 해방일지] 변경 tab2 캐릭터 이미지 업데이트, tab4 캐릭터 이미지 업데이트, 재획 카운터 기능 추가 중 (미완)

2023.09.03
tab1~5 일일퀘스트 황금마차 버튼 추가

2023.09.01 v1.1.5
tab2 퍼스널 컬러 변경, 캐릭터 이미지 업데이트, tab3 퍼스널 컬러 변경, 캐릭터 이미지 업데이트

2023.08.31 v1.1.4
tab1~5 '오늘의 메업적' 입력 textarea 추가 및 데이터베이스 연동 ( 자동 초기화 기능 추가 ), tab6 공지사항 textarea placeholder 속성 추가, 정식 배포 시작, og 태그 추가

2023.08.30
tab6 버튼 삭제 ( vip 쿠폰, 레범몬 ), tab6 버튼 추가 ( 경험치 부스트링, 엘 클리어, 엘 페일, 츄츄 슬러시 ), 각 tab 이벤트 container 이름 이벤트(종료) 로 변경 후 닫음, tab3 너보 → 제41대 변경 ( 이미지 수정 및 app.py 서버 내 level27 추가 )

2023.08.29 v1.1.3
도메인 구매 및 연결, 주간 초기화 버튼 통합화, 졸업 심볼지역 자동 클릭 기능 추가, 로비 저장 버튼 디자인 변경, 배경 디자인 변경

2023.08.27 v1.1.2
(tab5) 핑크빈버튼 에러 수정, 로비 저장 버튼 영역 확대, (tab7) 이름 관리로 변경, 선데이메이플 url 입력 기능 추가

2023.08.24 v1.1.1
테스트 배포 시작

</details>

