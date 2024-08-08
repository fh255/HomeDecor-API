from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    def to_representation(self, instance):
        # Call the parent's to_representation method to get the serialized data
        ret = super().to_representation(instance)

        # Print each field's value
        for field, value in ret.items():
            print(f"{field}: {value}")

        # Return the serialized data
        return ret

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 
        )