# Support Dual Mongo DB now
# For free users

from DaisyX.config import get_str_key
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

MONGO2 = get_str_key("MONGO_URI_2", None)
MONGO = get_str_key("MONGO_URI", required=True)
if MONGO2 == None:
  MONGO2 = MONGO
  
mongo_client = MongoClient(MONGO2)
db = mongo_client.daisy
