from django.shortcuts import render

def index(request):
    
    a = None
    a.hello() # Creating an error with an invalid line of code

    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )


def start(request):
    
    #b = None
    #b.start() # Creating an error with an invalid line of code

    return render(
        request,
        "start.html",
        {
            "title": "Onboaring example",
        },
    )
