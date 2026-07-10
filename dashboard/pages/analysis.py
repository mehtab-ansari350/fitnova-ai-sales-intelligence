import streamlit as st

from api import get_analysis

st.title("📊 AI Sales Analysis")

call_id = st.number_input(
    "Call ID",
    min_value=1,
    step=1,
)

if st.button("Get Analysis"):

    response = get_analysis(call_id)

    if response.status_code == 200:

        data = response.json()
        score = data["overall_score"]

        if score >= 80:
            st.success(f"Overall Score : {score}/100")
        elif score >= 50:
            st.warning(f"Overall Score : {score}/100")
        else:
            st.error(f"Overall Score : {score}/100")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Call ID",
                data["call_id"]
            )

        with col2:
            st.metric(
                "Analysis ID",
                data["id"]
            )

        st.divider()

        st.subheader("📝 Summary")
        st.info(data["summary"])

        st.subheader("💡 Recommendations")
        st.success(data["recommendation"])

        st.caption(f"Generated on: {data['created_at']}")

    else:

        st.error("Analysis not found.")