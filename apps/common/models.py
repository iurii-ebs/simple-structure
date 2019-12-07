from django.db import models


# Abstract model, you can use this model as common model to your's models
# Django is not creating migrations for this model
class AbstractModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MyModel(AbstractModel):  # Inheritance from Abstract Model, adding all fields from abstract model
    text = models.TextField()
