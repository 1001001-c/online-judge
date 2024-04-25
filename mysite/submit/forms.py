# 引入表单类
from django import forms
from .models import SubmitPost

# 提交代码的表单

class SubmitPostForm(forms.ModelForm):
    class Meta:
        model = SubmitPost
        fields = ('submitCode',)