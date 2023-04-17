from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Path
from ninja import Router

from workflow_builder.auth.security import JWTUserAuth


router = Router(tags=["{{camel_case_app_name}}"], auth=[JWTUserAuth()])
