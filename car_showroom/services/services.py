from django.conf import settings
from rest_framework.exceptions import ValidationError


def upload_photo_customer_user(instance, filename):
    '''
       Построение к пути аватарки пользователя media/users/username/file
    '''
    return f'{settings.BASE_DIR}/media/users/{instance.username}/{filename}'


def validate_size_image(file):
    '''
    Проверка размера файла
    '''
    file_size = 2
    if file_size.size > file_size * 1024 * 1024:
        raise ValidationError(f'Максимальный размер {file_size}')
