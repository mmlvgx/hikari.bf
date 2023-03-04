'''
    Bot setup module
'''
import os

from bot.core import Bot
from config import BotConfig


try:
    import hikari

except ImportError:
    # Install dependencies if not
    os.system('pip install -r requirements.txt')


def main() -> None:
    '''
        Main process
    '''
    if os.name != 'nt':
        # If a UNIX-like system is used
        # It is possible to replace
        # the standard asyncio with libuv uvloop
        try:
            import uvloop
            uvloop.install()

        except ImportError:
            pass

    bot = Bot(BotConfig.TOKEN, BotConfig.PREFIX)

    bot.run()


if __name__ == "__main__":
    main()
