from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

from django.urls import reverse
from django.conf import settings


ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class DefectCode(models.Model):
	name 				= models.CharField(max_length=50,primary_key=True)
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('defectcode:detail', kwargs={'slug': self.slug})

def create_defectcode_slug(instance, new_slug=None):
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = DefectCode.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_defect_slug(instance, new_slug=new_slug)
    return slug

def pre_save_defectcode_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_defectcode_slug(instance)

pre_save.connect(pre_save_defectcode_receiver, sender=DefectCode)




from symptom.models import Symptom

class Defect(models.Model):
	symptom			= models.ForeignKey(Symptom,
						related_name='defects',
						on_delete=models.CASCADE,)
	defectcode		= models.ForeignKey(DefectCode,
						related_name='defects',
						on_delete=models.CASCADE,)
	ndf				= models.BooleanField(verbose_name='No Defect Found',default=False)
	note 			= models.TextField(max_length=255,blank=True, null=True)
	created_date 	= models.DateTimeField(auto_now_add=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.defectcode))

	def get_absolute_url(self):
		return reverse('defect:defect', kwargs={'pk': self.pk})