# 导入 HttpResponse 模块
from django.http import HttpResponse
# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
# 引入刚才定义的SubmitPostForm表单类
from .forms import SubmitPostForm
# 引入User模型
from django.contrib.auth.models import User
# 引入markdown模块
import markdown
from problem.models import ProblemPost

from django.urls import reverse
from .models import SubmitPost

# 提交代码的视图
def code_submit(request):
    # 判断用户是否提交数据
    print(request.method)
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        submit_post_form = SubmitPostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if submit_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_submit = submit_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            new_submit.submitCode = markdown.markdown(new_submit.submitCode, 
                                            extensions=[
                                                # 包含 缩写、表格等常用扩展
                                                'markdown.extensions.extra',
                                                # 语法高亮扩展
                                                'markdown.extensions.codehilite',     
                                            ])
            # 此时请重新创建用户，并传入此用户的id
            new_submit.submitter = User.objects.get(id=1)
            new_submit.problemId = ProblemPost.objects.get(id=1)
            send_judgeProgram(new_submit)
            new_submit = subscribe_consequnce(new_submit)
            # 将新文章保存到数据库中
            new_submit.save()
            # 完成后返回到文章列表
            context = {'consequnce' : new_submit}
            return redirect(reverse('submit:consequnce') + '?consequnce=' + str(new_submit.id))
        # 如果数据不合法，返回错误信息
        else:
            print(submit_post_form.errors)
            return HttpResponse(submit_post_form.errors)
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        submit_post_form = SubmitPostForm()
        # 赋值上下文
        context = { 'submit_post_form': submit_post_form }
        # 返回模板
        return render(request, 'submit/submit.html', context)
    

def send_judgeProgram(new_submit):
    # TODO
    return False

def subscribe_consequnce(new_submit):
    # TODO
    new_submit.userScore = 5
    new_submit.memoryCost = 256
    new_submit.runtime = 100
    new_submit.repeatRatio = 60
    return new_submit


def consequnce(request):
    # 获取 URL 参数中的 consequnce
    consequnce_id = request.GET.get('consequnce')
    
    # 根据 consequnce_id 获取相应的 Consequnce 对象
    consequnce = SubmitPost.objects.get(id=consequnce_id)
    
    # 在模板中渲染 Consequnce 对象
    return render(request, 'submit/consequnce.html', {'consequnce': consequnce})
