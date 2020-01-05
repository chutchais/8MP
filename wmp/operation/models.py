from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.urls import reverse
from django.conf import settings

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

OPERATION_TYPE_CHOICE =(
		('ASSEMBLY'			, 'Assembly'),
		('REGISTRATION' 	, 'Registration'),
		('INSPECTION' 		, 'Inspection'),
		('TROUBLESHOOTING' 	, 'Troubleshooting'),
		('REPAIR'			, 'Repairation'),
		('SHIPMENT' 		, 'Shipment'),
		('PACKING'			, 'Packing'),
		('END'				, 'Ending Process')
	)

class Operation(models.Model):
	name 				= models.CharField(max_length=50,primary_key=True,
									validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Name does not allow special charecters',
										),
									])
	operation_type		= models.CharField(max_length=20,choices=OPERATION_TYPE_CHOICE,
							default='INSPECTION')
	title 				= models.CharField(max_length=100,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	customer_name 		= models.CharField(max_length=50,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True, related_name='owner')
	
	def __str__(self):
		return ('%s' % (self.name))

	def get_absolute_url(self):
		return reverse('operation:detail', kwargs={'slug': self.slug})

	@property
	def wip(self):
		return self.wips.count()


def create_operation_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Operation.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_operation_slug(instance, new_slug=new_slug)
    return slug

def pre_save_operation_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_operation_slug(instance)

pre_save.connect(pre_save_operation_receiver, sender=Operation)