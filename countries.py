from typing import List, Tuple

country_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "usa",  # country name
        "north america",  # continent
        1776,  # year of founding
        50, # number of states
        9833517, # area measured in square kilometers
        [
            "coal",
            "copper",
            "lead",
            "iron",
            "natural gas",
            "timber",
            "bauxite",
            "uranium"
        ],  # natural resources
        339665118, # population as of 2023
        "english", # primary language
        "republic", # type of government
        "washington dc", # capital
        [
            "maize",
            "milk",
            "soybeans",
            "wheat",
            "sugar canes",
            "sugar beet",
            "poultry",
            "potatoes",
            "cotton",
            "pork"
        ],  # agricultural products
        [
            "trade",
            "agriculture",
            "consturction",
            "retail",
            "fincance",
            "management",
            "transport",
            "technology"
        ],  # industries
    ),
    (
        "guatemala",  # country name
        "central america",  # continent
        1821,  # year of founding
        22, # number of states
        108889, # area measured in square kilometers
        [
            "petroleum",
            "nickel",
            "rare woods",
            "fish",
            "chicle",
            "hydropower"
        ],  # natural resources
        17980803, # population as of 2023
        "spanish", # primary language
        "republic", # type of government
        "guatemala city", # capital
        [
            "sugar cane",
            "bananas",
            "oil palm fruit",
            "maize",
            "melons",
            "potatoes",
            "milk",
            "plantains",
            "pineapples",
            "rubber"
        ],  # agricultural products
        [
            "sugar",
            "textiles and clothing",
            "furniture",
            "chemicals",
            "petroleum",
            "metals",
            "rubber",
            "tourism"
        ],  # industries
    ),
    (
        "israel",  # country name
        "asia",  # continent
        1948,  # year of founding
        6, # number of states
        21937, # area measured in square kilometers
        [
            "timber",
            "potash",
            "copper ore",
            "natural gas",
            "phosphate rock",
            "magnesium bromide",
            "clays",
            "sand"
        ],  # natural resources
        9043387, # population as of 2023
        "hebrew", # primary language
        "democracy", # type of government
        "jerusalem", # capital
        [
            "milk",
            "potatoes",
            "poultry",
            "tomatoes",
            "carrots",
            "turnips",
            "oranges",
            "green peppers",
            "eggs",
            "vegetables"
        ],  # agricultural products
        [
            "chemicals",
            "plastics",
            "metals",
            "food products",
        ],  # industries
    ),
    (
        "ireland",  # country name
        "europe",  # continent
        1921,  # year of founding
        4, # number of states
        70273, # area measured in square kilometers
        [
            "natural gas",
            "peat",
            "copper",
            "lead",
            "zinc",
            "silver",
            "barite",
            "gypsum",
            "limestone",
            "dolomite"
        ],  # natural resources
        5323991, # population as of 2023
        "english", # primary language
        "republic", # type of government
        "dublin", # capital
        [
            "milk",
            "barley",
            "beef",
            "wheat",
            "potatoes",
            "pork",
            "oats",
            "poultry",
            "mushrooms",
            "mutton"
        ],  # agricultural products
        [
            "pharmaceuticals",
            "chemicals",
            "technology",
            "food products",
            "beverages",
            "medical devices"
        ],  # industries
    ),
    (
        "india",  # country name
        "asia",  # continent
        1947,  # year of founding
        28, # number of states
        3287263, # area measured in square kilometers
        [
            "coal",
            "antimony",
            "iron ore",
            "lead",
            "manganese",
            "mica",
            "bauxite",
            "rare earth elements",
            "titanium ore",
            "chromite",
            "natural gas",
            "diamonds",
            "petroleum",
            "limestone",
            "arable land"
        ],  # natural resources
        1399179585, # population as of 2023
        "hindi", # primary language
        "republic", # type of government
        "new delhi", # capital
        [
            "sugar canes",
            "rice",
            "wheat",
            "buffalo milk",
            "milk",
            "potatoes",
            "vegetables",
            "bananas",
            "maize",
            "mushrooms"
        ],  # agricultural products
        [
            "textiles",
            "chemicals",
            "food products",
            "steel",
            "transportation",
            "cement",
            "mining",
            "petroleum",
            "machinery",
            "software",
            "pharmaceuticals"
        ],  # industries
    ),
    (
        "fiji",  # country name
        "oceania",  # continent
        1970,  # year of founding
        14, # number of states
        18274, # area measured in square kilometers
        [
            "timber",
            "fish",
            "gold",
            "copper",
            "offshore oil potential",
            "hydropower"
        ],  # natural resources
        947760, # population as of 2023
        "itaukei", # primary language
        "republic", # type of government
        "suva", # capital
        [
            "sugar canes",
            "cassava",
            "taro",
            "poultry",
            "vegetables",
            "coconuts",
            "eggs",
            "milk",
            "ginger",
            "sweet potatoes"
        ],  # agricultural products
        [
            "tourism",
            "sugar",
            "clothing",
            "copra",
            "gold",
            "silver",
            "lumber"
        ],  # industries
    ),
    (
        "bahamas",  # country name
        "central america",  # continent
        1973,  # year of founding
        700, # number of states
        183880, # area measured in square kilometers
        [
            "salt",
            "aragonite",
            "timber",
            "arable land"
        ],  # natural resources
        358508, # population as of 2023
        "english", # primary language
        "demmocracy", # type of government
        "nassau", # capital
        [
            "sugar canes",
            "grapefruit",
            "vegetales",
            "bananas",
            "tomatoes",
            "poultry",
            "tropical fruit",
            "oranges",
            "coconuts",
            "mangoes"
        ],  # agricultural products
        [
            "tourism",
            "banking",
            "oil bunkering",
            "maritime",
            "transshipment",
            "salt",
            "aragonite",
            "pharmaceuticals"
        ],  # industries
    ),
]