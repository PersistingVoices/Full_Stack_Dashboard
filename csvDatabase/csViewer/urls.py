from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.csView, name='csView'),
	# url(r'^$', Templates.csViewer.first, name='first'),
	url(r'^$', views.index, name='index'),
	url(r'dashboard/$', views.dashboard, name='dashboard'),
	url(r'index2/$', views.index2, name='index2')
	]