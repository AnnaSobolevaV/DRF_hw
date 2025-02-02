from rest_framework import serializers

link_ok = 'youtube.com'


def lesson_video_link_validator(value):
    if not (value['video'] is None or value['video'] == '' or link_ok in str(value['video'])):
        raise serializers.ValidationError("You can only use the link to youtube.com")
