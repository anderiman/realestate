from django.db import models

from django.db import models

class mdl_sale(models.Model):
    sale_choices=(
        ("apartement","apartement"),
        ("land","land"),
        ("home","home"),
    )
    sale =models.CharField(choices=sale_choices,default="apartement", max_length=300)

    def __str__(self):
        return self.sale

class mdl_apartement(models.Model):
    
    apartement = models.ForeignKey(mdl_sale, on_delete=models.CASCADE)
    img =models.ImageField(null=True)
    topic =models.CharField( max_length=300,null=True)
    text =models.TextField(max_length=1000,null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.topic


class mdl_land(models.Model):
    
    land = models.ForeignKey(mdl_sale, on_delete=models.CASCADE,null=True)
    img =models.ImageField(null=True)
    topic =models.CharField( max_length=300,null=True)
    text =models.TextField(max_length=1000,null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.topic

    

class mdl_home(models.Model):
    
    home = models.ForeignKey(mdl_sale, on_delete=models.CASCADE,null=True)
    img =models.ImageField(null=True)
    topic =models.CharField( max_length=300,null=True)
    text =models.TextField(max_length=1000,null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.topic

   
class mdl_rent(models.Model):
    
    img =models.ImageField(null=True)
    topic =models.CharField( max_length=300,null=True)
    text =models.TextField(max_length=1000,null=True)
    date = models.DateTimeField(null=True)



    def __str__(self):
        return self.topic
 
    



class mdl_participation(models.Model):
    
    img =models.ImageField(null=True)
    topic =models.CharField( max_length=300,null=True)
    text =models.TextField(max_length=1000,null=True)
    date = models.DateTimeField(null=True)



    def __str__(self):
            return self.topic


class mdl_Contact(models.Model):

    first_name=models.CharField(max_length=300,null=True) 
    last_name=models.CharField(max_length=300,null=True) 
    mobile= models.CharField(max_length=12, null=True)
    subject=models.TextField(max_length=4000,null=True)
    

    def __str__(self):
        return self.subject

