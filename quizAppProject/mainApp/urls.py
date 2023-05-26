from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home' ),
    path('accounts/register', views.register, name='register' ),
    path('all-categories', views.all_categories, name='all_categories' ),
    path('cat-questions/<int:cat_id>', views.cat_questions, name='cat_questions' ),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)