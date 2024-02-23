from zte_l13 import ZTEL13
import configparser


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    host = config.get('ZTE', 'host')
    password = config.get('ZTE', 'password')
    zte_l13 = ZTEL13(host, password)
    if not zte_l13.login():
        print('Login failed')
    zte_l13.reboot()


if __name__ == '__main__':
    main()
