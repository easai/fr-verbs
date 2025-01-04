import streamlit as st
import pandas as pd

from data import VerbData
from test import VerbTest
from table import VerbTable
from quiz import VerbQuiz
from const import TITLE


st.set_page_config(
    page_title=TITLE,
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="auto",
)


def clear_ending_with_input():
    for key in list(st.session_state.keys()):
        if key.endswith("_input"):
            st.session_state[key] = ""

verbData = VerbData()
menu = verbData.get_menu()
selected_item = st.sidebar.selectbox(TITLE, menu, on_change=clear_ending_with_input)
menuIndex = menu.index(selected_item)
table = verbData.get_table(menuIndex)

# Streamlit app title
st.title(TITLE)
st.write("Challenge yourself with our French verbs quizzes and tests, and see how much you know! The app can test various aspects of French verbs.")
st.subheader(selected_item)

# Side menu
st.write(verbData.get_desc(menuIndex))

st.write("French uses the following characters: é, à, è, ù, â, ê, î, ô, û, ë, ï, ü, ÿ, ç.")

# Accordion for the pronoun table
VerbTable(table)

# Pronouns table quiz
VerbQuiz(table)

# Fill-in-the-box test
test = verbData.get_test(menuIndex)
if test != "":
    swquiz = VerbTest(test)
