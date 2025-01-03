from const import SUBJUNCTIVE_ETRE, SUBJUNCTIVE_AVOIR, CONDITIONAL_ETRE, CONDITIONAL_AVOIR, PRETERIT_ETRE, PRETERIT_AVOIR, IMPERFECT_ETRE


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

        if selection == PRETERIT_ETRE:
            self.verbs = {
                "1st Person": {
                    "Singular": {
                        "text": "I (je fus)",
                        "question": "je",
                        "answer": "fus",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (nous fûmes)",
                        "question": "nous",
                        "answer": "fûmes",
                        "audio": ""
                    }
                },
                "2nd Person": {
                    "Singular": {
                        "text": "You (tu fus)",
                        "question": "tu",
                        "answer": "fus",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "You (vous fûtes)",
                        "question": "vous",
                        "answer": "fûtes",
                        "audio": ""
                    }
                },
                "3rd Person": {
                    "Singular": {
                        "text": "He/She (il/elle fut)",
                        "question": "il/elle",
                        "answer": "fut",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "They (ils/elles furent)",
                        "question": "ils/elles",
                        "answer": "furent",
                        "audio": ""
                    }
                }
            }
        if selection == PRETERIT_AVOIR:
            self.verbs = {
                "1st Person": {
                    "Singular": {
                        "text": "I (j'eus)",
                        "question": "je",
                        "answer": "eus",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (nous eûmes)",
                        "question": "nous",
                        "answer": "eûmes",
                        "audio": ""
                    }
                },
                "2nd Person": {
                    "Singular": {
                        "text": "You (tu eus)",
                        "question": "tu",
                        "answer": "eus",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "You (vous eûtes)",
                        "question": "vous",
                        "answer": "eûtes",
                        "audio": ""
                    }
                },
                "3rd Person": {
                    "Singular": {
                        "text": "He/She (il/elle eut)",
                        "question": "il/elle",
                        "answer": "eut",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "They (ils/elles eurent)",
                        "question": "ils/elles",
                        "answer": "eurent",
                        "audio": ""
                    }
                }
            }
        if selection == IMPERFECT_ETRE:
            self.verbs = {
                "1st Person": {
                    "Singular": {
                        "text": "I (j'étais)",
                        "question": "je",
                        "answer": "étais",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "We (nous étions)",
                        "question": "nous",
                        "answer": "étions",
                        "audio": ""
                    }
                },
                "2nd Person": {
                    "Singular": {
                        "text": "You (tu étais)",
                        "question": "tu",
                        "answer": "étais",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "You (vous étiez)",
                        "question": "vous",
                        "answer": "étiez",
                        "audio": ""
                    }
                },
                "3rd Person": {
                    "Singular": {
                        "text": "He/She (il/elle était)",
                        "question": "il/elle",
                        "answer": "était",
                        "audio": ""
                    },
                    "Plural": {
                        "text": "They (ils/elles étaient)",
                        "question": "ils/elles",
                        "answer": "étaient",
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
        if self.selection == PRETERIT_ETRE:
            lst = {
                "1s": ("fus", "je ___ à Paris.", "I was in Paris."),
                "2s": ("fus", "tu ___ en vacances.", "You were on vacation."),
                "3s": ("fut", "il/elle ___ étudiant.", "He/She was a student."),
                "1p": ("fûmes", "nous ___ au concert.", "We were at the concert."),
                "2p": ("fûtes", "vous ___ en retard.", "You all were late."),
                "3p": ("furent", "ils/elles ___ heureux.", "They were happy.")
            }
        if self.selection == PRETERIT_AVOIR:
            lst = {
                "1s": ("eus", "j'___ un livre.", "I had a book."),
                "2s": ("eus", "tu ___ une idée.", "You had an idea."),
                "3s": ("eut", "il/elle ___ un chien.", "He/She had a dog."),
                "1p": ("eûmes", "nous ___ une réunion.", "We had a meeting."),
                "2p": ("eûtes", "vous ___ une chance.", "You all had a chance."),
                "3p": ("eurent", "ils/elles ___ des amis.", "They had friends.")
            }
        if self.selection == IMPERFECT_ETRE:
            lst = {
                "1s": ("étais", "j'___ content.", "I was happy."),
                "2s": ("étais", "tu ___ fatigué.", "You were tired."),
                "3s": ("était", "il/elle ___ à l'école.", "He/She was at school."),
                "1p": ("étions", "nous ___ en vacances.", "We were on vacation."),
                "2p": ("étiez", "vous ___ en retard.", "You all were late."),
                "3p": ("étaient", "ils/elles ___ amis.", "They were friends.")
            }


        return lst
