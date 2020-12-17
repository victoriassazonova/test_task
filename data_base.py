import mysql.connector


def create_db(host_address, port_address, username, user_password):
    con = mysql.connector.connect(host=host_address, port=port_address, user=username, password=user_password)
    cur = con.cursor(dictionary=True)
    cur.execute("CREATE DATABASE IF NOT EXISTS chatbot /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;")
    con = mysql.connector.connect(host=host_address, port=port_address, database='chatbot',
                                  user=username, password=user_password)
    cur = con.cursor(dictionary=True)
    cur.execute("""CREATE TABLE IF NOT EXISTS chatbot_answers(
    id INT NOT NULL AUTO_INCREMENT,
    text_time DATETIME, 
    user_text VARCHAR(4),
    bot_answer VARCHAR(100),
    PRIMARY KEY (id),
    UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE);""")
    return cur


def insert_into_db(text_time, user_text, bot_answer, host_address, port_address, username, user_password):
    con = mysql.connector.connect(host=host_address, port=port_address, database='chatbot', user=username,
                                  password=user_password)
    cur = con.cursor(dictionary=True)
    insert_line = f"INSERT INTO chatbot_answers (text_time, user_text, bot_answer) VALUES " \
                  f"('{text_time}', '{user_text}', '{bot_answer}')"
    cur.execute(insert_line)
    con.commit()
