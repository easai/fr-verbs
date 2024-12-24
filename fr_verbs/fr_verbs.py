import streamlit as st
import pandas as pd
from fr_data import FrData
from fr_test import FrTest
from fr_table import FrTable
from fr_quiz import FrQuiz
from fr_desc import FrDesc


def clear_inputs():
    for person, _ in verbs.items():
        col1, col2 = st.columns(2)

        with col1:
            st.session_state[f"singular_{person}"] = ""
        with col2:
            st.session_state[f"plural_{person}"] = ''


menuItem = st.sidebar.selectbox("French Verb Quizzes", ("Subjunctive être"))#, on_change=clear_inputs)

dat = FrData(menuItem)
verbs = dat.verbs

# Streamlit app title
st.title("French Verbs")
st.write("Challenge yourself with our French verbs quizzes and tests, and see how much you know! The app can test various aspects of French verbs.")
st.subheader(menuItem)

# Side menu
FrDesc(menuItem)

# Accordion for the pronoun table
FrTable(verbs)

# Pronouns table quiz
FrQuiz(verbs)

# Fill-in-the-box test
test = dat.test()
if test != "":
    swquiz = FrTest(test)
