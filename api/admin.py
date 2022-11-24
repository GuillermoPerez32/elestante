from django.contrib import admin
from .models import Libro,Material,Modulo
# Register your models here.
admin.site.register(Material)
admin.site.register(Modulo)
admin.site.register(Libro)