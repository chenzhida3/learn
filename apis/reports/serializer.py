from rest_framework import serializers
from .models import Reports
from datetime import datetime


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reports
        exclude = ["is_delete"]
        extra_kwargs = {
            'create_time': {
                'read_only': True
            },
            'update_time': {
                'read_only': True
            },
            'html': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        report_name = validated_data['name']
        validated_data['name'] = report_name+'_'+datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        report = Reports.objects.create(**validated_data)
        return report