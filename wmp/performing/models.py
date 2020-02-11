from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings

from serialnumber.models import SerialNumber
from operation.models import Operation
import uuid

class Performing(models.Model):
	uid		    	= models.UUIDField(default=uuid.uuid4, editable=False)
	sn 				= models.ForeignKey(SerialNumber,
						on_delete=models.CASCADE,
						related_name ='performings')
	operation 		= models.ForeignKey(Operation,
						on_delete=models.SET_NULL,blank=True,null=True)
	interval		= models.IntegerField(default=1)
	resource_name	= models.CharField(max_length=100,blank=True, null=True) #PC name or Any name
	start_time 		= models.DateTimeField(blank=True, null=True)
	stop_time 		= models.DateTimeField(blank=True, null=True)
	result 			= models.BooleanField(default=False)
	remark 			= models.TextField(max_length=255,blank=True, null=True)
	created_date 	= models.DateTimeField(auto_now_add=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	class Meta:
		ordering = ['-stop_time']

	def __str__(self):
		return ('%s on %s' % (self.sn,self.operation))

	def get_absolute_url(self):
		return reverse('performing:detail', kwargs={'uid': self.uid})

	@property
	def duration(self):
		return self.stop_time - self.start_time

	@property
	def perform_year(self):
		return self.stop_time.year

	@property
	def perform_month(self):
		return self.stop_time.month

	@property
	def perform_day(self):
		return self.stop_time.day

	@property
	def perform_hour(self):
		return self.stop_time.hour
	

# def create_performing_slug(instance, new_slug=None):
#     # import datetime
#     default_slug = '%s-%s' % (instance.sn.number,instance.operation.name )
#     slug = slugify(default_slug)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Performing.objects.filter(slug=slug)
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug,qs.first().id)
#         return create_performing_slug(instance, new_slug=new_slug)
#     return slug

def pre_save_performing_interval(sender, instance, *args, **kwargs):
	qs = Performing.objects.filter(sn=instance.sn ,operation=instance.operation)
	instance.interval = qs.count()+1 


pre_save.connect(pre_save_performing_interval, sender=Performing)