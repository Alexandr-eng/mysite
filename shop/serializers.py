from rest_framework import serializers

from shop.models import User, Category, Warehouse, Product


class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'cat']
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}
        password = serializers.CharField(min_length=6, max_length=20,write_only=True)


    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            username=validated_data["name"],
            cat=validated_data['cat'],
            )

        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user
# class ApiUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=128, validators=[
#         validators.UniqueValidator(ApiUser.objects.all())
#     ])
#     email = serializers.EmailField(validators=[
#         validators.UniqueValidator(ApiUser.objects.all())
#     ])
#     password = serializers.CharField(min_length=6, max_length=20,
#                                      write_only=True)
#
#     def update(self, instance, validated_data):
#         if email := validated_data.get("email"):
#             instance.email = email
#             instance.save(update_fields=["email"])
#
#         if password := validated_data.get("password"):
#             instance.set_password(password)
#             instance.save(update_fields=["password"])
#
#         return instance
#
#     def create(self, validated_data):
#         user = ApiUser.objects.create(
#             email=validated_data["email"],
#             name=validated_data["name"],
#         )
#
#         user.set_password(validated_data["password"])
#         user.save(update_fields=["password"])
#         return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {"id": {"read_only": True}}


class WarhouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
