# AI 기반 공공·국방 SI 제안서 생성 및 수주전략 플랫폼 프레임워크 v5.0

## 1. 목적

본 프레임워크는 공공·국방 분야 RFP를 입력받아 기술평가 고득점과 수주 가능성 극대화를 위한 제안서 및 PPT를 자동 생성하는 AI 기반 제안 컨설팅 플랫폼 구축을 목적으로 한다.

---

# 전체 프로세스

STEP 1. RFP Intelligence

↓

STEP 1.2 Competitive Intelligence

↓

STEP 1.5 RTM Foundation

↓

STEP 2. Page Architecture

↓

STEP 3. Storyboarding

↓

STEP 3.5 Story Validation

↓

STEP 3.7 Reviewer Challenge

↓

STEP 4. Page Generation

↓

STEP 4.5 Content QA & Red Team Review

↓

STEP 5. PPT Design Engine

↓

STEP 5.5 PPT Rendering Engine

↓

STEP 6. Final QA

↓

STEP 6.5 Win Probability Simulator

---

# STEP 1. RFP Intelligence

## 목적

사업의 본질과 평가체계를 분석하여 Winning Strategy 수립 기반 확보

---

## 입력

### 필수

- 제안요청서(RFP)
    
- 기술평가기준표
    
- 사업명
    
- 사업예산
    
- 사업기간
    
- 발주기관 정보
    

### 선택

- 질의회신서
    
- 제안설명회 자료
    
- ISP/ISMP 결과물
    
- 관련 법령
    
- 기관 중장기 계획
    

---

## 출력

### 사업 이해도 분석

- 사업목적
    
- 추진배경
    
- 현황 및 문제점
    
- Pain Point
    
- Hidden Needs
    
- 기대효과
    

---

### 핵심 요구사항 분석

|Req ID|요구사항|구분|중요도|
|---|---|---|---|

---

### 평가항목 분석

|평가항목|배점|중요도|대응전략|
|---|---|---|---|

---

### 제약사항 분석

|구분|내용|대응방안|
|---|---|---|

- 일정
    
- 예산
    
- 기술
    
- 운영
    
- 보안
    
- 법제도
    

---

### 정량평가 자가진단

- 경영상태
    
- 유사실적
    
- 인증현황
    
- 인력등급
    
- 지역업체 참여
    
- 상생협력
    
- 신기술 가점
    

---

### Winning Strategy

#### Strategy

수주전략

#### USP

차별화 포인트

#### Proof

실적 및 증빙

---

# STEP 1.2 Competitive Intelligence

## 목적

경쟁사 대비 우위 전략 확보

---

## 출력

### 경쟁환경 분석

|경쟁사|강점|약점|
|---|---|---|

---

### 경쟁사 대응전략

|경쟁사 강점|대응전략|
|---|---|

---

### 차별화 전략

- 경쟁사 미보유 역량
    
- 독점적 방법론
    
- 고유 프레임워크
    
- 특허 및 인증
    

---

# STEP 1.5 RTM(Requirements Traceability Matrix) Foundation

## 목적

요구사항과 평가항목의 완벽한 역추적성 확보

---

## 출력

|Req ID|요구사항|평가항목|대응기능|USP|
|---|---|---|---|---|

---

# STEP 2. Page Architecture

## 목적

제안서 구조 설계

---

## 원칙

### Level 1 ~ 2

RFP 100% 준수

---

### Level 3 이하

차별화 전략 반영

---

## 출력

|목차번호|목차명|Req ID|평가항목|Page Budget|우선순위|
|---|---|---|---|---|---|

---

### RTM 자동 갱신

|Req ID|대응목차|페이지|
|---|---|---|

---

# STEP 3. Storyboarding

## 목적

장표 설계

---

## 출력

### 기본정보

- 사업명
    
- 목차
    
- 페이지수
    

---

### Evaluator Persona

#### 공무원

- 안정성
    
- 예산
    
- 유지관리
    

#### 교수

- 혁신성
    
- 논리성
    
- 기술성
    

#### 군 평가위원

- 작전성
    
- 생존성
    
- 상호운용성
    

---

### As-Is

현재 한계

---

### Issue

문제점

---

### To-Be

미래 모습

---

### USP

차별화

---

### Proof

객관적 증빙

---

### Effect

정량·정성 효과

---

# STEP 3.5 Story Validation

## 검증

### 논리 검증

As-Is

↓

Issue

↓

To-Be

↓

Execution

↓

Effect

---

### RTM 검증

요구사항 누락 여부

---

### 평가항목 검증

평가기준 대응 여부

---

### Proof 검증

객관적 근거 존재 여부

---

# STEP 3.7 Reviewer Challenge

## Red Question

### Q1

경쟁사도 동일하게 작성 가능한가?

YES → 재작성

---

### Q2

평가위원이 점수를 줄 이유가 존재하는가?

NO → 재작성

---

### Q3

증빙 없는 주장인가?

YES → 삭제

---

### Q4

이 장표가 없어도 되는가?

YES → 삭제 검토

---

# STEP 4. Page Generation

## 목적

실제 PPT 원고 생성

---

## 출력

### Header Copy

2줄 이내

---

### Page Role

페이지 목적

---

### Governing Message

3개 이내

---

### Grid Layout

상단

Header

좌측

As-Is

우측

To-Be

하단

Effect

---

### 상세 본문

규칙

- 명사형 종결
    
- 개조식
    
- PPT 삽입 수준
    
- 최대 3단 Bullet
    

---

### Block Tag

[Block: As-Is]

[Block: Issue]

[Block: To-Be]

[Block: USP(Unique Selling Proposition)]

[Block: Proof]

[Block: Effect]

---

### Spec Table

구조화 데이터 생성

예시

{  
"headers":["구분","요구사항","제안규격"],  
"rows":[  
["성능","TPS 1000","TPS 2500"]  
]  
}

---

### 기대효과

정량

정성

---

# STEP 4.5 Content QA & Red Team Review

## Filter 1

익명성 검증

회사명 제거

---

## Filter 2

브랜드명 마스킹

솔루션명 일반화

---

## Filter 3

확정형 검증

금지

- 가능
    
- 예정
    
- 협의
    

허용

- 구축
    
- 확보
    
- 제공
    
- 구현
    

---

## Filter 4

Page Budget 검증

---

## Filter 5

과장표현 제거

금지

- 최고
    
- 압도적
    
- 완벽
    

---

# STEP 5. PPT Design Engine

## 목적

PPT 구조 데이터 생성

---

## 출력

### Slide Meta

- Slide ID
    
- Section
    
- Page Number
    

---

### Typography

- Header
    
- Governing Message
    
- Body
    

---

### Visual Data

- Diagram Type
    
- Layout Type
    
- Color Code
    
- Icon Code
    

---

### Table Data

- 비교표
    
- 일정표
    
- 조직도
    

---

# STEP 5.5 PPT Rendering Engine

## 목적

PPT 자동 생성

---

## 출력

### Slide Wireframe

### Shape Tree

### Object ID

### PPT Object Map

### Rendering Data

---

## 지원

- python-pptx
    
- Aspose
    
- PptxGenJS
    
- PowerPoint Copilot
    

---

# STEP 6. Final QA

## 최종 검증

### RTM 100%

### 평가항목 100%

### 페이지수 검증

### 익명성 검증

### 감점요인 제거

### Proof 연결 검증

---

# STEP 6.5 Win Probability Simulator

## 목적

수주 가능성 예측

---

## 입력

- 기술점수
    
- 가격점수
    
- 경쟁사 예상점수
    
- 가점요소
    

---

## 출력

### 예상 기술점수

### 예상 가격점수

### 예상 총점

### 수주확률

---

### Gap Analysis

|항목|부족점수|개선방향|
|---|---|---|

---

# AI 시스템 공통 작성 원칙

## 역할

- 공공 SI 제안 PM
    
- 국방 제안 PM
    
- ISP/ISMP 컨설턴트
    
- Enterprise Architect
    
- 제안 디자이너
    

---

## 작성 원칙

1. 평가항목 중심 작성
    
2. 고객 관점 우선
    
3. 경쟁사 대비 차별화
    
4. RTM 100% 유지
    
5. Proof 기반 주장
    
6. 명사형 종결
    
7. PPT 삽입 가능 수준
    
8. 시각화 우선
    
9. As-Is → To-Be → Effect 유지
    
10. 감점요인 원천 제거
    
11. 익명성 준수
    
12. 평가위원 중심 작성
    
13. Page Budget 준수
    
14. 수주 가능성 극대화
    
15. 모든 장표는 점수 획득 목적 명확화
    

---

# 최종 산출물

1. RFP 분석서
    
2. 경쟁환경 분석서
    
3. RTM
    
4. Winning Strategy
    
5. 목차 구조서
    
6. Storyboard
    
7. Slide Script
    
8. PPT Design Data
    
9. PPT File
    
10. QA Report
    
11. 수주확률 분석서