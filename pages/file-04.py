import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image 


tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
st.write("Appear in both")

with tab1:
    st.write("Content for Tab 1")
    st.write("Does not appear in tab 2")
with tab2:
    st.write("Content for Tab 2")



placeholder = st.empty()
placeholder.text("Initial text")
# Later in the code
placeholder.text("Updated text")

uploaded_file = st.file_uploader("Upload an Excel or Image file", type=["xls", "xlsx", "xlsm", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()  # Get file extension
    
    if file_extension in ["xls", "xlsx", "xlsm"]:
        # ✅ Read and Display Excel File
        dataframe = pd.read_excel(uploaded_file)
        st.write("### 📊 Excel File Preview:")
        st.dataframe(dataframe)
    
    elif file_extension in ["png", "jpg", "jpeg"]:
        # ✅ Read and Display Image
        image = Image.open(uploaded_file)
        st.write("### 🖼️ Uploaded Image:")
        st.image(image, caption="Uploaded Image", use_container_width =True)
    else:
        # ❌ Unsupported file format
        st.error("Unsupported file type! Please upload an Excel or Image file.")

import streamlit as st
import time

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()

st.caption("This is a caption __bold__  :blue[colors] and emojis :sunglasses:")

code = '''def hello():
    a = 10
    print("Hello, Streamlit!")
    return a'''
st.code(code, language="python")

st.write("This is some text.")

values = st.slider("This is a slider", 0, 150, (25, 75))
print(values)
print(type(values))
st.write(f"Selected range: {values[0]} to {values[1]}")

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule



def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)

if st.button("Send Balloons!!!"):
    st.balloons()