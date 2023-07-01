import csv
import random
import string
import os.path

def generer_mot_de_passe():
    caracteres = string.ascii_letters + string.digits
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(20))
    return mot_de_passe

def enregistrer_mot_de_passe(nom_site, mot_de_passe):
    existe = os.path.isfile('mdp.csv')

    with open('mdp.csv', 'a', newline='') as csvfile:
        fieldnames = ['nom', 'mot_de_passe']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not existe:
            writer.writeheader()

        writer.writerow({'nom': nom_site, 'mot_de_passe': mot_de_passe})

nom_site = ""
while nom_site != "end" :
    nom_site = input("Entrez le nom du site : ")
    if nom_site != "end" :
        mot_de_passe = generer_mot_de_passe()
        enregistrer_mot_de_passe(nom_site, mot_de_passe)
        print("Mot de passe enregistré avec succès dans le fichier CSV.")


#                                               
#                                                ██████████████                          
#                                        ████████▓▓▓▓██░░░░██▓▓████                      
#                                ████████░░░░░░░░██▓▓██░░░░██▓▓▓▓▓▓██                    
#                            ████░░██▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                        ████░░░░░░░░██▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                      ██▓▓▓▓██░░░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                        
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                            
#                      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                                
#                          ████████▓▓▓▓▓▓▓▓▓▓▓▓██████                                    
#                                  ████████████           