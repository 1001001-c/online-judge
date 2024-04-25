from django.db import models
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from problem.models import ProblemPost

class SubmitPost(models.Model):
    # 题目提交者 参数
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    # 题目
    problemId = models.CharField(max_length=100)
    # 提交代码
    submitCode = models.TextField()
    # 得分
    userScore = models.IntegerField()
    # 内存花费
    memoryCost = models.FloatField()
    # 运行时间
    runtime = models.FloatField()
    # 重复率
    repeatRatio = models.FloatField()

    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        ordering = ('id',)
        
    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self. 将题目标题
        return self.problemId