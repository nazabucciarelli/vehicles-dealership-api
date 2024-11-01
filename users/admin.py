from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'id_number', 'gender', 'city')
    search_fields = ('user__username', 'address', 'phone_number', 'id_number')
    list_filter = ('gender', 'city')
    ordering = ('user',)

    def __str__(self):
        return self.user.username
