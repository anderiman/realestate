from django.contrib import admin
from hamahang.models import mdl_apartement,mdl_home,mdl_land,mdl_participation,mdl_rent ,mdl_Contact

class adm_apartement(admin.ModelAdmin):
    pass
admin.site.register(mdl_apartement,adm_apartement)


class adm_home(admin.ModelAdmin):
    pass
admin.site.register(mdl_home,adm_home)

class adm_land(admin.ModelAdmin):
    pass
admin.site.register(mdl_land,adm_land)

class adm_participation(admin.ModelAdmin):
    pass
admin.site.register(mdl_participation,adm_participation)

class adm_rent(admin.ModelAdmin):
    pass
admin.site.register(mdl_rent,adm_rent)


class adm_Contact(admin.ModelAdmin):
    pass
admin.site.register(mdl_Contact,adm_Contact)

