from flask import request, url_for
from flask_login import current_user

from app import app


def render_post_pagination(page_title: str, posts):
    next_url = url_for(page_title, page=posts.next_num) if posts.has_next else None
    prev_url = url_for(page_title, page=posts.prev_num) if posts.has_prev else None
    return next_url, prev_url


def render_user_post_pagination(page_title: str, user, posts):
    next_url = url_for(page_title, username=user.username, page=posts.next_num) if posts.has_next else None
    prev_url = url_for(page_title, username=user.username, page=posts.prev_num) if posts.has_prev else None
    return next_url, prev_url