import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from databases import Database

from utils.const import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER, DB_URL

db = Database(DB_URL)