from django.db import models
class Email(models.Model):
    email = models.EmailField() #email field is special field which verify the email address as well before storing in the db.
