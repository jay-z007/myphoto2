from django.db import models
from django.utils import timezone
import string
from myphoto.settings import MEDIA_ROOT,IMAGE_ROOT
import os
from PIL import Image as PImage

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, first_name, last_name, gender,  password=None):
        """
        Creates and saves a User with the given email, date of
        birth, password, first name, last name, gender and time of registration.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            gender=gender,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, first_name, last_name, gender,  password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            gender=gender,

            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=100,default=None)
    last_name = models.CharField(max_length=100,default=None)
    gender = models.CharField(max_length=10,default=None)
    time_registered = models.DateTimeField(default=timezone.now())
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth','first_name','last_name','gender']

    def get_DOB(self):
        return self.date_of_birth.strftime("%Y-%m-%d")+""

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    description = models.TextField()
    cover_photo = models.ImageField(upload_to='covers')
    upload_time = models.DateTimeField(default=timezone.now())
    users = models.ManyToManyField(MyUser)

    def __str__(self):
        return self.album_name

    def user(self):
        return "\n".join([p.first_name+" "+p.last_name+"," for p in self.users.all()])

    class Meta:
        ordering = ('album_name',)


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag


class Photo(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to="images")
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=50)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(MyUser, null=True, blank=True)

    def __unicode__(self):
        return self.image.name

    def __str__(self):
        return self.image.name

    # def save(self, *args, **kwargs):
    #     """Save image dimensions."""
    #     super(Photo, self).save(*args, **kwargs)
    #     im = PImage.open(self.image.url)
    #     self.width, self.height = im.size
    #     super(Photo, self).save(*args, ** kwargs)

    def save_dimen(self, *args, **kwargs):
        """Save image dimensions."""
        im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size
        self.save()


    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return "\n".join(lst)

    def albums_(self):
        lst = [x[1] for x in self.albums.values_list()]
        return "\n".join(lst)

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True