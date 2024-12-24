import streamlit as st
from const import SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR

class VerbDesc:
    def __init__(self, menuItem):
        if menuItem == SUBJUNCTIVE_ETRE or menuItem == SUBJUNCTIVE_AVOIR:
            desc = "The French subjunctive is a verb mood used to express doubt, emotion, necessity, or uncertainty, often introduced by 'que' and requiring specific conjugations for each subject pronoun."
        st.write(desc)
