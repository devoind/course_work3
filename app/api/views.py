from flask import Blueprint, request, jsonify
import logging

from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

posts_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/')
def posts_all():
    """
    Выводит посты в виде словаря

    :return: возвращает словарь постов
    """
    logger.info("Запрошены все посты через API")
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_pk>/')
def posts_one(post_pk):
    """
    Выводит пост согласно post_pk в виде словаря

    :param post_pk: получает post_pk
    :return: возвращает пост согласно post_pk в виде словаря
    """
    logger.info(f"Запрошены все посты c pk-{post_pk} через API")
    post = posts_dao.get_by_pk(post_pk)
    return jsonify(post)
