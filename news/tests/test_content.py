from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news.models import Comment, News
from yanews.settings import NEWS_COUNT_ON_HOME_PAGE


User = get_user_model()

class TestHomePage(TestCase):

    HOME_URL = reverse('news:home')

    @classmethod
    def setUpTestData(cls):
        all_news = []
        for index in range(NEWS_COUNT_ON_HOME_PAGE + 1):
            news = News(title=f'Новость {index}', text='Просто текст.')
            all_news.append(news)
        News.objects.bulk_create(all_news)


    def test_news_count(self):
        # Загружаем главную страницу.
        response = self.client.get(self.HOME_URL)
        # Код ответа не проверяем, его уже проверили в тестах маршрутов.
        # Получаем список объектов из словаря контекста.
        object_list = response.context['object_list']
        # Определяем количество записей в списке.
        news_count = object_list.count()
        # Проверяем, что на странице именно 10 новостей.
        self.assertEqual(news_count, NEWS_COUNT_ON_HOME_PAGE) 