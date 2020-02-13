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

class Routing(models.Model):
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
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,blank=True,null=True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('routing:detail', kwargs={'slug': self.slug})

	@property
	def operations_count(self):
		# c = self.weight + self.runner
		return self.details.count()
	operations_count.fget.short_description = "Total Operations"

def create_routing_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Routing.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_routing_slug(instance, new_slug=new_slug)
    return slug

def pre_save_routing_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routing_slug(instance)

pre_save.connect(pre_save_routing_receiver, sender=Routing)


# Routing Next
from snippet.models import Snippet

class RoutingDetailNext(models.Model):
	name 				= models.CharField(max_length=100,
									validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Name does not allow special charecters',
										),
									])
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	snippet 			= models.ForeignKey(
					        Snippet,
					        on_delete=models.CASCADE,
					        related_name='routing_next',blank=True, null=True
					    )
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.name))

	def get_absolute_url(self):
		return reverse('routing:next-detail', kwargs={'slug': self.slug})

def create_routingnext_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = RoutingDetailNext.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_routingnext_slug(instance, new_slug=new_slug)
    return slug


def pre_save_routingnext_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routingnext_slug(instance)

pre_save.connect(pre_save_routingnext_receiver, sender=RoutingDetailNext)


# Routing Accept
class RoutingDetailAccept(models.Model):
	name 				= models.CharField(max_length=100,
									validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Name does not allow special charecters',
										),
									])
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	snippet 			= models.ForeignKey(
							Snippet,
							on_delete=models.CASCADE,
							related_name='routing_accept',blank=True, null=True
						)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.name))

	def get_absolute_url(self):
		return reverse('routing:accept-detail', kwargs={'slug': self.slug})

def create_routingaccept_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = RoutingDetailAccept.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_routingaccept_slug(instance, new_slug=new_slug)
    return slug

def pre_save_routingaccept_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routingaccept_slug(instance)

pre_save.connect(pre_save_routingaccept_receiver, sender=RoutingDetailAccept)


# Reject
class RoutingDetailReject(models.Model):
	name 			= models.CharField(max_length=100,
									validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Name does not allow special charecters',
										),
									])
	title 			= models.CharField(max_length=100,blank=True, null=True)
	description 	= models.TextField(max_length=255,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	snippet 		= models.ForeignKey(
							Snippet,
							on_delete=models.CASCADE,
							related_name='routing_reject',blank=True, null=True
						)
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

	def get_absolute_url(self):
		return reverse('routing:reject-detail', kwargs={'slug': self.slug})

def create_routingreject_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = RoutingDetailReject.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_routingreject_slug(instance, new_slug=new_slug)
    return slug

def pre_save_routingreject_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routingreject_slug(instance)

pre_save.connect(pre_save_routingreject_receiver, sender=RoutingDetailReject)


# Routing Details
from operation.models import Operation
from parameter.models import Parameter
# from routing_accept.models import RoutingAccept
# from routing_reject.models import RoutingReject
# from routing.models import RoutingNext

class RoutingDetail(models.Model):
	FIRST='F'
	LAST='L'
	NORMAL = 'N'
	OPERATION_POS_CHOICES = (
			(FIRST, 'First Operation'),
			(LAST, 'Last Operation'),
			(NORMAL, 'Normal'),
		)
	operation 			= models.ForeignKey(Operation,
								on_delete=models.CASCADE,
								blank=True, null=True,
								related_name = 'routings')
	routing 			= models.ForeignKey(Routing,
								on_delete=models.CASCADE,
								related_name = 'details')
	title 				= models.CharField(max_length=100,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	position 			= models.CharField(max_length=1,choices=OPERATION_POS_CHOICES,default=NORMAL)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	next_pass 			= models.ForeignKey(Operation,
								related_name='nextpasses',
								on_delete=models.SET_NULL,blank=True, null=True)
	next_fail 			= models.ForeignKey(Operation,
								related_name='nextfails',
								on_delete=models.SET_NULL,blank=True, null=True)
	parameter 			= models.ManyToManyField(Parameter, through='RoutingDetailParameterSet')
	accept_code 		= models.ManyToManyField(RoutingDetailAccept, through='RoutingDetailAcceptSet')
	reject_code 		= models.ManyToManyField(RoutingDetailReject, through='RoutingDetailRejectSet')
	next_code 			= models.ManyToManyField(RoutingDetailNext, through='RoutingDetailNextSet')
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.SET_NULL,
								blank=True,null=True)
	class Meta:
    		unique_together = ['routing', 'operation']
	
	def __str__(self):
		return ('%s on %s' % (self.operation,self.routing))

	def get_absolute_url(self):
		return reverse('routing:operation-detail', kwargs={'slug': self.slug})

def create_routingdetail_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.operation,instance.routing)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = RoutingDetail.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_routingdetail_slug(instance, new_slug=new_slug)
    return slug

def pre_save_routingdetail_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routingdetail_slug(instance)

pre_save.connect(pre_save_routingdetail_receiver, sender=RoutingDetail)


class RoutingDetailParameterSet(models.Model):
	routingdetail 			= models.ForeignKey('RoutingDetail', 
								on_delete=models.CASCADE,
								related_name ='parameters')
	parameter 				= models.ForeignKey(Parameter, on_delete=models.CASCADE)
	ordered 				= models.IntegerField(default=1)
	required 				= models.BooleanField(default=False)
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.SET_NULL,
								blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.parameter,self.routingdetail))


class RoutingDetailAcceptSet(models.Model):
	routingdetail 			= models.ForeignKey('RoutingDetail', 
								on_delete=models.CASCADE,
								related_name ='accepts')
	routingaccept 			= models.ForeignKey(RoutingDetailAccept, on_delete=models.CASCADE)
	ordered 				= models.IntegerField(default=1)
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.SET_NULL,
								blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.routingaccept,self.routingdetail))


class RoutingDetailRejectSet(models.Model):
	routingdetail 			= models.ForeignKey('RoutingDetail', 
											on_delete=models.CASCADE,
											related_name ='rejects')
	routingreject 			= models.ForeignKey(RoutingDetailReject, on_delete=models.CASCADE)
	ordered 				= models.IntegerField(default=1)
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
									on_delete=models.SET_NULL,
									blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.routingreject,self.routingdetail))


class RoutingDetailNextSet(models.Model):
	routingdetail 			= models.ForeignKey('RoutingDetail',
									related_name='nexts',
									on_delete=models.CASCADE)
	routingnext 			= models.ForeignKey(RoutingDetailNext, 
									related_name='nexts',
									on_delete=models.CASCADE)
	title 					= models.CharField(max_length=100,blank=True, null=True)
	ordered 				= models.IntegerField(default=1)
	operation 				= models.CharField(max_length=100,blank=True, null=True)# models.ForeignKey(Operation, related_name='routingdetailsets')
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
									on_delete=models.SET_NULL,
									blank=True,null=True)
	
	def __str__(self):
		return ('%s of %s' % (self.routingnext,self.routingdetail))


# Routing Hook
EVENT_CHOICES = (
        ('PRE', 'Pre-check'), #For Button at the beginning of Click event
        ('POST', 'Post-check'), #For Button at the end of Click event
        ('CLICK','Click-on'), #For Option,Radio and Combo list after Click or Selected event
        ('VALIDATE','Validate') #for Text lost focus event (once Failed , keep focus)
    )


class RoutingDetailHook(models.Model):
	name 			= models.CharField(max_length=100,
									validators=[
										RegexValidator(
											regex='^[\w-]+$',
											message='Name does not allow special charecters',
										),
									])#Local object name
	title 			= models.CharField(max_length=100,blank=True, null=True)
	description 	= models.TextField(max_length=255,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	ordered 		= models.IntegerField(default=1)
	event			= models.CharField(max_length=10,choices=EVENT_CHOICES,
						default='',blank=True, null=True)
	routing_detail	= models.ForeignKey(
					        RoutingDetail,
					        on_delete=models.CASCADE,
					        blank=True, null=True,
							related_name='hooks'
					    )
	snippet 		= models.ForeignKey(
					        Snippet,
					        on_delete=models.CASCADE,
					        blank=True, null=True,
							related_name='routing_hook'
					    )
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

	def get_absolute_url(self):
		return reverse('routing:hook-detail', kwargs={'slug': self.slug})

def create_hook_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s-%s' % (instance.name,instance.event,instance.routing_detail)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = RoutingDetailHook.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_hook_slug(instance, new_slug=new_slug)
    return slug

def pre_save_hook_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_hook_slug(instance)

pre_save.connect(pre_save_hook_receiver, sender=RoutingDetailHook)


class RoutingDetailOperationChoice(models.Model):
	ordered 				= models.IntegerField(default=1)
	routingdetail 			= models.ForeignKey('RoutingDetail',
									related_name='choices',
									on_delete=models.CASCADE)
	title 					= models.CharField(max_length=100,blank=True, null=True)
	operation 				= models.ForeignKey(Operation, on_delete=models.CASCADE,
									related_name='choices')
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
									on_delete=models.SET_NULL,
									blank=True,null=True)
	
	def __str__(self):
		return ('%s of %s' % (self.operation,self.routingdetail))

	# def get_absolute_url(self):
	# 	return reverse('routing:choice-detail', kwargs={'id': self.id})