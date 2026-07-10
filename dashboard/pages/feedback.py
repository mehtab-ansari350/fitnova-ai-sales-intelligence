import streamlit as st

from api import submit_feedback

st.title("💬 Submit Feedback")

call_id = st.number_input(
    "Call ID",
    min_value=1,
    step=1,
)

reviewer = st.text_input(
    "Reviewer Name"
)

decision = st.selectbox(
    "Decision",
    [
        "ACCEPTED",
        "CONTESTED"
    ]
)

comment = st.text_area(
    "Comment"
)

if st.button("Submit Feedback"):

    if reviewer.strip() == "":
        st.error("Reviewer name is required.")

    else:

        response = submit_feedback(
            call_id,
            reviewer,
            decision,
            comment,
        )

        if response.status_code == 201:

            st.success("✅ Feedback submitted successfully!")

            st.balloons()

            st.success("Feedback submitted successfully!")

            st.write("### Saved Feedback")

            st.json(response.json())

        else:

            st.error("Failed to submit feedback.")
            st.write(response.text)