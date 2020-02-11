from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from workorder.models 		import WorkOrder
from routing.models 		import Routing
from operation.models 		import Operation

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
		(ACTIVE, 'Active'),
		(DEACTIVE, 'Deactive'),
	)

# Build Type Choice
BUILT 		= 'BUILT'
COMPONENT 	= 'COMPONENT'
BUILT_CHOICES = (
		(BUILT, 'Built'),
		(COMPONENT, 'Component'),
	)

class SerialNumber(models.Model):
	number 				= models.CharField(max_length=100)
	workorder 			= models.ForeignKey(WorkOrder,
							on_delete=models.CASCADE,
							related_name='serialnumbers')
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	registered_date 	= models.DateTimeField(auto_now_add=True)
	routing 			= models.ForeignKey(Routing,
							on_delete=models.SET_NULL,
							blank=True, null=True)
	current_operation 	= models.ForeignKey(Operation,
							related_name='wips',
							on_delete=models.SET_NULL,
							blank=True, null=True)
	last_operation 		= models.ForeignKey(Operation,
							related_name='lastoperation',
							on_delete=models.SET_NULL,
							blank=True, null=True)
	last_modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	last_result 		= models.BooleanField(verbose_name = 'Last Result',default=False)
	finished_date 		= models.DateTimeField(blank=True, null=True)
	wip 				= models.BooleanField(verbose_name = 'Still In Process',default=True)
	perform_start_date 	= models.DateTimeField(blank=True, null=True)
	perform_operation 	= models.ForeignKey(Operation,
							related_name='performoperation',
							on_delete=models.SET_NULL,
							blank=True, null=True)
	perform_resource	= models.CharField(max_length=100,blank=True, null=True) #PC name or Any name
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)
	parent				= models.ForeignKey('self', null=True, 
							on_delete=models.SET_NULL,related_name='child')
	unit_type			= models.CharField(max_length=10,choices=BUILT_CHOICES,default = BUILT)

	class Meta:
		unique_together = ('number','workorder')
		ordering = ['-last_modified_date']

	def __str__(self):
		return ('%s on %s' % (self.number,self.workorder))

	def get_absolute_url(self):
		return reverse('serialnumber:detail', kwargs={'slug': self.slug})

	# Validation
	# def clean(self):
	# 	# Don't allow draft entries to have a pub_date.
	# 	if True:
	# 		raise ValidationError(_('Over WorkOrder QTY'))

	

def create_serialnumber_slug(instance, new_slug=None):
	# import datetime
	default_slug = '%s-%s' % (instance.number,instance.workorder )
	slug = slugify(default_slug)
	if new_slug is not None:
		slug = new_slug
	qs = SerialNumber.objects.filter(slug=slug)
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug,qs.first().id)
		return create_serialnumber_slug(instance, new_slug=new_slug)
	return slug

def pre_save_serialnumber_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_serialnumber_slug(instance)

pre_save.connect(pre_save_serialnumber_receiver, sender=SerialNumber)