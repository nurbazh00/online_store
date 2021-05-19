from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'phone_number',
                    'email', 'get_avatar'
    )

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src={obj.avatar.url} width="100" />'
            )

        return '-'

    get_avatar.short_description = 'Фото'