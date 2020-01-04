from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from parametric.models import Parametric

admin.site.register(Parametric)