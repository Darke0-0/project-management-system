"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

from channels.auth import AuthMiddlewareStack
from chat import routing
from channels.routing import ProtocolTypeRouter, URLRouter
 
from daphne import ASGItoWSGIAdapter
application = ASGItoWSGIAdapter(get_asgi_application())

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
