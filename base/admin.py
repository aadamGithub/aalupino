from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext_lazy as _
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Product, Article

admin.site.register(Product)
admin.site.register(Article)

class UserAdmin(AuthUserAdmin):
  fieldsets = (
    (None, {"fields": ("email", "password",)}),
    (
      _("Personal info"),
      {
        "fields": (
          "first_name",
          "last_name",
          "shopping_preference",
          "date_of_birth",
        )
      }
    ),
    (
      _("Permissions"),
      {
        "fields": (
          "is_active",
          "is_staff",
          "is_superuser",
          "groups",
          "user_permissions",
        ),
      },
    ),
    (_("Important dates"), {"fields": ("last_login", "date_joined")}),
  )
  add_fieldsets = (
    (
        None,
        {
          "classes": ("wide",),
          "fields": ("email", "password1", "password2"),

        }
    )
  )

  list_display = ("email", "first_name", "last_name", "is_staff")
  search_fields = ("first_name", "last_name", "email")
  ordering = ("email",)

admin.site.register(User, UserAdmin)