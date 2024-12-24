import streamlit as st


class FrDesc:
    def __init__(self, menuItem):
        if menuItem == "Subjunctive être":
            desc = "The French subjunctive is a verb mood used to express doubt, emotion, necessity, or uncertainty, often introduced by 'que' and requiring specific conjugations for each subject pronoun."
        st.write(desc)
