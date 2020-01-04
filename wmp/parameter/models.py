from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.core.validators import RegexValidator

from django.conf import settings


from item.models import Item

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class Parameter(models.Model):
	name 			= models.CharField(max_length=50,primary_key=True,
						validators=[
									RegexValidator(
										regex='^[\w-]+$',
										message='Name does not allow special charecters',
									),
								])
	title 			= models.CharField(max_length=100,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	description 	= models.TextField(max_length=255,blank=True, null=True)
	items 			= models.ManyToManyField(Item, through='ParameterDetail')
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.name))

	def item_count(self):
		return self.items.count()

	def get_absolute_url(self):
		return reverse('parameter:detail', kwargs={'slug': self.slug})

def create_parameter_slug(instance, new_slug=None):
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Parameter.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_parameter_slug(instance, new_slug=new_slug)
    return slug

def pre_save_parameter_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_parameter_slug(instance)

pre_save.connect(pre_save_parameter_receiver, sender=Parameter)


class ParameterDetail(models.Model):
	parameter 			= models.ForeignKey('Parameter',
							related_name='details', 
							on_delete=models.CASCADE)
	item 				= models.ForeignKey(Item, 
							related_name='parameters',
							on_delete=models.CASCADE)
	ordered 			= models.IntegerField(default=1)
	required 			= models.BooleanField(default=False)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.item,self.parameter))

	# def get_absolute_url(self):
	# 	return reverse('parameter:item', kwargs={'pk': self.id})

	class Meta:
		ordering = ['ordered',]