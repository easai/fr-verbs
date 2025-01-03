import streamlit as st
import pandas as pd
from data import VerbData
from test import VerbTest
from table import VerbTable
from quiz import VerbQuiz
from desc import VerbDesc
from const import TITLE, SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR, CONDITIONAL_ETRE, CONDITIONAL_AVOIR, PRETERIT_ETRE, PRETERIT_AVOIR, IMPERFECT_ETRE

import streamlit as st

st.set_page_config(
    page_title=TITLE,
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="auto",
)

def clear_inputs():
    for person, _ in verbs.items():
        st.session_state[f"singular_{person}_input"] = ""
        st.session_state[f"plural_{person}_input"] = ""


menuItem = st.sidebar.selectbox(TITLE, (SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR, CONDITIONAL_ETRE, CONDITIONAL_AVOIR, PRETERIT_ETRE, PRETERIT_AVOIR, IMPERFECT_ETRE), on_change=clear_inputs)

dat = VerbData(menuItem)
verbs = dat.verbs

# Streamlit app title
st.title(TITLE)
st.write("Challenge yourself with our French verbs quizzes and tests, and see how much you know! The app can test various aspects of French verbs.")
st.subheader(menuItem)

# Side menu
VerbDesc(menuItem)

st.write("French uses the following characters: é, à, è, ù, â, ê, î, ô, û, ë, ï, ü, ÿ, ç.")

# Accordion for the pronoun table
VerbTable(verbs)

# Pronouns table quiz
VerbQuiz(verbs, menuItem)

# Fill-in-the-box test
test = dat.test()
if test != "":
    swquiz = VerbTest(test)
