from tkinter.messagebox import QUESTION
from django.db import models

# Create your models here.
# Replicate the attributes of a card in the model of your cards app
NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    question = models.CharField(max_length=100) #question
    answer = models.CharField(max_length=100) #answer
    # keep track of the box number where your card sits
    box = models.IntegerField( #box
        choices=zip(BOXES,BOXES), # ensure models.IntegerField contains a number within BOXES range
        default=BOXES[0], #by default create your flashcard in the first box
    )
    date_created = models.DateTimeField(auto_now_add=True) #automatically contains a timestamp of your card's date and time of creation

    def __str__(self):
        return self.question #conveniently spot which card you're working with
    
    # replicate the behavior of moving a card between boxes
    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0] # if correct move card up one box else move card back to the first box

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self
