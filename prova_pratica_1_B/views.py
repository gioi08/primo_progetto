from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "prova_pratica_1_B/index.html")

def massimo(request):
    from random import randint

    n1=randint(1,20)
    n2=randint(1,20)
    n3=randint(1,20)
    if(n1>n2 and n1>n3):
        var1=n1
        var2=n2
        var3=n3
    elif(n2>n1 and n2>n3):
        var1=n2
        var2=n1
        var3=n3
    else:
        var1=n3
        var2=n1
        var3=n2
    return render(request, "prova_pratica_1_B/massimo.html",var1,var2,var3)

def pari(request):
    from random import randint
    lista=[]
    for i in range(30):
        lista[i]=randint(1,20)

    contpar=0
    contdisp=0
    for i in lista:
        if lista[i]%2==0:
            contpar=contpar+1
        else:
            contdisp=contdisp+1


    return render(request, "prova_pratica_1_B/pari.html",lista,contpar, contdisp)

def studenti(request):
    return render(request, "prova_pratica_1_B/studenti.html")