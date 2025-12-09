<%*
const today = tp.date.now("YYYY-MM-DD (ddd)");
const day = tp.date.now("d"); // 1=Mon ... 7=Sun

let workoutRoutine = "";
if (day == 6 || day == 7) {
    workoutRoutine = "### 😌 주말 회복 루틴\n- [ ] 가벼운 유산소 20–30분\n- [ ] 전신 스트레칭 10분";
} else {
    workoutRoutine = "### 🏋️ 평일 운동 루틴\n- [ ] 웨이트 (가슴/등/하체 중 선택)\n- [ ] 유산소 20분\n- [ ] 스트레칭 10분";
}
%>

# 🗓️ <%= today %>

---

## 🔥 전일 미완료 작업
```tasks
not done
```

---

## ✔ 오늘 할 일
```tasks
not done
```
- [ ] 주요 업무
- [ ] 운동
- [ ] 개인 루틴

---

## 📅 오늘의 일정
(여기에 Google Calendar Sync 플러그인이 자동 삽입됩니다)

---

## 🏋️ 오늘 운동(간단)
- [ ] 운동 수행 완료  
운동 내용: (수영 / 웨이트 등 자유 입력)

---

## 🏋️ 오늘 운동 루틴 (자동 분기)
<%= workoutRoutine %>

---

## 😄 감정 기록
- 기분(이모지):  
- 피로도(1~5):  
- 집중도(1~5):

---

## ✍️ 메모

---

## 🙏 오늘 회고
- 잘한 점:  
- 개선할 점:  
- 내일 목표:  
