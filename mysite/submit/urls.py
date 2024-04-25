# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'submit'

urlpatterns = [
    # 目前还没有urls
    path('code_submit/', views.code_submit, name='code_submit'),
    path('consequnce/', views.consequnce, name='consequnce'),
]