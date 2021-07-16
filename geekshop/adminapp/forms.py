from django.forms import ModelForm

from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm
from mainapp.models import ProductCategory


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductCategoryAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
