'''
    pass
'''
import hikari

from bot import __version__
from .helpers import brainfuck


class Bot(hikari.GatewayBot):
    '''
        pass
    '''

    def __init__(
            self,
            token: str,
            prefix: str
    ) -> None:
        '''
            pass
        '''
        self.PREFIX = prefix
        self.__TOKEN = token
        intents = hikari.Intents.ALL
        super().__init__(
            token=self.__TOKEN,
            intents=intents,
        )

    def setup(self) -> None:
        '''
            pass
        '''
        self.event_manager.subscribe(
            hikari.MessageCreateEvent,
            self.on_message
        )

    def run(self) -> None:
        '''
            pass
        '''
        self.setup()
        super().run(
            activity=hikari.Activity(
                name=f'hikari.bf {__version__}',
                type=hikari.ActivityType.LISTENING
            ),
            status=hikari.Status.IDLE,
        )

    async def on_message(self, event: hikari.MessageCreateEvent) -> None:
        '''
            pass
        '''
        if event.content.startswith(self.PREFIX):
            print(event.author)
            brainfuck.main()