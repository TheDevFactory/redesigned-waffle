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
