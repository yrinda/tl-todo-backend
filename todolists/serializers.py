from rest_framework import serializers
from todolists.models import Todolist


class TodolistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, min_length=1, max_length=30)
    created = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        return Todolist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        TASK: 今の仕様ではlistは更新されないので、未実装
        後で実装するかも。
        @see http://sandmark.hateblo.jp/entry/2017/09/30/160945
        """
        pass
