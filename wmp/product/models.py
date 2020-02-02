from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from routing.models import Routing
from bom.models import Bom

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

# Todo , Dec 13,2019
# 1) Add Parent Product - to identify Semi sub-product or Finish goods product.
# 2) Change customer_pn and Rev to Finished goods and Rev

class Product(models.Model):
	name 				= models.CharField(max_length=50,primary_key=True,
							validators=[
									RegexValidator(
										regex='^[\w-]+$',
										message='Name does not allow special charecters',
									),
								])
	title 				= models.CharField(max_length=100,blank=True, null=True)
	pn  				= models.CharField(verbose_name='Part number',max_length=50,blank=True, null=True)
	rev  				= models.CharField(verbose_name='Revision number',max_length=50,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	routing 			= models.ForeignKey(Routing,
							on_delete=models.SET_NULL,blank=True, null=True,
							verbose_name='Routing Name',)
	regexp 				= models.CharField(verbose_name='RegExp Validation',
							max_length=100,blank=True, null=True,default='*')
	description 		= models.TextField(max_length=255,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	fg_pn		 		= models.CharField(verbose_name='Finish Goods Part number',max_length=50,blank=True, null=True)
	fg_rev		  		= models.CharField(verbose_name='Finish Goods Revision number',max_length=50,blank=True, null=True)
	parent 				= models.ForeignKey('self', null=True,blank = True,
							on_delete=models.SET_NULL,
							related_name='childs')
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,blank=True,null=True)
	bom 				= models.ForeignKey(Bom,
							on_delete=models.SET_NULL,blank=True, null=True,
							verbose_name='Bom Name',)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product:detail', kwargs={'slug': self.slug})

def create_product_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_product_slug(instance, new_slug=new_slug)
    return slug

def pre_save_product_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_product_slug(instance)

pre_save.connect(pre_save_product_receiver, sender=Product)