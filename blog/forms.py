from wtforms import fields
from wtforms.ext.appengine.db import model_form
from wtforms.ext.appengine.fields import ReferencePropertyField
from blog.models import Article, Comment

ArticleFormBase = model_form(Article)

class ArticleForm(ArticleFormBase):
    views = fields.IntegerField(default=0)

CommentFormBase = model_form(Comment)

class CommentForm(CommentFormBase):
    pass
