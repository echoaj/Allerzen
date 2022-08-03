from django.shortcuts import render
from survey.services.algorithm import *
import json

with open('survey/allergies.json', 'r') as json_file:
    allergies = json.load(json_file)['allergies']

allergy_types = list(allergies.keys())

symptoms = []
for key in allergies:
    symptoms += allergies[key]['symptoms']
symptoms = set(symptoms)

all_symptoms = []
for symp in symptoms:
    item = symp.replace(" ", "_").replace("/", "_")
    all_symptoms.append(item)


allergy_symptoms = []
temp = []

for i in range(len(all_symptoms)):
    temp.append(all_symptoms[i])
    if i % 3 == 2:
        allergy_symptoms.append(temp)
        temp = []
# loop through all_symptoms list and
# append an empty list containing 3 items in it


seasons = [["January", "February", "March", "April"], ["May",
           "June", "July", "August"], ["September", "October",
           "November", "December"]]

medical_conditions = [["Asthma", "Eczema", "Hay Fever"], ["Lactose Intolerance",
                     "Celiac Disease", "Oral Allergy Syndrome"]]


# Create your views here.
def home_view(request):
    data = {
        "symptoms_matrix": allergy_symptoms,
        "seasons": seasons,
        "medical_conditions": medical_conditions,
        "allergies": allergy_types
    }

    if request.method == "GET":
        return render(request, 'home.html', data)
    elif request.method == "POST":
        result = algo.calculate(request.POST)
        data['result'] = result
        return render(request, 'home.html', data)
