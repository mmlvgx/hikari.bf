'''
    Bot Core Module
'''
import os

import hikari
import brainfuck

from bot import __version__


class Bot(hikari.GatewayBot):
    '''
        This is the main class for the Discord Bot.
    '''

    def __init__(
            self,
            token: str,
            prefix: str
    ) -> None:
        '''
            The constructor for Bot class.\n

            Parameters:\n
            token (str): Discord Bot authorization token.\n
            prefix (str): Discord Bot prefix.
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
            Pre-run setup
        '''
        self.event_manager.subscribe(
            hikari.MessageCreateEvent,
            self.on_message
        )

    def run(self) -> None:
        '''
            Shell of the inherited run method with setup
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
            Method responding to MessageCreateEvent
        '''
        path = os.getcwd()
        # If message content starts with prefix
        #   Example:
        #   !test
        #   ^ prefix
        if event.content.startswith(self.__PREFIX):
            # Check each file from the directory with plugins
            #   Example:
            #   /bot/plugins/
            #   /bot/plugins/test.bf
            #                ^^^^^^^ plugin
            for file__ in os.listdir(f'{path}/bot/plugins/'):
                # Ignore file if not ends with brainfuck format
                if not file__.endswith('.bf'):
                    return
                #   Example:
                #   !test
                #    ^^^^ file__[:-3]
                #   ^ prefix
                _format = self.__PREFIX + file__[:-3]

                if event.content.startswith(_format):
                    with open(f'{path}/bot/plugins/' + file__, 'r') as file_:
                        code = str(file_.read().encode('utf-8'))
                    # Converting code to content
                    content = brainfuck.evaluate(code)
                    # Sending message
                    await event.message.respond(content, reply=True)
