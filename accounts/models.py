from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	major = models.CharField(max_length=150, blank=True, null=True)
	student_id = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	date_of_birth = models.DateField(blank=True, null=True)
	department = models.CharField(max_length=150, blank=True, null=True)
	enrollment_date = models.DateField(blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	expected_graduation = models.DateField(blank=True, null=True)
	advisor = models.CharField(max_length=150, blank=True, null=True)
	emergency_contact_name = models.CharField(max_length=150, blank=True, null=True)
	emergency_contact_phone = models.CharField(max_length=50, blank=True, null=True)
	emergency_contact_relationship = models.CharField(max_length=100, blank=True, null=True)
	emergency_contact_email = models.EmailField(blank=True, null=True)

	def __str__(self):
		return f"Profile: {self.user.username}"
