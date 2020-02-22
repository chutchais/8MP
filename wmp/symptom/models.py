from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from django.urls import reverse
from django.conf import settings

from product.models import Product

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

DEFECT_TYPE_CHOICE =(
		('VISUAL'			, 'Visual Inspection'),
		('FUNCTIONAL'		, 'Functional Test')
	)

class SymptomCode(models.Model):
	name 				= models.CharField(max_length=50,primary_key=True,
									validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Name does not allow special charecters',
										),
									])
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	symptom_type		= models.CharField(max_length=20,choices=DEFECT_TYPE_CHOICE,
							default='VISUAL')
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)
	# products			= models.ManyToManyField(Product)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('symptom:detail', kwargs={'slug': self.slug})

def create_symptomcode_slug(instance, new_slug=None):
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = SymptomCode.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_symptom_slug(instance, new_slug=new_slug)
    return slug

def pre_save_symptomcode_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_symptomcode_slug(instance)

pre_save.connect(pre_save_symptomcode_receiver, sender=SymptomCode)


# Add on Feb 17,2020
# To define Symptom code for operation.

from routing.models import RoutingDetail
class SymptomCode_Usage(models.Model):
	routingdetail 			= models.ForeignKey(RoutingDetail, 
								on_delete=models.CASCADE,
								related_name ='symptomcode_usages')
	symptomcode 				= models.ForeignKey(SymptomCode, 
								on_delete=models.CASCADE,
								related_name ='symptomcode_usages')
	ordered 				= models.IntegerField(default=1)
	slug 					= models.SlugField(unique=True,blank=True, null=True)
	title 					= models.CharField(max_length=100,blank=True, null=True)
	description 			= models.TextField(max_length=255,blank=True, null=True)
	category1 				= models.CharField(max_length=50,blank=True, null=True)
	category2 				= models.CharField(max_length=50,blank=True, null=True)
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.SET_NULL,
								blank=True,null=True)

	def __str__(self):
		return ('%s on %s' % (self.symptomcode,self.routingdetail))

	def get_absolute_url(self):
		return reverse('symptom:detail', kwargs={'slug': self.slug})

def create_symptomcode_usage_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.symptomcode,instance.routingdetail)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = SymptomCode_Usage.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return pre_save_assembly_usage_receiver(instance, new_slug=new_slug)
    return slug

def pre_save_symptomcode_usage_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_symptomcode_usage_slug(instance)

pre_save.connect(pre_save_symptomcode_usage_receiver, sender=SymptomCode_Usage)



from performing.models import Performing
from symptom.models import SymptomCode

class Symptom(models.Model):
	performing		= models.ForeignKey(Performing,
						related_name='symptoms',
						on_delete=models.CASCADE,)
	symptomcode		= models.ForeignKey(SymptomCode,
						related_name='symptoms',
						blank=True, null=True,
						on_delete=models.SET_NULL,)
	cnd				= models.BooleanField(verbose_name='Can Not Duplicate',default=False)
	note 			= models.TextField(max_length=255,blank=True, null=True)
	fixed 			= models.BooleanField(verbose_name='Is Fixed',default=False)
	fixed_date 		= models.DateTimeField(blank=True, null=True)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	def __str__(self):
		return ('%s on %s' % (self.symptomcode,self.performing))

	def get_absolute_url(self):
		return reverse('symptom:performing', kwargs={'pk': self.pk})