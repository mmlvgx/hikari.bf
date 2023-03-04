''''''
import os


try:
    import hikari
    import crescent

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

    pass


if __name__ == "__main__":
    main()
