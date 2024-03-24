#Imported necesseary modules
import streamlit as st
import whisper

st.title("Audio To Text Generation")

st.text("Step 1 : Click the below browse file and upload your audio file.")
st.text("Step 2 : After it uploaded, you can play, hear and verify it in the left side bar.")
st.text("Step 3 : Click 'Transcribe Audio' button.")

#Upload external audio
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

#Model loading
model = whisper.load_model("base")

#sidebar
st.sidebar.header("Play your Audio file")
st.sidebar.audio(audio_file)

st.subheader("Output : ")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")

st.sidebar.divider()
st.sidebar.write("This project was developed by,")
st.sidebar.write("Athiyaman M")