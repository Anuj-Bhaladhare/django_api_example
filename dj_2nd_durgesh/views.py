from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")
    friends = {
        "name": "anuj",
        "lastName": "bhaladhare",
        "someDetails": {
            "age": 20,
            "address": "bangalore"
        }
    }
    # return HttpResponse("<h1>this is home page</h1>")
    return JsonResponse(friends, safe=False)