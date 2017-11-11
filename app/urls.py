from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    # url(r'^login/',views.login,name="login")
    url(r'^$', views.home, name="home"),
    url(r'^result', views.result, name='result'),
    #url(r'^login/', views.login, name="login"),
    #url(r'^user/', views.show_user, name="showuser"),
    #url(r'^forms/', views.show_form, name="showform"),
    #url(r'^form_page/', views.show_basic_form, name="showbasicform"),
    #url(r'register/', views.toRegister, name='register'),
]


#/(?P<pk>\d+)/$