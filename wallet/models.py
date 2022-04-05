from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	wallet_address = models.CharField(default="none",max_length=10)
	wallet_key = models.CharField(default="none",max_length=10)

	passphrase0 = models.CharField(default="none",max_length=10)
	passphrase1 = models.CharField(default="none",max_length=10)
	passphrase2 = models.CharField(default="none",max_length=10)
	passphrase3 = models.CharField(default="none",max_length=10)
	passphrase4 = models.CharField(default="none",max_length=10)
	passphrase5 = models.CharField(default="none",max_length=10)
	passphrase6 = models.CharField(default="none",max_length=10)
	passphrase7 = models.CharField(default="none",max_length=10)
	passphrase8 = models.CharField(default="none",max_length=10)
	passphrase9 = models.CharField(default="none",max_length=10)
	passphrase10 = models.CharField(default="none",max_length=10)
	passphrase11 = models.CharField(default="none",max_length=10)
	
	status = models.BooleanField(default=False)
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username


