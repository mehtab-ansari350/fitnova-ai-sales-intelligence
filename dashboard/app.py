import streamlit as st

st.set_page_config(
    page_title="FitNova AI Sales Intelligence",
    page_icon="📞",
    layout="wide",
)

st.title("📞 FitNova AI Sales Intelligence")
st.markdown("### AI-Powered Sales Call Quality Monitoring Dashboard")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🤖 AI Engine",
        value="Online"
    )

with col2:
    st.metric(
        label="🎙️ Speech-to-Text",
        value="Whisper"
    )

with col3:
    st.metric(
        label="🧠 LLM",
        value="Gemini"
    )

st.divider()

st.subheader("🚀 Features")

c1, c2 = st.columns(2)

with c1:
    st.success("""
✅ Upload Sales Calls

✅ Automatic Speech-to-Text

✅ AI Sales Analysis

✅ Issue Detection
""")

with c2:
    st.info("""
✅ Recommendations

✅ Human Feedback

✅ SQLite Database

✅ REST API
""")

st.divider()

st.subheader("📋 Workflow")

st.markdown("""
1. Upload a sales call recording.

2. AI transcribes the audio.

3. Gemini analyzes sales quality.

4. Issues & recommendations are generated.

5. Reviewer submits feedback.
""")

st.divider()

st.success("🎉 System Status: Ready")