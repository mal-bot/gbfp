from django.core.management import BaseCommand
from authapp.models import User
from resumeapp.models import Resume
from vacancyapp.models import Vacancy
from mainapp.models import Responses, BlogPost
import datetime


class Command(BaseCommand):
    tables = [User, Resume, Vacancy, Responses, BlogPost]

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
            {
                'user': User.objects.filter(username='test2').first(),
                'resume_name': 'Желаемая должность Test2 опубликована',
                'cellphone': 22222222,
                'salary': 100000,
                'education': 'Образование Test2',
                'job_list': 'Опыт работы Test2',
                'key_words': 'Ключевые навыки Test2',
                'languages': 'Языки Test2',
                'is_active': True,
                'is_approved': True
            },
            {
                'user': User.objects.filter(username='test2').first(),
                'resume_name': 'Желаемая должность Test2 черновик',
                'cellphone': 22222222,
                'salary': 100000,
                'education': 'Образование Test2',
                'job_list': 'Опыт работы Test2',
                'key_words': 'Ключевые навыки Test2',
                'languages': 'Языки Test2',
                'is_draft': True
            },
            {
                'user': User.objects.filter(username='test2').first(),
                'resume_name': 'Желаемая должность Test2 неопубликовано',
                'cellphone': 22222222,
                'salary': 100000,
                'education': 'Образование Test2',
                'job_list': 'Опыт работы Test2',
                'key_words': 'Ключевые навыки Test2',
                'languages': 'Языки Test2',
            },
            {
                'user': User.objects.filter(username='test3').first(),
                'resume_name': 'Желаемая должность Test3 опубликована',
                'cellphone': 333333333,
                'salary': 100000,
                'education': 'Образование Test3',
                'job_list': 'Опыт работы Test3',
                'key_words': 'Ключевые навыки Test2',
                'languages': 'Языки Test2',
                'is_active': True,
                'is_approved': True
            },
            {
                'user': User.objects.filter(username='test3').first(),
                'resume_name': 'Желаемая должность Test3 черновик',
                'cellphone': 333333333,
                'salary': 100000,
                'education': 'Образование Test3',
                'job_list': 'Опыт работы Test3',
                'key_words': 'Ключевые навыки Test3',
                'languages': 'Языки Test3',
                'is_draft': True
            },
            {
                'user': User.objects.filter(username='test3').first(),
                'resume_name': 'Желаемая должность Test3 неопубликовано',
                'cellphone': 333333333,
                'salary': 100000,
                'education': 'Образование Test3',
                'job_list': 'Опыт работы Test3',
                'key_words': 'Ключевые навыки Test3',
                'languages': 'Языки Test3',
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "LpimnrXY8O3koMd31WEJQIlhiJhwq3sk5sqRPUnrIiCmjmy1Ga",
                "cellphone": 305101,
                "salary": 305101,
                "education": "rFfSo5fLogsXBsG975VppPU89YboOOQJgg07HR82W4wCCNgh6E",
                "job_list": "DIIe6cuhSQd17ZPi0f1I",
                "key_words": "1q6cTudS5v14rJL",
                "languages": "HBBjYMj8rY",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "wdXBqxMWMpLM8blhYjJxNIhy5d6RsPEzxGgcY0O47z5V0XZu8b",
                "cellphone": 457147,
                "salary": 457147,
                "education": "o6lWY25JIiVP0YML7hDLTQ6Qen61fzuBCCK8ue8gyzSucESucu",
                "job_list": "kiJplXAU1v6EnSxUNyNN",
                "key_words": "bdigWe8LxZVLZvP",
                "languages": "M1Wbw8ZnNk",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "7I1egOSH9nTHZyhbZuo2Dld0WbPC0U5lS8Opi1oLcHMODUWJ1L",
                "cellphone": 132961,
                "salary": 132961,
                "education": "Rprrybk23iFda5YOwCEGKogFg9B19gtjLL0hhVf5i9RPvl3A7a",
                "job_list": "OEB2FmImLzat2XygROF1",
                "key_words": "rahIhLXRT4GA4jR",
                "languages": "phTGNY4Kqf",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "aPTo5Fsxh2V4O1SQtZyTFJ88I2dwQ0nsEd0EkbFy0dHo8L8hl3",
                "cellphone": 468684,
                "salary": 468684,
                "education": "hqPmzvAOqRTAclCUA636KW4hsQpkxP5CM46bZVVNgXNowAVMO6",
                "job_list": "UjJpvLwr4jFabbWRxipk",
                "key_words": "5pkqZxJPvr5cV15",
                "languages": "W3gJvorbwH",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "SfMxhnBo8dP7Bg6MomEkgAYQZ46OOyiT1X7PeH5r0QXZQLtIuO",
                "cellphone": 395762,
                "salary": 395762,
                "education": "aK46FojrsgrWuPm8ANLydApDSfHoIitRADzMfUFEiDfmxolApJ",
                "job_list": "6Kc3Taf1nkh4iJwZWraa",
                "key_words": "cpHGPaeDPn3H99m",
                "languages": "jzHtZroqfh",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "zYS4jOqQCVn35bl9qa5jhNjP7Bsy8mjl5IN1V8huTVgdd0dQCq",
                "cellphone": 430869,
                "salary": 430869,
                "education": "RawC8xNuor2KPLqGwHicwRxc29UlDSB9ObDFra2pCSCGNiqm5s",
                "job_list": "Q0ADEAmTJ8cmqVq35yHl",
                "key_words": "YVO2aeOqOUTsqVC",
                "languages": "K8LWDcYR3N",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "aUn2eUT5lHnkv6Ezpu6VSf4tbEIAEVo92gQ4qbNVBHj1ivSgTb",
                "cellphone": 157917,
                "salary": 157917,
                "education": "1QcnsOpJIOgkUL6DLpvlqmHLfnHWfxAxKrPTY5DD1KT9745N7V",
                "job_list": "rvojnOIRHEHToUOtZm5n",
                "key_words": "pQlsugSHOks3YJF",
                "languages": "OIkEAKGx86",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "uNeSRUpbK6yG6BDgWN4eO9kzh4djcmwNATXAGZmDdoEMv7EJDQ",
                "cellphone": 57176,
                "salary": 57176,
                "education": "8hJlGmnCa7l1Ak5YDk0UfMADk8jmXboPMWpgCK1bfAzoHvBJzP",
                "job_list": "lKgglwgGBHDBp9SWon4Y",
                "key_words": "V3sYzfWW5y7ZwHz",
                "languages": "esqv396JtY",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "VvHXOa4sbIrFZKKMJnPhJyn71BYYu9AVLfAJqkKVNGCk8qdzv6",
                "cellphone": 251713,
                "salary": 251713,
                "education": "8cHV43KBfjc3UDwD9LijnxZPHYydBhE7TsHjcmvjoua9RUcnuE",
                "job_list": "KUoc1KD1NfFq98fejl5N",
                "key_words": "lWZ843WZ8x6Ls7W",
                "languages": "uS117fkZPe",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "ewv0shcy4qh8yn3aj38ClvMru8rB7Jd6J44LBFdLeizmT2I2q8",
                "cellphone": 224948,
                "salary": 224948,
                "education": "1uMlz3srYdawiC5jY1zzU8d26bDLk89tWCrFZsDPJ8jMKNJyyB",
                "job_list": "pO4AH2RTpX0hGaeqafV0",
                "key_words": "JqxkpVYQssROXjT",
                "languages": "uzV5zxGDpY",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "sdxoc718aUUwdBl6GlKhGu1EkgCDnILEdPhO5mvZsUTfAIVweG",
                "cellphone": 398218,
                "salary": 398218,
                "education": "VSIQSOdXBdzuywaWDbKQjgiZnIMjlMize58AWu0HTHFF6qgQhP",
                "job_list": "pmwoOzttnJB3vz4AP2xZ",
                "key_words": "9TlD7bbdc6m6BVh",
                "languages": "6C0rJRnHqF",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "K6ancIQVBtqwYQQqhE2ZS88ZLnIWM47iFKSgg8e3FL5TJ4vBWa",
                "cellphone": 449310,
                "salary": 449310,
                "education": "JGvIqN7uKjk9TGDoPQ2H9wv5BIMGiffp2MCyhBNiDlQjahm1IT",
                "job_list": "vL633XV0GiA0MpD5GHDP",
                "key_words": "HOCUDYfLeegV8Ot",
                "languages": "Us9Spcr4ph",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "ffafx3MgImzf1JVmCp275tNGzYwZUXwz95q9DBhECMLFJwyTWR",
                "cellphone": 389203,
                "salary": 389203,
                "education": "Mv0Ag5dViAIx5siH7DkdDCt4dhP3ruVI8QAZPJQ2zAtmtif6OK",
                "job_list": "WmznsJB5g8pjoypAyorI",
                "key_words": "2xwrnDTGK5CTpgX",
                "languages": "tTVh1YTmRM",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "7tt1OFRizH9pz5vk6W3Ia6rdG0ujLffXrYJaLKEjOz3LV2CchC",
                "cellphone": 360105,
                "salary": 360105,
                "education": "XUlm7avUZvRU3kCfHOxRBJKpAd4IY5apNfcjkt5lrNmjiCU38h",
                "job_list": "JfkErOJ6ldgn6eUlGXIc",
                "key_words": "5XTMjxglH7JAJ0v",
                "languages": "4FJyNaoHbF",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test2').first(),
                "resume_name": "O666ufmvMYe3riyoUfdFsZg6i4CQQ2HfgXWLBMPoOAsqo5f1zd",
                "cellphone": 173014,
                "salary": 173014,
                "education": "fUR8WULmnHPy0rr0SnYKbwvh5U7hwByZL3fXZpiLqM09TvVsHj",
                "job_list": "rubR4sjtDCXn0lS0n7MT",
                "key_words": "bmENeO6wOJ8OaNU",
                "languages": "D849wypmgy",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "qdIYgxHFqOwqwxf4EJNnRO1t8afvAhYc1rFuAjrnFPXuHS9BKr",
                "cellphone": 182310,
                "salary": 182310,
                "education": "EIzUyFru4ebkiB1HlpaelSFtnIsoJkJlVsKO5we3TZx8NOK6jd",
                "job_list": "xupxvwDFrpWDlTU0Pz1n",
                "key_words": "MzKhKLfHfY7wEpx",
                "languages": "Y5h7YLzFzg",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "nX9VE6R8kImjQ5jTrk95g54r2cbWtVA4WBeIYmrHXyyw4XHQQw",
                "cellphone": 459765,
                "salary": 459765,
                "education": "OOIsNPbb4F22hrGHxeVLG7NDoeDvpGJFlcjjoMK2yy1CEYUQlV",
                "job_list": "e8QTyQBFDsMpvx5wQFHg",
                "key_words": "dkUdWRGL8QJxKUm",
                "languages": "LyRoTijIbp",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "GRHPIE13nx7hKzGxjZfbLu78ay74c3xNOCEqI3oFcthAUHIscV",
                "cellphone": 480230,
                "salary": 480230,
                "education": "buAtSHvZppuZ9bN7oTqObHBgjnJrW9FV8eSxAkyA7CpLfOlbIW",
                "job_list": "efn2fUsdKo8DDpkZbeJa",
                "key_words": "6DfpRYbzAVBsi9e",
                "languages": "jrG88EgaJC",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "lGwHRsZb98kH22cznPfDLArUfLVanVnYZbO4i4b0jDktg1FLEl",
                "cellphone": 498620,
                "salary": 498620,
                "education": "xoVLrboiQtyodHa7ynGKVBz0AcmnfGSVdkP5YUJogfUx7tdrJb",
                "job_list": "m89MnvzeLPyADJbdL31f",
                "key_words": "jedbnzrC2Q95eDe",
                "languages": "TVR6dG3I4z",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "Weikzo1IehixExm4P3g9pHH36XZpWjmHXfqXsZFzMVyxtIZSRN",
                "cellphone": 95973,
                "salary": 95973,
                "education": "v55aaiHOM0xrxTSUKy8GYJ4qI49bAEwnkAk32Sr0LCByISpM6C",
                "job_list": "dycJxmBOSgipNHEKGwtZ",
                "key_words": "b2HI5VIFizOxf8l",
                "languages": "7LbN81n9LR",
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "t8L3dglkrTObe5qdRvKPgH8pjvhy251ZgOWkoVU8XAP1Nvd56g",
                "cellphone": 392782,
                "salary": 392782,
                "education": "rvcy5PjGy6aM2f1HcyRm1WCWF61tlICm9kSdZYzOW0r7EIr1v1",
                "job_list": "CeaW5VtFt9Y0fq4yNSNX",
                "key_words": "sE9DPBoER6PA7tF",
                "languages": "hLmp7tTpz0",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "CQ4ZoYI8eXG3qoywuX2vkWnkmPnZZKNuqnCACzWjkHCxfvQFe2",
                "cellphone": 365974,
                "salary": 365974,
                "education": "jUKWNCmyu4BSKcUzF19i5gEuGGMWXrD7y1irnIhNcqIKaUZ7Vy",
                "job_list": "P4ZMyCPZQHzQaC0DdS4m",
                "key_words": "L6TvGOX4UwrPAjc",
                "languages": "IimDfbN2aX",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "TX0GDtmSlnGjpVFeZkP1jse1PZK7D3X49Rk65lLQ7Jh5fe0GIY",
                "cellphone": 327057,
                "salary": 327057,
                "education": "PrPMjXvIiyY84ZKjVviEzp2k7lv8E6uhrS4zpT4dU9zMX7dGbS",
                "job_list": "nFFfzkzoO8lwDmD1RlfU",
                "key_words": "4C0FtzzqMAHohwS",
                "languages": "pcMdUAAE61",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "Igp1lGXkO9w9uJcO07PRTYYFIKU474OL3mhpUPDaYsacadj1i0",
                "cellphone": 234349,
                "salary": 234349,
                "education": "nUvkGIlw3k3y2l75poldWGyU2Oswhugnn5EGrzXaPw7eAdwRxM",
                "job_list": "4EyTGgfas2ZzOIEPL6g0",
                "key_words": "O0RKOkJUTZbb9Uz",
                "languages": "byUzilQHeB",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "ZuS0u78EwoFgWLHSa803Tna0G8O7swJyCU4iGlqBWuoKPSLaJy",
                "cellphone": 13658,
                "salary": 13658,
                "education": "V9eQdCQiMySyhi8Qlywyx4sGOYzHOo23TUYop8zJJlmPtuG7xD",
                "job_list": "05A4ObRXBFMJTh6ZfMJT",
                "key_words": "kn8moLScXeS1ULy",
                "languages": "72YG7XR6t6",
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "TUP3xdcN6YQCIyAhxVyIt9gHGL6SqPpn4NJDOYE0skAeHEyjRY",
                "cellphone": 83576,
                "salary": 83576,
                "education": "grsmH4o7TYQ8aI8C9CXWBSSDcv20QGkcShETvf634TFhVMsMUu",
                "job_list": "IuOKINYpKWByrMyyq2Ep",
                "key_words": "RdGdcrNusPDqff7",
                "languages": "0NHY04FVk1",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "tggzIpdpovsbAo74SVTLP8ljdNvLIglWEVBMtOi0CSLbZ7zQIa",
                "cellphone": 147151,
                "salary": 147151,
                "education": "gIKVWpnvLExdJ7wJKgXfCsOFknsPRw3n6twDRDkKmXONtTQp9v",
                "job_list": "wygYPx3Eus7XdZLJhZKt",
                "key_words": "1G5N2oeBWRWCQf9",
                "languages": "EHhe8JNT1M",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "Cjv0eP3q3SgkT2sdV5H7ZGCA5MkoxDAnvo9wffhAmSLyA3pRe0",
                "cellphone": 121788,
                "salary": 121788,
                "education": "3zS2zo3670XGVG5O9CgSK6htgzODPtkOVXZVgHDAYi2p4AkT9S",
                "job_list": "w2vWE6RiWAZzqNPIv8rk",
                "key_words": "r28g4mE2yfP5E67",
                "languages": "rd8ScE7uDk",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "avPlmZl44Pcc2Zu1veutPhpwqOfuH55VuZbCQnTpVDxNg0kpN3",
                "cellphone": 422394,
                "salary": 422394,
                "education": "w9UGrc7rkHLFYMubQzn0hNnyhmAi6xs5vfQy3ZIHrfSK5stMIo",
                "job_list": "LFtDSiVgjEcYuxZPU356",
                "key_words": "i0rgIB5c2y3xaRm",
                "languages": "mLrMrcW0Dp",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "user": User.objects.filter(username='test3').first(),
                "resume_name": "vqXzQMGVXN5Qn2nuKo8dKwDnqOeLAo0zRZrMaDhNLRO8v5EjtF",
                "cellphone": 456030,
                "salary": 456030,
                "education": "UtWG9NLaTHHuS3hF1vJ4b4v0e9Fskq4efQ6elp50YTvv3j9bbh",
                "job_list": "2X2xca8glAIc0nMmPB7C",
                "key_words": "dMzTgIIA65AoRCx",
                "languages": "hmsyggFD5s",
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
        ]
        for item in resume:
            Resume.objects.create(**item)

        vacancy = [
            {
                'company': User.objects.filter(username='test4').first(),
                'vacancy_name': 'Вакансия компании Test4 не опубликована',
                'description': 'Описание требований на должность от компании Test4',
                'salary': 40000,
            },
            {
                'company': User.objects.filter(username='test4').first(),
                'vacancy_name': 'Вакансия компании Test4 черновик',
                'description': 'Описание требований на должность от компании Test4',
                'salary': 40000,
                'is_draft': True,
            },
            {
                'company': User.objects.filter(username='test4').first(),
                'vacancy_name': 'Вакансия компании Test4 опубликована',
                'description': 'Описание требований на должность от компании Test4',
                'salary': 40000,
                'is_active': True,
                'is_approved': True
            },
            {
                'company': User.objects.filter(username='test5').first(),
                'vacancy_name': 'Вакансия компании test5 не опубликована',
                'description': 'Описание требований на должность от компании test5',
                'salary': 50000,
            },
            {
                'company': User.objects.filter(username='test5').first(),
                'vacancy_name': 'Вакансия компании test5 черновик',
                'description': 'Описание требований на должность от компании test5',
                'salary': 50000,
                'is_draft': True,
            },
            {
                'company': User.objects.filter(username='test5').first(),
                'vacancy_name': 'Вакансия компании test5 опубликована',
                'description': 'Описание требований на должность от компании test5',
                'salary': 50000,
                'is_active': True,
                'is_approved': True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "iLq9wZWY8w1jCqWacqtcl07rl7urnJ",
                "description": "7FRSrSJ61Pr8buEARcvLB2eZXrO8XzoovzywRu8EQfzdvmZMnlpS5cIFk249ELiCkCNm5Sshdr4fCAnvSBVvJVsTrtMZz99F6x3s",
                "salary": 204055,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "3HzOhmCkOJrDzw2OT45LFSsesyiPH4",
                "description": "WfuA2CgevEqmLpR6PJ5oZd2FPkZVftDxcTwLTz40szJ0edHCMviYTcf2novSmK9CA3J12GnaPF6kUBkvdWJtKpdAx4ioEmNh0H0l",
                "salary": 174096,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "IIJOg5imD9yQBP1VZIE8h8Wn1YuNL9",
                "description": "aNMDkCfPe1V6kEx7gkPeLMLLiJvgWHLUbEjlD8ozzJoMmlYSz42J7qxOCAfaQ93WqBfffM3i6aoBh8j7vdqbOCXuRUiCcNi0QSgl",
                "salary": 54967,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "BUNhBvrDbhpxSbHnnuOKn0Fs2yvPc7",
                "description": "13qDa4yztgnfk5iviyK27VnmAKPepNAbleqvGPBNyyBsgHPJKHP6FjAgQDDPoUKffL4GOxoTx6DJT5G24FUh7DWBeJeCMvjenfMU",
                "salary": 118541,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "c6JIf0MV7KVi9mhcz2mFSmHBXjgxsv",
                "description": "ovK7FB4Ogn6JEBaAeA7ufVg0E0zIv6UZmMfjYChgilW8IIhFkXEf08PTOU3OLvcjThh1f1lccaL49hr5TuhY1zin7MUEISUwIwpk",
                "salary": 305091,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "vmCZwUUqm75bOEre834TghTJFZwM2H",
                "description": "UnKymPwJ1m2nbLX3iDELlsvQMOS2TXiHyfmSRZccrzCRa3FHwM1tHqfm13mY730dEuy6jEmIlmdwpezTIKGGgy9I9AaXxEfy9iMp",
                "salary": 44301,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "ksHfMt6XDSPwwt6Pvq6ioOVgHpxGRK",
                "description": "O9lYgxrd6QDDTeysBPl64YNADVXkYg5zF3DQLYNJiRtpfl40sYnheVP0vlVKaGFZUN7aaihnCcXnohecbg293YUunNejDDscLUUS",
                "salary": 325226,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "1AfC7mMOG2t4NFg62MwND7k8u4bUMM",
                "description": "y6FsH22SxBBQcKUyPGxYZbsNG4ahRCL1B4Dwye8nEjZuLxeZo5pVgyxXN2mNcVAuzJOiGh9uHJUzC7BSZA2VW0UNHqi52uLsjo5C",
                "salary": 289082,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "55NXe7UQ1TxbcoY9yAba8E1X8lQXC9",
                "description": "tdrvZbn7tJVSEj6tP4Q5Nie2I1EzY2r7N2jTtrO6W1RREp9RaOVWHGvK8zniXxi0cYEMAm9ipTjVRNyc2wZJgUzHGYV4DqjjSayp",
                "salary": 303012,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "PwqyhZ3vBKpkXYTHj7GlRFe8tAC1YI",
                "description": "1Fel4uoBkqej22B9L4GrGnqpfJRsEgWCW3TjFwejdhXZGrMm7uzIurBNZzGuc56DTcN9jb3ZagNiQQjx7pvTrNSp1FKQptHilTFo",
                "salary": 252900,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "1asNdd7IPSxwKnWFKhIdRmtqZp76K4",
                "description": "TumPcRfELXIBAX5UX87Ad6EjOPrByygB8V9CJ5KEkGWuVQlVuER98KaWqDANkdPW1GCpY3Kcx2ZXkTO8nVQtghDx4mVG47eH093O",
                "salary": 114940,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "3zLFvDvWzCjOMg0UDPvwhEhzYShka9",
                "description": "urZZ0rV7C109R1XQ4UJiK7KKTzRVrcfL6zR1yxpI9GN45iwqcHYNb2yxhOFAZ9QjVpCbjgbHoAjEuPPvCl3kESuEBeTkrot90njP",
                "salary": 261227,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "pQiaStCS9U8yFqfC58aFM1Z9RjOHq9",
                "description": "Pre84xtTvRcBkXq44KIgTh4Bty1jJtf4m9ERTHvrTmNJmLQCTWoE8KqswdPG6KKBwhZlSZlxYaNrTvYhhyQwEa6cTWe02pvIbLXF",
                "salary": 392795,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "v1qh68YBEriH4X6Vl7S54u4spEPHYT",
                "description": "v2EWBNuYfU8cwKHoOEPBdzWy9A6722tQnu6pChWtkNb87b8ulB0L2W05fQXAQwfmlrzBOblqsfaPXY1hCMW0CiXR4AKwKVdxrzXP",
                "salary": 312122,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test4').first(),
                "vacancy_name": "ZJcW5kiGY08DapkCTiHNRzgXCmihBl",
                "description": "5GqMa2FBVTcDXUXaXCPU5DyT2knFUSCAFx51WOOr7SMxuNcM9mPfSrp1RXT0P9qDRc7jYfDJyiWn1BipIbGsCgrYHEk94Yb7lJgS",
                "salary": 134855,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "iGruUC9Qyory38AuujbU4DOaGZBseQ",
                "description": "ZQolJ6z7DFEUKPqnDnIvhpacjf1Qn5ARviPbJRzE5xgWQk29tcVXktttzLCoEiTIExjmAPdvyD0uJEL9m2hKjnrCzgl7PLAWdYRd",
                "salary": 17697,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "9jjg28jvADBLAIibFhxdofgnDeQvws",
                "description": "8W3ELADKJ06z7LJyVU00XdcfzdD6dYry9RFpR67iX5X7hyhUeOI656Ue3YOr7HruIH0pGdhYWRccGf7A5sbPQv3C7lv3sPlPOmya",
                "salary": 485135,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "rujne2XYaNwOpbeXNysfrnqHqMOdqh",
                "description": "CDebifLQiENXcedWjwIbMKJsSDEc6Ro4s3LsuO38L6PoSULLnUmcVPU24vIebtURaTpiSvlV2JPQ4ea822yloMicjSx9GYgcm8O8",
                "salary": 332216,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "tRjM9E8aUJmj5smOuM9A7mPdmxn5Qb",
                "description": "TP952XmWdfUXp6w7h3W9Ocm25HCFjMaCJ2zWk90PlYtepj7SrpPujQN1mGAvVhwQESOwGZXiCGY0sINVKtX46pc2p8td8F4DldZW",
                "salary": 181305,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "Rrrd2WIe2pllJ1TZ0VHIp3j7MUOPt1",
                "description": "99gFnP79ASzPkTdS4uJAf9DDmYItQhH3vBqlFEOEb1VyTaSQe4aeGtV96cdOGNscK5ejm1MzfFiooOuLF2PWGnwCqqpmk97NI2oX",
                "salary": 473506,
                "is_draft": False,
                "is_active": True,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "rk8AKqVrsRIO7WWhJb26MkPgHUfvkW",
                "description": "OWOnofow19V83S1sPwfGOe0raGVc2zLjGVDwAUr02Wk3kOq6oZEsPdItfhNiJM3Bxw1iPEs5FoO147GLaZxdvcTnNTRcHJrpdiFy",
                "salary": 192791,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "rJnkPQziaBHuYZQVdOU6xPy67jXW1S",
                "description": "yRsNwlzsY6esBFB6QDRuVJxuwbVqnp3cqIMzCLnogu0YcENs5ASTEH6pe7aUQIFsDBB22L4EanOkTYSrOmvmXjXjMhVEvTXXpIVa",
                "salary": 34764,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "GN3b3WWFpsGoXcUeocqVz0THP04LD1",
                "description": "o3wBfKp5qzKQYCMt9Mx0wknf4P3wMCbLByEN2W6Kzsv1KjbR4g1rXNEDPQHPQ2soY9Ok890nPnBEzwUUym1qLtxytA7lOr469HdK",
                "salary": 178115,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "pNbuLAOd6wbnACdoLa08COYisFErTJ",
                "description": "96T6A7SDmtvepcPQ57oz94BU3ay2BG6gJwxfUEBfVHxHMij6TcJHDeKE48DjJZCfwPU3ot515Id1H3IV11ji6ycpmtkVBcW6FRU6",
                "salary": 118982,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "gSL4BS6AzsrR0dj8woR4Ij0dwgwzjM",
                "description": "HMj8BomhoTwkgTuFGmsWJjYXb7csIegHbnkfr1b4VOA7IiDgtrZJGNCixLhEL4ZKxoI2sOXPKxB4jaP3359bEWBOkCrgUWtbzzKd",
                "salary": 214475,
                "is_draft": True,
                "is_active": False,
                "is_approved": True
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "UK8SLH9X6nLQ47Fan4Sqg05yEkFtQw",
                "description": "dsHeG3XsCcDUkqLdg1utzf2I8dPKNlCPHJKcJa1LC51zmMQOmlDN9g6708gnoNfaaxNagtUFAiq4nDfvNAhlhzQlMMlK3NhzZbZz",
                "salary": 493152,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "R7MbzCTxcuaop32kgmNTHJMxA1eMnq",
                "description": "wWRoUknzvK2yrIx2KgiySXmYwIvZa8iHJw8DWBjS7r0DbSbD9Iq7ozXZu21LyNZxlvo5KtfJ7P0lgj7dqsZRRkcUYiTeJXetRDbp",
                "salary": 327010,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "mh9Y8w3K5YfGxHfBSUgmaB9kvGTdIR",
                "description": "zKzJptkDVmpIju1X5KhZWT9QzlhZm1caCniUQobvaP947RcPtYKI5s4fLjUEMLadJPG5MhHRsv9HUEShISqOrUeUsCIqTXjOygvs",
                "salary": 97706,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "R2aJswLHQw53fMwzuwMJYa8VMuTyTk",
                "description": "WmPe7y3Ul50BZhcptlt67ZT3x04F78dXyqZToBO75ZKRSWAb2gBrEWm7SWqG3yXncdNtHIBsXvAiOClb0dMb7vTbDcARVHEGCgyz",
                "salary": 81585,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            },
            {
                "company": User.objects.filter(username='test5').first(),
                "vacancy_name": "eTUSWEsQuOQam6qrJwppItXPr4grNw",
                "description": "SjJc6oaBF9tthG1oeF0HpXkolu6EkbiAC86qQK9CQIqq6YMRYDaa1FG59e0LsVanbsriJKXUGy1hq4sMioqhBHJ61BrwTyU4rDPO",
                "salary": 353743,
                "is_draft": True,
                "is_active": False,
                "is_approved": False
            }
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
            {'user': User.objects.filter(username='test4').first(),
             'resume': Resume.objects.filter(id=7).first()},
            {'user': User.objects.filter(username='test4').first(),
             'resume': Resume.objects.filter(id=8).first()},
            {'user': User.objects.filter(username='test4').first(),
             'resume': Resume.objects.filter(id=9).first()},
            {'user': User.objects.filter(username='test4').first(),
             'resume': Resume.objects.filter(id=10).first()},
            {'user': User.objects.filter(username='test4').first(),
             'resume': Resume.objects.filter(id=11).first()},


            {'user': User.objects.filter(username='test2').first(),
             'vacancy': Vacancy.objects.filter(id=3).first()},
            {'user': User.objects.filter(username='test2').first(),
             'vacancy': Vacancy.objects.filter(id=6).first()},
            {'user': User.objects.filter(username='test3').first(),
             'vacancy': Vacancy.objects.filter(id=6).first()},
            {'user': User.objects.filter(username='test2').first(),
             'vacancy': Vacancy.objects.filter(id=7).first()},
            {'user': User.objects.filter(username='test2').first(),
             'vacancy': Vacancy.objects.filter(id=8).first()},
            {'user': User.objects.filter(username='test3').first(),
             'vacancy': Vacancy.objects.filter(id=9).first()},
            {'user': User.objects.filter(username='test2').first(),
             'vacancy': Vacancy.objects.filter(id=10).first()},
            {'user': User.objects.filter(username='test2').first(),
             'vacancy': Vacancy.objects.filter(id=11).first()},

        ]

        for item in responses:
            Responses.objects.create(**item)

        blog_post = [
            {'title': 'НОВОСТЬ 1',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 2',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 3',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 4',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 5',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 6',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 7',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 8',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 9',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 10',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 11',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
            {'title': 'НОВОСТЬ 12',
             'text': 'ТЕКСТ ДЛЯ НОВОСТИ',
             },
        ]

        for item in blog_post:
            BlogPost.objects.create(**item)

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
