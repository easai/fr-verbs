import streamlit as st
from const import SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR, CONDITIONAL_ETRE

class VerbDesc:
    def __init__(self, menuItem):
        if menuItem == SUBJUNCTIVE_ETRE or menuItem == SUBJUNCTIVE_AVOIR:
            desc = "The French subjunctive is a verb mood used to express doubt, emotion, necessity, or uncertainty, often introduced by 'que' and requiring specific conjugations for each subject pronoun."
        elif menuItem == CONDITIONAL_ETRE:
            desc = "The conditional mood in French is used to express actions or events that are dependent on certain conditions, often translated as 'would' in English."
        st.write(desc)
