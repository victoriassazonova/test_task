import mysql.connector


# функция создания базы данных и таблицы
def create_db(host_address, port_address, username, user_password):
    con = mysql.connector.connect(host=host_address, port=port_address, user=username, password=user_password)
    cur = con.cursor(dictionary=True)
    cur.execute("CREATE DATABASE IF NOT EXISTS chatbot;")
    con = mysql.connector.connect(host=host_address, port=port_address, database='chatbot',
                                  user=username, password=user_password)
    cur = con.cursor(dictionary=True)
    cur.execute("""CREATE TABLE IF NOT EXISTS chatbot_answers(
    id INT NOT NULL AUTO_INCREMENT,
    text_time DATETIME COMMENT 'Time of the message', 
    user_text VARCHAR(4) COMMENT 'Emoji of the user or TEXT if not an emoji',
    bot_answer VARCHAR(100) COMMENT 'Bot answer',
    PRIMARY KEY (id),
    UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE)
    COMMENT 'Table for user texts and bot answers with time';""")
    return cur


# фунция добавления записи в таблицу
def insert_into_db(text_time, user_text, bot_answer, host_address, port_address, username, user_password):
    con = mysql.connector.connect(host=host_address, port=port_address, database='chatbot', user=username,
                                  password=user_password)
    cur = con.cursor(dictionary=True)
    insert_line = f"INSERT INTO chatbot_answers (text_time, user_text, bot_answer) VALUES " \
                  f"('{text_time}', '{user_text}', '{bot_answer}')"
    cur.execute(insert_line)
    con.commit()
