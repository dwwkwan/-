import streamlit as st

# 페이지 스타일 설정 (배경 초록색, 버튼 및 텍스트 디자인)
st.markdown(
    """
    <style>
    /* 전체 앱 배경 초록색 */
    .stApp {
        background-color: #2ECC71;
    }
    
    /* 화면 중앙 배치용 컨테이너 */
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
    }

    /* 동그란 빨간색 버튼 스타일 */
    div.stButton > button {
        background-color: #E74C3C;
        color: white;
        border-radius: 50%;
        width: 140px;
        height: 140px;
        border: none;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }
    div.stButton > button:hover {
        background-color: #C0392B;
        color: white;
    }

    /* 검은색 '안녕' 텍스트 스타일 */
    .hello-text {
        color: black;
        font-size: 64px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 세션 상태를 이용해 버튼 클릭 여부 저장
if "clicked" not in st.session_state:
    st.session_state.clicked = False

def on_button_click():
    st.session_state.clicked = True

# 중앙 컨테이너 시작
st.markdown('<div class="center-container">', unsafe_allow_html=True)

if not st.session_state.clicked:
    # 빨간색 동그란 버튼
    if st.button("클릭", on_click=on_button_click):
        pass
else:
    # 검은색 '안녕' 글씨
    st.markdown('<div class="hello-text">안녕</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
