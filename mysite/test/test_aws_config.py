import pytest
from django.conf import settings
from unittest.mock import MagicMock, patch


@pytest.mark.django_db
def test_aws_configuration():
    required_settings = [
        'AWS_ACCESS_KEY_ID',
        'AWS_SECRET_ACCESS_KEY',
        'AWS_STORAGE_BUCKET_NAME',
        'AWS_S3_OBJECT_PARAMETERS',
        'AWS_PRELOAD_METADATA',
        'AWS_AUTO_CREATE_BUCKET',
        'AWS_QUERYSTRING_AUTH',
        'AWS_S3_CUSTOM_DOMAIN',
        'AWS_DEFAULT_ACL',
        'STATICFILES_STORAGE',
        'STATIC_S3_PATH',
        'STATIC_ROOT',
        'STATIC_URL',
        'ADMIN_MEDIA_PREFIX',
        'DEFAULT_FILE_STORAGE',
        'DEFAULT_S3_PATH',
        'MEDIA_ROOT',
        'MEDIA_URL',
    ]

    # Create a MagicMock object for settings
    mock_settings = MagicMock()

    with patch('django.conf.settings', mock_settings):
        for setting_name in required_settings:
            setattr(mock_settings, setting_name, None)

        for setting_name in required_settings:
            assert hasattr(settings, setting_name), f"Missing setting: {setting_name}"
