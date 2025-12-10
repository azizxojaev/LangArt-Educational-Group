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
    course_overview = models.TextField()
    what_you_will_learn = models.JSONField(default=list)
    how_much_5stars = models.IntegerField()
    how_much_4stars = models.IntegerField()
    how_much_3stars = models.IntegerField()
    how_much_2stars = models.IntegerField()
    how_much_1stars = models.IntegerField()

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    locations = models.JSONField(default=list)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
    
    def __str__(self):
        return "Контакты"


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=40)
    user_image = models.ImageField(upload_to="reviews/")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
    def __str__(self):
        return f"Отзыв от {self.name}"


class Teacher(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="teachers/")
    about = models.TextField()
    experience = models.PositiveIntegerField()
    students = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.id}")
        super(Teacher, self).save(*args, **kwargs)