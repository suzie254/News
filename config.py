import os
class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY') 
class ProdConfig(Config):
    '''
    production configuration child class
    
    Args:
        config: The parent configuration class with general configuration settings
    ''' 
    DEBUG = True

class DevConfig(Config):
    '''
    development configuration child class

    Args:
         config: The parent configuration class with general configuration settings
    '''

    DEBUG = True   

config_options = {
'development':DevConfig,
'production':ProdConfig
}      