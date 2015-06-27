from wtforms import fields
from wtforms.ext.appengine.db import model_form
from blog.models import Article, Comment

ArticleFormBase = model_form(Article)

class ArticleForm(ArticleFormBase):
    title = fields.StringField(label="title")

CommentFormBase = model_form(Comment)

class CommentForm(CommentFormBase):
    article = fields.HiddenField()
    user = fields.HiddenField()
    timestamp = fields.HiddenField()
    comment = fields.TextAreaField()