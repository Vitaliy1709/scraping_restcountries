import requests
from prettytable import PrettyTable

BASE_URL = "https://restcountries.com/v3.1/all?fields=name,capital,flags"


def fetch_countries_data():
    """
    Fetches the data for all countries from the REST API.

    Returns:
        list: A list of country data dictionaries, or an empty list if an error occurs.
    """
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return []


def sort_countries_data(countries_data):
    """
    Sorts the countries data alphabetically by the official name.

    Args:
        countries_data (list): A list of country data dictionaries.

    Returns:
        list: A sorted list of country data dictionaries.
    """
    return sorted(countries_data, key=lambda x: x.get("name", {}).get("official", ""))


def create_countries_table(sorted_countries_data):
    """
    Creates a pretty table displaying country name, capital, and flag URL.

    Args:
        sorted_countries_data (list): A sorted list of country data dictionaries.

    Returns:
        PrettyTable: A formatted table of country information.
    """
    table = PrettyTable()
    table.field_names = ["Назва країни", "Назва столиці", "Посилання на зображення прапору (png)"]

    for country in sorted_countries_data:
        country_name = country.get("name", {}).get("official", "N/A")
        capital_name = country.get("capital", ["N/A"])
        capital = capital_name[0] if capital_name else "N/A"
        flag_url = country.get("flags", {}).get("png", "N/A")
        table.add_row([country_name, capital, flag_url])

    return table


def display_countries_info():
    """
    Main function to fetch, sort, and display country information.
    """
    countries_data = fetch_countries_data()
    if not countries_data:
        print("No data to display.")
        return

    sorted_countries_data = sort_countries_data(countries_data)
    table = create_countries_table(sorted_countries_data)
    print(table)


if __name__ == "__main__":
    display_countries_info()
