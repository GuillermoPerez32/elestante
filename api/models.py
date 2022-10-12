from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Libro(models.Model):

    cantidad_unidades = models.IntegerField(_("cantidad de unidades"))
    fecha = models.DateField(_("date"), auto_now=True)
    usuarios = models.ManyToManyField("directorio.User", verbose_name=_(
        "usuarios"), blank=True, null=True)
    asignatura = models.CharField(_("subject"), max_length=80)
    anno_escolar = models.PositiveSmallIntegerField(_("scholar year"))

    class Meta:
        verbose_name = _("libro")
        verbose_name_plural = _("libros")

    def __str__(self):
        return self.asignatura

    def get_absolute_url(self):
        return reverse("libro_detail", kwargs={"pk": self.pk})


class Material(models.Model):

    cantidad_unidades = models.IntegerField(_("cantidad de unidades"))
    nombre = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("material")
        verbose_name_plural = _("materials")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("material_detail", kwargs={"pk": self.pk})


class Modulo(models.Model):

    materiales = models.ManyToManyField(
        "api.Material", verbose_name=_("materiales"))
    fecha = models.DateField(_("date"), auto_now=True)
    usuario = models.ForeignKey("directorio.User", verbose_name=_(
        "usuario"), on_delete=models.SET_NULL, blank=True, null=True)
    anno_escolar = models.PositiveSmallIntegerField(_("scholar year"))

    class Meta:
        verbose_name = _("Modulo")
        verbose_name_plural = _("Modulos")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("Modulo_detail", kwargs={"pk": self.pk})
