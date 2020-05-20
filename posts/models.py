#from tinymce.models import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    JOB_TITLE_CHOICES = (
        ('Associate Engineer', 'Associate Engineer'),
        ('Senior Engineer', 'Senior Engineer'),
        ('Team Leader', 'Team Leader'),
        ('Project Architect', 'Project Architect'),
        ('Project Scrum Master', 'Project Scrum Master'),
        ('Project Delivery Manager', 'Project Delivery Manager')
    )
    EXPERIENCE_CHOICES = (
        ('Fresher', 'Fresher'),
        ('Experienced', 'Experienced')
    )
    EMPLOYMENT_TYPE_CHOICES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time')
    )
    JOB_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Expired', 'Expired')
    )

    blog_title = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100, choices=JOB_TITLE_CHOICES)
    job_description = models.TextField(max_length=3000)
    skills = models.TextField(max_length=3000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    featured = models.BooleanField()
    experience = models.CharField(max_length=100, choices=EXPERIENCE_CHOICES)
    employment_type = models.CharField(
        max_length=100, choices=EMPLOYMENT_TYPE_CHOICES)
    vacancy = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    job_status = models.CharField(max_length=100, choices=JOB_STATUS_CHOICES)

    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={
            'pk': self.pk
        })

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()
