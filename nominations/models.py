from django.contrib import admin
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils import timezone
from django.utils.html import format_html


class Project(models.Model):
    class Type(models.IntegerChoices):
        CATEGORY = 1
        INTELLECTUAL_PROPERTY = 2

    name = models.CharField(max_length=200, unique=True, help_text='Must be unique.')
    type = models.IntegerField(choices=Type, default=Type.CATEGORY, help_text='If Intellectual Property is chosen, '
                                                                              'the name will render in italics.')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.type == Project.Type.INTELLECTUAL_PROPERTY:
            return format_html('<em>{}</em>', self.name)
        return self.name

    @admin.display
    def styled_name(self):
        return self.__str__()

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='project_lower_name_unique',
                violation_error_message='WookieProject name already exists (case insensitive)'
            )
        ]


class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('styled_name', 'type', 'created_at')
    list_filter = ('type', 'created_at')


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


class NominatorAdmin(admin.ModelAdmin):
    search_fields = ['name']


class NominatorRightTimeframe(models.Model):
    class Right(models.IntegerChoices):
        AGRI_CORP = 1
        EDU_CORP = 2
        INQUISITOR = 3
        BANNED = 4

    nominator = models.ForeignKey(Nominator, on_delete=models.RESTRICT)
    right = models.IntegerField(choices=Right)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)


class Continuity(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text='Must be unique.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'continuities'
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
    list_display = ('article_name', 'category', 'outcome', 'started_at', 'ended_at')
    list_filter = ('category', 'outcome', 'projects', 'nominators', 'started_at')
