# 🤖 GPT 기반 AI 비트코인 자동 매매 시스템

OpenAI GPT를 활용한 지능형 비트코인 자동 매매 시스템입니다. 실시간 시장 데이터 분석, 기술적 지표, 그리고 AI 기반 의사결정을 통해 자동으로 비트코인을 거래합니다.

## 📚 참고 자료

- [한빛미디어 도서](https://www.hanbit.co.kr/store/books/look.php?p_code=B5063161940&type=book)
- [프로젝트 노션 페이지](https://abrasive-detective-fdd.notion.site/GPT-AI-240567bebf704f29adb6cc7bd61962fc)

## ✨ 주요 기능

### 🔄 자동 매매 시스템 (`app/autotrade.py`)

- **AI 기반 의사결정**: OpenAI GPT-4o를 활용한 매매 의사결정
- **기술적 분석**: 다양한 기술적 지표(RSI, MACD, 볼린저 밴드 등) 자동 분석
- **실시간 시장 데이터**: pyupbit를 통한 실시간 비트코인 시세 및 거래량 분석
- **차트 이미지 분석**: Selenium을 활용한 차트 스크린샷 및 GPT Vision 분석
- **자동 반성일기**: 과거 거래 분석 및 개선점 도출
- **다중 환경 지원**: 로컬 및 AWS EC2 환경 모두 지원
- **데이터베이스 관리**: SQLite를 통한 거래 기록 및 반성일기 저장

### 📊 모니터링 대시보드 (`app/streamlit-app.py`)

- **실시간 자산 현황**: BTC 보유량, KRW 잔고, 총 자산가치 표시
- **거래 히스토리**: 시간별 거래 내역 및 BTC 가격 변동 차트
- **매매 분석**: 매수/매도 비율 및 평균 변동률 시각화
- **반성일기 조회**: AI가 작성한 트레이딩 반성일기 확인
- **자동 새로고침**: 설정 가능한 간격으로 데이터 자동 업데이트

## 🛠️ 기술 스택

- **Python 3.x**
- **OpenAI API** - GPT-4o 기반 AI 의사결정
- **pyupbit** - 업비트 거래소 API 연동
- **Selenium** - 차트 이미지 수집
- **TA-Lib** - 기술적 분석 지표
- **Streamlit** - 웹 대시보드
- **SQLite** - 거래 기록 데이터베이스
- **Plotly** - 인터랙티브 차트
- **Schedule** - 정기 작업 스케줄링

## 📦 설치 방법

### 1. 저장소 클론

```bash
git clone <repository-url>
cd gpt-bitcoin-book
```

> 💡 **Git 사용법이 필요하신가요?** 자세한 Git 명령어와 워크플로우는 [GIT.md](./GIT.md) 문서를 참고하세요.

### 2. 가상환경 생성 및 활성화

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

`.env` 파일을 생성하고 다음 내용을 입력하세요:

```env
# OpenAI API
OPENAI_API_KEY=your_openai_api_key

# Upbit API
UPBIT_ACCESS_KEY=your_upbit_access_key
UPBIT_SECRET_KEY=your_upbit_secret_key

# Optional: Headless 모드 설정 (기본값: false)
HEADLESS=false
```

## 🚀 사용 방법

### 자동 매매 시스템 실행

```bash
python app/autotrade.py
```

시스템이 실행되면:

- 4시간마다 자동으로 시장 분석 및 매매 결정
- 매일 자정에 자동 반성일기 작성
- 거래 기록은 `trading.db`에 자동 저장

### 모니터링 대시보드 실행

```bash
streamlit run app/streamlit-app.py
```

브라우저에서 `http://localhost:8501`로 접속하여 대시보드를 확인할 수 있습니다.

## 📁 프로젝트 구조

```
gpt-bitcoin-book/
├── app/
│   ├── autotrade.py          # 메인 자동매매 로직
│   ├── streamlit-app.py      # 모니터링 대시보드
│   └── pyupbit_sample.py     # pyupbit 샘플 코드
├── strategy.txt              # 트레이딩 전략 참고 자료
├── requirements.txt          # Python 의존성
├── pyrightconfig.json        # Python 타입 체크 설정
├── ruff.toml                 # Python 린터 설정
├── GIT.md                    # Git 명령어 가이드
└── README.md                 # 프로젝트 문서
```

## 🔍 주요 기능 상세

### AI 의사결정 프로세스

1. **데이터 수집**: 실시간 시세, 거래량, 기술적 지표, 차트 이미지
2. **AI 분석**: GPT-4o가 수집된 데이터를 종합 분석
3. **매매 결정**: buy, sell, hold 결정 및 투자 비율 산정
4. **실행**: 결정에 따라 자동으로 주문 실행
5. **기록**: 모든 거래 내역 데이터베이스에 저장

### 반성일기 시스템

- 매일 자정에 자동으로 실행
- 과거 24시간의 거래 내역 분석
- 시장 상황, 의사결정 분석, 개선점 도출
- 학습 포인트 정리 및 성공률 계산

## ⚠️ 주의사항

- 실제 자금을 투자하기 전 충분한 테스트를 진행하세요
- OpenAI API 및 Upbit API 키 관리에 주의하세요
- 시장 변동성에 따른 손실 가능성을 인지하고 사용하세요
- 법적 책임은 사용자에게 있습니다

## 📝 라이선스

이 프로젝트는 교육 목적으로 제공됩니다.

## 🤝 기여

버그 리포트, 기능 제안, Pull Request는 언제나 환영합니다!

---

**면책 조항**: 이 시스템은 교육 및 연구 목적으로 제공됩니다. 실제 투자에서 발생하는 손실에 대해 개발자는 책임을 지지 않습니다.
