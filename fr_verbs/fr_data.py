class FrData:
    def __init__(self, selection):
        self.selection = selection

        # Define the personal pronouns in English and Swahili along with audio links
        self.verbs = {
            "1st Person": {
                "Singular": {
                    "text": "I (que je sois)",
                    "question": "que je",
                    "answer": "sois",
                    "audio": ""
                },
                "Plural": {
                    "text": "We (que nous soyons)",
                    "question": "que nous",
                    "answer": "soyons",
                    "audio": ""
                }
            },
            "2nd Person": {
                "Singular": {
                    "text": "You (que tu sois)",
                    "question": "que tu",
                    "answer": "sois",
                    "audio": ""
                },
                "Plural": {
                    "text": "You (que vous soyez)",
                    "question": "que vous",
                    "answer": "soyez",
                    "audio": ""
                }
            },
            "3rd Person": {
                "Singular": {
                    "text": "He/She (qu'il/qu'elle soit)",
                    "question": "qu'il/qu'elle",
                    "answer": "soit",
                    "audio": ""
                },
                "Plural": {
                    "text": "They (qu'ils/qu'elles soient)",
                    "question": "qu'ils/qu'elles",
                    "answer": "soient",
                    "audio": ""
                }
            }
        }

    def test(self):
        lst = {}
        if self.selection == "Subjunctive être":
            lst = {
                "1s": ("sois", "que je ___ heureux.", "I am happy."),
                "2s": ("sois", "que tu ___ en bonne santé.", "You are healthy."),
                "3s": ("soit", "qu'il/qu'elle ___ à l'heure.", "He/She is on time."),
                "1p": ("soyons", "que nous ___ amis.", "We are friends."),
                "2p": ("soyez", "que vous ___ prêts.", "You all are ready."),
                "3p": ("soient", "qu'ils/qu'elles ___ contents.", "They are happy.")
            }
        return lst
