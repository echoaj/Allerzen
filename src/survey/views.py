from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


allergies = {"pollen": ["sneezing", "nasal congestion", "sinus pressure", "runny nose", "itchy and/or watery eyes",
                        "sore throat", "coughing", "swollen eyes", "loss of taste and/or smell"],
             "mold": ["sneezing", "coughing", "nasal congestion", "itchy and/or watery eyes", "postnasal drip",
                      "chest tightness", "symptoms of asthma and/or hay fever"],
             "dust": ["sneezing", "runny nose", "nasal congestion", "sinus pressure", "itchy and/or watery eyes",
                      "itchy nose and/or throat", "postnasal drip", "coughing", "shortness of breath",
                      "symptoms of asthma and/or hay fever"],
             "latex": ["chest tightness", "skin rashes", "runny nose", "throat and/or mouth swelling",
                       "itchy and/or watery eyes", "sneezing", "shortness of breath"],
             "insects": ["pain", "redness", "swelling", "flushing", "skin rashes", "itching", "anaphylaxis",
                         "throat and/or mouth swelling", "fainting", "blurry vision", "temporary hearing loss"],
             "pets": ["sneezing", "runny nose", "sinus pressure", "itchy and/or watery eyes", "skin rashes",
                      "chest tightness", "shortness of breath", "nose and/or throat swelling", "anaphylaxis"],
             "medication": ["wheezing", "shortness of breath", "throat and/or mouth swelling",
                            "nausea", "diarrhea", "fainting", "anaphylaxis"],
             "food": ["skin rashes", "runny nose", "nausea", "diarrhea", "itchy mouth and/or lips",
                      "throat and/or mouth swelling", "breathing difficulties", "itchy and/or watery eyes",
                      "lightheadedness", "anaphylaxis"]}

allergy_types = list(allergies.keys())

symptoms = []
for key in allergies:
    symptoms += allergies[key]
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
print(allergy_symptoms)

seasons = [["January", "February", "March", "April"], ["May",
           "June", "July", "August"], ["September", "October",
           "November", "December"]]

medical_conditions = [["Asthma", "Eczema", "Hay Fever", "Lactose Intolerance"],
                      ["Celiac Disease", "Oral Allergy Syndrome", "Atopic Dermatitis"]]


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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        print(request.POST)
        print(first_name, last_name, age)
        print(request.POST.getlist('symptoms'))
        print(request.POST.getlist('seasons'))
        print(request.POST.getlist('medical_conditions'))
        return render(request, 'home.html', data)
