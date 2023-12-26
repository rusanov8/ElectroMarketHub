from django.core.management import BaseCommand

from users.models import User
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

SU_EMAIL = os.getenv('SU_EMAIL')
SU_PASSWORD = os.getenv('SU_PASSWORD')


class Command(BaseCommand):
    """
       Custom management command to create a superuser.
    """

    def handle(self, *args, **options):

        if SU_EMAIL is None or SU_PASSWORD is None:
            raise ValueError("Необходимо определить SU_EMAIL и SU_PASSWORD в файле .env")

        user = User.objects.create(email=SU_EMAIL,
                                   is_staff=True,
                                   is_superuser=True,
                                   )

        user.set_password(SU_PASSWORD)
        user.save()

        self.stdout.write(self.style.SUCCESS('Суперпользователь успешно создан.'))


