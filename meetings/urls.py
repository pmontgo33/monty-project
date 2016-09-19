#   meetings/urls.py
#   Patrick W. Montgomery
#   created: 9/19/2016

#   import statements
from django.conf.urls import url
from . import views


urlpatterns = [
    
    #   url for the meetings index or home page
    url(r'^$', views.meetings_index, name="meetings_index")
    
    #   Future urls for creating, viewing, editing individual minutes
    
    ]