import sys
import configparser
from pathlib import Path
from zte_l13 import ZTEL13


def main():
    config = configparser.ConfigParser()
    config.read(Path(__file__).parent.parent / 'config.ini')
    host = config.get('ZTE', 'host')
    password = config.get('ZTE', 'password')
    zte_l13 = ZTEL13(host, password)
    if not zte_l13.login():
        print('Login failed')
        sys.exit(1)
    zte_l13.reboot()


if __name__ == '__main__':
    main()
