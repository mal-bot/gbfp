from django.core.management import BaseCommand
from authapp.models import User
from resumeapp.models import Resume
from vacancyapp.models import Vacancy
from mainapp.models import Responses
import datetime


class Command(BaseCommand):
    tables = [User, Resume, Vacancy, Responses]

    # # sqlite
    def handle(self, *args, **options):

        self.clear_all_tables()
        # Супер юзер
        User.objects.create_superuser(username='test', email='test@test.ru', password='test',
                                      user_about='Суперюзер', first_name='Имя Test',
                                      last_name='Фамилия Test', user_patronymic='Отчество Test')
        # Соискатели
        User.objects.create_user(username='test2', email='test2@test.ru', password='test2',
                                 first_name='Имя Test2',
                                 last_name='Фамилия Test2',
                                 user_patronymic='Отчество Test2',
                                 user_age='30',
                                 user_about='О себе соискатель Test2')
        User.objects.create_user(username='test3', email='test3@test.ru', password='test3',
                                 first_name='Имя Test3',
                                 last_name='Фамилия Test3',
                                 user_patronymic='Отчество Test3',
                                 user_age='18',
                                 user_about='О себе соискатель Test3')
        # Работодатели
        User.objects.create_user(username='test4', email='test4@test.ru', password='test4',
                                 is_staff=True, is_partner=True,
                                 company_name='Название компании Test4',
                                 company_about='Описание компании Test4',
                                 company_main_business='Основной вид деятельности компании Test4',
                                 company_since=datetime.date(2021, 3, 19))
        User.objects.create_user(username='test5', email='test5@test.ru', password='test5',
                                 is_staff=True,
                                 company_name='Название компании Test5',
                                 company_about='Описание компании Test5',
                                 company_main_business='Основной вид деятельности компании Test5',
                                 company_since=datetime.date(2021, 1, 1))

        resume = [
            {'user': User.objects.filter(username='test2').first(),
             'resume_name': 'Желаемая должность Test2 опубликована',
             'cellphone': 22222222,
             'salary': 100000,
             'education': 'Образование Test2',
             'job_list': 'Опыт работы Test2',
             'key_words': 'Ключевые навыки Test2',
             'languages': 'Языки Test2',
             'is_active': True
             },
            {'user': User.objects.filter(username='test2').first(),
             'resume_name': 'Желаемая должность Test2 черновик',
             'cellphone': 22222222,
             'salary': 100000,
             'education': 'Образование Test2',
             'job_list': 'Опыт работы Test2',
             'key_words': 'Ключевые навыки Test2',
             'languages': 'Языки Test2',
             'is_draft': True
             },
            {'user': User.objects.filter(username='test2').first(),
             'resume_name': 'Желаемая должность Test2 неопубликовано',
             'cellphone': 22222222,
             'salary': 100000,
             'education': 'Образование Test2',
             'job_list': 'Опыт работы Test2',
             'key_words': 'Ключевые навыки Test2',
             'languages': 'Языки Test2',
             },
            {'user': User.objects.filter(username='test3').first(),
             'resume_name': 'Желаемая должность Test3 опубликована',
             'cellphone': 333333333,
             'salary': 100000,
             'education': 'Образование Test3',
             'job_list': 'Опыт работы Test3',
             'key_words': 'Ключевые навыки Test2',
             'languages': 'Языки Test2',
             'is_active': True
             },
            {'user': User.objects.filter(username='test3').first(),
             'resume_name': 'Желаемая должность Test3 черновик',
             'cellphone': 333333333,
             'salary': 100000,
             'education': 'Образование Test3',
             'job_list': 'Опыт работы Test3',
             'key_words': 'Ключевые навыки Test3',
             'languages': 'Языки Test3',
             'is_draft': True
             },
            {'user': User.objects.filter(username='test3').first(),
             'resume_name': 'Желаемая должность Test3 неопубликовано',
             'cellphone': 333333333,
             'salary': 100000,
             'education': 'Образование Test3',
             'job_list': 'Опыт работы Test3',
             'key_words': 'Ключевые навыки Test3',
             'languages': 'Языки Test3',
             },
        ]
        for item in resume:
            Resume.objects.create(**item)

        vacancy = [
            {'company': User.objects.filter(username='test4').first(),
             'vacancy_name': 'Вакансия компании Test4 не опубликована',
             'description': 'Описание требований на должность от компании Test4',
             'salary': 40000,
             },
            {'company': User.objects.filter(username='test4').first(),
             'vacancy_name': 'Вакансия компании Test4 черновик',
             'description': 'Описание требований на должность от компании Test4',
             'salary': 40000,
             'is_draft': True,
             },
            {'company': User.objects.filter(username='test4').first(),
             'vacancy_name': 'Вакансия компании Test4 опубликована',
             'description': 'Описание требований на должность от компании Test4',
             'salary': 40000,
             'is_active': True
             },
            {'company': User.objects.filter(username='test5').first(),
             'vacancy_name': 'Вакансия компании test5 не опубликована',
             'description': 'Описание требований на должность от компании test5',
             'salary': 50000,
             },
            {'company': User.objects.filter(username='test5').first(),
             'vacancy_name': 'Вакансия компании test5 черновик',
             'description': 'Описание требований на должность от компании test5',
             'salary': 50000,
             'is_draft': True,
             },
            {'company': User.objects.filter(username='test5').first(),
             'vacancy_name': 'Вакансия компании test5 опубликована',
             'description': 'Описание требований на должность от компании test5',
             'salary': 50000,
             'is_active': True
             },

        ]

        for item in vacancy:
            Vacancy.objects.create(**item)

        responses = [
            {'user': User.objects.filter(username='test4').first(),
             'resume': Resume.objects.filter(id=1).first()},
            {'user': User.objects.filter(username='test4').first(),
             'resume': Resume.objects.filter(id=4).first()},
            {'user': User.objects.filter(username='test5').first(),
             'resume': Resume.objects.filter(id=4).first()},
            {'user': User.objects.filter(username='test2').first(),
             'vacancy': Vacancy.objects.filter(id=1).first()},
            {'user': User.objects.filter(username='test2').first(),
             'vacancy': Vacancy.objects.filter(id=4).first()},
            {'user': User.objects.filter(username='test3').first(),
             'vacancy': Vacancy.objects.filter(id=4).first()},
        ]

        for item in responses:
            Responses.objects.create(**item)

        #    self.show_all_tables()
        self.count_tables_data()

    def clear_all_tables(self):
        for table in self.tables:
            table.objects.all().delete()

    def count_tables_data(self):
        for table in self.tables:
            print(f'Количество строк в таблице {table.__name__}: {len(table.objects.all())}')

    def show_all_tables(self):
        for table in self.tables:
            print(table.objects.all())
