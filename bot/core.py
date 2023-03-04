'''
    pass
'''
import hikari


class Bot(hikari.GatewayBot):
    '''
        pass
    '''

    def __init__(
            self,
            token: str
    ) -> None:
        '''
            pass
        '''
        intents = hikari.Intents.GUILD_MESSAGES
        super().__init__(
            token=token,
            intents=intents
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
                name='https://github.com/mmlvgx/hikari.bf',
                type=hikari.ActivityType.LISTENING
            ),
            status=hikari.Status.IDLE,
        )

    async def on_message(self, event: hikari.MessageCreateEvent) -> None:
        '''
            pass
        '''
        print(event.author)
