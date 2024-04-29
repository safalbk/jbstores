from django.urls import path

from . import views


app_name = "book"

urlpatterns = [

    path("", views.index, name="index"),
    path("allperson/", views.allperson, name="allperson"),
    path("add_purchase/", views.add_purchase, name="add_purchase"),

    path("add_person/", views.add_person, name="add_person"),
    path("edit_person/<int:p_id>/", views.edit_person, name="edit_person"),

    path("single_person_transactions/<str:name>/", views.single_person_transactions, name="single_person_transactions"),
    path("register/", views.register, name="register"),
    path("calculator/", views.calculator, name="calculator"),
        path("ipl/", views.ipl, name="ipl"),


    # path("quizrd_login", views.quizrd_login, name="quizrd_login"),
]
