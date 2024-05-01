from django.db import models
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
# Create your models here.


class ProblemPost(models.Model):
    # 题目作者 参数
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 题目标题 char
    name = models.CharField(max_length=100)

    # 题面 string
    description = models.TextField()

    # 题目分值 int
    score = models.IntegerField()

    # 测试点数 int
    test_point_num = models.IntegerField()

    # 每个测试点对应测试代码 JSON
    test_codes = models.JSONField()

    # 每个测试点对应测试用例 JSOn
    test_cases = models.JSONField()

    # 每个测试点对应预设结果 JSOn
    preset_results = models.JSONField()
    
    # 内部类 class Meta 用于给 model 定义元数据              
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        ordering = ('id',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.name 将题目标题返回
        return self.name


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