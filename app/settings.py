import os
from dotenv import load_dotenv

load_dotenv()


APP_PORT = int(os.environ["APP_PORT"])
APP_HOST = os.environ["APP_HOST"]


DB_SCHEME = os.environ["DB_SCHEME"]
DB_PORT = int(os.environ["DB_PORT"])
DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_NAME = os.environ["DB_NAME"]

REDIS_PORT = int(os.environ["REDIS_PORT"])
REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_DB = int(os.environ["REDIS_DB"])
REDIS_PASS = os.environ["REDIS_PASS"]
