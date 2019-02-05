from django.conf.urls import url, include
from API import views

# thanks to
# https://stackoverflow.com/questions/43304923/typeerror-at-admin-set-object-is-not-reversible-and-argument-to-reverse-m?noredirect=1&lq=1
urlpatterns = [
    url(r'^projects$', views.all_projects, name='All Projects'),
    url(r'^project$', views.project, name='One Project'),
]
