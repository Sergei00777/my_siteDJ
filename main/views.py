from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')

def resume(request):
    return render(request, 'main/resume.html')

def about(request):
    return render(request, 'main/about.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def skills(request):
    return render(request, 'main/skills.html')

def diplomas(request):
    diplomas_list = [
        {
            "title": "Python-разработчик (Нетология)",
            "file": "5bbadd4abacab2959d6c9c433a0bbda2.jpeg",
            "institution": "Нетология",
            "year": 2025
        },
        {
            "title": "Основы Python: телеграм-бот (Нетология)",
            "file": "60d9d334284a95b4db2936d81575302d.jpeg",
            "institution": "Нетология",
            "year": 2022
        },
        {
            "title": "ООП и работа с API (Нетология)",
            "file": "72c0ccb64abe1ec1e2b45d2e221cf050.jpeg",
            "institution": "Нетология",
            "year": 2025
        },
        {
            "title": "Основы языка программирования Python (Нетология)",
            "file": "97db4c865af4b72e025525da50746459.jpeg",
            "institution": "Нетология",
            "year": 2025
        },
        {
            "title": "Git - система контроля версий (Нетология)",
            "file": "3804da23da3c709181edfdeb723bd8d4.jpeg",
            "institution": "Нетология",
            "year": 2025
        },
        {
            "title": "Поколение Python: курс для начинающих (Stepik)",
            "file": "2025-06-03_10-15-39.jpeg",
            "institution": "Stepik",
            "year": 2023
        },
        {
            "title": "Лучший по Python. Для всех начинающих! (Stepik)",
            "file": "2025-07-24_18-17-00.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Лучший по Python. Часть 2! (Stepik)",
            "file": "2025-07-24_18-17-59.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Лучший по Python. Часть 3! (Stepik)",
            "file": "Python3.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Git: от новичка до профи (Stepik)",
            "file": "git2.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Создание Телеграм БОТОВ (Stepik)",
            "file": "BOT.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Риторика (Stepik)",
            "file": "ritorika.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Игрофикация (Stepik)",
            "file": "igrofik.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Профессиональная работа с Python (Нетология)",
            "file": "profickPython.jpeg",
            "institution": "Нетология",
            "year": 2025
        },
        {
            "title": "Основы Excel (Stepik)",
            "file": "Excel.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Обучения онлайн (Нетология)",
            "file": "onlain.jpeg",
            "institution": "Нетология",
            "year": 2025
        },
        {
            "title": "Компьютерная грамотность (Нетология)",
            "file": "komp.jpeg",
            "institution": "Нетология",
            "year": 2025
        },
        {
            "title": "Офисные приложения для начинающих (Word, Excel, Google сервисы) (Stepik)",
            "file": "WordExcelGoogle.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Войти в IT (Stepik)",
            "file": "voit.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Риск-менеджмент в стартапах (Stepik)",
            "file": "stertap.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Основы программирования на языке Python (Stepik)",
            "file": "Pythonuzik.jpeg",
            "institution": "Stepik",
            "year": 2025
        },
        {
            "title": "Stepik для учащихся (Stepik)",
            "file": "Stepikunik.jpeg",
            "institution": "Stepik",
            "year": 2025
        }
    ]
    return render(request, 'main/diplomas.html', {'diplomas': diplomas_list})

def contacts(request):
    return render(request, 'main/contacts.html')