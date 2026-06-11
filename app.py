import streamlit as st
import random
import time

st.set_page_config(page_title="미니게임 모음", page_icon="🎮")

st.title("🎮 미니게임 6종 모음")

# 세션 상태 초기화
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)

game = st.sidebar.selectbox(
    "게임 선택",
    [
        "숫자 맞추기",
        "가위바위보",
        "동전 던지기",
        "주사위 굴리기",
        "퀴즈 게임",
        "행운의 슬롯머신"
    ]
)

# 1. 숫자 맞추기
if game == "숫자 맞추기":
    st.header("🔢 숫자 맞추기")

    guess = st.number_input(
        "1~100 사이 숫자를 입력하세요",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("확인"):
        if guess < st.session_state.answer:
            st.warning("UP!")
        elif guess > st.session_state.answer:
            st.warning("DOWN!")
        else:
            st.success("🎉 정답!")
            st.session_state.answer = random.randint(1, 100)

# 2. 가위바위보
elif game == "가위바위보":
    st.header("✌️ 가위바위보")

    user = st.radio(
        "선택하세요",
        ["가위", "바위", "보"]
    )

    if st.button("대결"):
        computer = random.choice(["가위", "바위", "보"])

        st.write("컴퓨터:", computer)

        if user == computer:
            st.info("무승부!")
        elif (
            (user == "가위" and computer == "보") or
            (user == "바위" and computer == "가위") or
            (user == "보" and computer == "바위")
        ):
            st.success("승리!")
        else:
            st.error("패배!")

# 3. 동전 던지기
elif game == "동전 던지기":
    st.header("🪙 동전 던지기")

    if st.button("던지기"):
        result = random.choice(["앞면", "뒷면"])
        st.success(f"결과: {result}")

# 4. 주사위 굴리기
elif game == "주사위 굴리기":
    st.header("🎲 주사위")

    if st.button("굴리기"):
        result = random.randint(1, 6)
        st.success(f"🎲 {result}")

# 5. 퀴즈 게임
elif game == "퀴즈 게임":
    st.header("📚 퀴즈 게임")

    score = 0

    q1 = st.text_input("대한민국의 수도는?")
    q2 = st.text_input("1 + 1 = ?")
    q3 = st.text_input("태양계에서 가장 큰 행성은?")

    if st.button("채점"):
        if q1.strip() == "서울":
            score += 1

        if q2.strip() == "2":
            score += 1

        if q3.strip() in ["목성", "Jupiter"]:
            score += 1

        st.success(f"점수: {score}/3")

# 6. 슬롯머신
elif game == "행운의 슬롯머신":
    st.header("🎰 슬롯머신")

    if st.button("돌리기"):
        symbols = ["🍒", "🍋", "🍇", "⭐", "💎"]

        a = random.choice(symbols)
        b = random.choice(symbols)
        c = random.choice(symbols)

        st.markdown(
            f"# {a} {b} {c}"
        )

        if a == b == c:
            st.success("🎉 JACKPOT!")
        elif a == b or b == c or a == c:
            st.info("😊 당첨!")
        else:
            st.error("꽝!")
