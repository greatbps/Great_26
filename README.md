# Great_26
# ✅ 1. 최종 추천 폴더 구조 (2025년 기준 최적화)

Obsidian 세컨드 브레인은 아래 6개 최상위 폴더만 있으면 된다.

`📁 00_INBOX 📁 01_Daily 📁 02_Projects 📁 03_Areas 📁 04_Resources 📁 05_Archive`

여기에 플러그인(Templater, Dataview, Tasks, Calendar 등)을 붙이면 완전 자동화된 세컨드 브레인이 된다.

---

# ✅ 2. 폴더별 상세 설명 + 실전 활용 예시

---

## 📁 00_INBOX

**역할:** 모든 자료의 임시 저장함 (영감, 스크랩, 빨리 기록해야 할 내용)

**여기 들어오는 것:**

- 모바일에서 Lilys AI 요약 넣기
    
- 유튜브·뉴스 요약
    
- 트레이딩 아이디어 순간 생각
    
- 웹사이트 스크랩 (Obsidian Clipper / MarkDownload)
    

**중요 원칙 → ‘고민 없이 그냥 INBOX로 넣기’**

### 매일 해야 하는 3분 정리 루틴

- INBOX → 각각 "Daily / Project / Area / Resource / Archive" 중 하나로 이동
    
- 이동만 하면 됨 (정리 강박 금지)
    

---

## 📁 01_Daily

**매일 쓰는 데일리 노트.**  
Templater로 아예 템플릿 자동 생성.

**템플릿 구성 예시:**

`# 📅 {{date}} Daily Note  ## 🧠 Log & Thoughts - 오늘의 생각: - 감정 상태:  ## 📈 Trading Log - 시장 상황: - 관심 종목: - 오늘의 전략: - 백테스트 아이디어:  ## 🧠 Learning - 공부 내용 요약:  ## ✔️ Tasks - [ ] 오늘 꼭 해야 할 일 - [ ] 미완료: {{yesterday}}  ## 🗂️ Inbox 처리 - [[00_INBOX]]`

Daily 폴더는 "**나의 하루 기록 + 학습 + 트레이딩 심리 기록**" 저장소.

---

## 📁 02_Projects

**90일 이내 완료해야 하는 모든 작업(프로젝트) 보관**

프로젝트 예시:

- `TradingSystem_v4.0`
    
- `Oracle_Cloud_Ampere_Setup`
    
- `Notion→Rhymix 자동화`
    
- `자동매매_전략_연구`
    
- `Carlinkit Android AI Box`
    

각 프로젝트 폴더에는 다음 3개 파일만 있으면 깔끔하다.

`📄 1. README (프로젝트 개요) 📄 2. Plan (작업 계획) 📄 3. Log (진행 기록)`

프로젝트 = “끝이 있는 일”  
완료되면 → Archive로 이동.

---

## 📁 03_Areas

**중장기적으로 유지해야 하는 ‘관리 영역’**

예시 (너에게 최적화):

- Trading / Automation System
    
- Personal Finance / Portfolio
    
- Health / Workout
    
- AI Research
    
- Programming Skill
    
- Car / Device Setup
    
- 가족·연인
    

특징:

- 끝나지 않음(영구 유지)
    
- 관련되는 노트 계속 추가
    
- 전략·원칙·매뉴얼 저장하기 딱 좋음
    

예:  
`Trading > 전략 아카이브.md`  
`Trading > 15분봉 SuperTrend 전략.md`  
`Personal Finance > 미국 ETF 연구.md`

---

## 📁 04_Resources

**학습·지식 아카이브**  
읽은 책, 유튜브 요약, 뉴스 분석, 트레이딩 전략 정리, 코드 스니펫 등...

즉, “내가 언젠가 참고할 정보의 창고”

분류 예시:

- Investing
    
- Trading Strategies
    
- Quant & Backtesting
    
- Python Snippets
    
- Linux & Server
    
- Machine Learning
    
- AI Agents (Claude, Codex, MCP)
    
- Car / Hardware
    
- Health
    

여기는 reference용이라 가공 없이 넣어도 OK.

---

## 📁 05_Archive

**끝난 것 / 오래된 것 / 다시 안 볼 것 → 다 여기로**

정리 기준:

- 완료된 프로젝트
    
- 6개월 이상 안 보는 노트
    
- 시효가 지난 자료
    

Why? → 메인 폴더가 깔끔해야 생각이 잘 정리됨.

---

# ✅ 3. Obsidian 플러그인 추천 (세컨드 브레인 필수 세팅)

|플러그인|이유|
|---|---|
|**Calendar**|데일리 노트 자동|
|**Templater**|템플릿 자동화|
|**Tasks Plugin**|TODO 관리|
|**Dataview**|프로젝트·자료 자동 대시보딩|
|**QuickAdd**|INBOX 빠르게 수집|
|**Periodic Notes**|Daily/Weekly/Monthly 자동 생성|
|**Advanced URI**|Make.com / Telegram 자동화 연동|

---

# ✅ 4. 실제 사용 흐름 (너에게 맞춘 워크플로우)

---

## 📌 Step 1: 정보 수집

모든 정보 → **INBOX**

- 트레이딩 아이디어
    
- 뉴스
    
- 유튜브 요약
    
- 기술 연구
    
- ChatGPT 답변
    

---

## 📌 Step 2: 매일 아침 Daily에서 INBOX 정리

- 프로젝트성 문서는 `02_Projects`
    
- 장기적 관리 문서는 `03_Areas`
    
- 나중에 참고한 자료는 `04_Resources`
    
- 오래된 건 `Archive`
    

3분이면 충분함.

---

## 📌 Step 3: 프로젝트 진행

예: `TradingSystem_v4.0`

- 오늘 할 작업은 Daily에 자동 링크
    
- 코드 스니펫·전략 문서는 Projects 폴더 안에 저장
    
- 백테스트 결과는 Resources로 이동
    

---

## 📌 Step 4: 주간 리뷰(Weekly Note)

자동 생성 템플릿:

`# Weekly Review ({{date}}) ## 1. 이번 주 핵심 성과 -  ## 2. 진행 중 프로젝트 상태 ```dataview LIST FROM "02_Projects"`

## 3. 시장 분석/트레이딩 리뷰

- 이번 주 성공 전략:
    
- 실패 원인:
    

## 4. 다음 주 계획

`---  # ✅ 5. 당신의 스타일에 맞춰 최종 커스터마이징  너의 패턴을 반영해 특별히 아래 3가지를 강하게 추천함.  ---  ## ⭐ (1) “트레이딩”을 Areas 아래에 크게 분리`

03_Areas/  
└ Trading/  
├ 전략 아카이브  
├ 백테스트 결과  
├ 뉴스·리서치  
├ 감정 로그  
└ 자동매매 시스템 기록

`---  ## ⭐ (2) 코드/프로젝트는 Projects 폴더에 통일`

02_Projects/  
├ TradingSystem_v4.0/  
├ NewsSentimentBot/  
├ OracleCloud_Server/  
├ KIS_WebSocket/  
└ Rhymix_Automation/

`---  ## ⭐ (3) YouTube·뉴스 요약 자동 정리 Lilys AI / Make.com 연동시:  - 자동으로 Obsidian 00_INBOX에 생성 - Daily Note에서 체크하면서 분류  너처럼 콘텐츠 입력량 많은 사람에게 **폭발적인 효율** 나옴.  ---  # 🎁 원하면 드릴 수 있는 것 말만 하면 만들어줄게:  ### ✔ 데일리 노트 템플릿  ✔ Weekly / Monthly 템플릿   ✔ 프로젝트 템플릿   ✔ 트레이딩 로그 템플릿   ✔ 뉴스 리서치 자동화 템플릿   ✔ Make.com → Obsidian 자동화 시나리오   ✔ Dataview 대시보드 완성본    원하는 템플릿 형식 말하면,   **너의 전체 투자·자동매매 시스템에 딱 맞춘 세컨드 브레인 구조**로 커스텀해서 바로 만들어줄게.`

##### 나의 말:

내가 개인 프로젝트도 하지만 회사 프로젝트도 하거든. 그걸 분류해서 만들어 줘

###### ChatGPT의 말:

좋아.  
너처럼 **개인 프로젝트 + 회사 프로젝트**를 동시에 진행하는 사람에게는  
Obsidian 폴더 구조를 “두 개의 세계”로 확실히 구분해야 **스트레스도 줄고** **정리 효율도 압도적으로 올라가**.

아래는 **2025년 기준으로 가장 효율적인 세컨드 브레인 구조 (회사 + 개인 겸용)**.

---

# ✅ 최종 폴더 구조(개인 + 회사 구분 포함)

`📁 00_INBOX 📁 01_Daily 📁 02_Projects       ├ 📁 Personal       └ 📁 Work 📁 03_Areas       ├ 📁 Personal       └ 📁 Work 📁 04_Resources       ├ 📁 Personal       └ 📁 Work 📁 05_Archive       ├ 📁 Personal       └ 📁 Work`

---

# ✅ 폴더별 역할과 활용 방법 (개인/회사 분리 기준)

---

# 📁 00_INBOX

**모든 자료 임시 저장소(개인/회사 구분 없이 전부 여기로)**  
정리할 때 각 카테고리로 이동시키면 됨.

- 회사 회의록 메모
    
- 너의 자동매매 전략 아이디어
    
- 기사·논문 요약
    
- 코드 스니펫
    
- 유튜브 요약  
    → 전부 **INBOX**로
    

**정리 루틴(매일 3분):**  
INBOX → Projects / Areas / Resources / Archive 중 적절한 곳으로 이동

---

# 📁 01_Daily

**일별 기록 + 업무/개인 분리 템플릿 자동 생성**  
데일리 노트 안에서 Personal / Work를 나눠 기록하면 구조 유지됨.

템플릿 예시:

`# 📅 {{date}} Daily Note  ## 🧑‍💼 Work Notes - 오늘 할 일 - 회의록 - 진행 중 프로젝트 관련 기록  ## 🏠 Personal Notes - 공부/책/유튜브 요약 - 트레이딩 로그 - 개인 프로젝트 진행  ## 📈 Trading Log - 시장 상황: - 트레이딩 전략: - 개선 아이디어:  ## ✔️ Tasks - [ ] Work - [ ] Personal  ## 🗂️ Inbox 처리 - [[00_INBOX]]`

---

# 📁 02_Projects (가장 중요한 폴더)

“**끝이 있는 일**”을 분리하는 곳  
→ 회사일과 개인일은 절대 섞이면 안 됨.  
→ 그래서 **Personal / Work**로 분리.

`02_Projects/  ├ Personal/  │   ├ TradingSystem_v4.0  │   ├ OracleCloud_Server  │   ├ Rhymix_Automation  │   └ AI_Agent_Workflow  └ Work/      ├ 사내_API_고도화      ├ B2B_AI_도입_프로젝트      ├ 문서_자동화_시스템      └ Data_Integration_Pipeline`

각 프로젝트 폴더에는 반드시 3개 파일:

`📄 README.md — 프로젝트 개요 📄 PLAN.md — 목표/할일/설계 📄 LOG.md — 진행 기록`

프로젝트 완료하면 Personal/Work 각각의 Archive로 이동.

---

# 📁 03_Areas

“**끝이 없는 지속적 관리 영역**”  
회사/개인 모두 존재.

### ▷ Personal Areas 예시

`Trading   Personal Finance   Health / Fitness   AI Research   Linux & Server   Programming Skill   Car / Device Setup   가족·관계   라이프로그`  

### ▷ Work Areas 예시

`Team Operations   DevOps / Platform   AI Model Research   API Architecture   사내 기술 문서 관리   회사 기술 스택 정리   정책/규정/규칙`  

**원칙:**  
“지속적으로 개선하거나 관리하는 영역 → Areas”

---

# 📁 04_Resources

**참고 자료 아카이브 (Personal / Work 분리)**

여기에는 “읽은 것, 공부한 것, 참고할 자료”만 들어감.

### Personal Resources

- 백테스트 결과
    
- 트레이딩 전략 정리
    
- 투자/경제 리서치
    
- Python 스니펫
    
- Linux 서버 설정 가이드
    

### Work Resources

- 사내 기술 스택 정리
    
- API 응답 규격
    
- 내부 산출물 참고 자료
    
- 회의록 중 장기 참고자료
    
- 논문/문서 요약
    

이곳은 **가공 불필요한 Reference 저장소**  
→ 그냥 쌓이면 됨.

---

# 📁 05_Archive

회사/개인 각각 보관.

- 완료된 프로젝트
    
- 더 이상 필요 없는 문서
    
- 과거 데이터를 모아두는 곳
    

구조:

`05_Archive/  ├ Personal  └ Work`

---

# 🔥 실전 사용 흐름 (너의 작업 방식에 최적화)

---

## ▶ Step 1. 모든 정보는 INBOX

회사건 개인이건 무조건 **INBOX**  
→ 생각 안 하고 기록해서 뇌 부담 최소화

---

## ▶ Step 2. Daily Note에서 INBOX 정리

- 회사 관련 자료 → Work/Projects or Work/Areas
    
- 개인 관련 자료 → Personal/Projects or Personal/Areas
    
- 참고만 할 자료 → Resources
    
- 필요 없거나 완료 → Archive
    

---

## ▶ Step 3. 프로젝트 진행

**회사 일은 Work/Projects 내부에서만 작업**  
**개인 일은 Personal/Projects 내부에서만 작업**

Daily Note에서 프로젝트 파일 자동 링크로 이동.

---

## ▶ Step 4. 주간/월간 리뷰

Templater로 자동 생성:

`# Weekly Review ({{date}})  ## Work Summary - 이번 주 성과 - 다음 주 목표   - 리스크 및 해결 전략    ## Personal Summary - 트레이딩 성과 - 시스템 개선 - 학습/리서치 정리  ## Project Dashboard ```dataview TABLE status, deadline FROM "02_Projects"`

`---  # 💡 보너스: 회사/개인 섞이지 않게 하는 팁 3가지  ### 1) Project명 앞에 접두사`  

[W] API_고도화  
[P] TradingSystem_v4.0

`### 2) Daily Note 안에서 Work/Personal 구분  필수.  ### 3) Dataview 대시보드도 분리  - Work Project Dashboard   - Personal Project Dashboard    원하면 **완성된 Dataview Dashboard까지 제작**해줄 수 있음.  ---  # 🎁 필요하면 만들어줄 수 있는 것 원하는 것 말해줘:  ✔ Personal/Work 분리된 데일리 템플릿   ✔ Work 프로젝트 템플릿   ✔ Personal 프로젝트 템플릿   ✔ Areas 템플릿   ✔ Dataview 프로젝트 대시보드 완성본   ✔ INBOX 자동 분류 QuickAdd 스크립트   ✔ Make.com → Obsidian 자동화 시나리오    너 작업 스타일에 맞춰 “실전 최적화 세컨드 브레인”을 완성해줄게.`

##### 나의 말:

프로젝트 나누는 것 말고 굳이 다른 것 까지 개인과 업무를 구분할 필요가 있을까?

###### ChatGPT의 말:

결론부터 말하면 **프로젝트만 개인/업무로 나누고**,  
나머지(Areas, Resources, Archive)는 **굳이 분리하지 않는 게 더 효율적**이다.

이게 가장 현실적이고 관리 스트레스도 적다.  
즉, 구조는 이렇게 단순해진다:

`00_INBOX 01_Daily 02_Projects       ├ Personal       └ Work 03_Areas 04_Resources 05_Archive`

왜 이게 최적일까? 아주 논리적으로 설명해줄게.

---

# ✅ 왜 “프로젝트만” 개인/업무 분리가 필요한가?

프로젝트는 **성격과 목적이 완전히 다르기 때문**이야.

- 회사 프로젝트 → 조직 목표, 마감, 협업
    
- 개인 프로젝트 → 너의 성장, 자동매매, 개인 개발, 취미
    

이건 섞이면 안 되고,  
진행 관리 과정도 완전히 다름.

그래서 프로젝트 분리 = 필수.

---

# ❌ 그런데 Areas/Resources/Archive는 왜 굳이 분리할 필요가 없을까?

여기서 많은 사람들이 실수하는데,  
너처럼 **일도 하고 공부도 하고 투자·개발·코딩도 하는 사람**은  
구조가 복잡해지면 바로 귀찮아지고 시스템이 무너진다.

즉,

### ✔ Areas, Resources, Archive는 “카테고리 성격”이라 분리 의미가 없다.

예시로 보면 바로 이해돼.

---

# 🔍 1. Areas는 ’지속적 관리 영역’ → 개인/업무 구분 불필요

예:

- Trading
    
- Personal Finance
    
- Health
    
- AI Research
    
- Linux
    
- Server/DevOps
    
- Software Skill
    
- Documentation
    
- Leadership
    

여기에 “Work” / “Personal” 붙이면?

→ 오히려 경계가 모호해지고 관리 부담만 증가  
→ 예: AI Research는 회사 일이야? 개인 일이야? 둘 다 가능함  
→ 운동·건강은 개인이니 OK  
→ 서버/DevOps는 회사 일도 개인 서버도 있음

즉, **현실은 업무/개인을 정확히 나누기 어려운 영역이 대부분**

➡ 그래서 카테고리는 그냥 통합하는 게 훨씬 효율적.

---

# 🔍 2. Resources는 “참고 자료 아카이브” → 회사/개인 구분 의미 없음

예시:

- Python 코드 스니펫
    
- 백테스트 연구 자료
    
- AI 논문
    
- AWS 문서
    
- 회계/세금 자료
    
- 머신러닝 연구
    
- DevOps 참고 문서
    

이걸 회사/개인으로 나누면?

- Python 스니펫이 개인용인지 회사용인지 애매함
    
- AI 논문도 개인 연구 + 회사 프로젝트에 둘 다 사용 가능
    
- 학습 자료는 대부분 “겸용”임
    

즉, **리소스는 ‘주제별’로 정리해야 의미가 있고, 업무/개인은 불필요함.**

---

# 🔍 3. Archive는 그냥 ‘완료된 것’ → 나눌 이유 없음

Archive는 “어차피 안 볼 자료”

회사/개인을 나누는 건 의미 없음.

아카이브 기준은 딱 2개뿐이다:

- 더 이상 쓰지 않는 파일
    
- 끝난 프로젝트
    

끝.

프로젝트는 Personal/Work 폴더 자체가 있으니  
그 폴더 통째로 Archive로 들어가면 자연스럽게 구분됨.

---

# ✔ 결론: 딱 하나만 구분하면 된다

**프로젝트만 Personal/Work 분리**  
나머지는 통합.

이게 실전에서 가장 효율적이며 장기적으로 유지 가능하다.

---

# 📌 최종 권장 구조(복잡도 최소 + 효율 최대)

`00_INBOX 01_Daily 02_Projects       ├ Personal       └ Work 03_Areas 04_Resources 05_Archive`

이 구조가 너 같은  
**개발자 + 자동매매 구축 + 회사 프로젝트 병행**  
유저에게 가장 안정적이다.

---

# 🎁 원하면 지금 바로:

- Daily Note 템플릿
    
- Projects 템플릿 (Personal/Work 버전)
    
- Areas 구조 샘플
    
- Resources 정리 기준
    
- Dataview 프로젝트 대시보드
    

까지 자동으로 만들어줄게.

##### 나의 말:

Daily Note 템플릿 Projects 템플릿 (Personal/Work 버전) Areas 구조 샘플 Resources 정리 기준 Dataview 프로젝트 대시보드 까지 자동으로 만들어 줘

###### ChatGPT의 말:

좋아.  
너의 **개인/업무 병행 + 트레이딩 + 개발자 워크플로우**에 최적화된 템플릿과 구조를 “바로 복사해서 Obsidian에 붙여넣을 수 있도록” 완성형으로 만들어줄게.

아래 내용 그대로 복붙하면 **즉시 사용 가능한 세컨드 브레인 시스템**이 완성된다.

---

# ✅ 1) Daily Note 템플릿 (Templater 용)

파일명: `daily_template.md`

`# 📅 {{date}} Daily Note  ## 🧑‍💼 Work ### 📝 Today’s Work Tasks - [ ]   ### 📊 Meetings / Notes -   ### 🔧 Progress Log -   ---  ## 🏠 Personal ### 📌 Personal Tasks - [ ]   ### 📈 Trading Log - 시장 상황: - 관심 종목: - 오늘 전략: - 감정 상태: - 개선 아이디어:  ### 🧠 Learning / Study - 공부/리서치 요약:  ---  ## ✔️ Today’s Main Goals (Top 3) 1.  2.  3.   ---  ## 🗂️ Inbox to Process ```dataview LIST FROM "00_INBOX"`

---

## ✔️ Review Tonight

- 오늘 잘한 점:
    
- 부족했던 점:
    
- 내일 개선 사항:
    

`` **TIP:**   Templater에서 Daily Note 자동 생성 시 적용하도록 설정하면 끝.  ---  # ✅ 2) Projects 템플릿 (Personal / Work 공통)  파일명: `project_template.md` ``

# 📁 {{title}}

## 📌 프로젝트 개요

- 목적:
    
- 배경:
    
- 기대 효과:
    

---

## 🎯 목표 (Goals)

-  1차 목표
    
-  2차 목표
    
-  3차 목표
    

---

## 🔧 작업 계획 (PLAN)

### 📅 타임라인

- 시작일:
    
- 예상 종료일:
    

### 🧩 주요 Task

-  작업 1
    
-  작업 2
    
-  작업 3
    

---

## 📜 진행 로그 (LOG)

> 날짜별 진행 상황을 아래와 같이 기록

`### {{date}} - 한 일: - 문제점: - 다음 액션:`

---

## 🧠 참고 자료 (Links / Files)

- 관련 문서:
    
- 리서치 링크:
    
- 코드:
    

``### Personal 프로젝트 생성 위치 `02_Projects/Personal/프로젝트명`  ### Work 프로젝트 생성 위치 `02_Projects/Work/프로젝트명`  ---  # ✅ 3) Areas 구조 샘플 (그대로 폴더 만들어도 됨)``

03_Areas  
├ Trading  
│ ├ 전략 아카이브.md  
│ ├ 백테스트 결과.md  
│ ├ 자동매매 시스템 구성.md  
│ └ 심리관리.md  
│  
├ Personal Finance  
│ ├ 포트폴리오 전략.md  
│ ├ 은퇴계획.md  
│ └ 세금·연금.md  
│  
├ Health  
│ ├ 운동 루틴.md  
│ └ 식단·체력 관리.md  
│  
├ AI Research  
│ ├ Claude/A GPT Agents.md  
│ ├ 모델 구조 탐구.md  
│ └ 벤치마크 정리.md  
│  
├ Programming  
│ ├ Python  
│ ├ Linux/Server  
│ ├ DevOps  
│ └ Architecture  
│  
├ Productivity  
│ ├ Workflows.md  
│ └ Templates.md  
│  
├ Car / Device Setup  
│ └ Android Auto, AI Box 정리.md

`` Areas는 절대 개인/업무를 나누지 않음.   중복되거나 모호한 분류는 시간이 지나면 시스템 붕괴를 부름.  ---  # ✅ 4) Resources 정리 기준 (가이드 문서)  파일명: `04_Resources/README.md` ``

# 📚 Resources 정리 기준

Resources는 “참고용 자료 보관소”로, 다음 기준에 따라 정리한다.

---

## 📌 1) 성격 기반 정리

자료는 성격별 폴더에 넣는다:

- Tech / Programming
    
- Trading / Finance
    
- AI / Machine Learning
    
- Quant Research
    
- Documentation / Guides
    
- Snippets / Code
    
- Hardware / Devices
    
- Articles / Book Notes
    
- Study Notes
    

---

## 📌 2) Work / Personal 구분 ❌

대부분 자료는 개인/업무 구분이 모호하므로 분리하지 않는다.

Reference는 “누구의 것이냐”가 아니라 “무슨 내용이냐”가 핵심.

---

## 📌 3) 자료는 가공하지 않아도 됨

- 스크랩
    
- 복사/붙여넣기
    
- PDF 요약
    
- 유튜브 요약
    
- 뉴스
    
- 논문 발췌
    

그냥 그대로 넣으면 됨.

---

## 📌 4) 프로젝트 관련 자료는?

2가지 기준:

- 단기적으로 자주 참고 → 프로젝트 폴더 내부
    
- 장기 참고용 → Resources로 이동
    

---

## 📌 5) 불필요한 폴더 만들지 않기

자료가 겹칠 수밖에 없으므로 “중복을 허용하되, 체계는 단순하게 유지한다.”

---

## 📌 6) Archive 기준

6개월 이상 안 본 자료 → 05_Archive로 이동

`` ---  # ✅ 5) Dataview 프로젝트 대시보드 (Obsidian 홈 화면용)  파일명: `project_dashboard.md` ``

# 📊 Project Dashboard

## 🧑‍💼 Work Projects (진행 중)

`TABLE status AS "Status", deadline AS "Due", file.link AS "Project" FROM "02_Projects/Work" WHERE status != "Done" SORT deadline ASC`

---

## 🏠 Personal Projects (진행 중)

`TABLE status AS "Status", deadline AS "Due", file.link AS "Project" FROM "02_Projects/Personal" WHERE status != "Done" SORT deadline ASC`

---

## 🗂 완료된 프로젝트

`LIST FROM "05_Archive" WHERE contains(file.folder, "Projects")`

`이걸 홈 화면이나 사이드바에 배치하면   **회사 + 개인 프로젝트를 자동 정렬해서 한 방에 관리**할 수 있음.  ---  # 🎁 원하면 확장해줄 수 있는 추가 기능 - Daily Note에서 자동으로 현재 프로젝트 task 불러오기   - 개인/업무 분리된 Task 대시보드   - Trading 전용 데일리 템플릿   - 백테스트 기록 자동 템플릿   - 프로젝트 생성 자동화(QuickAdd 매크로)   - Make.com → Obsidian 자동 수집 템플릿    필요한 추가 기능 있으면 말해줘.   너의 전체 시스템에 맞춰 더 정교하게 확장해줄게.`