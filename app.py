import streamlit as st

# 페이지 설정 및 CSS 스타일 (콩그리 밈 연출 및 공포스러운 버튼)
st.markdown(
    """
    <style>
    /* 전체 앱 배경 초록색 */
    .stApp {
        background-color: #1b3822;
    }
    
    /* 화면 전체를 채우는 중앙 정렬 컨테이너 */
    .center-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 75vh;
        width: 100%;
    }

    /* Streamlit 버튼을 감싸는 div를 중앙으로 정렬 */
    .stButton {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* 피처럼 붉고 음산한 동그란 버튼 스타일 */
    div.stButton > button {
        background: radial-gradient(circle, #8B0000 0%, #3a0000 100%) !important;
        color: #ffcccc !important;
        border-radius: 50% !important;
        width: 160px !important;
        height: 160px !important;
        min-height: unset !important;
        border: 3px solid #ff0000 !important;
        font-size: 20px;
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 2px;
        box-shadow: 0 0 25px #ff0000, inset 0 0 15px #000000 !important;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        animation: pulse-horror 2s infinite;
    }
    
    @keyframes pulse-horror {
        0% { transform: scale(1); box-shadow: 0 0 15px #8B0000, inset 0 0 15px #000; }
        50% { transform: scale(1.05); box-shadow: 0 0 35px #ff0000, inset 0 0 25px #3a0000; }
        100% { transform: scale(1); box-shadow: 0 0 15px #8B0000, inset 0 0 15px #000; }
    }

    div.stButton > button:hover {
        background: radial-gradient(circle, #ff0000 0%, #5a0000 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 0 45px #ff0000, inset 0 0 20px #000000 !important;
    }

    /* 검은색 '안녕' 텍스트 스타일 */
    .hello-text {
        color: #000000;
        font-size: 80px;
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        width: 100%;
        text-shadow: 2px 2px 10px rgba(255, 0, 0, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 세션 상태 초기화
if "clicked" not in st.session_state:
    st.session_state.clicked = False

def on_button_click():
    st.session_state.clicked = True

# 화면 중앙 배치를 위한 HTML 레이아웃
st.markdown('<div class="center-wrapper">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if not st.session_state.clicked:
        if st.button("위험", on_click=on_button_click):
            pass
    else:
        # '안녕' 텍스트 출력과 동시에 해당 유튜브 영상의 1분 36초(96초)부터 1분 45초(105초) 구간 재생
        st.markdown('<div class="hello-text">안녕</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-top: 20px;">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/jpjl0PGjMF8?start=96&end=105&autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)
