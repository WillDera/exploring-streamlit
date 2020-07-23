import time
import datetime
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

# SelectBox
occupation = st.selectbox("Your Occupation", [
                          "Web Developer", "Data Scientist", "Business Intel Analyst"])
st.write("You selected ", occupation)


# Multiselect
location = st.multiselect("Where do you work?", (
    "London", "Las Vegas", "Lagos", "Accra", "Kiev", "Nepal", "Rivers", "Abuja"))
st.write("You selected %s location(s)", len(location))

# Slider
age = st.slider("Your level?", 1, 10)
if age < 4:
    st.write("You're at Beginner Level")
elif age > 7:
    st.write("You're at Pro Level")
else:
    st.write("You're at Intermidiate Level")

# Button
# st.button("Simple Button")
if st.button("Tell Me Something"):
    st.text("The Earth Isn't Flat! or Is it?")

# Handling Text Input
firstname = st.text_input("Firstname: ", "Type Here...")
# if st.button("Submit"):
#     result = firstname.title()
#     st.success(result)

# Handling Text Area
Message = st.text_input("Message: ", "Type Here...")
if st.button("Submit"):
    result = Message.title()
    st.success(result)

# Date Input
today = st.date_input("Today is:", datetime.datetime.now())

# Time
current_time = st.time_input("Time is:", datetime.time())

# Displaying JSON
st.text("Display JSON")
st.json({'name': "Will", 'level': "Kami"})

# Display Code
st.text("Display Raw code")
# first method
st.code("import numpy as np")

# second method
with st.echo():
    # Shows even comment
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar
bar = st.progress(0)
for p in range(10):
    bar.progress(p+1)

# Spinner
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Finished!")
