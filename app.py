import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

venteparproduit = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')

données['ca'] = données['prix'] * données['qte']

chiffreaffaireparproduit = px.bar(données, x='produit', y='ca', title="Chiffre d'affaires par produit")

figure.write_html('ventes-par-region.html')
venteparproduit.write_html('ventes-par-produit.html')
chiffreaffaireparproduit.write_html('chiffre-affaire-produit.html')

print('Fichier HTML générés !')
