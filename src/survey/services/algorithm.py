from survey.templatetags.survey_tags import remove_underscores
import json

with open('survey/allergies.json', 'r') as json_file:
    json_data = json.load(json_file)['allergies']


allergies = None


def clear_allergies():
    global allergies
    allergies = {"pollen": 0, "mold": 0, "dust": 0, "latex": 0, "insects": 0, "pets": 0, "medication": 0, "food": 0}


# class Survey:
#     def __init__(self):
#         self.syptoms = ["runny nose", "itching"]
#         self.seasons = ["April", "May", "June"]

class BaseCalc:
    @staticmethod
    def rank_by_indicator(survey, indicator, points):
        attr_list = survey.getlist(indicator)
        print(attr_list)
        for key in allergies:
            for symptom in attr_list:
                symptom = remove_underscores(symptom)
                if symptom in json_data[key][indicator]:
                    allergies[key] += points


class Symptoms(BaseCalc):
    next_chain = None

    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, survey):
        print("Survey: ", survey)
        print("Calculating Symptoms")
        self.rank_by_indicator(survey, "symptoms", 10)
        print("Allergies: ", allergies)
        return self.next_chain.calculate(survey)


class Seasons(BaseCalc):
    next_chain = None

    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, survey):
        print("Calculating seasons")
        self.rank_by_indicator(survey, "seasons", 10)
        print("Allergies: ", allergies)
        return self.next_chain.calculate()


class Result:
    def calculate(self):
        # convert allergies dict to list and sort it by value
        sorted_allergies = sorted(allergies.items(), key=lambda kv: kv[1], reverse=True)
        print("Sorted allergies: ", sorted_allergies)
        top_rank = sorted_allergies[0][1]
        top_allergies = [allergy[0] for allergy in sorted_allergies if allergy[1] == top_rank]
        return f"You are allergic to {', '.join(top_allergies)}"


# survey = Survey()
algo = Symptoms()
seas = Seasons()
res = Result()

# chains
algo.set_next_chain(seas)
seas.set_next_chain(res)

# symp.calculate()