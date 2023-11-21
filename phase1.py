import argparse
import datetime
import json
import requests

def analyse_commande():
    parser = argparse.ArgumentParser(description="Extraction de valeurs historiques pour un"
                                     "ou plusieurs symboles boursiers.")
    parser.add_argument(
        nargs = "+",
        metavar = 'symbole',
        dest = 'symbole',
        default = "null",
        help="Nom d'un symbole boursier",
    )
    parser.add_argument(
        '-d', '--debut',
        metavar = 'DATE',
        dest = 'date_deb',
        default = None,
        help = "Date recherchée la plus ancienne (format: AAAA-MM-JJ)",
    )
    parser.add_argument(
        '-f', '--fin',
        metavar = 'DATE',
        dest = 'date_fin',
        default = datetime.datetime.now().strftime('%Y-%m-%d'),
        help = "date recherchée la plus récente (format: AAAA-MM-JJ)",
    )
    parser.add_argument(
        '-v', '--valeur',
        metavar = {'fermeture','ouverture','min','max','volume'},
        dest = 'valeur',
        default = 'fermeture',
        choices = ['fermeture','ouverture','min','max','volume'],
        help = "La valeur désirée (par défaut: fermeture)",
    )
    return parser.parse_args()

def historique_serveur(symbole, debut, fin):
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

    params = {
        'début': debut,
        'fin': fin,
    }
    réponse = requests.get(url=url, params=params)
    return json.loads(réponse.text)

def produire_historique(symbole, debut, fin, valeur):
    historique = historique_serveur(symbole, debut, fin)
    if historique is not None:
        for date, valeurs in historique.get('historique', {}).items():
            print(f'Date: {date}, Valeur ({valeur}): {valeurs[valeur]}')
            
args = analyse_commande()
print(f'titre = {args.symbole[0]}: valeur = {args.valeur}, debut = {args.date_deb}, fin = {args.date_fin}')

for symbole in args.symbole:
    produire_historique(symbole, args.date_deb, args.date_fin, args.valeur)

