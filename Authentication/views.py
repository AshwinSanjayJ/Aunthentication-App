from django.shortcuts import render,redirect

# Create your views here.

def auth(req):
    if req.method == "POST":
        username = req.POST["Username"]
        password = req.POST["password"]
        if username == "ashwin" and password == "ashwin123":
            return redirect("home")
        else:
            return render(req,"index.html",{"error":"Invalid Credentials"})
    return render(req,"index.html")

def home_view(req):
    return render(req,"home.html")    