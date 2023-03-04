'''
    Bot configuration module
'''
import os

from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()


@dataclass
class BotConfig:
    # Discord Bot authorization token
    TOKEN = os.environ.get('token')
    # Discord Bot prefix
    PREFIX = os.environ.get('prefix')
