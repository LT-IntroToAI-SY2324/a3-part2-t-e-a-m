from countries import country_db
from match import match
from typing import List, Tuple, Callable, Any

def get_name(country: Tuple[str, str, int, List[str]]) -> str:
    return country[0]

def get_continent(country: Tuple[str, str, int, List[str]]) -> str:
    return country[1]

# yof = year of founding
def get_yof(country: Tuple[str, str, int, List[str]]) -> int:
    return country[2]

def get_numofstates(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[3]

def get_area(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[4]

def get_naturalresources(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[5]

def get_population(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[6]

def get_language(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[7]

def get_governmenttype(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[8]

def get_capital(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[9]

def get_agriproducts(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[10]

def get_industries(country: Tuple[str, str, int, List[str]]) -> List[str]:
    return country[11]

def name_by_yof(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if int(matches[0]) == get_yof(country):
         results.append(get_name(country))
    return results


def name_by_yof_range(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if int(matches[0]) <= get_yof(country) <= int(matches[1]):
         results.append(get_name(country))
    return results


def name_before_yof(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if int(matches[0]) > get_yof(country):
         results.append(get_name(country))
    return results


def name_after_yof(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if int(matches[0]) < get_yof(country):
         results.append(get_name(country))
    return results


def continent_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_continent(country))
    return results


def yof_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_yof(country))
    return results


def numofstates_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results = (get_numofstates(country))
    results = (f"{results} states")
    return results


def area_by_name(matches: List[str]) -> List[int]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_area(country))
    results = (f"{results} sq km")
    return results

def naturalresources_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_naturalresources(country))
    return results

def population_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_population(country))
    return results

def language_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_language(country))
    return results

def govtype_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_governmenttype(country))
    return results

def capital_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_capital(country))
    return results

def agriproducts_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_agriproducts(country))
    return results

def industries_by_name(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_name(country):
         results.append(get_industries(country))
    return results

def name_by_continent(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_continent(country):
         results.append(get_name(country))
    return results

def naturalresources_by_continent(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_continent(country):
         results.append(get_naturalresources(country))
    return results

def language_by_continent(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_continent(country):
         results.append(get_language(country))
    return results

def name_by_numofstates_range(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if int(matches[0]) <= get_numofstates(country) <= int(matches[1]):
         results.append(get_name(country))
    return results

def name_by_area_range(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if int(matches[0]) <= get_area(country) <= int(matches[1]):
         results.append(get_name(country))
    return results

def name_by_naturalresource(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] in get_naturalresources(country):
         results.append(get_name(country))
    return results

def continent_by_naturalresource(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] in get_naturalresources(country):
         results.append(get_continent(country))
    return results

def name_by_language(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_language(country):
         results.append(get_name(country))
    return results

def continent_by_language(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_language(country):
         results.append(get_continent(country))
    return results

def name_by_govtype(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_governmenttype(country):
         results.append(get_name(country))
    return results

def name_by_capital(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] == get_capital(country):
         results.append(get_name(country))
    return results

def name_by_agriproducts(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] in get_agriproducts(country):
         results.append(get_name(country))
    return results

def continent_by_agriproducts(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] in get_agriproducts(country):
         results.append(get_continent(country))
    return results

def name_by_industry(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] in get_industries(country):
         results.append(get_name(country))
    return results

def continent_by_industry(matches: List[str]) -> List[str]:
    results = []
    for country in country_db:
        if matches[0] in get_industries(country):
         results.append(get_continent(country))
    return results


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what countries were founded in _"), name_by_yof),
    (str.split("what countries gained independence in _"), name_by_yof),
    (str.split("what countries were founded between _ and _"), name_by_yof_range),
    (str.split("what countries gained independence between _ and _"), name_by_yof_range),
    (str.split("what countries were founded before _"), name_before_yof),
    (str.split("what countries gained independence before _"), name_before_yof),
    (str.split("what countries were founded after _"), name_after_yof),
    (str.split("what countries gained independence after _"), name_after_yof),
    (str.split("what continent is % located"), continent_by_name),
    (str.split("when was % founded"), yof_by_name),
    (str.split("when did % gain independence"), yof_by_name),
    (str.split("how many states does % have"), numofstates_by_name),
    (str.split("what is the area of % in square kilometers"), area_by_name),
    (str.split("what is the area of %"), area_by_name),
    (str.split("what are the natural resources of the country of %"), naturalresources_by_name),
    (str.split("what is the population of %"), population_by_name),
    (str.split("what is the language of %"), language_by_name),
    (str.split("what do people speak in %"), language_by_name),
    (str.split("what kind of government is %"), govtype_by_name),
    (str.split("what is the capital of %"), capital_by_name),
    (str.split("what does % produce"), agriproducts_by_name),
    (str.split("what industries are in %"), industries_by_name),
    (str.split("what are the industries of %"), industries_by_name),
    (str.split("what countries are located in %"), name_by_continent),
    (str.split("what are the natural resources in the entire continent of %"), naturalresources_by_continent),
    (str.split("what languages do people speak in %"), language_by_continent),
    (str.split("what countries have between _ and _ states"), name_by_numofstates_range),
    (str.split("what countries have an area between _ and _ square kilometers"), name_by_area_range),
    (str.split("what countries have %"), name_by_naturalresource),
    (str.split("what continents have %"), continent_by_naturalresource),
    (str.split("what countries speak _"), name_by_language),
    (str.split("what continents speak _"), continent_by_language),
    (str.split("what countries are a _"), name_by_govtype),
    (str.split("what is % the capital of"), name_by_capital),
    (str.split("what countries are % produced"), name_by_agriproducts),
    (str.split("what continents are % produced"), continent_by_agriproducts),
    (str.split("what countries are part of the % industry"), name_by_industry),
    (str.split("what continents are part of the % industry"), continent_by_industry),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
       mat = match(pat, src)
       if mat is not None:
          answer = act(mat)
          return answer if answer else ["No answers"]
    return ["I don't understand"]
       


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the country database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()

