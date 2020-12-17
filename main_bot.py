import chat_bot
import data_base


def main():
    data_base.create_db('127.0.0.1', 3306, 'root', '{Password}')
    chat_bot.chat_bot('127.0.0.1', 3306, 'root', '{Password}')

if __name__ == '__main__':
    main()
