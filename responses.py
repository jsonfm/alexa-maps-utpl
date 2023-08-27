import logging

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

from arduino import arduinoService


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def smart_response(slots):
    response = "No estoy preparada para responder a esa pregunta."
    what_question = slots["whatQuestion"].value or ""
    how_question = slots["howQuestion"].value or ""
    lights_word = slots["lights"].value or ""

    try:
        is_utpl = utpl_string_cases_on_phrase(what_question) or utpl_string_cases_on_phrase(
            how_question)  # "utpl" word was detected!
        is_cities = "ciudades" in what_question or "ciudades" in how_question
        is_convenios = "convenios" in what_question or "convenios" in how_question
        is_countries = "países" in what_question or "países" in how_question
        is_careers = "carreras" in what_question or "carreras" in how_question
        is_objetivos = "objetivos" in what_question or "objetivos" in how_question

        is_light = "enciende" in lights_word
        is_dark = "apaga" in lights_word

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

            if is_light:
                arduinoService.turn_on_all()
                response = "¡Luces encendidas!"

            if is_dark:
                arduinoService.turn_off_all()
                response = "¡Luces apagadas!"

    except Exception as e:
        logger.warn(f"error {str(e)}")
    return response
