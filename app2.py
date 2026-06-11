import streamlit as st
import time
import random

st.set_page_config(
    page_title="Reaction Master",
    page_icon="⚡",
    layout="centered"
)

# -------------------------
# CSS
# -------------------------
st.markdown("""
<style>
.main {
    text-align:center;
}

.big-title {
    font-size:50px;
    font-weight:bold;
    color:#00ffcc;
}

.score-box {
    padding:15px;
    border-radius:15px;
    background-color:#1e1e1e;
    text-align:center;
    font-size:22px;
}

.result-box {
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Session State
# -------------------------
if "game_state" not in st.session_state:
    st.session_state.game_state = "idle"

if "best_score" not in st.session_state:
    st.session_state.best_score = None

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "target_time" not in st.session_state:
    st.session_state.target_time = None

# -------------------------
# Header
# -------------------------
st.markdown(
    '<p class="big-title">⚡ REACTION MASTER ⚡</p>',
    unsafe_allow_html=True
)

st.write(
"""
### 게임 방법

1. 게임 시작 버튼을 누른다.
2. 화면이 빨간색 상태일 때는 기다린다.
3. 초록색 신호가 나오면 즉시 클릭한다.
4. 너무 빨리 누르면 실격!
"""
)

# 최고 기록
if st.session_state.best_score is not None:
    st.markdown(
        f"""
        <div class="score-box">
        🏆 최고 기록<br>
        <b>{st.session_state.best_score:.3f}초</b>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# -------------------------
# 시작 전
# -------------------------
if st.session_state.game_state == "idle":

    if st.button("🚀 게임 시작", use_container_width=True):
        st.session_state.game_state = "waiting"
        st.session_state.target_time = time.time() + random.uniform(2, 6)
        st.rerun()

# -------------------------
# 대기 상태
# -------------------------
elif st.session_state.game_state == "waiting":

    st.error("🔴 기다리세요!")

    now = time.time()

    if now >= st.session_state.target_time:
        st.session_state.game_state = "ready"
        st.session_state.start_time = time.time()
        st.rerun()

    if st.button("❌ 지금 클릭"):
        st.session_state.game_state = "fail"
        st.rerun()

    time.sleep(0.1)
    st.rerun()

# -------------------------
# 반응 단계
# -------------------------
elif st.session_state.game_state == "ready":

    st.success("🟢 지금 클릭!!!")

    if st.button("⚡ CLICK ⚡", use_container_width=True):

        reaction = time.time() - st.session_state.start_time

        st.session_state.last_score = reaction
        st.session_state.game_state = "result"

        if (
            st.session_state.best_score is None
            or reaction < st.session_state.best_score
        ):
            st.session_state.best_score = reaction

        st.rerun()

# -------------------------
# 조기 클릭
# -------------------------
elif st.session_state.game_state == "fail":

    st.markdown(
        """
        <div class="result-box">
        💀 실격!<br>
        너무 빨리 눌렀습니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("다시 하기"):
        st.session_state.game_state = "idle"
        st.rerun()

# -------------------------
# 결과
# -------------------------
elif st.session_state.game_state == "result":

    score = st.session_state.last_score

    if score < 0.18:
        rank = "👑 전설"
        msg = "사람 맞아?"
        st.balloons()

    elif score < 0.25:
        rank = "🔥 프로"
        msg = "엄청 빠르다!"

    elif score < 0.35:
        rank = "😎 상위권"
        msg = "훌륭한 반응속도"

    elif score < 0.50:
        rank = "🙂 평균 이상"
        msg = "좋은 기록"

    else:
        rank = "🐢 초보"
        msg = "조금 더 연습해보자"

    st.markdown(
        f"""
        <div class="result-box">
        ⚡ {score:.3f}초<br><br>
        {rank}<br>
        {msg}
        </div>
        """,
        unsafe_allow_html=True
    )

    if score == st.session_state.best_score:
        st.success("🏆 새로운 최고 기록!")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 다시 하기", use_container_width=True):
            st.session_state.game_state = "idle"
            st.rerun()

    with col2:
        if st.button("🗑 기록 초기화", use_container_width=True):
            st.session_state.best_score = None
            st.session_state.game_state = "idle"
            st.rerun()
