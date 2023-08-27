from typing import List
import pandas as pd
import random


def exclude_strings_on_list(input: List = [], exclude: List = []):
    """Exclude a list."""
    results = []
    for item in input:
        is_included = [string.lower() in item.lower() for string in exclude]
        is_included = any(is_included)
        if not is_included:
            results.append(item)
    return results


class Database:
    """Pandas Database."""

    def __init__(self):
        self.df: pd.DataFrame = None

    def load(self, file: str):
        """loads an excel file"""
        if ".xlsx" in file:
            self.df = pd.read_excel(file)
        if ".csv" in file:
            self.df = pd.read_csv(file, encoding="utf-8")

    def save_as_csv(self, path: str):
        """Saves a `csv`."""
        if self.df is not None:
            self.df.to_csv(path)

    def get_all_countries(self):
        """Returns all the countries."""
        if self.df is None:
            return []
        countries = self.df['Paìs'].str.strip().dropna().unique()
        return list(countries)

    def get_all_cities(self, randomized: bool = True, limit: int = 5):
        """Returns all the cities in the Excel."""
        if self.df is None:
            return []
        cities = self.df['Ciudad'].str.strip().dropna().unique()
        if randomized:
            cities = random.choices(cities, k=limit)
        return list(cities)

    def get_all_continents(self):
        """Returns all the continents."""
        if self.df is None:
            return []
        continents = self.df['Continente'].dropna().unique()
        return list(continents)

    def get_careers(self, randomized: bool = True, limit: int = 8):
        """Returns all careers."""
        if self.df is None:
            return []
        careers = self.df['Carreras beneficiadas'].str.strip(
        ).dropna().unique()

        careers = exclude_strings_on_list(
            input=careers, exclude=["Vicerrectorado", "Área", "Todas"])
        if randomized:
            careers = random.choices(careers, k=limit)
        return careers

    def get_convenios(self):
        """Returns a list of convenios"""
        if self.df is None:
            return []
        convenios = self.df['Tipo de convenio'].dropna().unique()
        return convenios

    def get_institutions(self, randomized: bool = True, limit: int = 5):
        """Returns a list of institutions."""
        if self.df is None:
            return []
        institutions = self.df['Institución contraparte'].dropna().unique()
        if randomized:
            institutions = random.choices(institutions, k=limit)
        return institutions

    def get_objetivos(self, randomized: bool = True, limit: int = 2):
        """Returns a list of objetivos."""
        if self.df is None:
            return []
        objetivos = self.df["Objeto del convenio"].dropna().unique()
        if randomized:
            objetivos = random.choices(objetivos, k=limit)
        return objetivos

    def single_query(self, comparation_key: str, comparation_value: str, retrieve_key: str):
        try:
            data = self.df.query(f"{comparation_key} == '{comparation_value}'")[retrieve_key].dropna().unique()
            return list(data)
        except:
            return []

    def get_country_related_info(self, country: str):
        if self.df is None:
            return {}
        institutions = self.single_query("Paìs", country, "Institución contraparte")
        convenios = self.single_query("Paìs", country, "Objeto del convenio")
        careers = self.single_query("Paìs", country, "Carreras beneficiadas")
        data = {
            "institutions": institutions,
            "covenios": convenios,
            "careers": careers
        }    
        return data


db = Database()


if __name__ == '__main__':
    db.load("dbutplcampus.csv")

    # print("Ciudades: ", db.get_all_cities())
    # print("Paises: ", db.get_all_countries())
    # print("Continentes: ", db.get_all_continents())
    # print("Institutions: ", db.get_institutions(randomized=True))
    # print("careers: ", db.get_careers())
    # print("convenios: ", db.get_convenios())
    # print("objetivos: ", db.get_objetivos())
    info = db.get_country_related_info("Perú")
    print("info: ", info)