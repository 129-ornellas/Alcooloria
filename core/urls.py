from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/cadastro$', views.cadastro),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),
    url(r'^api/add_todo$', views.add_todo),
    url(r'^api/list_todos$', views.list_todos),
    url(r'^api/metricas$', views.metricas),
    url(r'^api/calculo$', views.calculo),
    url(r'^api/cadastra_cerveja$', views.cadastra_cerveja),
]
