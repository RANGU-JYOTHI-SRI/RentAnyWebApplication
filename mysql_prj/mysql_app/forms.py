
from django import forms
from .models import UserRegistration,additem,cartpage1,cartpage,Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
class RegisterForm(forms.ModelForm):
    name=forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your full name'}))
    email=forms.EmailField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    password=forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your password'}))
    class Meta:
            model=UserRegistration
            fields= [ "name", "email", "password"]




class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"

class AddItemForm(forms.ModelForm):
    class Meta:
        model = additem
        exclude = ('fileuploadtime',)

class AddCartForm1(forms.ModelForm):
    class Meta:
        model = cartpage
        exclude = ('fileuploadtime',)

class AddCartForm(forms.ModelForm):
    class Meta:
        model = cartpage1
        exclude = ('fileuploadtime',)




PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)






class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            'address',

            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('postal_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),)
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

