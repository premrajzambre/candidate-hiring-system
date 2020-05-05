#les classes qu'on retrouve dans ladmin de django
#ATTENTION: a chaque modif, lancer la commande  makemigrations + migrate

from django.db import models

class Question(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

    def get_number(self):
        return Question.objects.filter(id__lte=self.id).count()

    def get_next_question(self):
        return Question.objects.filter(id__gt=self.id).first()

    def is_correct(self, option_id):
        try:
            return self.options.get(id=option_id).is_correct
        except Option.DoesNotExist:
            return False


class Option(models.Model):
    label = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='options'
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.label
