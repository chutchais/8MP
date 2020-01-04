from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from operation.models import Operation
# from django.db.models.signals import post_save
# from django.dispatch import receiver


ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

# class WMPUser(AbstractUser):
# 	department 			= models.CharField(max_length=20)
# 	operations 			= models.ManyToManyField(Operation,through='UserAccess')
# 	class Meta:
# 		permissions = [('can_login','Login to system')]

# class UserAccess(models.Model):
# 	user 			= models.ForeignKey(WMPUser, on_delete=models.CASCADE)
# 	operation 		= models.ForeignKey(Operation, on_delete=models.CASCADE)


# 	def __str__(self):
# 		return ('%s' % (self.operation))

class Profile(models.Model):
	user 				= models.OneToOneField(User, 
								on_delete=models.CASCADE,
								primary_key=True)
	department 			= models.CharField(max_length=20,blank=True, null=True)
	title	 			= models.CharField(max_length=30,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	
	def __str__(self):
		return ('%s' % (self.user))

class AccessOperation(models.Model):
	profile 			= models.ForeignKey(Profile, 
											on_delete=models.CASCADE,
											related_name = 'operations')
	operation 			= models.ForeignKey(Operation, 
											on_delete=models.CASCADE,
											related_name = 'users')


	def __str__(self):
		return ('%s' % (self.operation))

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         print('create')
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print(instance.profile_set.first().department)



# class Access(models.Model):
# 	user 				= models.ForeignKey(Profile)
# 	operation 			= models.ManyToManyField(Operation,through='UserAccess')
# 	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
# 	created_date 		= models.DateTimeField(auto_now_add=True)
# 	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
# 	user 				= models.ForeignKey('auth.User',blank=True,null=True)

# ,through='UserAccess'
