from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image


# creating custom UserProfile Account Manager
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have email Id")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(email=self.normalize_email(email),
                          username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=self.normalize_email(email),
                                username=username,
                                password=password)
        user.role = 'ADM'
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# creating custom user
class User(AbstractUser):
    email = models.EmailField(verbose_name="Email", unique=True)
    ROLE_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    batch = models.IntegerField()
    gender = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Male')
    name = models.CharField(max_length=30)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateField()
    college_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'gender', 'batch', 'name', 'image', 'date_of_birth', 'college_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Team(models.Model):
    name = models.CharField(max_length=100)
    team_points = models.IntegerField(default=0)
    url = models.URLField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.name} Profile'
