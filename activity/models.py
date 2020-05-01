from random import randint

from django.db import models
from django.db.models.aggregates import Count
from django.core.validators import MinValueValidator, MaxValueValidator

from activity import RandomOnEmptyQuerySetException


class ActivityQuerySet(models.QuerySet):

    def random(self):
        """Random algo extracted from
        http://web.archive.org/web/20110802060451/http://bolddream.com/2010/01/22/getting-a-random-row-from-a-relational-database/
        """
        count = self.aggregate(count=Count('id'))['count']
        if count == 0:
            # queryset empty
            raise RandomOnEmptyQuerySetException
        random_index = randint(0, count - 1)
        return self[random_index]


class ActivityManager(models.Manager):

    def get_queryset(self):
        return ActivityQuerySet(self.model, using=self._db)

    def random(self):
        return self.get_queryset().random()


class Activity(models.Model):
    description = models.CharField(max_length=255)
    accessibility = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=(
            MinValueValidator(0.0),
            MaxValueValidator(1.0),
        )
    )
    type = models.CharField(max_length=255, db_index=True)
    participants = models.IntegerField(
        validators=(MinValueValidator,),
        db_index=True
    )
    price = models.DecimalField(
        db_index=True,
        max_digits=3,
        decimal_places=2,
        validators=(
            MinValueValidator(0.0),
            MaxValueValidator(1.0),
        )
    )
    link = models.URLField(blank=True, null=True)

    objects = ActivityManager()

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.type = self.type.lower()
        return super(Activity, self).save(*args, **kwargs)
