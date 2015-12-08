from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from forms import UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password', 'token_key')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups')}),
    )