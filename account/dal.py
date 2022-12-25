
from django.contrib.auth.models import User

__copyright__ = 'Copyright (c)'

def get_user_by_id(id):
    """Adds User given user attributes"""

    return User.objects.get(pk=id)


def get_or_create_user_by_email(email, defaults):
    """Adds User given user attributes"""

    user, _ = User.objects.get_or_create(email=email, defaults=defaults)
    if user:
        return user
