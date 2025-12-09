from django.db import models
from django.utils.text import slugify



class Course(models.Model):
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    title = models.CharField(max_length=100)
    short_tag = models.CharField(max_length=20)
    image = models.ImageField(upload_to="courses/")
    price = models.IntegerField()
    duration = models.IntegerField()
    lesson_duration = models.IntegerField()

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


