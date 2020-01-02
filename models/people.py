from django.db import models


class Person(models.Model):
    person_id = models.AutoField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(blank=False, null=False)
    last_name = models.CharField(blank=False, null=False)
    birth_date = models.DateTimeField(blank=True, null=True)


class Households(models.Model):
    household_id = models.AutoField(primary_key=True, blank=False, null=False)
    household_name = models.CharField(blank=False, null=False)


class HouseholdPeople(models.Model):
    household_id = models.ForeignKey('Households', to_field="household_id", blank=True, null=True)
    person_id = models.ForeignKey('Person', to_field="person_id", blank=True, null=True)
