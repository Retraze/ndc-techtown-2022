import random

NAMES = [
    "Erengisle Nilsson",
    "Henrik Jansøn",
    "Folmer Jakobsen",
    "Algot Magnusson",
    "Predbjørn Podebusk",
    "Filippus Karlsson",
    "Hannes Podebusk",
    "Nils Erengislesson",
    "Berneke Skinkel",
    "Eindride Erlendsson",
    "Gyrd Gyrdsson",
    "Ogmund Bolt",
    "Gotskalk Bengtsson",
    "Svarte Skåning",
    "Loft Guttormsson",
    "Hall Olavsson",
    "Hoskuld Runolvsson",
    "Sæmund Oddsson",
    "Bodvar Ravnsson",
    "Berdor Mort",
    "Arne Stolpe",
    "Tore Korlægemathr",
    "Berdor Brak",
    "Bergtor Bannamule",
    "Botolv Byks",
    "Berulv Bondason",
    "Knut Ståggå",
    "Jon Elg",
    "Pål Bjert",
    "Gudulv Valtjovsson",
    "Grjotgard Ånundsson",
    "Balduzius Vinland",
    "Baldvinus Britonis",
    "Galfrid FitzPeter",
    "Geirlaug Torleivsson",
    "Gjavleik Torkjellsson",
    "Kjetil Vigleikssons",
    "Torivil Ormsson",
    "Tolv Valtjovsson",
    "Orm Leidulvsson",
    "Torleiv Torivil",
    "Torgunna Eivindsdotter",
    "Aslaug Torleivsdotter",
    "Vetrlid Helgesson",
    "Rolleiv Gunnulvsson",
    "Tore Torleiv",
    "Bjorn Sveinungsson",
    "Tolv Valtjovsson",
    "Torleiv Ånundsson",
    "Ragnhild Simonsdotter",
    "Papa Stour",
    "Sidan Torvald",
    "Eirik Unge",
    "Gregorius Benediktsson",
    "Ivar Sperra",
    "Magnus Hognesson",
    "Erlend Geirmundsson",
    "Erlend Alfeity",
]

PLACES = [
    "Oslo",
    "Trondheim",
    "Røros",
    "Stavanger",
    "Bergen",
    "Bodø",
    "Kongsberg",
]

BLOOD_GROUPS = [
    "A",
    "B",
    "AB",
    "O",
]

def generate_people(number, add_header=False):
    if add_header:
        yield "Given name", "Family name", "Age", "Gender", "Current location", "Home town", "Blod type"
    for _ in range(number):
        age = random.randrange(16, 87)
        gender = random.choice(["male", "female"])
        if random.random() < 0.015:
            gender = "other"

        home_town        = random.choice(PLACES + [None])
        current_location = random.choice(PLACES)

        blood_group  = random.choice(BLOOD_GROUPS)
        blood_rhesus = random.choice(["-", "+"])

        given_name, _  = random.choice(NAMES).split(" ")
        _, family_name = random.choice(NAMES).split(" ")

        yield given_name, family_name, age, gender, current_location, home_town, f"{blood_group}{blood_rhesus}"


USERS = [
    {
        "username": "hunterx",
        "realname": "Andrew",
        "age": 13,
    },
    {
        "username": "alice32",
        "realname": "Alice",
        "is_admin": True,
    },
    {
        "username": "natural20",
        "role": 'game_master',
    },
]
