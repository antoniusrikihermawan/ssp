from django.urls import path
from profil import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('omah/',views.home),
    path('about/', views.about),
]
