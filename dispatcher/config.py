class Config:
  TESTING = False
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ditto:dummy@db/ditto'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True
