import pytest
from django.conf import settings


@pytest.mark.django_db
def test_aws_configuration():
    required_settings = {
        'AWS_ACCESS_KEY_ID': 'sua_chave_de_acesso',
        'AWS_SECRET_ACCESS_KEY': 'sua_chave_secreta',
        'AWS_STORAGE_BUCKET_NAME': 'seu_bucket',
        'AWS_S3_OBJECT_PARAMETERS': {'param1': 'valor1', 'param2': 'valor2'},
        'AWS_PRELOAD_METADATA': True,
        'AWS_AUTO_CREATE_BUCKET': True,
        'AWS_QUERYSTRING_AUTH': False,
        'AWS_S3_CUSTOM_DOMAIN': 'seu_domain',
        'AWS_DEFAULT_ACL': 'public-read',
        'STATICFILES_STORAGE': 'seu_staticfiles_storage',
        'STATIC_S3_PATH': 'caminho_static_s3',
        'STATIC_ROOT': '/caminho/para/static/root',
        'STATIC_URL': '/static/url/',
        'ADMIN_MEDIA_PREFIX': '/admin/media/prefix/',
        'DEFAULT_FILE_STORAGE': 'seu_default_file_storage',
        'DEFAULT_S3_PATH': 'caminho_default_s3',
        'MEDIA_ROOT': '/caminho/para/media/root',
        'MEDIA_URL': '/media/url/',
    }

    for setting_name, setting_value in required_settings.items():
        setattr(settings, setting_name, setting_value)

    for setting_name, setting_value in required_settings.items():
        assert getattr(settings, setting_name) == setting_value, f"Setting {setting_name} is not correctly set."
