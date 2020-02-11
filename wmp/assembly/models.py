from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import RegexValidator

# Create your models here.
from product.models import Product
from routing.models import RoutingDetail

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class Assembly(models.Model):
	name 			= models.CharField(max_length=50,primary_key=True,
						validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Name does not allow special charecters',
										),
						])
	title 			= models.CharField(max_length=100,blank=True, null=True)
	product 		= models.ForeignKey(Product,
							on_delete=models.CASCADE,
							related_name='assemblys')
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	description 	= models.TextField(blank=True, null=True)
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('assembly:detail', kwargs={'slug': self.slug})

	@property
	def items_count(self):
		# c = self.weight + self.runner
		return self.assembly_details.count()
	items_count.fget.short_description = "Total Items"
	# def item_count(self):
	# 	return self.bom_detail_set.count()

def create_assembly_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Assembly.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_assembly_slug(instance, new_slug=new_slug)
    return slug

def pre_save_assembly_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_assembly_slug(instance)

pre_save.connect(pre_save_assembly_receiver, sender=Assembly)



from bom.models import Bom_Detail

class Assembly_Detail(models.Model):
	ordered 			= models.IntegerField(default=1)
	assembly 			= models.ForeignKey(Assembly,
								on_delete=models.CASCADE,
								related_name='assembly_details')
	part 				= models.ForeignKey(Bom_Detail,
								on_delete=models.CASCADE,
								related_name='assembly_details')
	title 				= models.CharField(max_length=100,blank=True, null=True)
	datecode_regexp 	= models.CharField(max_length=50,blank=True, null=True,
								verbose_name='Datecode RegExp Validation')
	lotcode_regexp 		= models.CharField(max_length=50,blank=True, null=True,
								verbose_name='Lotcode RegExp Validation')
	supplycode_regexp 	= models.CharField(max_length=50,blank=True, null=True,
								verbose_name='Supplycode RegExp Validation')
	sn_regexp 			= models.CharField(max_length=50,blank=True, null=True,
								verbose_name='Serial number RegExp Validation')
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	critical 			= models.BooleanField(default=False)
	msd_control			= models.BooleanField(default=False,verbose_name='Enable MSD Control')
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)
	
	class Meta:
		unique_together = ('assembly','part')
		ordering 		= ['ordered',]

	def __str__(self):
		return ('%s' % (self.part))

	def get_absolute_url(self):
		return reverse('assembly:assembly-detail', kwargs={'slug': self.slug})

def create_assembly_detail_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.assembly,instance.part)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Assembly_Detail.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return pre_save_assembly_detail_receiver(instance, new_slug=new_slug)
    return slug

def pre_save_assembly_detail_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_assembly_detail_slug(instance)

pre_save.connect(pre_save_assembly_detail_receiver, sender=Assembly_Detail)



class Assembly_Usage(models.Model):
	routingdetail 			= models.ForeignKey(RoutingDetail, 
								on_delete=models.CASCADE,
								related_name ='assembly_usages')
	assembly 				= models.ForeignKey(Assembly, 
								on_delete=models.CASCADE,
								related_name ='assembly_usages')
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
		return ('%s on %s' % (self.assembly,self.routingdetail))

	def get_absolute_url(self):
		return reverse('assembly_usage:detail', kwargs={'slug': self.slug})

def create_assembly_usage_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.assembly,instance.routingdetail)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Assembly_Usage.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return pre_save_assembly_usage_receiver(instance, new_slug=new_slug)
    return slug

def pre_save_assembly_usage_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_assembly_usage_slug(instance)

pre_save.connect(pre_save_assembly_usage_receiver, sender=Assembly_Usage)