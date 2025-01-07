from django.db import models
from django.utils import timezone


class Fakultet(models.Model):
    nomi = models.CharField(max_length=150, unique=True)
    dekan = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nomi


class Yonalish(models.Model):
    nomi = models.CharField(max_length=150)
    fakultet = models.ForeignKey(Fakultet, related_name='yonalishlar', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nomi} ({self.fakultet.nomi})"


class Guruh(models.Model):
    nomi = models.CharField(max_length=50)
    yonalish = models.ForeignKey(Yonalish, related_name='guruhlar', on_delete=models.CASCADE)
    boshlanish_yili = models.PositiveIntegerField()
    bitiruv_yili = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nomi} - {self.yonalish.nomi}"


class Talaba(models.Model):
    ismi = models.CharField(max_length=100)
    familiyasi = models.CharField(max_length=100)
    tugilgan_sana = models.DateField()
    guruh = models.ForeignKey(Guruh, related_name='talabalar', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.ismi} {self.familiyasi} ({self.guruh.nomi if self.guruh else 'Guruh belgilanmagan'})"


class Oqituvchi(models.Model):
    toliq_ismi = models.CharField(max_length=150)
    fakultet = models.ForeignKey(Fakultet, related_name='oqituvchilar', on_delete=models.SET_NULL, null=True)
    mutaxassislik = models.CharField(max_length=150)

    def __str__(self):
        return self.toliq_ismi
