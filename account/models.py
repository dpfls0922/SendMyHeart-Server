from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, email, phone, username, profile_image, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            username=username,
            profile_image=profile_image,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone, username, profile_image, password, **kwargs):
        superuser = self.create_user(
            email=email,
            password=password,
            phone=phone,
            username=username,
            profile_image=profile_image,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        
        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    # id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False) 
    username = models.CharField(max_length=30, null=False)
    profile_image = models.ImageField(upload_to='profile_images/')
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

   # 이메일로 식별
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'username', 'profile_image'] # 추가 필드 명시
    

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True