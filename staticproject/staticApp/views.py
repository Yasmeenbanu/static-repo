from django.shortcuts import render

# Create your views here.
def view1(request):
    myName="Yasmeen"
    favPlayer="dhoni"
    favAnimal="Lion"
    favSubject="Python"
    d={'name':myName,'player':favPlayer,'subject':favSubject,'animal':favAnimal}
    return render(request,'staticApp/1.html',d)
