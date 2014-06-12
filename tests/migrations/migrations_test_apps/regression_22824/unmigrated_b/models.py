from django.db import models
from migrations.migrations_test_apps.regression_22824.unmigrated_c.models import ModelC


class ModelB(models.Model):
    somefield = models.CharField()
    somefk = models.ForeignKey(ModelC)
