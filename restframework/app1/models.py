from django.db import models


class Questions(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='Questions', on_delete=models.CASCADE, editable = False, null = True)


class Choices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


class C(models.Model):
    a = models.CharField(max_length=31)