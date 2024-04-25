
# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse
from .models import ProblemPost
# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
# 引入User模型
from django.contrib.auth.models import User
# 引入markdown模块
import markdown

# 视图函数
def problem_list(request):
    # 取出所有题目
    problems = ProblemPost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'problems': problems }
    # render函数：载入模板，并返回context对象
    return render(request, 'problem/list.html', context)

def problem_content(request, id):
    problem = ProblemPost.objects.get(id=id)
    context = {'problem':problem}
    print(id)
    problem.description = markdown.markdown(problem.description, 
                                            extensions=[
                                                # 包含 缩写、表格等常用扩展
                                                'markdown.extensions.extra',
                                                # 语法高亮扩展
                                                'markdown.extensions.codehilite',     
                                            ])
    return render(request, 'problem/content.html', context)

def my_custom_404_view(request, exception):
    # 重定向到主页的URL
    print('404')
    return render(request, '404.html')




