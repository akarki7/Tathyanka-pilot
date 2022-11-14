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
    # temp_display(question)
    sql_display(question)
    test_db()


def test_db():
    conn = utl.connect_to_database()
    cursor = conn.cursor(as_dict=True)
    cursor.execute("Select * FROM V_DepositLendingTrendByYearMonth")
    data = cursor.fetchall()
    data_df = pd.DataFrame(data)

    print(data_df)

    cursor.close()


def sql_display(question):
    if question:
        import models as mdl

        result = mdl.get_sql(question)
        result = result[6:]
        result = result[:-4]
        if any(x in question for x in ["deposit", "Deposit"]):
            result = result.replace("table", "deposit")

        st.write(result)


def temp_display(query):
    if query:
        if query == "bank":
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.line_chart(chart_data)
        elif query == "nepse":
            chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
        elif query == "prabhu":
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.area_chart(chart_data)
        else:
            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                st.write("")

            with col2:
                st.image("static/img/notfound.png")

            with col3:
                st.write("")


if __name__ == "__main__":
    main()
