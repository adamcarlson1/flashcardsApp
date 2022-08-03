# cards/template/cards_tags.py

from django import template

from cards.models import BOXES, Card

register = template.Library() #creates an instance of Library used for registering template tags

@register.inclusion_tag("cards/box_links.html") #tells Django that boxes_as_links is an inclustion tag

def boxes_as_links():
    boxes = [] #declare dictionary
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count() #keeps track of the number of cards in the current box
        boxes.append({ # append to dictionary
            "number":box_num, #box number as key
            "card_count": card_count, #number of cards in the box 
        })
    return {"boxes": boxes} # returns a dictionary with boxes data

    

