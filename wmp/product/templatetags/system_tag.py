from django import template
from datetime import timedelta
from django.db.models import Avg,Sum
import datetime

register = template.Library()

import os

@register.simple_tag
def multiply_by_two(value):
    return float(value) * 2.0
    
@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def percent(x,total):
	if x:
		return (x/total)*100
	else:
		return 0