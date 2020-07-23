from PIL import Image
import streamlit as st

# Text/Title
st.title("Streamlit Kami")

# Header/Subheader
st.header("The kami header")
st.subheader("The kami subheader")

# Normal Text
st.text("Hello from kami")

# Markdown
st.markdown("### This is a kamidown")

# Error/Colourful text
st.success("Kami sucess")
st.info("Kamisoooo")
st.warning("Be damned")

# Get help Info about Python range
st.help(range)

# Writing text/super func
st.write("Text with kami")

st.write(range(10))

# Working with images
img = Image.open("camper-image-placeholder.png")
st.image(img, width=400, caption="Simple Streamlit Image")

# Video
# video_file = open("video", "rb").read()
# st.video(video_file)

# Audio
audio_file = open("./PolynomialRegressionandPipelines.mp3", "rb").read()
st.audio(audio_file, format="audio/mp3")


# Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing/Hiding Widget")

# Radio Button
status = st.radio("What is your status", ("Active", "Inactive"))

if status == "Active":
    st.success("You're Active")
else:
    st.warning("Inactive")
