import os
class Config:
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey=87ac3a0f6a0f4533bca9d4ca6891a417'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources=bbc-news&apiKey=87ac3a0f6a0f4533bca9d4ca6891a417'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG=True
config_options={
    'development':DevConfig,
    'production':ProdConfig
}
