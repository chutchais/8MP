from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from failure.models import Failure

admin.site.register(Failure)