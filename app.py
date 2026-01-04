import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정
st.set_page_config(page_title="Gomoku Dev Project", layout="wide")

# 2. 사이드바 - 보고서 내용 작성
with st.sidebar:
    st.title("📄 진로 탐구 보고서")
    st.subheader("주제: 웹 기술을 활용한 오목 게임 구현")
    st.markdown("""
    **1. 개발 환경**
    - 언어: Python, JavaScript
    - 프레임워크: Streamlit
    - 라이브러리: HTML5 Canvas API
    
    **2. 핵심 알고리즘**
    - 8방향 탐색 승리 판정
    - `setInterval` 활용 비동기 타이머
    - Radial Gradient 입체 그래픽
    """)
    st.divider()
    st.write("제작자: [본인 이름]")

# 3. 메인 화면 UI
st.title("🎮 JavaScript 기반 오목 웹 앱")
st.info("이 게임은 JavaScript로 작성되었으며, Streamlit 컴포넌트로 렌더링되었습니다.")

# 사용자가 작성한 HTML/JS 코드를 그대로 변수에 담습니다.
# 주의: f-string을 사용하지 않으려면 따옴표 3개로 감싸는 것이 가장 안전합니다.
html_source = """
<div style="display: flex; flex-direction: column; align-items: center; font-family: 'Malgun Gothic', sans-serif;">
    <div style="display: flex; gap: 30px; margin-bottom: 15px; background: #eee; padding: 10px 30px; border-radius: 50px; box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);">
        <div style="text-align: center;">
            <div style="font-size: 0.8em; color: #666;">BLACK</div>
            <div id="score-black" style="font-size: 1.8em; font-weight: bold; color: #000;">0</div>
        </div>
        <div style="font-size: 1.5em; font-weight: bold; color: #aaa; align-self: center;">:</div>
        <div style="text-align: center;">
            <div style="font-size: 0.8em; color: #666;">WHITE</div>
            <div id="score-white" style="font-size: 1.8em; font-weight: bold; color: #444;">0</div>
        </div>
    </div>
    </div>

<script>
    // 사용자님이 주신 <script> 로직 전체 복사
</script>
"""

# 4. Streamlit에 HTML 코드 주입
# height와 width를 넉넉하게 설정해야 스크롤이 생기지 않습니다.
components.html(html_source, height=800, scrolling=False)
