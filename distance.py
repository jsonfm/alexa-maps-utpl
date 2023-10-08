from typing import List

import numpy as np
from hermetrics.levenshtein import Levenshtein
from unidecode import unidecode

from database import dbv2

lev = Levenshtein()


UTPL_CASES = [
    "u.t.p.l",
    "u. t. p. l.",
    "UTPL",
    "U. T. P. L.",
    "utpl",
    "o. t. p. l.",
    "t. p. l.",
    "p. l.",
]


def utpl_string_cases(word: str, cases: List = UTPL_CASES):
    """Checks 'utpl' word similarity with some variations. To be used with Alexa."""
    similities = [
        lev.normalized_distance(word.lower(), target.lower()) for target in cases
    ]
    mean = sum(similities) / len(similities)
    return mean <= 0.5


def utpl_string_cases_on_phrase(phrase: str = ""):
    """Checks if `utpl cases` are included in a phrase."""

    is_utpl_on_phrase = any(case in phrase for case in UTPL_CASES)

    # words = phrase.split(" ")
    # is_utpl = [utpl_string_cases(word) for word in words]
    # is_utpl = any(is_utpl)
    # is_utpl_on_phrase = is_utpl_on_phrase or is_utpl

    return is_utpl_on_phrase


def find_similar_question_on_list(text: str, questions: list[str]):
    clean = lambda text: unidecode(text.lower().rstrip())
    distances = [
        lev.normalized_distance(clean(text), clean(question)) for question in questions
    ]
    distances = np.array(distances)
    question_index = np.argmin(distances)
    question = questions[question_index]
    return question


def find_similar_question(text: str):
    question = find_similar_question_on_list(text, list(dbv2.questions.keys()))
    answer = dbv2.questions[question]
    return question, answer


if __name__ == "__main__":
    import time

    t0 = time.time()
    question, answer = find_similar_question("certificado inglés")
    t1 = time.time()
    print("--> question: ", question)
    print("--> answer: ", answer)
    print("dt: ", t1 - t0)
