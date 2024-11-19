from rest_framework import serializers
from models.models.partners import Partners

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #
    #     try:
    #         data['stores'] = data['db_context']['Store']
    #     except KeyError:
    #         data['stores'] = []
    #
    #     try:
    #         data['course_providers'] = data['db_context']['CourseProvider']
    #     except KeyError:
    #         data['course_providers'] = []
    #
    #     return data