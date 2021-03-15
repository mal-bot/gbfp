from django.core.management import BaseCommand
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        current_path = os.getcwd()
        apps_to_clear_migrations = ['applicantapp', 'authapp', 'mainapp', 'companyapp', 'resumeapp', 'vacancyapp']

        for app in apps_to_clear_migrations:
            path = os.path.join(current_path, f'{app}\\migrations')
            print(f'Миграции для {app} очищены.')
            self.remove_files(path)

        db_path = os.path.join(current_path, 'db.sqlite3')
        if os.path.exists(db_path):
            os.remove(db_path)
            print('База данны удалена.\n')

        print(os.popen('py manage.py makemigrations').read())
        print(os.popen('py manage.py migrate').read())

    def remove_files(self, path):
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            if file != '__init__.py' and '.gitkeep' \
                    and os.path.isfile(filepath):
                os.remove(filepath)
