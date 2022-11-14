import streamlit as st
import utils as utl
from PIL import Image
import pandas as pd
import numpy as np


def main():
    utl.local_css("static/css/style.css")
    utl.remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")
    image = Image.open("static/img/tathyanka_logo.jpg")

    st.image(image)

    # title and description

    st.markdown(
        "<h1 style= 'text-align: center;'>NLQ for Banking Data</h1>",
        unsafe_allow_html=True,
    )

    searchbox()


def searchbox():
    # search bar
    question = st.text_input("", "")
    utl.temp_display(question)
    # utl.sql_display(question)
    # utl.test_db()


if __name__ == "__main__":
    main()
