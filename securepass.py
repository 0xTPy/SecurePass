import os
import random
import argparse

ct = ["&","#","{","|","^","@","]","}","[","~","`","*","§","$","¤","%","-"]
cf = ["0","1","2","3","4","5","6","7","8","9"]
ab = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
maj = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def generate(nb):
	tout = ct + cf + ab + maj
	mdp = ""
	
	for i in range(nb):
		mdp += random.choice(tout)
	print("")
	print("Le mot de passe est : ", mdp)
	print("")
	
def check(mdp):
	n_ct = sum(1 for c in mdp if c in ct)
	n_cf = sum(1 for c in mdp if c in cf)
	n_ab = sum(1 for c in mdp if c in ab)
	n_maj = sum(1 for c in mdp if c in maj)
	
	print("")
	print(f"Symboles : {n_ct} | Chiffres : {n_cf} | Lettres : {n_ab} | Majuscules : {n_maj}")
	print("")
	
	if len(mdp) < 8:
		print("")
		print("Le mot de passe est FAIBLE")
		print("")

	elif (n_cf == 0 or n_ab == 0 or n_maj ==0 or n_ct == 0) and len(mdp) < 10:
		print("")
		print("Le mot de passe est MOYEN")
		print("")
	
	elif (n_cf == 0 or n_ab == 0 or n_maj == 0 or n_ct == 0):
		print("")
		print("MOYEN")
			
	elif len(mdp) < 12:
		print("")
		print("Le mot de passe est BON")
		print("")

	else:
		print("")
		print("Le mot de passe est ROBUSTE")
		print("")

analy = argparse.ArgumentParser(description="Générateur et vérificateur de mot de passe")
analy2 = analy.add_subparsers(dest="commande")

gen_mdp = analy2.add_parser("gen", help="Générer un mot de passe")
gen_mdp.add_argument("--long", type=int, required=True, metavar="nombre", help="Longueur du mot de passe")

verif_mdp = analy2.add_parser("verif", help="Vérifier un mot de passe")
verif_mdp.add_argument("motdepasse", metavar="motdepasse", help="Le mot de passe à vérifier")

args = analy.parse_args()

if args.commande == "gen":
	generate(args.long)
elif args.commande == "verif":
	check(args.motdepasse)
