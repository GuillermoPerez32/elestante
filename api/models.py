from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Libro(models.Model):

    cantidad_unidades = models.IntegerField(_("cantidad de unidades"))
    fecha = models.DateField(_("date"), auto_now=True)
    usuario = models.ForeignKey("directorio.User", verbose_name=_(
        "usuario"), on_delete=models.SET_NULL, blank=True)
    asignatura = models.CharField(_("subject"), max_length=80)
    anno_escolar = models.PositiveSmallIntegerField(_("scholar year"))

    class Meta:
        verbose_name = _("libro")
        verbose_name_plural = _("libros")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("libro_detail", kwargs={"pk": self.pk})


class Modulo(models.Model):

    cantidad_unidades = models.IntegerField(_("cantidad de unidades"))
    fecha = models.DateField(_("date"), auto_now=True)
    usuario = models.ForeignKey("directorio.User", verbose_name=_(
        "usuario"), on_delete=models.SET_NULL, blank=True)
    anno_escolar = models.PositiveSmallIntegerField(_("scholar year"))

    class Meta:
        verbose_name = _("Modulo")
        verbose_name_plural = _("Modulos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Modulo_detail", kwargs={"pk": self.pk})
