from settings import *


DEBUG = True

DATABASES['default'] = {
  'ENGINE': 'django.db.backends.sqlite3',
  'TEST_NAME': ':memory:'}

PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher', )

SOUTH_TESTS_MIGRATE = False

TEST_RUNNER = 'redrover.RedRoverRunner'

CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = tuple(INSTALLED_APPS) + ('redrover', )

# import warnings
# warnings.filterwarnings(
#   'error', r"DateTimeField received a naive datetime",
#   RuntimeWarning, r'django\.db\.models\.fields')
