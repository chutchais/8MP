from django import template
from datetime import timedelta
from django.db.models import Count,Sum,Value, When,Case,IntegerField,CharField
import datetime

register = template.Library()

from serialnumber.models import SerialNumber

import os

# @register.assignment_tag
@register.simple_tag
def workorder_wip(obj):
	# print (obj.strip())
	sns = obj.serialnumber_set.all()
	return sns.values('current_operation').annotate(number=Count('number'))

@register.simple_tag
def product_wip(obj):
	# print (obj.strip())
	sns = SerialNumber.objects.filter(workorder__product = obj )
	return sns.values('current_operation').annotate(number=Count('number'))

# @register.simple_tag
# def get_operation(name):
# 	# print (obj.strip())
# 	sns = obj.serialnumber_set.all()
# 	return sns.values('current_operation').annotate(number=Count('number'))