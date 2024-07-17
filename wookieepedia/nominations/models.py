from django.contrib import admin
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class Project(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Must be unique.')

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='project_lower_name_unique',
                violation_error_message='WookieProject name already exists (case insensitive)'
            )
        ]


class NominatorRight(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Must be unique.')

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='nominator_right_lower_name_unique',
                violation_error_message='Nominator Right already exists (case insensitive)'
            )
        ]


class Nominator(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Must be unique.')

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='nominator_lower_name_unique',
                violation_error_message='Nominator already exists (case insensitive)'
            )
        ]


class NominatorRightTimeframe(models.Model):
    nominator = models.ForeignKey(Nominator, on_delete=models.RESTRICT)
    right = models.ForeignKey(NominatorRight, on_delete=models.RESTRICT)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)


class Continuity(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Must be unique.')

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='continuity_lower_name_unique',
                violation_error_message='Continuity already exists (case insensitive)'
            )
        ]


class Nomination(models.Model):
    class Category(models.IntegerChoices):
        FEATURED = 1
        GOOD = 2
        COMPREHENSIVE = 3

    class Outcome(models.IntegerChoices):
        SUCCESSFUL = 1
        UNSUCCESSFUL = 2
        WITHDRAWN = 3
        OTHER = 4

    article_name = models.CharField(max_length=200, unique=True, help_text='Must be unique.')
    category = models.IntegerField(choices=Category)
    outcome = models.IntegerField(choices=Outcome)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True, help_text='Must be after Started At')
    start_word_count = models.IntegerField(null=True, blank=True)
    end_word_count = models.IntegerField(null=True, blank=True)

    continuities = models.ManyToManyField(Continuity)
    nominators = models.ManyToManyField(Nominator)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.article_name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('article_name'),
                name='nomination_lower_article_name_unique',
                violation_error_message='Article Name already exists (case insensitive)'
            )
        ]


class NominationAdmin(admin.ModelAdmin):
    search_fields = ['article_name']
    list_display = ('article_name', 'category', 'outcome')
    list_filter = ('category', 'outcome', 'projects', 'nominators')
