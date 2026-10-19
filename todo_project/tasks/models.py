from django.db import models
from django.forms import ValidationError

class Type(models.Model):
    name = models.CharField(max_length=50)
    suggested_completion_time = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Task(models.Model):

    TYPE_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Shopping', 'Shopping'),
        ('Other', 'Other'),
    ]

    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]

    def validate_decimal(value):
        if value < 0.0 :
            raise ValidationError(
                ('%(value)s must be a positive number'),
                params={'value': value},
            )

    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    type = models.CharField(max_length=24, choices=TYPE_CHOICES, blank=False)
    task_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    complete_date = models.DateTimeField(auto_now_add=True)


    @property
    def get_description(self):
        if self.description:
            return self.description
        else:
            return "No description provided."

    def __str__(self):
        return self.title
   