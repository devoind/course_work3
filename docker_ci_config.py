# SQLALCHEMY_DATABASE_URI = "postgresql://$DB_USER:$DB_PASSWORD@pg/$DB_NAME"
import os
from typing import List

from dotenv import load_dotenv

load_dotenv()

DEBUG = False
SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{host}:{port}/{db_name}".format(
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST', '127.0.0.1'),
    port=int(os.getenv('POSTGRES_PORT', 5432)),
    db_name=os.getenv('POSTGRES_DB')
)
SWAGGER_SUPPORTED_SUBMIT_METHODS: List[str] = []
