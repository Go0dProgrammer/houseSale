from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, surname, age, phone, avatar, password=None):
        if not email:
            raise ValueError("Users must hae an email adress!")
        if not first_name:
            raise ValueError("Users must hae a fist_name!")
        if not surname:
            raise ValueError("Users must hae a surname!")
        if not age:
            raise ValueError("Users must hae an age!")
        if not phone:
            raise ValueError("Users must hae a phone!")

        if not avatar:
            user = self.model(
                email = self.normalize_email(email),
                first_name = first_name,
                surname = surname,
                age = age,
                phone = phone,
                avatar = "static/img/accounts/base/base_avatar.png",
            )
        else:
            user = self.model(
                email = self.normalize_email(email),
                first_name = first_name,
                surname = surname,
                age = age,
                phone = phone,
                avatar = avatar,                
            )


        user.set_password(password)
        user.save(using = self._db)
        
        return user

    def create_superuser(self, email, first_name, surname, age, phone, avatar, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            surname = surname,
            age = age,
            phone = phone,
            avatar = "static/img/accounts/base/admin.png",
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user   

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=30, unique=True)
    first_name = models.CharField(verbose_name="name", max_length=30)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()
    avatar = models.ImageField(upload_to="static/img/accounts/avatars/users", blank=True)
    date_joined = models.DateTimeField(verbose_name="date joinded", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_supperuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname', 'age', 'phone', 'avatar']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True