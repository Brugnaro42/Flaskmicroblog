from app import db 

class User(db.Model):
    #Classe criada para modelar o banco de dados
    id = db.Column(db.Integer)