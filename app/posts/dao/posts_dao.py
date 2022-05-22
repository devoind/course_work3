import json


class PostsDAO:
    """Класс ответственный за работу со всеми постами"""

    def __init__(self, path):
        self.path = path

    def _load(self):
        """
        Выводит посты

        :return: возвращает посты
        """
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        """
        Возврат всех постов

        :return: возвращает все посты
        """
        return self._load()

    def get_by_pk(self, pk):
        """
        Выводит пост по его идентификатору

        :param pk: получает идентификатор поста
        :return: возвращает пост по его идентификатору
        """
        posts = self.get_all()
        for post in posts:
            if post['pk'] == pk:
                return post

    def get_by_user(self, user_name):
        """
        Выводит посты определенного пользователя

        :param user_name: получает пост определенного пользователя
        :return: возвращает посты определенного пользователя
        """
        posts = self.get_all()
        posts_by_user = []

        for post in posts:
            if post['poster_name'] == user_name:
                posts_by_user.append(post)

        return posts_by_user

    def search(self, query):
        """
        Возвращает список постов по вхождению query

        :param query: получает значение вхождения query
        :return: возвращает список постов по вхождению query
        """
        posts = self.get_all()
        matching_posts = []
        query_lower = query.lower()

        for post in posts:
            if query_lower in post['content'].lower():
                matching_posts.append(post)

        return matching_posts
