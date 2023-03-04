# hikari.bf

## Use
1. Clone the repository
2. Create a .env file
```
token = 'YOUR BOT TOKEN'
prefix = 'YOUR BOT PREFIX'
```
3. Launch run.sh or run.bat
The necessary dependencies will be automatically installed
## Speed up
If you use a UNIX-like system, you will get additional performance benefits from using a library called uvloop. This replaces the default asyncio event loop with one that uses libuv internally.\
`pip install uvloop`
