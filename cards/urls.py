import imp
from django.urls import path
from . import views

# dispatches urls
urlpatterns = [
    # serve CardListView as a view and rename routes name to card-list
    path("", views.CardListView.as_view(),name="card-list"),
    path("new", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("box/<int:box_num>", views.BoxView.as_view(), name="box"
    ),
]

