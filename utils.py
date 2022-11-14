import streamlit as st
import pymssql
import pandas as pd
from dotenv import dotenv_values

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
