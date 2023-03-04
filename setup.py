''''''
import os

from bot.core import Bot
from config import BotConfig


try:
    import hikari

except ImportError:
    os.system('pip install -r requirements.txt')


def main() -> None:
    ''''''
    if os.name != 'nt':
        ''''''
        try:
            import uvloop
            uvloop.install()

        except ImportError:
            pass

    bot = Bot(BotConfig.TOKEN)

    bot.run()


if __name__ == "__main__":
    main()
