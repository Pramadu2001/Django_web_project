from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm

urlpatterns =[
    path("",views.home ,name ="home"),
    path("About/",views.About ,name ="About"),
    path("Contact/",views.Contact ,name ="Contact"),
    path("Promotion/",views.Promotion ,name ="Promotion"),
    path("category/<slug:val>/",views.CategoryView.as_view(),name ="category"),
    path("category-title/<val>",views.CategoryView.as_view(),name ="category-title"),
    path("product-details/<int:pk>",views.ProductDetails.as_view(),name ="product-details"),

    #loging authentication
      path("registration/",views.CustomRegistrationView.as_view(),name ="customerregistration"),
      path("account/login/", auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name="Login")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)