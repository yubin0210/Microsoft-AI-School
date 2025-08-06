from rest_framework import serializers

from news.models.news import NewsItem

class NewsSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S", read_only=True)

    current_date = serializers.SerializerMethodField()
    channel_name = serializers.SerializerMethodField()

    class Meta:
        model = NewsItem
        fields = [
            'id',
            'title',
            'pub_date',
            'current_date',
            'channel_name'
        ]
        read_only_fields = ['id', 'pub_date', 'current_date', 'channel_name']

    def get_current_date(self, obj):
        return obj.pub_date.strftime("%Y년 %m월 %d일")
    
    def get_channel_name(self, obj):
        return "{}({})".format(obj.channel.title, obj.channel.generator) if obj.channel else "Unknown Channel"