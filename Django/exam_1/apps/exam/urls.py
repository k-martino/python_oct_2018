from django.conf.urls import url

from . import views

urlpatterns = [
    # render routes
    url(r"^$", views.index, name="index"),
    url(r"books", views.home, name="home"),
    url(r"books/add", views.add_bk, name="add_bk"),
    url(r"books/(?P<book_id>\d+)", views.bk, name="view_bk"),
    url(r"users/(?P<user_id>\d+)", views.usr, name="view_usr"),
    # process routes
    url(r"register", views.register, name="reg"),
    url(r"login", views.login, name="login"),
    url(r"logout", views.logout, name="logout"),
    url(r"process", views.process_bk, name="process_bk"),
    url(r"process", views.process_rev, name="process_rev"),
    url(r"destroy", views.destroy, name="delete_rev"),
]
