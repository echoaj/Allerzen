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
             "pets": ["sneezing", "runny nose", "sinus pressure", "itchy and/or watery eyes", "skin rashes"
                      "chest tightness", "shortness of breath", "nose and/or throat swelling", "anaphylaxis"],
             "medication": ["wheezing", "shortness of breath", "throat and/or mouth swelling",
                            "nausea", "diarrhea", "fainting", "anaphylaxis"],
             "food": ["skin rashes", "runny nose", "nausea", "diarrhea", "itchy mouth and/or lips",
                      "throat and/or mouth swelling", "breathing difficulties", "itchy and/or watery eyes",
                      "lightheadedness", "anaphylaxis"]}


symptoms = []
for key in allergies:
    symptoms += allergies[key]
symptoms = set(symptoms)

all_symptoms = []
for symp in symptoms:
    item = symp.replace(" ", "_").replace("/", "_")
    all_symptoms.append(item)

print(all_symptoms)


# Create your views here.
def home_view(request):
    print("User on website")
    if request.method == "GET":
        return render(request, 'home.html', {"symptoms_list": all_symptoms})
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        print(request.POST)
        print(first_name, last_name)
        print(age)
        return render(request, 'home.html', {"success": True})
