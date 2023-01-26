from psycopg2 import *


class Badgeuse_psql:
    def __init__(self):
        self.conn = self.connect()
        self.cur = self.conn.cursor()
        # Si le tableau des users n'est pas encore créé dans la base de donnée psql:
        # self.cur.execute("CREATE TABLE users (id serial PRIMARY KEY, name varchar(150), last_name varchar(150),"
        #                 " password varchar(150), email varchar(150), peremption DATE DEFAULT CURRENT_DATE);")
        # Si le tableau des logs n'est pas encore créé dans la base de donnée psql:
        # self.cur.execute("CREATE TABLE logs (l serial PRIMARY KEY, id Numeric, name varchar(150), "
        #                 "last_name varchar(150), time TIME DEFAULT LOCALTIME(0), day DATE DEFAULT CURRENT_DATE);")
        # Si le tableau des waiting user n'est pas encore créée dans la base de donnée psql:
        # self.cur.execute("CREATE TABLE waiting_users (id serial PRIMARY KEY, name varchar(150), "
        #                 "last_name varchar(150), email varchar(150), peremption DATE DEFAULT CURRENT_DATE);")

    def connect(self):
        """Connecte le code à la base de données badgeuse stockée sur Always Data"""
        
        conn = connect(
            host="",
            port="",
            database="",
            user="",
            password="")
        return conn

    def f_add(self, n, l, p, e):
        """Rajoute un utilisateur à la table users. n = prénom, l = nom, p = password et e = email"""
        
        self.cur.execute("INSERT INTO users (name, last_name, password, email) VALUES (%s, %s, %s, %s)",
                         (n, l, p, e))

    def add_card(self, password):
        """Rajoute un utilisateur à la table users depuis la table waiting users puis supprime cet utilisateur de la
        table waiting users"""
        
        self.cur.execute(f"SELECT * FROM waiting_users;")
        x = self.cur.fetchall()
        name = x[0][1]
        last_name = x[0][2]
        email = x[0][3]
        peremption = x[0][4]
        self.cur.execute("INSERT INTO users (name, last_name, password, email, peremption) VALUES (%s, %s, %s, %s, %s)",
                         (name, last_name, password, email, peremption))
        self.cur.execute(f"DELETE FROM waiting_users WHERE id = {x[0][0]};")



    def add_user(self):
        """Rajoute un utilisateur à la table users en passant par la console."""
        
        name = input("Enter your first name:        ")
        last_name = input("Enter your last name:         ")
        password = input("Enter a password:             ")
        email = input("Enter your email:             ")
        self.cur.execute("INSERT INTO users (name, last_name, password, email) VALUES (%s, %s, %s, %s)",
                         (name, last_name, password, email))

    def check(self, password):
        """Regarde si la carte scannée est enregistrée dans la table users"""
        
        self.cur.execute(f"SELECT * FROM users WHERE password = '{password}';")
        x = self.cur.fetchall()
        print(x)
        if x == []:
                return False
        return True
        

    def check_card(self, password):
        """Renvoie les données associées à la carte de la table users."""
        
        try:
            self.cur.execute(f"SELECT * FROM users WHERE password = '{password}';")
            print(self.cur.fetchall())
        except:
            print("ERROR")

    def check_name(self, name):
        """Affiche les données associées au prénom dans la table users"""
        
        try:
            self.cur.execute(f"SELECT * FROM users WHERE name = '{name}';")
            print(self.cur.fetchall())
        except:
            print("ERROR")

    def check_lname(self, lname):
        """Affiche les données associées au nom dans la table users"""
        
        try:
            self.cur.execute(f"SELECT * FROM users WHERE last_name = '{lname}';")
            print(self.cur.fetchall())
        except:
            print("ERROR")

    def select_all(self):
        """Affiche toutes les informations de la table users"""
        
        self.cur.execute("SELECT * FROM users;")
        print(self.cur.fetchall())

    def card_c(self, password):
        """Rajoute aux logs la carte scannée"""
        
        self.cur.execute(f"SELECT id, name, last_name FROM users WHERE password = '{password}';")
        user = self.cur.fetchall()
        print(user)
        self.cur.execute(f"INSERT INTO logs (id, name, last_name) VALUES (%s, %s, %s)",
                         (user[0][0], user[0][1], user[0][2]))

    def root(self, data):
        """Renvoie True si la carte scannée est la carte qui a comme id associé 1 (la carte admin)"""
        
        self.cur.execute("SELECT password FROM users WHERE id = 1;")
        x = self.cur.fetchall()
        return data == x[0][0]

    def show_logs(self):
        """Affiche tous les logs"""
        
        self.cur.execute(f"SELECT * FROM logs;")
        print(self.cur.fetchall())

    def waiting(self):
        """Renvoie True si la table waiting_users n'est pas vide et False si elle est vide."""
        
        self.cur.execute(f"SELECT * FROM waiting_users;")
        x = self.cur.fetchall()
        if x == []:
            return False
        return True

    def test(self):
        """"Passe en mode test, permet de tester plusieurs fonctions de la badgeuse depuis la console python"""
        
        while True:
            x = int(input("Press 1 to enter a user, press 2 to see the list of the existing users, "
                          "press 3 to look if someone is in the database, press 4 to stop the programme.\n"))
            if x == 2:
                self.select_all()
            elif x == 1:
                self.add_user()
            elif x == 3:
                y = int(input("Press 1 to check a name, 2 to check a last name and 3 to check a password.\n"))
                if y == 1:
                    self.check_name(input("Enter your first name:    "))
                if y == 2:
                    self.check_lname(input("Enter your last name:    "))
                if y == 3:
                    self.check_card(input("Enter your password:      "))
            elif x == 4:
                break

    def commit(self):
        """Pour que les changements soient pris en compte par la base de données"""

        self.conn.commit()

    def stop(self):
        """Permet au code de se deconnecter de la base de données badgeuse"""
        
        self.cur.close()
        self.conn.close()
