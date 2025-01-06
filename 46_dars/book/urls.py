from django.urls import path
from .views import *

urlpatterns = [
    path("", my_books, name="books"),
    path("Istiqlol_jallodlari/", Istiqlol_jallodlari, name="Istiqlol_jallodlari"),
    path("Otkan_kunlar/", Otkan_kunlar, name="Otkan_kunlar"),
    path("Mehrobdan_chayon/", Mehrobdan_chayon, name="Mehrobdan_chayon"),
    path("Qor_qiygir/", Qor_qiygir, name="Qor_qiygir"),
    path("Olovli_yillar/", Olovli_yillar, name="Olovli_yillar"),
    path("Ufq/", Ufq, name="Ufq"),
    path("Choliqushi/", Choliqushi, name="Choliqushi"),
    path("Shum_bola/", Shum_bola, name="Shum_bola"),
    path("Temur_tuzuklari/", Temur_tuzuklari, name="Temur_tuzuklari"),
    path("Sarvqomat_dilbarim/", Sarvqomat_dilbarim, name="Sarvqomat_dilbarim"),
]
