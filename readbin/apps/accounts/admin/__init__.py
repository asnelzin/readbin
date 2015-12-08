from django.contrib import admin
from readbin.apps.accounts.admin.models import UserAdmin
from readbin.apps.accounts.models import User

admin.site.register(User, UserAdmin)
