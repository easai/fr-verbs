import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from const import TITLE, SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR, CONDITIONAL_ETRE, CONDITIONAL_AVOIR, PRETERIT_ETRE

class VerbQuiz:
    def __init__(self, verbs, menuItem):
        self.verbs = verbs
        audio_html = f"""
<style>
.stAudio {{
    height: 30px;
}}
</style>
"""
        st.markdown(audio_html, unsafe_allow_html=True)

        # Loop through the pronouns to create inputs
        for person, forms in verbs.items():
            col1, col2 = st.columns(2)

            with col1:
                singular_answer = st.text_input(
                    f"{person} Singular", key=f"singular_{person}", autocomplete="off")
                if singular_answer:
                    correct_singular = forms["Singular"]["answer"]
                    if singular_answer.strip().lower() == correct_singular.lower():
                        st.success("✅ Correct")
                    else:
                        st.error(f"❌ Incorrect (Correct: {correct_singular})")
                if forms["Singular"]["audio"]:
                    st.audio(forms["Singular"]["audio"])

            with col2:
                plural_answer = st.text_input(
                    f"{person} Plural", key=f"plural_{person}", autocomplete="off")
                num = "plural"
                if menuItem == PRETERIT_ETRE and person != "3rd Person":
                    st.button("û", on_click=self.add_circumflex, key=f"{num}_{person}_circumflex", args=(num, person,))
                if plural_answer:
                    correct_plural = forms["Plural"]["answer"]
                    if plural_answer.strip().lower() == correct_plural.lower():
                        st.success("✅ Correct")
                    else:
                        st.error(f"❌ Incorrect (Correct: {correct_plural})")

                # Play audio for plural
                if forms["Plural"]["audio"]:
                    st.audio(forms["Plural"]["audio"])

        st.button("Clear", on_click=self.clear_inputs)

    def clear_inputs(self):
        for person, _ in self.verbs.items():
            col1, col2 = st.columns(2)

            with col1:
                st.session_state[f"singular_{person}"] += "û"
            with col2:
                st.session_state[f"plural_{person}"] = ''

    def add_circumflex(self, num, person):
        st.session_state[f"{num}_{person}"] += "û"
