from const import SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR


class VerbData:
    def __init__(self, selection):
        self.selection = selection

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

        if selection == SUBJUNCTIVE_AVOIR:
            self.verbs = {
                "1st Person": {
                    "Singular": {
                        "text": "I (que j'aie)",
                        "question": "que j'",
                        "answer": "aie",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (que nous ayons)",
                        "question": "que nous",
                        "answer": "ayons",
                        "audio": ""
                    }
                },
                "2nd Person": {
                    "Singular": {
                        "text": "You (que tu aies)",
                        "question": "que tu",
                        "answer": "aies",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "You (que vous ayez)",
                        "question": "que vous",
                        "answer": "ayez",
                        "audio": ""
                    }
                },
                "3rd Person": {
                    "Singular": {
                        "text": "He/She (qu'il/qu'elle ait)",
                        "question": "qu'il/qu'elle",
                        "answer": "ait",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "They (qu'ils/qu'elles aient)",
                        "question": "qu'ils/qu'elles",
                        "answer": "aient",
                        "audio": ""
                    }
                }
            }


    def test(self):
        lst = {}
        if self.selection == SUBJUNCTIVE_ETRE:
            lst = {
                "1s": ("sois", "que je ___ heureux.", "I am happy."),
                "2s": ("sois", "que tu ___ en bonne santé.", "You are healthy."),
                "3s": ("soit", "qu'il/qu'elle ___ à l'heure.", "He/She is on time."),
                "1p": ("soyons", "que nous ___ amis.", "We are friends."),
                "2p": ("soyez", "que vous ___ prêts.", "You all are ready."),
                "3p": ("soient", "qu'ils/qu'elles ___ contents.", "They are happy.")
            }
        elif self.selection == SUBJUNCTIVE_AVOIR:
            lst = {
                "1s": ("aie", "que j'___ de la chance.", "I am lucky."),
                "2s": ("aies", "que tu ___ du courage.", "You have courage."),
                "3s": ("ait", "qu'il/qu'elle ___ raison.", "He/She is right."),
                "1p": ("ayons", "que nous ___ de la patience.", "We have patience."),
                "2p": ("ayez", "que vous ___ de la force.", "You all have strength."),
                "3p": ("aient", "qu'ils/qu'elles ___ des idées.", "They have ideas.")
            }

        return lst