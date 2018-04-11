# coding: utf-8
from rest_framework import serializers

from sleep.functions import code_authorize, get_user_info
from sleep.models import UserInfo, Question


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'university', 'major', 'sleep_time', 'nickname', 'head_img']
        read_only_fields = ['nickname', 'head_img']

    def create(self, validated_data):
        code = self.initial_data.get('code')
        if not code:
            raise serializers.ValidationError('请传入CODE值')
        data = self.check_account(code)
        validated_data.update(data)
        instance = super().create(validated_data)
        return instance

    def check_account(self, code):
        res = code_authorize(code)
        user_info = get_user_info(access_token=res['access_token'], openid=res['openid'])
        if user_info.get('errorcode', 0) != 0:
            raise serializers.ValidationError('user info 获取错误')
        data = {'unionid': user_info.get('unionid'), 'openid': res['openid'], 'head_img': user_info['headimgurl'],
                'nickname': user_info['nickname'], }
        return data


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'user', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6']

    def create(self, validated_data):
        if Question.objects.filter(user=validated_data['user']).exists():
            raise serializers.ValidationError('该用户已经提交答案')
        instance = super().create(validated_data)
        return instance
