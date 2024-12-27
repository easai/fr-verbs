from const import SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR, CONDITIONAL_ETRE, CONDITIONAL_AVOIR


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

        if selection == CONDITIONAL_ETRE:
            self.verbs = {
                "1st Person": {
                    "Singular": {
                        "text": "I (je serais)",
                        "question": "je",
                        "answer": "serais",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (nous serions)",
                        "question": "nous",
                        "answer": "serions",
                        "audio": ""
                    }
                },
                "2nd Person": {
                    "Singular": {
                        "text": "You (tu serais)",
                        "question": "tu",
                        "answer": "serais",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "You (vous seriez)",
                        "question": "vous",
                        "answer": "seriez",
                        "audio": ""
                    }
                },
                "3rd Person": {
                    "Singular": {
                        "text": "He/She (il/elle serait)",
                        "question": "il/elle",
                        "answer": "serait",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "They (ils/elles seraient)",
                        "question": "ils/elles",
                        "answer": "seraient",
                        "audio": ""
                    }
                }
            }
        
        if selection == CONDITIONAL_AVOIR:
            self.verbs = {
                "1st Person": {
                    "Singular": {
                        "text": "I (j'aurais)",
                        "question": "je",
                        "answer": "aurais",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (nous aurions)",
                        "question": "nous",
                        "answer": "aurions",
                        "audio": ""
                    }
                },
                "2nd Person": {
                    "Singular": {
                        "text": "You (tu aurais)",
                        "question": "tu",
                        "answer": "aurais",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "You (vous auriez)",
                        "question": "vous",
                        "answer": "auriez",
                        "audio": ""
                    }
                },
                "3rd Person": {
                    "Singular": {
                        "text": "He/She (il/elle aurait)",
                        "question": "il/elle",
                        "answer": "aurait",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "They (ils/elles auraient)",
                        "question": "ils/elles",
                        "answer": "auraient",
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
        elif self.selection == CONDITIONAL_ETRE:
            lst = {
                "1s": ("serais", "je ___ heureux.", "I would be happy."),
                "2s": ("serais", "tu ___ en bonne santé.", "You would be healthy."),
                "3s": ("serait", "il/elle ___ à l'heure.", "He/She would be on time."),
                "1p": ("serions", "nous ___ amis.", "We would be friends."),
                "2p": ("seriez", "vous ___ prêts.", "You all would be ready."),
                "3p": ("seraient", "ils/elles ___ contents.", "They would be happy.")
            }
        if self.selection == CONDITIONAL_AVOIR:
            lst = {
                "1s": ("aurais", "je ___ un livre.", "I would have a book."),
                "2s": ("aurais", "tu ___ une voiture.", "You would have a car."),
                "3s": ("aurait", "il/elle ___ un chien.", "He/She would have a dog."),
                "1p": ("aurions", "nous ___ des amis.", "We would have friends."),
                "2p": ("auriez", "vous ___ des devoirs.", "You all would have homework."),
                "3p": ("auraient", "ils/elles ___ des idées.", "They would have ideas.")
            }


        return lst
