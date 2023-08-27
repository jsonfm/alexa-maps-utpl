from typing import List
from hermetrics.levenshtein import Levenshtein


lev = Levenshtein()


UTPL_CASES = ["u.t.p.l", "u. t. p. l.", "UTPL",
              "U. T. P. L.", "utpl", "o. t. p. l.", "t. p. l.", "p. l."]


def utpl_string_cases(word: str, cases: List = UTPL_CASES):
    """Checks 'utpl' word similarity with some variations. To be used with Alexa."""
    similities = [lev.normalized_distance(
        word.lower(), target.lower()) for target in cases]
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


if __name__ == '__main__':
    is_utpl_included = utpl_string_cases_on_phrase(
        "qué carreras tiene o. t. p. l.")
    print(is_utpl_included)
