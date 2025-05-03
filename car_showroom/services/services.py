from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


def upload_photo_customer_user(instance, filename):
    '''
        Построение к пути аватарки пользователя media/users/username/file
    '''
    return f'{settings.BASE_DIR}/media/users/{instance.user.username}/{filename}'


def validate_size_image(file):
    '''
        Проверка размера файла
    '''
    file_size = 2
    if file.size > file_size * 1024 * 1024:
        raise ValidationError(f'Максимальный размер {file_size}')


def get_tokens_for_user(user):
    '''
        Создания токена вручную
    '''
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def upload_photo_car(instance, filename):
    '''
        Построение к пути аватарки пользователя media/users/username/file
    '''
    return f'{settings.BASE_DIR}/media/users/{instance.user.username}/{filename}'


def user_machine_verification(user, car):
    '''
        Проверка, что машина принадлежит пользователю
    '''
    if car in user.user_profile.profile_cars.all():
        return True
    return False


def user_record_verification(user, record):
    '''
        Проверка, что запись принадлежит пользователю
    '''
    if record in user.user_profile.profile_records.all():
        return True
    return False
