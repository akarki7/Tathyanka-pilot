import streamlit as st
import utils as utl
from PIL import Image


def main():
    utl.local_css("frontend/css/style.css")
    utl.remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")
    image = Image.open("frontend/img/tathyanka_logo.jpg")

    st.image(image)

    # title and description

    st.markdown(
        "<h1 style= 'text-align: center;'>NLQ for Banking Data</h1>",
        unsafe_allow_html=True,
    )

    searchbox()


def searchbox():
    # search bar
    query = st.text_input("", "")

    if query:
        st.write(f"You entered = '{query}'")


if __name__ == "__main__":
    main()
