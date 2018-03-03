from django.conf.urls import include, url
from .views import YoMamaBotView
urlpatterns = [


url(r'^7e9d2ac805daafc3b898090d24d7870c9e44b3a022ff8e494a/?$', YoMamaBotView.as_view())
]