import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()

from chat import routing  # noqa isort:skip
 
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa isort:skip
 
 
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(routing.websocket_urlpatterns),
    }
)