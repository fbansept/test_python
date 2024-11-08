class Utilisateur :
    
    def __init__(self, nouvel_email, password) :
        self.email = nouvel_email
        self.password = password

    def mot_de_passe_securise(self) :
        return len(self.password) > 8