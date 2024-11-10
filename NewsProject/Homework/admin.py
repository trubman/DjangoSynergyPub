from django.contrib import admin
from .models import Human, Profession
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class HumanAdminForm(forms.ModelForm):
    biography = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Human
        fields = '__all__'


class HumanAdmin(admin.ModelAdmin):
    form = HumanAdminForm
    list_display = (
        'id',
        'profession',
        'first_name',
        'middle_name',
        'last_name',
        'biography',
        'date_of_birth',
        'created_at',
        'updated_at',
        'passport_photo',
        'is_adult',
    )
    list_display_links = (
        'id',
        'first_name',
    )
    search_fields = (
        'first_name',
        'middle_name',
        'last_name',
        'biography',
    )
    list_filter = ('is_adult', 'id',)
    list_editable = ('is_adult', 'profession',)

class ProfessionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    list_display_links = (
        'id',
        'title',
    )
    search_fields = (
        'title',
    )

admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)

