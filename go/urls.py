from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('north country', views.get_redirect),
    path('<side>', views.get_side, name="name"),

]

