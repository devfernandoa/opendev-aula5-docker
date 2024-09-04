import sqlite3

def create_database():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    # Criação da tabela USER
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS USER (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL UNIQUE,
        pass TEXT NOT NULL,
        type TEXT NOT NULL
    )
    ''')
    # Adiciona um usuário admin com senha criptografada em MD5
    cursor.execute('''
    INSERT OR IGNORE INTO USER (user, pass, type)
    VALUES ('admin', '21232f297a57a5a743894a0e4a801fc3', 'admin')
    ''')
    # Criação da tabela QUIZ
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS QUIZ (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        release TEXT NOT NULL,
        expire TEXT NOT NULL,
        problem TEXT NOT NULL,
        tests TEXT NOT NULL,
        results TEXT NOT NULL,
        diagnosis TEXT NOT NULL,
        numb INTEGER NOT NULL
    )
    ''')
    # Criação da relação USERQUIZ
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS USERQUIZ (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER NOT NULL,
        quizid INTEGER NOT NULL,
        sent TEXT NOT NULL,
        answer TEXT NOT NULL,
        result TEXT NOT NULL,
        FOREIGN KEY (userid) REFERENCES USER(id),
        FOREIGN KEY (quizid) REFERENCES QUIZ(id)
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()