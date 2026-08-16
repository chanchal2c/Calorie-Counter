from django.contrib import admin
from CaloryCounterApp.models import *

# Register your models here.

admin.site.register([customUser, profileModel, consumedColorieModel])