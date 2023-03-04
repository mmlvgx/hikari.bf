# hikari.bf
[Discord](https://discord.com/) bot template written in Python3 using [Hikari](https://github.com/hikari-py/hikari) framework with **Brainfuck** commands.
## Using
1. Clone the repository
2. Create a .env file
```
token = 'YOUR BOT TOKEN'
prefix = 'YOUR BOT PREFIX'
```
3. Launch run.sh or run.bat
The necessary dependencies will be automatically installed
## Extending
To add commands just add files to the `plugins` folder. The name of a **Brainfuck** like file is the name of command. So that for example `test.bf` will be `!test`
## Speed up
If you use a UNIX-like system, you will get additional performance benefits from using a library called uvloop. This replaces the default asyncio event loop with one that uses libuv internally.\
`pip install uvloop`
# Support
My discord is `лось#2600`
# Contributing
Create an issue for your feature

![](https://cdn.discordapp.com/attachments/913529716521173003/1081552792465985556/hippo.gif)
