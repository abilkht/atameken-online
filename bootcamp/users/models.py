from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from bootcamp.notifications.models import Notification, notification_handler

BUSINESS_TYPE_CHOICES = (
    ('0111', 'Выращивание зерновых культур (за исключением риса), бобовых культур и масличных семян'),
    ('0112', 'Выращивание риса'),
    ('0113', 'Выращивание овощей и бахчевых, корнеплодов и клубнеплодов'),
    ('0114', 'Выращивание сахарного тростника'),
    ('0115', 'Выращивание табака'),
    ('0116', 'Выращивание волокнистых прядильных культур'),
    ('0119', 'Выращивание прочих сезонных культур'),
    ('0121', 'Выращивание винограда'),
    ('0122', 'Выращивание тропических и субтропических фруктов'),
    ('0123', 'Выращивание цитрусовых фруктов'),
    ('0124', 'Выращивание семечковых и косточковых плодов'),
    ('0125', 'Выращивание прочих видов плодовых деревьев, кустарников и орехов'),
    ('0126', 'Выращивание маслосодержащих плодов'),
)
REGION_CHOICES = (
    ('akmola', 'Акмолинская область'),
    ('aktobe', 'Актюбинская область'),
    ('almaty', 'Алматинская область'),
    ('atyrau', 'Атырауская область'),
    ('eastern', 'Восточно-Казахстанская область'),
    ('dzhambul', 'Жамбылская область'),
    ('western', 'Западно-Казахстанская область'),
    ('karaganda', 'Карагандинская область'),
    ('kostanai', 'Костанайская область'),
    ('kyzylorda', 'Кызылординская область'),
    ('mangystau', 'Мангистауская область'),
    ('pavlodar', 'Павлодарская область'),
    ('north', 'Северо-Казахстанская область'),
    ('turkestan', 'Туркестанская область'),
)


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns around the globe.
    name = models.CharField(
        _('ФИО'), blank=True, max_length=255)
    picture = models.ImageField(
        _('Картинка профиля'), upload_to='profile_pics/', null=True, blank=True)
    location = models.CharField(
        _('Адрес'), max_length=50, null=True, blank=True)
    job_title = models.CharField(
        _('Название предприятия'), max_length=50, null=True)
    personal_url = models.URLField(
        _('Сайт компании'), max_length=255, blank=True, null=True)
    business_type = models.CharField(
        _('Вид деятельности'), max_length=50, choices=BUSINESS_TYPE_CHOICES)
    region = models.CharField(
        _('Область'), max_length=50, choices=REGION_CHOICES, default='akmola')
    city = models.CharField(
        _('Город'), max_length=50, null=True)
    # facebook_account = models.URLField(
    #     _('Профиль Facebook'), max_length=255, blank=True, null=True)
    # linkedin_account = models.URLField(
    #     _('Профиль LinkedIn'), max_length=255, blank=True, null=True)
    short_bio = models.CharField(
        _('Должность'), max_length=60, blank=True, null=True)
    bio = models.CharField(
        _('О компании'), max_length=555, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11}$', message="Номер должен быть в формате: '+7xxxxxxxxxx' или '8xxxxxxxxxx'.")
    phone_number = models.CharField(
        _('Номер телефона'), validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_profile_name(self):
        if self.name:
            return self.name

        return self.username


def broadcast_login(sender, user, request, **kwargs):
    """Handler to be fired up upon user login signal to notify all users."""
    notification_handler(user, "global", Notification.LOGGED_IN)


def broadcast_logout(sender, user, request, **kwargs):
    """Handler to be fired up upon user logout signal to notify all users."""
    notification_handler(user, "global", Notification.LOGGED_OUT)


user_logged_in.connect(broadcast_login)
user_logged_out.connect(broadcast_logout)
