# coding: utf-8

from rest_framework import mixins, viewsets

from sleep.models import UserInfo, Question
from sleep.serializers import UserInfoSerializer, QuestionSerializer


class UserInfoViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class QuestionViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
