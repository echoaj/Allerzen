# impot default dictionary


allergies = {"pollen": 0, "mold": 0, "dust": 0, "latex": 0, "insects": 0, "pets": 0, "medication": 0, "food": 0}


class Survey:
    def __init__(self):
        self.syptoms = ["runny nose", "itching"]
        self.seasons = ["April", "May", "June"]


class Symptoms:
    next_chain = None

    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, survey):
        print("Calculating Symptoms")
        self.next_chain.calculate(survey)


class Seasons:
    next_chain = None

    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, survey):
        print("Calculating seasons")
        # self.next_chain.calculate()


survey = Survey()

symp = Symptoms()
seas = Seasons()
# chains
symp.set_next_chain(seas)

symp.calculate(survey)