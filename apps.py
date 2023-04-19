from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class {{camel_case_app_name}}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "workflow_builder.{{app_name}}"
