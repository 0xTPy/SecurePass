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
	print("The password is : ", mdp)
	print("")
	
def check(mdp):
	n_ct = sum(1 for c in mdp if c in ct)
	n_cf = sum(1 for c in mdp if c in cf)
	n_ab = sum(1 for c in mdp if c in ab)
	n_maj = sum(1 for c in mdp if c in maj)
	
	print("")
	print(f"Symbols : {n_ct} | Numbers : {n_cf} | Letters : {n_ab} | Capital letters : {n_maj}")
	print("")
	
	if len(mdp) < 8:
		print("")
		print("The password is WEAK")
		print("")

	elif (n_cf == 0 or n_ab == 0 or n_maj ==0 or n_ct == 0) and len(mdp) < 10:
		print("")
		print("The password is MEDIUM")
		print("")
	
	elif (n_cf == 0 or n_ab == 0 or n_maj == 0 or n_ct == 0):
		print("")
		print("The password is MEDIUM")
			
	elif len(mdp) < 12:
		print("")
		print("The password is CORRECT")
		print("")

	else:
		print("")
		print("The password is STRONG")
		print("")

analy = argparse.ArgumentParser(description="Password generator and checker")
analy2 = analy.add_subparsers(dest="command")

gen_mdp = analy2.add_parser("gen", help="Generate a password")
gen_mdp.add_argument("--len", type=int, required=True, metavar="number", help="Password length")

verif_mdp = analy2.add_parser("verif", help="Verify a password")
verif_mdp.add_argument("password", metavar="password", help="The password to verify")

args = analy.parse_args()

if args.commande == "gen":
	generate(args.len)
elif args.commande == "verif":
	check(args.password)
