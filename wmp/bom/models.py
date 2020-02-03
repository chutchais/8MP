from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import RegexValidator




ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class Bom(models.Model):
	name 			= models.CharField(max_length=50,primary_key=True,
						validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Name does not allow special charecters',
										),
						])
	pn 				= models.CharField(verbose_name ='Part Number',max_length=50,blank=True, null=True,
						validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Part number does not allow special charecters',
										),
						])
	rev 			= models.CharField(verbose_name ='Revision',max_length=10,blank=True, null=True)
	title 			= models.CharField(max_length=100,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	description 	= models.TextField(blank=True, null=True)
	fg_pn 			= models.CharField(verbose_name ='Finish Goods Part Number',max_length=50,blank=True, null=True)
	fg_rev 			= models.CharField(verbose_name ='Finish Goods Revision',max_length=10,blank=True, null=True)
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)
	
	@property
	def items_count(self):
		# c = self.weight + self.runner
		return self.items.count()
	items_count.fget.short_description = "Total Items"
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('bom:detail', kwargs={'slug': self.slug})

	# def item_count(self):
	# 	return self.bom_detail_set.count()

def create_bom_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Bom.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_bom_slug(instance, new_slug=new_slug)
    return slug

def pre_save_bom_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_bom_slug(instance)

pre_save.connect(pre_save_bom_receiver, sender=Bom)




PART_TYPE_CHOICE = (
		('COMPONENT','Component'),
		('MODULE','Module with serial number'),
		('BUILD','Inernal Build with serial number')
	)

class Bom_Detail(models.Model):
	rd 				= models.CharField(verbose_name ='Ref Destinator',max_length=50,
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
	customer_pn 	= models.CharField(verbose_name ='Customer Part Number',max_length=50,blank=True, null=True)
	pn_type			= models.CharField(verbose_name ='Part Type',max_length=10,choices=PART_TYPE_CHOICE,default='COMPONENT')
	bom 			= models.ForeignKey(Bom,
								on_delete=models.CASCADE,
								related_name='items')
	title 			= models.CharField(max_length=100,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	description 	= models.TextField(max_length=255,blank=True, null=True)
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	critical 		= models.BooleanField(default=False)
	# alt_pn 			= models.IntegerField(default=0,verbose_name ='Alternative Part')
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)
	
	class Meta:
		unique_together = ('rd','pn','bom')

	def __str__(self):
		return ('%s : %s' % (self.rd,self.pn))

	def get_absolute_url(self):
		return reverse('bom:item-detail', kwargs={'slug': self.slug})

def create_bom_detail_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s-%s' % (instance.bom,instance.pn,instance.rd)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Bom_Detail.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return pre_save_bom_detail_receiver(instance, new_slug=new_slug)
    return slug

def pre_save_bom_detail_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_bom_detail_slug(instance)

pre_save.connect(pre_save_bom_detail_receiver, sender=Bom_Detail)



class Alternate_Part(models.Model):
	bom_detail 		= models.ForeignKey(Bom_Detail,
						on_delete=models.CASCADE,
						related_name='alternates')
	pn 				= models.CharField(verbose_name ='Part Number',max_length=50)
	customer_pn 	= models.CharField(max_length=50,blank=True, null=True)
	ordered 		= models.IntegerField(default=1)
	title 			= models.CharField(max_length=100,blank=True, null=True)
	description 	= models.TextField(max_length=255,blank=True, null=True)
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	def __str__(self):
		return ('%s : %s' % (self.bom_detail,self.pn))