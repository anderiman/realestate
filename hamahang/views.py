from django.shortcuts import render
from . import  models
#from hamahang.forms import forms
#from hamahang.forms import frm_Contact

def index(request):
    return render(request,
    "index.html",
    )

    #sales =models.mdl_sale.objects.all()
    # apartements=models.mdl_apartement.objects.all()
    # lands =models.mdl_land.objects.all()
    # homes =models.mdl_home.objects.all()
    # rents =models.mdl_rent.objects.all()
    # participations=models.mdl_participation.objects.all()
    #context={'sales':sales}
    

def vw_sale(request):
    sales =models.mdl_sale.objects.all()
    return render(request,
    "sale.html",
    context={'sales':sales}
    )
    



def vw_apartement(request):
    apartements=models.mdl_apartement.objects.all()
    return render(request,
    "apartement.html",
    context={'apartements':apartements}

    )

def vw_home(request):
    homes =models.mdl_home.objects.all()
    return render(request,
    "home.html",
    context={'homes':homes}
    )


def vw_land(request):
    lands =models.mdl_land.objects.all()
    return render(request,
    "land.html",
    context={'lands':lands}
    )


def vw_rents(request):
    rents =models.mdl_rent.objects.all()
    return render(request,
    "rent.html",
    context={'rents':rents}
    )



def vw_participation(request):
    participations=models.mdl_participation.objects.all()
    return render(request,
    "participation.html",
    context={'participations':participations}
    )    




def vw_Contact(request):
    Contacts=models.mdl_Contact.objects.all()
    if request.method=='POST':
       
        return render(request,
        "Contact.html",
        context={'Contacts':Contacts}
         )
    else:
        return render(request,
        "Contact.html",)


def vw_kish(request):
    return render(request,'kish.html')

def vw_georgin(request):
    return render(request,'georgin.html')


def vw_mashhad(request):
    return render(request,'mashhad.html')

 