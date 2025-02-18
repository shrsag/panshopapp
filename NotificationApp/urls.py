from django.urls import path
from .views import home, open_notification, close_notification, add_email_page, add_email_database,login_view,logout_view,about

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name='about'),  # About page
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('open/', open_notification, name="open_notification"),
    path('close/', close_notification, name="close_notification"),
    path('add_email/', add_email_page, name="add_email_page"),  # Page to enter email
    path('add_email_submit/', add_email_database, name="add_email_database"),  # Backend function to store email
]


