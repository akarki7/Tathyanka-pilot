import streamlit as st
import pymssql
import pandas as pd
import numpy as np
from dotenv import dotenv_values
import altair as alt

config = dotenv_values(".env")

host_db = config["HOST_db"]
user_db = config["USER_db"]
passw_db = config["PASSWORD_db"]
name_db = config["DATABASE_db"]


def connect_to_database():
    conn = pymssql.connect(
        host=host_db,
        user=user_db,
        password=passw_db,
        database=name_db,
    )
    return conn


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(
        f'<i class="material-icons search-button">{icon_name}</i>',
        unsafe_allow_html=True,
    )


def temp_display(query):
    if query:
        if query == "deposit":
            data = get_deposit_data()
            st.line_chart(data, x="MonthName", y="DEPOSIT")
        elif query == "lending":
            data = get_lending_data()
            c = (
                alt.Chart(data)
                .mark_line(color="red")
                .encode(x="MonthName", y="LENDING")
            )
            st.altair_chart(c, use_container_width=True)
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


def sql_display(question):
    if question:
        import models as mdl

        result = mdl.get_sql(question)
        result = result[6:]
        result = result[:-4]
        if any(x in question for x in ["deposit", "Deposit"]):
            result = result.replace("table", "deposit")

        st.write(result)


def test_db():
    conn = connect_to_database()
    cursor = conn.cursor(as_dict=True)
    cursor.execute("Select * FROM V_DepositLendingTrendByYearMonth")
    data = cursor.fetchall()
    data_df = pd.DataFrame(data)

    print(data_df)

    cursor.close()


def get_deposit_data():
    conn = connect_to_database()
    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        "Select MonthName,DEPOSIT  FROM V_DepositLendingTrendByYearMonth ORDER BY MonthName"
    )
    data = cursor.fetchall()
    data_df = pd.DataFrame(data)
    cursor.close()
    return data_df


def get_lending_data():
    conn = connect_to_database()
    cursor = conn.cursor(as_dict=True)
    cursor.execute(
        "Select MonthName,LENDING  FROM V_DepositLendingTrendByYearMonth ORDER BY MonthName"
    )
    data = cursor.fetchall()
    data_df = pd.DataFrame(data)
    cursor.close()
    return data_df
