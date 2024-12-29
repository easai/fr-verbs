import streamlit as st
from const import SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR, CONDITIONAL_ETRE, CONDITIONAL_AVOIR, PRETERIT_ETRE

class VerbDesc:
    def __init__(self, menuItem):
        if menuItem == SUBJUNCTIVE_ETRE or menuItem == SUBJUNCTIVE_AVOIR:
            desc = "The French subjunctive is a verb mood used to express doubt, emotion, necessity, or uncertainty, often introduced by 'que' and requiring specific conjugations for each subject pronoun."
        elif menuItem == CONDITIONAL_ETRE or menuItem == CONDITIONAL_AVOIR:
            desc = "The conditional mood in French is used to express actions or events that are dependent on certain conditions, often translated as 'would' in English."
        elif menuItem == PRETERIT_ETRE:
            desc = "The preterit (or passé simple) is a verb tense used to describe actions that were completed in the past and are often used in formal writing and literature."
        st.write(desc)
