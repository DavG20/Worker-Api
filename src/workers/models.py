from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, phone_number, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")
        self.phone_number = phone_number
        # password = self.make_random_password(12)
        user = self.model(phone_number=phone_number, **extra_fields)
        # user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_active = True
        user.save(using=self._db)
        return user
    def create_superuser(self, phone_number, password, **extra_fields):
        user = self.create_user(phone_number=phone_number)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        
        user.is_superuser = True
        user.email_verified = True
        user.set_password(password)
        user.save(using=self._db)
        
class Worker(AbstractUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = PhoneNumberField(max_length=255, unique=True, blank=False, null=False )
    # to make the field nullable ob the admin panel
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    
    USERNAME_FIELD = "phone_number"
    object = UserManager()
    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"
    
    def __str__(self):
        return f"{self.phone_number}"



class Unit(models.Model):  
    name = models.CharField(max_length=255, null=False, blank=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='unit_worker')
    def __str__(self):
        return self.name

class Visit(models.Model):  
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='visit_unit')
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    visit_date  = models.DateTimeField()

    
    

