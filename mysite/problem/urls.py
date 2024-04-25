# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'problem'

urlpatterns = [
    # 目前还没有urls
    path('problem_list/', views.problem_list, name='problem_list'),
    path('content/<int:id>/', views.problem_content, name='problem_content'),
]