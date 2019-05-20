from django.test import TestCase

# Create your tests here.
@method_decorator(login_required, name='dispatch')