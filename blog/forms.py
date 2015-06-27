from wtforms import fields
from wtforms.ext.appengine.db import model_form
from blog.models import Article

ArticleFormBase = model_form(Article)

class ArticleForm(ArticleFormBase):
    title = fields.StringField(label="title")