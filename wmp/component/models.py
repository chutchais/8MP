from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from serialnumber.models import SerialNumber
from operation.models import Operation

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
		(ACTIVE, 'Active'),
		(DEACTIVE, 'Deactive'),
	)

# Part Type
PART_TYPE_CHOICE = (
		('COMPONENT','Component'),
		('MODULE','Module with serial number'),
		('BUILD','Inernal Build with serial number')
	)

ASSEMBLY_ACTION_CHOICES = (
		(True, 'Assembly'),
		(False, 'De-Assembly'),
	)


# With Serial number from In-comming part or Internal build.
class Module(models.Model):
	number 				= models.CharField(max_length=100,
							validators=[
								RegexValidator(
									regex='^[\w-]+$',
									message='Number does not allow special charecters',
								),
							])
	parent 				= models.ForeignKey(SerialNumber,
							on_delete=models.SET_NULL,blank=True, null=True,
							related_name='components',
							verbose_name ='Assembled on')
	reserved_for 		= models.ForeignKey(SerialNumber,
							on_delete=models.SET_NULL,
							related_name='reservedfors',blank=True, null=True,
							verbose_name ='Reserved for')
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	title 				= models.CharField(max_length=100,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	pn 					= models.CharField(max_length=100,blank=True, null=True,
							validators=[
								RegexValidator(
									regex='^[\w-]+$',
									message='Part number does not allow special charecters',
								),
							],verbose_name ='Part number')
	rev 				= models.CharField(verbose_name ='Part Revision',max_length=100,blank=True, null=True)
	datecode			= models.CharField(verbose_name ='Date code',max_length=100,blank=True, null=True)
	lotcode				= models.CharField(verbose_name ='Lot code',max_length=100,blank=True, null=True)
	supcode				= models.CharField(verbose_name ='Supplier code',max_length=100,blank=True, null=True)
	registered_date 	= models.DateTimeField(auto_now_add=True)
	last_operation 		= models.ForeignKey(Operation,
							related_name='component_last_operations',
							on_delete=models.SET_NULL,
							blank=True, null=True)
	last_modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)
	pn_type				= models.CharField(verbose_name ='Part Type',
							max_length=10,choices=PART_TYPE_CHOICE,default='MODULE')

	class Meta:
		unique_together = ('number','pn')
		ordering = ['-last_modified_date']

	def __str__(self):
		return ('%s' % (self.number))

	def get_absolute_url(self):
		return reverse('component:module-detail', kwargs={'slug': self.slug})

	# Validation
	# def clean(self):
	# 	# Don't allow draft entries to have a pub_date.
	# 	if True:
	# 		raise ValidationError(_('Over WorkOrder QTY'))

def create_module_slug(instance, new_slug=None):
	# import datetime
	default_slug = '%s' % (instance.number)
	slug = slugify(default_slug)
	if new_slug is not None:
		slug = new_slug
	qs = Module.objects.filter(slug=slug)
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug,qs.count())
		return create_module_slug(instance, new_slug=new_slug)
	return slug

def pre_save_module_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_module_slug(instance)

pre_save.connect(pre_save_module_receiver, sender=Module)



# tray, tube, or tape and reel
CARRIER_TYPE_CHOICE = (
		('TRAY','Tray'),
		('TUBE','Tube'),
		('TAPE','Tape'),
		('REEL','Reel'),
		('OTHER','Other')
	)

MSL_TYPE_CHOICE = (
		('1','1'),
		('2','2'),
		('2A','2a'),
		('3','3'),
		('4','4'),
		('5','5'),
		('5A','5a'),
		('6','6'),
	)

# MSL 	Floor life
# 1	Unlimited at ≤30°C/85% RH
# 2	1 year
# 2a	4 weeks
# 3	168 hours
# 4	72 hours
# 5	48 hours
# 5a	24 hours
# 6	Mandatory bake before use. After bake, must be reflowed within the time limit specified on the label.

# SMT component (without Serial number)
class Component(models.Model):
	number 				= models.CharField(primary_key = True,max_length=100,
							validators=[
								RegexValidator(
									regex='^[\w-]+$',
									message='Number does not allow special charecters',
								),
							],
							verbose_name ='Batch number')
	barcode 			= models.CharField(verbose_name ='Barcode label',max_length=100,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	title 				= models.CharField(max_length=100,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	pn 					= models.CharField(max_length=100,blank=True, null=True,
							validators=[
								RegexValidator(
									regex='^[\w-]+$',
									message='Part number does not allow special charecters',
								),
							],verbose_name ='Part number')
	rev 				= models.CharField(verbose_name ='Part Revision',max_length=100,blank=True, null=True)
	datecode			= models.CharField(verbose_name ='Date code',max_length=100,blank=True, null=True)
	lotcode				= models.CharField(verbose_name ='Lot code',max_length=100,blank=True, null=True)
	supcode				= models.CharField(verbose_name ='Supplier code',max_length=100,blank=True, null=True)
	qty 				= models.IntegerField(verbose_name ='Total Qty',default=0)
	carrier 			= models.CharField(max_length=10,choices=CARRIER_TYPE_CHOICE,default='REEL')
	msl 				= models.CharField(verbose_name ='Moisture Sensitivity Levels',
											max_length=3,choices=MSL_TYPE_CHOICE,default='2')
	floor_life			= models.IntegerField(verbose_name ='Floor life (hr)',default= 72)
	shelf_life			= models.IntegerField(verbose_name ='Shelf life (day)',default= 365)
	met 				= models.IntegerField(verbose_name ='Manufacturer Exposure Time (hr)',default= 1)
	exp_date			= models.DateTimeField(verbose_name ='Expire Date',blank=True, null=True)
	baking_start_date	= models.DateTimeField(verbose_name ='Start Baking Datetime',blank=True, null=True)
	baking_finish_date  = models.DateTimeField(verbose_name ='Finish Baking Datetime',blank=True, null=True)
	registered_date 	= models.DateTimeField(auto_now_add=True)
	last_modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)

	class Meta:
		ordering = ['-last_modified_date']

	def __str__(self):
		return ('%s' % (self.number))

	def get_absolute_url(self):
		return reverse('component:detail', kwargs={'pk': self.pk})

	# Validation
	# def clean(self):
	# 	# Don't allow draft entries to have a pub_date.
	# 	if True:
	# 		raise ValidationError(_('Over WorkOrder QTY'))

def create_component_slug(instance, new_slug=None):
	# import datetime
	default_slug = '%s' % (instance.number)
	slug = slugify(default_slug)
	if new_slug is not None:
		slug = new_slug
	qs = Component.objects.filter(slug=slug)
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug,qs.count())
		return create_component_slug(instance, new_slug=new_slug)
	return slug

def pre_save_component_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_component_slug(instance)

pre_save.connect(pre_save_component_receiver, sender=Component)


class Assembled(models.Model):
	number 				= models.ForeignKey(SerialNumber,
							on_delete=models.SET_NULL,blank=True, null=True,
							related_name='assembled',
							verbose_name ='Unit serial number')
	pn_type				= models.CharField(verbose_name ='Part Type',
							max_length=10,choices=PART_TYPE_CHOICE,default='MODULE')
	refdes 				= models.CharField(verbose_name ='Ref Destinator',max_length=50,
						validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='RD does not allow special charecters',
										),
						])
	pn 				= models.CharField(verbose_name ='Part Number',max_length=50,
						validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Part number does not allow special charecters',
										),
						])
	rev 				= models.CharField(verbose_name ='Part Revision',max_length=20,blank=True, null=True)
	module_number 	= models.ForeignKey(Module,
							on_delete=models.SET_NULL,blank=True, null=True,
							related_name='assembled',
							verbose_name ='Module Number')
	component_number 	= models.ForeignKey(Component,
							on_delete=models.SET_NULL,blank=True, null=True,
							related_name='assembled',
							verbose_name ='Part Number')
	operation 		= models.ForeignKey(Operation,
							on_delete=models.SET_NULL,blank=True, null=True,
							related_name='assembled',
							verbose_name ='Assembled Operation')
	note 			= models.TextField(max_length=255,blank=True, null=True)
	action_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	action_status 	= models.BooleanField(choices=ASSEMBLY_ACTION_CHOICES,default=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)
	def __str__(self):
		return ('%s on %s' % (self.refdes,self.number))

	def get_absolute_url(self):
		return reverse('component:assembled-detail', kwargs={'slug': self.slug})

def create_assembled_slug(instance, new_slug=None):
	# import datetime
	default_slug = '%s-%s' % (instance.number,instance.refdes)
	slug = slugify(default_slug)
	if new_slug is not None:
		slug = new_slug
	qs = Assembled.objects.filter(slug=slug)
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug,qs.count())
		return create_assembled_slug(instance, new_slug=new_slug)
	return slug

def pre_save_assembled_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_assembled_slug(instance)

pre_save.connect(pre_save_assembled_receiver, sender=Assembled)