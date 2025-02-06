from django.contrib import admin
# from . import models
from .models import Tips
from .models import Greeting


# Register your models here.
admin.site.register(Tips)
admin.site.register(Greeting)
