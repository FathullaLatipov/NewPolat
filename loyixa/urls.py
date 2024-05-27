from django.urls import path
from .views import *

urlpatterns = [
    path('zapchast/', Zapchast_all.as_view()),
    path('maxsulot/', Maxsulot_all.as_view()),
    path('order/', OrdersView.as_view()),
]
