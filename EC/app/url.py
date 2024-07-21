from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns =[
    path("",views.home ,name ="home"),
    path("About/",views.About ,name ="About"),
    path("Contact/",views.Contact ,name ="Contact"),
    path("Promotion/",views.Promotion ,name ="Promotion"),
    path("category/<slug:val>/",views.CategoryView.as_view(),name ="category"),
    path("category-title/<val>",views.CategoryView.as_view(),name ="category-title"),
    path("product-details/<int:pk>",views.ProductDetails.as_view(),name ="product-details"),
    path("accounts/profile/", views.profileView.as_view(),name="profile"),
    path("address/", views.address,name="address"),
    path("updateAddress/<int:pk>", views.updateaddress.as_view(),name="updateAddress"),

    #loging authentication
      path("registration/",views.CustomRegistrationView.as_view(),name ="customerregistration"),
      path("account/login/", auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name="Login"),
      path("passwordchange/", auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class = MyPasswordChangeForm, success_url='/passwordchangedone' ), name="passwordchange"),
      path("passwordchangedone/", auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html' ), name="passwordchangedone"),
      path("logout/", auth_view.LogoutView.as_view(next_page='Login'), name="logout"),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)