from django.contrib import admin
from .models import Event


def update_publish_status(modeladmin, request, queryset, status):
    queryset.update(is_published=status)


def publish_selected_events(modeladmin, request, queryset):
    update_publish_status(modeladmin, request, queryset, True)


def unpublish_selected_events(modeladmin, request, queryset):
    update_publish_status(modeladmin, request, queryset, False)


publish_selected_events.short_description = "Опубликовать выбранные события"
unpublish_selected_events.short_description = "Отменить публикацию выбранных событий"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'title', 'publish_at', 'removal_at', 'is_published')
    actions = (publish_selected_events, unpublish_selected_events)