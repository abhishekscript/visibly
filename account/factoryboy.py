
import factory

from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'test%s' % n)

    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    is_active = True
    is_superuser = False
    is_staff = False
