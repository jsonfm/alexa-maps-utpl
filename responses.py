from questions import fix_slot
from chatgpt import ask_to_chatgpt_v2
from distance import utpl_string_cases_on_phrase

from answers import (
    get_cities_answer,
    get_convenios_answer,
    get_countries_answer,
    get_careers_answer,
    get_objetivos_answer
)


def ps(string):
    """String parsers"""
    string.lower()


def smart_response(slots):
    response = "No estoy preparada para responder a esa pregunta."
    what_question = slots["whatQuestion"].value or ""
    how_question = slots["howQuestion"].value or ""

    try:
        is_utpl = utpl_string_cases_on_phrase(what_question) or utpl_string_cases_on_phrase(
            how_question)  # "utpl" word was detected!
        is_cities = "ciudades" in what_question or "ciudades" in how_question
        is_convenios = "convenios" in what_question or "convenios" in how_question
        is_countries = "países" in what_question or "países" in how_question
        is_careers = "carreras" in what_question or "carreras" in how_question
        is_objetivos = "objetivos" in what_question or "objetivos" in how_question

        if is_utpl:
            if is_cities:
                response = get_cities_answer()

            if is_convenios:
                response = get_convenios_answer()

            if is_countries:
                response = get_countries_answer()

            if is_careers:
                response = get_careers_answer()

            if is_objetivos:
                response = get_objetivos_answer()

        else:
            if what_question is not None:
                response = fix_slot(what_question, "qué")
                response = ask_to_chatgpt_v2(response, max_tokens=100)

            if how_question is not None:
                response = fix_slot(how_question, "cómo")
                response = ask_to_chatgpt_v2(response, max_tokens=100)
    except Exception as e:
        pass
    return response
