from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_article
from ..models import News


#views
@main.route('/', methods=['GET'])
def index():

    '''
    view news page function that returns the news details  and its data
    '''
    
    news = get_news()
    # print(news)
    title = "News_Highlight"
    
    return render_template('news.html', news = news, title=title)

@main.route('/source/<id>')
def article(id):
    '''
    view news page function that returns the news details  and its data
    '''
    
    articles = get_article(id)
    title = "News_Highlight"
    
    return render_template('article.html', articles = articles, title=title)
