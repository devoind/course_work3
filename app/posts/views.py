import logging

from flask import render_template, Blueprint, abort, request
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")


@posts_blueprint.route('/')
def posts_all():
    """
    Выводит все посты

    :return: возвращает страницу со всеми постами
    """
    logger.info("Запрошены все посты через PostsDAO")
    try:
        posts = posts_dao.get_all()
        return render_template("index.html", posts=posts)
    except:
        return "Что-то пошло не так"


@posts_blueprint.route('/posts/<int:post_pk>')
def posts_one(post_pk):
    """
    Выводит пост по post_pk

    :param post_pk: получает post_pk
    :return: возвращает страницу с постом по запросу post_pk
    """
    logger.info(f"Запрошен пост {post_pk} через PostsDAO и вывод коммента через CommentsDAO")
    try:
        post = posts_dao.get_by_pk(post_pk)
        comments = comments_dao.get_py_post_pk(post_pk)
    except:
        return "Произошла ошибка при получении данных поста"
    else:
        if post is None:
            abort(404)
        number_of_comments = len(comments)
        return render_template("post.html", post=post, comments=comments, number_of_comments=number_of_comments)


@posts_blueprint.route('/search/')
def posts_search():
    """
    Поиск поста

    :return: возвращает найденный пост по ключу s
    """
    logger.info(f"Поиск поста через PostsDAO")
    query = request.args.get("s", "")

    if query != "":
        posts = posts_dao.search(query)
        number_of_posts = len(posts)
    else:
        posts = []
        number_of_posts = 0

    return render_template("search.html", query=query, posts=posts, number_of_posts=number_of_posts)


@posts_blueprint.route('/users/<username>/')
def posts_user(username):
    """
    Выводит страницу с постами пользователя

    :param username: получает имя пользователя
    :return: возвращает посты пользователя
    """
    logger.info(f"Поиск поста по пользователю через PostsDAO")
    posts = posts_dao.get_by_user(username)
    number_of_posts = len(posts)

    return render_template("user-feed.html", posts=posts, number_of_posts=number_of_posts)


@posts_blueprint.errorhandler(404)
def post_error(e):
    """
    Выдает ошибку

    :param e: ошибка
    :return: возвращает ошибку
    """
    return "Такой пост не найден!", 404
