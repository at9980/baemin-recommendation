# Menu Recommendation AI

이 프로젝트는 음식 주문 모바일 앱(예: 배달의민족)에서 사용자 리뷰 텍스트를 기반으로 메뉴를 추천하는 시스템입니다. 주된 추천 키워드로 **해장**(숙취 해소)과 **다이어트**를 사용하며, 리뷰 내의 특정 키워드를 통해 메뉴 후보를 선정하고 OpenAI API를 활용해 임베딩과 텍스트 생성 과정을 거칩니다.

## 프로젝트 구조

project/ ├── main.py # 프로그램의 진입점: 전체 추천 프로세스 실행 ├── recommendation.py # 리뷰 분석, 후보 생성, 추천 메뉴 정렬 및 텍스트 생성 로직 포함 ├── db.py # MongoDB와의 연동: 레스토랑 정보 조회 및 추천 결과 저장 └── utils.py # 공통 유틸리티: 임베딩 생성, 코사인 유사도 계산, 키워드 추출, OpenAI API 호출 등

markdown

## 주요 기능

- **리뷰 분석 및 메뉴 후보 생성**  
  - 리뷰 텍스트에서 특정 컨텍스트 키워드(예: 해장, 숙취, 다이어트)를 추출합니다.
  - 블랙리스트에 포함되지 않은 메뉴 이름을 필터링하여 후보를 생성합니다.

- **추천 로직**  
  - OpenAI 임베딩 API를 통해 리뷰 컨텍스트와 메뉴 후보 간의 유사도를 계산합니다.
  - 미리 정의된 카테고리별 메뉴 조합(`COMBINATIONS`)을 기준으로 추천 순서를 정렬하고 중복을 제거합니다.
  
- **추천 텍스트 생성**  
  - 추천된 메뉴 목록을 바탕으로 OpenAI GPT 모델을 사용하여 사용자에게 전달할 추천 메시지를 생성합니다.

- **데이터베이스 연동**  
  - MongoDB Atlas를 사용하여 레스토랑 정보를 조회하고, 추천 결과를 저장합니다.

## 환경 설정

### 필수 전제 조건
- Python 3.x
- MongoDB Atlas 계정 (또는 연결 가능한 MongoDB 서버)
- OpenAI API 키

### 환경 변수 설정
아래의 환경 변수를 설정해야 합니다:

- `MONGODB_USERNAME`: MongoDB 사용자 이름
- `MONGODB_PASSWORD`: MongoDB 비밀번호
- `OPENAI_API_KEY`: OpenAI API 키

예를 들어, Linux/MacOS의 경우 터미널에서 아래와 같이 설정할 수 있습니다:
```bash
export MONGODB_USERNAME="your_username"
export MONGODB_PASSWORD="your_password"
export OPENAI_API_KEY="your_openai_api_key"
설치 및 실행
저장소 클론 및 의존성 설치

bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
pip install numpy pymongo certifi openai
프로그램 실행

bash
python main.py
이 명령은 MongoDB에서 레스토랑 정보를 조회하고, 추천 메뉴를 생성한 후 추천 결과를 데이터베이스에 저장합니다.
코드 확장 및 유지보수
새로운 추천 카테고리 추가:
recommendation.py 파일 내 COMBINATIONS 딕셔너리를 수정하여 추가 카테고리와 허용 메뉴 목록을 설정할 수 있습니다.

추천 텍스트 커스터마이징:
recommendation.py의 create_recommendation_text() 함수를 수정하여 원하는 스타일의 추천 메시지를 생성할 수 있습니다.

모듈화된 코드:
각 기능별로 파일을 분리해 관리하므로, 테스트나 디버깅이 용이하며 향후 기능 추가도 수월합니다.

의존성
numpy
pymongo
certifi
openai
