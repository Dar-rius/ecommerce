from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo', name='mohamed', firstName='tine', adresse='liberte 6', phone='71 06 18 32')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo", name='mohamed', firstName='tine', adresse='liberte 6', phone='71 06 18 32')