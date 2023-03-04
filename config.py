import os

from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()


@dataclass
class BotConfig:
    TOKEN = os.environ.get('token')
    PREFIX = os.environ.get('prefix')
