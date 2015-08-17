from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView

urlpatterns = [
url(r'', TemplateView.as_view(template_name="pyladies/index.html"), name='template_test'),
]
