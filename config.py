import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29441913"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2a9559f2aa30aac6e6d8365b1067ceb9")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://iamyourfan550:mX1YdWvJjgfgSOPR@cluster0.ylgci3b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
