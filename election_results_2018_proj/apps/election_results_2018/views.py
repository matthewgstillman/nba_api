from django.shortcuts import render
import requests
import election_results_api

# Create your views here.
def index(request):
    # url = "https://int.nyt.com/applications/elections/2018/api/1/races/2018-11-06.json"
    # response = requests.get(url)
    # print("Response: {}".format(response))
    # results = response.json()
    # print("Results: {}".format(results))
    with open("election_results_api.py") as fp:
        for i, line in enumerate(fp):
            if "\xe2" in line:
                print i, repr(line)
    context = {
        # 'results': results
        'response': response,
    }
    return render(request, 'election_results_2018/index.html', context)