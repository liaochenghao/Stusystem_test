# coding: utf-8
from django.db import models


class UserInfo(models.Model):
    university = models.CharField('大学', max_length=60, null=True)
    major = models.CharField('专业', max_length=60, null=True)
    sleep_time = models.TimeField('睡觉时间', null=True)
    head_img = models.CharField('微信头像url', max_length=255, null=True)
    nickname = models.CharField('微信昵称', max_length=30, null=True)
    unionid = models.CharField('微信服务号用户unionid', max_length=60, null=True, unique=True)
    openid = models.CharField('微信openid', max_length=60, null=True, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.university

    class Meta:
        db_table = 'user_info'


class Questions(models.Model):
    ANSWER_CHOICES = (
        (1, 'A'), (2, 'B'), (3, 'C'),
    )
    user = models.ForeignKey(UserInfo)
    create_time = models.DateTimeField(auto_now_add=True)
    question1 = models.CharField(choices=ANSWER_CHOICES, max_length=30)
    question2 = models.CharField(choices=ANSWER_CHOICES, max_length=30)
    question3 = models.CharField(choices=ANSWER_CHOICES, max_length=30)
    question4 = models.CharField(choices=ANSWER_CHOICES, max_length=30)
    question5 = models.CharField(choices=ANSWER_CHOICES, max_length=30)
    question6 = models.CharField(choices=ANSWER_CHOICES, max_length=30)

    class Meta:
        db_table = 'questions'
