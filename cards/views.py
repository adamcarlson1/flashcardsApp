import imp
from random import random
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .forms import CardCheckForm
import random

# Create your views here.
from django.views.generic import (
    ListView, CreateView, UpdateView
)

from .models import Card

class CardListView(ListView): # class-based view is a subclass of Django's ListView
    model = Card #Card is the model the CardListView refers to
    # recieve a Django QuerySet with cards  first ordered by their box in ascending order, then by their creation date in descending order. 
    # the descending order of the creation date is thanks to the dash (-) prefix in "-date_created"
    queryset = Card.objects.all().order_by("box", "-date_created") # get all cards and order them by box and date_created

# create card view
class CardCreateView(CreateView):
    model = Card
    fields = ['question', 'answer', 'box'] 
    success_url: reverse_lazy("card-create")
    
# updating an existing view.
class CardUpdateView(CardCreateView, UpdateView):
    success_url: reverse_lazy("card-list")

class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        # only return the cards where box number matches the box_num value
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list) # randomly pick a card and add it to context
        return context
    # handles incoming POST requests
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # ensure required fields are filled out
        if form.is_valid(): 
            # if form is valid, get Card object from the database by its card_id value
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            # if correct, promote card to the next box. 
            card.move(form.cleaned_data["solved"])
        # redirect the request to the page from which you posted the request
        return redirect(request.META.get("HTTP_REFERER"))