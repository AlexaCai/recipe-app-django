from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from recipes.models import Recipe


User = get_user_model()

class UserAdmin(BaseUserAdmin):
    search_fields = ['email']
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['id', 'full_name', 'email', 'admin']
    list_filter = ['admin', 'staff', '_is_active']
    fieldsets = (
        (None, {'fields': ('id', 'full_name', 'email', 'password')}),
        # ('User info', {'fields': ('full_name',)}),
        ('Favorite recipes', {'fields': ('favorite_recipes', 'user_created_recipes')}),
        ('Permissions', {'fields': ('admin','staff','_is_active')}),
    )

    readonly_fields = ['id', 'full_name', 'email', 'password']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_2')}
        ),
    )
    search_fields = ['email', 'full_name',]
    ordering = ['email']
    filter_horizontal = ()

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'user_created_recipes':
            kwargs['queryset'] = Recipe.objects.filter(user=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)