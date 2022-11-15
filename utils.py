import streamlit as st
import pymssql
import pandas as pd
import numpy as np
from dotenv import dotenv_values
import altair as alt
import re

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


def temp_display(text):
    MONTHS_LIST_DL = get_data_from_db(
        "Select MonthName FROM V_DepositLendingTrendByYearMonth ORDER BY MonthName"
    )
    pattern_deposit = re.match("deposit last \d{1,2} month$", text)
    pattern_lending = re.match("lending last \d{1,2} month$", text)
    pattern_bank__deposit_top = re.match("deposit bank top \d{1,2} last month$", text)
    pattern_bank_deposit_bottom = re.match(
        "deposit bank bottom \d{1,2} last month$", text
    )
    pattern_bank__lending_top = re.match("lending bank top \d{1,2} last month$", text)
    pattern_bank_lending_bottom = re.match(
        "lending bank bottom \d{1,2} last month$", text
    )
    if text:
        if text == "deposit all":
            query = "Select MonthName,DEPOSIT  FROM V_DepositLendingTrendByYearMonth ORDER BY MonthName"
            data = get_data_from_db(query)
            st.line_chart(data, x="MonthName", y="DEPOSIT")
        elif text == "lending all":
            query = "Select MonthName,LENDING  FROM V_DepositLendingTrendByYearMonth ORDER BY MonthName"
            data = get_data_from_db(query)
            c = (
                alt.Chart(data)
                .mark_line(color="red")
                .encode(x="MonthName", y="LENDING")
            )
            st.altair_chart(c, use_container_width=True)
        elif pattern_deposit:
            month_count = re.findall(r"\d{1,2}", text)[0]
            query = f"Select TOP({month_count}) MonthName,DEPOSIT  FROM V_DepositLendingTrendByYearMonth ORDER BY MonthName DESC"
            data = get_data_from_db(query)
            st.line_chart(data, x="MonthName", y="DEPOSIT")
        elif pattern_lending:
            month_count = re.findall(r"\d{1,2}", text)[0]
            query = f"Select TOP({month_count}) MonthName,LENDING  FROM V_DepositLendingTrendByYearMonth ORDER BY MonthName DESC"
            data = get_data_from_db(query)
            c = (
                alt.Chart(data)
                .mark_line(color="red")
                .encode(x="MonthName", y="LENDING")
            )
            st.altair_chart(c, use_container_width=True)
        elif pattern_bank__deposit_top:
            month = MONTHS_LIST_DL["MonthName"].iloc[-1]
            month_count = re.findall(r"\d{1,2}", text)[0]
            query = f"Select TOP({month_count}) BankCode,DEPOSIT FROM V_DepositLendingTrendByYearMonthBank WHERE MonthName='{month}' ORDER BY DEPOSIT DESC"
            data = get_data_from_db(query)
            c = (
                alt.Chart(data)
                .mark_bar(color="green")
                .encode(
                    x=alt.X("BankCode", sort=None), y="DEPOSIT", tooltip=["DEPOSIT"]
                )
            )
            st.altair_chart(c, use_container_width=True)
        elif pattern_bank_deposit_bottom:
            month = MONTHS_LIST_DL["MonthName"].iloc[-1]
            month_count = re.findall(r"\d{1,2}", text)[0]
            query = f"Select TOP({month_count}) BankCode,DEPOSIT FROM V_DepositLendingTrendByYearMonthBank WHERE MonthName='{month}' ORDER BY DEPOSIT ASC"
            data = get_data_from_db(query)
            c = (
                alt.Chart(data)
                .mark_bar(color="red")
                .encode(
                    x=alt.X("BankCode", sort=None), y="DEPOSIT", tooltip=["DEPOSIT"]
                )
            )
            st.altair_chart(c, use_container_width=True)

        elif pattern_bank__lending_top:
            month = MONTHS_LIST_DL["MonthName"].iloc[-1]
            month_count = re.findall(r"\d{1,2}", text)[0]
            query = f"Select TOP({month_count}) BankCode,LENDING FROM V_DepositLendingTrendByYearMonthBank WHERE MonthName='{month}' ORDER BY LENDING DESC"
            data = get_data_from_db(query)
            c = (
                alt.Chart(data)
                .mark_bar(color="green")
                .encode(
                    x=alt.X("BankCode", sort=None), y="LENDING", tooltip=["LENDING"]
                )
            )
            st.altair_chart(c, use_container_width=True)
        elif pattern_bank_lending_bottom:
            month = MONTHS_LIST_DL["MonthName"].iloc[-1]
            month_count = re.findall(r"\d{1,2}", text)[0]
            query = f"Select TOP({month_count}) BankCode,LENDING FROM V_DepositLendingTrendByYearMonthBank WHERE MonthName='{month}' ORDER BY LENDING ASC"
            data = get_data_from_db(query)
            c = (
                alt.Chart(data)
                .mark_bar(color="red")
                .encode(
                    x=alt.X("BankCode", sort=None), y="LENDING", tooltip=["LENDING"]
                )
            )
            st.altair_chart(c, use_container_width=True)

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


def get_data_from_db(query):
    conn = connect_to_database()
    cursor = conn.cursor(as_dict=True)
    cursor.execute(query)
    data = cursor.fetchall()
    data_df = pd.DataFrame(data)
    cursor.close()
    return data_df
