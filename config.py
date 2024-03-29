#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("BOT_TOKEN", "6341924529:AAFMFbD-V6T6W0nYhLSTC5Re7dHGFGjU-O4") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("API_ID", "20919880")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "0bb61198c9b5740cd2987d58f78be06d") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", "5100345229")) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://7xmovieshub:uoc0ajFxBrQ0wksk@movies7x.4axozzk.mongodb.net/?retryWrites=true&w=majority&appName=Movies7x") # Get from MongoDB Atlas

