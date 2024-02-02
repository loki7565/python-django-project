from django.db import models

class Signup(models.Model):
    signup_fname = models.CharField(max_length=255)
    signup_lname= models.CharField(max_length=255)
    signup_email = models.CharField(max_length=255)
    # signup_gender = models.CharField(max_length=255)
    signup_product = models.CharField(max_length=255)
    signup_number = models.CharField(max_length=255)