from django import forms

from .models import contact_me, Add_to_cart

class post_form(forms.ModelForm):

    class Meta:
        model = contact_me
        fields = ('name_field', 'email_field', 'message_text')

class Post_add_to_cart(forms.ModelForm):

    class Meta:
        model = Add_to_cart
        fields = ('quantity_of_product','product_foreign',)
