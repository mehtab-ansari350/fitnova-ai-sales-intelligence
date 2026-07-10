import streamlit as st

from api import upload_call

st.title("📤 Upload Sales Call")

st.write("Upload a customer call recording for AI analysis.")

advisor_id = st.number_input(
    "Advisor ID",
    min_value=0,
    step=1,
)

customer_name = st.text_input(
    "Customer Name"
)

audio_file = st.file_uploader(
    "Choose an audio file",
    type=["mp3", "wav", "m4a"],
)

if st.button("Upload Call"):

    if audio_file is None:
        st.error("Please select an audio file.")
    elif customer_name.strip() == "":
        st.error("Please enter the customer name.")
    else:

        with st.spinner("Uploading and processing..."):

            response = upload_call(
                advisor_id,
                customer_name,
                audio_file,
            )

        if response.status_code == 201:

            data = response.json()

            st.success("✅ Call uploaded successfully!")

            st.subheader("Call Details")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Call ID",
                    data["id"]
                )

                st.metric(
                    "Language",
                    data["language"]
                )

            with col2:
                st.metric(
                    "Duration",
                    f"{data['duration_seconds']} sec"
                )

                st.metric(
                    "Status",
                    data["processing_status"]
                )

            st.success(
                f"Call UUID: {data['call_uuid']}"
            )

        else:

            st.error("Upload failed.")

            st.write(response.text)