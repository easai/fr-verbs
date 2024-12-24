import streamlit as st
import pandas as pd
from data import VerbData
from test import VerbTest
from table import VerbTable
from quiz import VerbQuiz
from desc import VerbDesc
from const import TITLE, SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR


def clear_inputs():
    for person, _ in verbs.items():
        col1, col2 = st.columns(2)

        with col1:
            st.session_state[f"singular_{person}"] = ""
        with col2:
            st.session_state[f"plural_{person}"] = ''


# , on_change=clear_inputs)
menuItem = st.sidebar.selectbox(TITLE, (SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR))

dat = VerbData(menuItem)
verbs = dat.verbs

# Streamlit app title
st.title("French Verbs")
st.write("Challenge yourself with our French verbs quizzes and tests, and see how much you know! The app can test various aspects of French verbs.")
st.subheader(menuItem)

# Side menu
VerbDesc(menuItem)

# Accordion for the pronoun table
VerbTable(verbs)

# Pronouns table quiz
VerbQuiz(verbs)

# Fill-in-the-box test
test = dat.test()
if test != "":
    swquiz = VerbTest(test)
