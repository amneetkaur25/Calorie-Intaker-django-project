from django.shortcuts import render
#eeXOmDlG1ATya/gLjZJ8bQ==CB5iysUzR5SZFFhh
# Create your views here.
def home(request):
    import requests
    import json
    if request.method=="POST":
        query=request.POST.get('query')
  
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'eeXOmDlG1ATya/gLjZJ8bQ==CB5iysUzR5SZFFhh'})
        try:
            api=json.loads(response.content)
        except Exception as e:
            api="Opps there was an error!"
            print(e)
        return render(request,"home.html",{'api':api})
    else:
        return render(request,"home.html",{'query':"Enter a Valid Query"})

