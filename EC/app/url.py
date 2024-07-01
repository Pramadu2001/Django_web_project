from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("",views.home),
    path("category/<slug:val>/",views.CategoryView.as_view(),name ="category"),
     path("product-details/<int:pk>",views.ProductDetails.as_view(),name ="product-details"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)