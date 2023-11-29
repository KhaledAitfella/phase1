import phase1
import datetime
import ErreurDate
class Bourse:
    def prix(self, symbole, date = datetime.datetime.now().strftime('%Y-%m-%d')):
        if date > datetime.datetime.now().strftime('%Y-%m-%d'):
            raise ErreurDate("La date specifiee est superieure a la date actuel")
        historique_du_serveur = phase1.obtenir_historique_du_serveur(symbole)
        return historique_du_serveur.get['historique'][date]['fermeture']
        
        
        