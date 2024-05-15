from django.contrib import admin

from fenix_store.models import RegisterUserModel


# Register your models here.
@admin.register(RegisterUserModel)
class RegisterUserModelAdmin(admin.ModelAdmin):
    pass
