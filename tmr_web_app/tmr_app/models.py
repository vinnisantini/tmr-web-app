# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assets(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    heigh = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    hazmat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets'


class Missions(models.Model):
    unit = models.ForeignKey('Units', models.DO_NOTHING, db_column='unit', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'missions'


class TmrType(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmr_type'


class TmrWip(models.Model):
    tmr = models.ForeignKey('Tmrs', models.DO_NOTHING, blank=True, null=True)
    vic = models.ForeignKey('Vehicles', models.DO_NOTHING, blank=True, null=True)
    asset = models.ForeignKey(Assets, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmr_wip'


class Tmrs(models.Model):
    unit = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    mission = models.ForeignKey(Missions, models.DO_NOTHING, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(primary_key=True, max_length=255)
    pickup = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    dropoff = models.CharField(max_length=255, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    assets = models.CharField(max_length=255, blank=True, null=True)
    sup_unit = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    # edited_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='edited_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmrs'


class Units(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'units'


class Users(models.Model):
    unit = models.ForeignKey(Units, models.DO_NOTHING, db_column='unit', blank=True, null=True)
    f_name = models.CharField(max_length=255, blank=True, null=True)
    l_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vehicles(models.Model):
    make = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles'
