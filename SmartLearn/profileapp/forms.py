from django.contrib.auth.forms import AuthenticationForm
from profileapp.models import User


class UserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'