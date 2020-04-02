from django.shortcuts import render
from . import  models
def index(request):
    sales =models.mdl_sale.objects.all()
    # apartements=models.mdl_apartement.objects.all()
    # lands =models.mdl_land.objects.all()
    # homes =models.mdl_home.objects.all()
    # rents =models.mdl_rent.objects.all()

    return render(request,
    "index.html",
    context={'sales':sales}
    )


def rents(request):
    pass




 