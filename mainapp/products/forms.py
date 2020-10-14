from django.forms import ModelForm
from .models import Product
# we have imported the ModelForm method and our Product class

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # we have now created out productForm, originally referenced in
        # our html for products_page, which uses the model of our Product
        # class and inherits all the fields associated with it