from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings
from django.core.validators import RegexValidator


from snippet.models import Snippet

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )



class Item(models.Model):
	TEXTBOX ='TEXT'
	LIST ='LIST'
	RADIO ='RADIO'
	OPTION = 'OPTION'
	SCRIPT ='SCRIPT'
	PARAM_TYPE_CHOICES = (
	        (TEXTBOX, 'Text Box'),
	        (LIST, 'List Box'),
	        (RADIO, 'Radio Box'),
	        (OPTION, 'Option Box'),
	        (SCRIPT, 'Script Data'),
	    )
	name 				= models.CharField(max_length=50,
							validators=[
									RegexValidator(
										regex='^[\w-]+$',
										message='Name does not allow special charecters',
									),
								])
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	# product 			= models.ForeignKey(Product,
	# 						on_delete=models.SET_NULL,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	help_text 			= models.CharField(verbose_name='Help Text',max_length=100,blank=True, null=True)
	input_type 			= models.CharField(verbose_name='Input Type',max_length=10,choices=PARAM_TYPE_CHOICES,default=TEXTBOX)
	default_value 		= models.CharField(verbose_name='Default Value',max_length=100,blank=True, null=True)
	regexp 				= models.CharField(verbose_name='RegExp Validation',max_length=100,blank=True, null=True,default='\w')
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,blank=True,null=True)
	snippet 			= models.ForeignKey(Snippet, 
							on_delete=models.SET_NULL,verbose_name='Snippet Code',
							blank=True, null=True,
							related_name='items')
	expected_return 	= models.CharField(verbose_name='Expected Return',
							default='TRUE',max_length=100,blank=True, null=True)
	required 			= models.BooleanField(default=False)

	# @property
	def has_validation_code(self):
		return True if (self.snippet) else False
	has_validation_code.boolean =True
	has_validation_code.short_description = 'Has Validation'

	@property
	def item_count(self):
		# c = self.weight + self.runner
		return self.lists.count()
	item_count.fget.short_description = "Items count"

	def __str__(self):
		return ('%s : %s' % (self.name,self.input_type))

	def get_absolute_url(self):
		return reverse('item:detail', kwargs={'slug': self.slug})

def create_item_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.name,instance.input_type)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Item.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_item_slug(instance, new_slug=new_slug)
    return slug

def pre_save_item_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_item_slug(instance)

pre_save.connect(pre_save_item_receiver, sender=Item)



class ItemList(models.Model):
	name 			= models.CharField(max_length=50,
							validators=[
									RegexValidator(
										regex='^[\w-]+$',
										message='Name does not allow special charecters',
									),
								])
	value 			= models.CharField(max_length=50)
	title 			= models.CharField(max_length=100,blank=True, null=True)
	description 	= models.TextField(max_length=255,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	default 		= models.BooleanField(default=False)
	item 			= models.ForeignKey(Item,
						on_delete=models.CASCADE,
						related_name='lists')
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	ordered 		= models.IntegerField(default=1)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	class Meta:
		unique_together = ('name','item')

	def __str__(self):
		return ('%s of %s' % (self.name,self.item))

	def get_absolute_url(self):
		return reverse('item-list:detail', kwargs={'slug': self.slug})



def create_itemlist_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.name,instance.item )
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = ItemList.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_itemlist_slug(instance, new_slug=new_slug)
    return slug

def pre_save_itemlist_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_itemlist_slug(instance)

pre_save.connect(pre_save_itemlist_receiver, sender=ItemList)