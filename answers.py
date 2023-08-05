from database import Database


db = Database()
db.load("./dbutplcampus.csv")


def stringify(string_list, sep: str = ", "):
    """A cool wrapper for join function."""
    return sep.join(string_list)


def get_cities_answer():
    """Returns an answer with the cities where UTPL operates."""
    cities = db.get_all_cities()
    cities_string = stringify(cities)
    answer = "UTPL opera en ciudades como "
    answer += cities_string + ", entre otras."
    return answer


def get_countries_answer():
    """Returns an answer with the countries where UTPL operates."""
    countries = db.get_all_countries()
    countries_string = stringify(countries)
    answer = "Podrás encontrar a UTPL en los siguientes países: "
    answer += countries_string + ", entre otros."
    return answer


def get_careers_answer():
    """Returns the available careers at UTPL."""
    careers = db.get_careers()
    careers_string = stringify(careers)
    answer = "En UTPL podrás estudiar: "
    answer += careers_string + ", entre otras. Visita nuestra web para conocer más detalles."
    return answer


def get_institutions_answer(randomized: bool = True, limit: int = 5):
    institutions = db.get_institutions(randomized=randomized, limit=limit)
    institutions_string = stringify(institutions)
    answer = "Algunos de nuestros socios estratégicos son: "
    answer += institutions_string
    return answer


def get_convenios_answer():
    convenios = db.get_convenios()
    convenios_string = stringify(convenios)
    answer = "Los tipos de convenios que hemos establecido son: "
    answer += convenios_string
    return answer


def get_objetivos_answer(randomized: bool = True, limit: int = 2):
    objetivos = db.get_objetivos(randomized=randomized, limit=limit)
    objetivos_string = stringify(objetivos, sep=" y ")
    answer = ""
    answer += objetivos_string
    return answer


if __name__ == "__main__":
    # answer = get_cities_answer()
    # answer = get_countries_answer()
    # answer = get_careers_answer()
    # answer = get_institutions(randomized=True, limit=5)
    # answer = get_convenios_answer()
    # answer = get_objetivos_answer(randomized=True, limit=2)
    # print("answer: ", answer)
    ...
