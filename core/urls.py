from django.urls import path
from .views import index, contato, produto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
