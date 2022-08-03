import json

with open('survey/allergies.json', 'r') as json_file:
    json_data = json.load(json_file)['allergies']

allergies = {"pollen": 0, "mold": 0, "dust": 0, "latex": 0, "insects": 0, "pets": 0, "medication": 0, "food": 0}


# class Survey:
#     def __init__(self):
#         self.syptoms = ["runny nose", "itching"]
#         self.seasons = ["April", "May", "June"]


class Symptoms:
    next_chain = None

    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, survey):
        print("Survey: ", survey)
        print("Calculating Symptoms")
        user_symptoms = survey.getlist("symptoms")
        print("User Symptoms: ", user_symptoms)
        return self.next_chain.calculate(survey)


class Seasons:
    next_chain = None

    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, survey):
        print("Calculating seasons")
        return self.next_chain.calculate(survey)


class Result:
    def calculate(self, survey):
        return "You are allergic to pollen"


# survey = Survey()
algo = Symptoms()
seas = Seasons()
result = Result()

# chains
algo.set_next_chain(seas)
seas.set_next_chain(result)

# symp.calculate()