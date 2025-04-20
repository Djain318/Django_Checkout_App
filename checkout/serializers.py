from rest_framework import serializers

class CheckoutSerializer(serializers.Serializer):
    items = serializers.CharField(help_text="Enter item codes as a string. E.g., 'ABAC'")
