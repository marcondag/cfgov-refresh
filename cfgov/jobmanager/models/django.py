from __future__ import absolute_import, unicode_literals

import six

from django.db import models

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel
)
from wagtail.wagtailcore.fields import RichTextField

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


@six.python_2_unicode_compatible
class ApplicantType(models.Model):
    applicant_type = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.applicant_type

    class Meta:
        ordering = ['applicant_type']


@six.python_2_unicode_compatible
class Grade(models.Model):
    grade = models.CharField(max_length=32)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()

    def __str__(self):
        return self.grade

    def __lt__(self, other):
        return (self.grade < other.grade)

    class Meta:
        ordering = ['grade']


@six.python_2_unicode_compatible
class JobCategory(models.Model):
    job_category = models.CharField(max_length=255)
    blurb = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.job_category

    class Meta:
        ordering = ['job_category']


@six.python_2_unicode_compatible
class JobLocation(ClusterableModel):
    abbreviation = models.CharField(
        max_length=2,
        primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('abbreviation',)


class Region(JobLocation):
    panels = [
        FieldPanel('abbreviation'),
        FieldPanel('name'),
        InlinePanel('states', label="States"),
        InlinePanel('cities', label="Cities"),
    ]


class Office(JobLocation):
    panels = [
        FieldPanel('abbreviation'),
        FieldPanel('name'),
        InlinePanel('cities', label="Office location", max_num=1),
    ]


@six.python_2_unicode_compatible
class State(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="State name")
    abbreviation = models.CharField(
        max_length=2,
        primary_key=True)
    region = ParentalKey(
        'Region',
        related_name="states")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('abbreviation',)


@six.python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="City name")
    state = models.ForeignKey(
        State,
        null=False,
        blank=False,
        default=None,
        related_name='cities')
    location = ParentalKey(
        'JobLocation',
        related_name='cities'
    )

    class Meta:
        ordering = ('state_id', 'name')

    def __str__(self):
        return '{}, {}'.format(self.name, self.state.abbreviation)
