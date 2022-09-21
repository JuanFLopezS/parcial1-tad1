class Solution :
    def __init__(self):
        self.dictionary = {}

        dictionary = {
            serie: "",
            number_seasons: 0,
            original_lenguage: "",
            features_seasons: [{
                season_number: 0,
                season_name: "",
                premier_date: "",
                cast: [Actor1, Actor2],
                episodes: [{
                    episode_name: "",
                    time_duration: 0
                }]
            }]
        }

def actor_search():
    actor_name = input("Name of the actor: ")
    for serie in self.dictionary:
        for season in serie["features_seasons"]:
            for actor in season["cast"]:
                if actor == actor_name:
                    print(serie["serie"])

def language_search():
    language = input("Language: ")
    for serie in self.dictionary:
        if serie["original_lenguage"] == language:
            print(serie["serie"])

def premier_date_search():
    premier_date = input("Premier Date: ")
    for serie in self.dictionary:
        for season in serie["features_seasons"]:
            if season["premier_date"] == premier_date:
                del serie
