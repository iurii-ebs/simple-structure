# Create your serializers for common app here
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.common.models import MyModel

# ======================================================================================================================
# ModelSerializer example
# ======================================================================================================================
# Serializer for validate user data when he want to edit row
from apps.common.validators import CustomEmailValidator


class EditMyModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)  # custom field, which does not exist in model

    class Meta:
        model = MyModel
        fields = ("text",)  # fields to edit


# usage :
# serializer = EditMyModelSerializer(data={"email": "test@gmail.com", "text": "test})
# serializer.is_valid() - return boolean
# serializer.validated_data - return validated data from serializer

# Serializer for return model data
class ViewMyModelSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()  # custom field, need to create return function for this

    def get_title(self, obj):  # you must create function with name: get_{your_field_name}
        # obj - it's one object from Meta.model
        return "Need to implement"

    class Meta:
        model = MyModel
        fields = "__all__"  # getting all fields from model


# usage :
# data = ViewMyModelSerializer(MyModel.objects.first()).data - for one object
# data = ViewMyModelSerializer(MyModel.objects.filter(), many=True).data - for many objects set many=True

# ======================================================================================================================
# Custom serializer example
# ======================================================================================================================
class MyCustomSerializer(serializers.Serializer):
    username = serializers.CharField()


# Custom validation
class MyCustomValidationSerializer(serializers.Serializer):
    # when you start serializer.is_valid() - all validation run automatically
    phone = serializers.IntegerField(required=False)  # Ex1.: validate_phone function, validator for phone field
    email = serializers.EmailField(validators=[CustomEmailValidator(), ])  # Ex2.: append validator to field
    password = serializers.CharField()  # Ex3.: validate function - all attributes
    repeat_password = serializers.CharField()

    def validate_phone(self, value):  # you must create function with name: validate_{your_field_name}
        if "+" not in value:
            raise ValidationError("Enter a valid phone number")
        return value

    def validate(self, attrs):  # use this if you need to validate some fields together
        if attrs["password"] != attrs["repeat_password"]:
            raise ValidationError("Passwords do not match")
        return attrs  # it's required, you need return all attributes
