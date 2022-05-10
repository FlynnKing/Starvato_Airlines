from django.contrib import admin
from .models import *
class AereoAdmin (admin.ModelAdmin):
    list_display = ('name', 'locate', 'tot_posti')
    list_filter = ('name', 'locate', 'tot_posti')

# Register your models here.
admin.site.register(Aircraft,AereoAdmin)
admin.site.register(Airport)
admin.site.register(Fly)
admin.site.register(Prenotazione)
admin.site.register(Personale)



