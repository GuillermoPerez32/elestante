from django.db import models
from django.urls import reverse
from django.contrib.
# Create your models here.


class Libro(models.Model):

    cantidad_unidades = models.IntegerField(_("cantidad de unidades"))
    fecha = models.DateField(_("fecha"), auto_now=True)
    usuario = models.ForeignKey("directorio.User", verbose_name=_(
        "usuario"), on_delete=models.SET_NULL, blank=True)

    class Meta:
        verbose_name = _("libro")
        verbose_name_plural = _("libros")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("libro_detail", kwargs={"pk": self.pk})
