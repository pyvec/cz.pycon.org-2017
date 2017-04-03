from . import *

DEBUG = True
SECRET_KEY = 42

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'pyconcz',
    }
}


def show_toolbar(request):
    return not request.is_ajax()


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}
DEBUG_TOOLBAR_PATCH_SETTINGS = False

if 'debug_toolbar' not in INSTALLED_APPS:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(
        0, 'debug_toolbar.middleware.DebugToolbarMiddleware'
    )

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

SLACK_WEBHOOK = ''  # Webhook URL for slack CFP notifications
