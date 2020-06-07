import json
from datetime import datetime

class Manipulation_data:
	def depots_etoiles():
		liste =[]
		with open('all.json') as json_data:
			data_dict = json.load(json_data)
			print("Les 10 depots les plus etoiles qui ont ete mis à jour il y a moins d'un mois\n")
			for dict in data_dict:
				date_derniere_maj = datetime.strptime(dict.get("derniere_mise_a_jour"), "%Y-%m-%dT%H:%M:%SZ")
				duree = datetime.now() - date_derniere_maj
				if (duree.days<31):
					liste.append(dict)
			liste = sorted (liste, key =lambda elem: elem.get("nombre_stars"))
			taille =len(liste)
			i = taille - 10
			while i<taille :
				print(liste[i].get("nom"), "\n\tOrganisation : ",liste[i].get("organisation_nom"), "\n\tEtoiles : ", liste[i].get("nombre_stars"), "\n\tLien URL : ", liste[i].get("repertoire_url"), "\n *** \n")
				i = i + 1
		return liste


	def orga_modif_recentes():
		liste =[]
		liste_sans_doublons = []
		with open('all.json') as json_data:
			data_dict = json.load(json_data)
			print("Les organisation ayant modifie des depots dans le 7 derniers jours\n")
			for dict in data_dict:
				date_derniere_maj = datetime.strptime(dict.get("derniere_mise_a_jour"), "%Y-%m-%dT%H:%M:%SZ")
				duree = datetime.now() - date_derniere_maj
				if (duree.days<8):
					liste.append(dict)
			taille =len(liste)
			i = 0
			while i<taille :
				if (liste[i].get("organisation_nom")) not in liste_sans_doublons:
					liste_sans_doublons.append(liste[i].get("organisation_nom"))
					print("Organisation : ",liste[i].get("organisation_nom"), "\n\tDate mise a jour : ", liste[i].get("derniere_mise_a_jour"), "\n *** \n")
				i = i + 1
		return liste_sans_doublons
