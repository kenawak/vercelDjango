from django.db import models


# Create your models here.


class College(models.Model):
    STREAM_CHOICES = [
        ('Natural', 'Natural'),
        ('Social', 'Social'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_upload = models.ImageField(upload_to='college_images/', blank=True, null=True)

    image_url = models.URLField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    map_link = models.URLField(max_length=200, blank=True, null=True)
    stream = models.CharField(max_length=10, choices=STREAM_CHOICES, blank=True, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    Telegram = models.URLField(max_length=200, blank=True, null=True)

    def get_image(self):
        return self.image_url if self.image_url else self.image_upload.url

    def __str__(self):
        return self.name


class Departments(models.Model):
    EXTENSION_CHOICES = [
        ('extension', 'Extension'),
        ('regular', 'Regular'),
        ('both', 'Both'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    Telegram = models.URLField(max_length=200, blank=True, null=True)
    Years = models.IntegerField()
    icon_upload = models.ImageField(upload_to='department_images/', blank=True, null=True)
    icon_url = models.URLField(max_length=200, blank=True, null=True)
    programs = models.CharField(max_length=10, choices=EXTENSION_CHOICES, blank=True, null=True)

    # ForeignKey to establish the relationship with College
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name
