'''
    pass
'''
import os

import hikari
import brainfuck

from bot import __version__


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
        self.__PREFIX = prefix
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
        path = os.getcwd()
        # If message content starts with prefix
        if event.content.startswith(self.__PREFIX):
            # Check each file from the directory with plugins
            for file__ in os.listdir(f'{path}/bot/plugins/'):
                # Ignore file if not ends with brainfuck format
                if not file__.endswith('.bf'):
                    return

                _format = self.__PREFIX + file__[:-3]

                if event.content.startswith(_format):
                    with open(f'{path}/bot/plugins/' + file__, 'r') as file_:
                        code = str(file_.read().encode('utf-8'))
                        content = brainfuck.evaluate(code)

                        await event.message.respond(content, reply=True)
