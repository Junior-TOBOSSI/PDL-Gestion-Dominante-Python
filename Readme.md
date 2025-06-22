*Projet de Développement Logiciel*

**Tables des matières**
1. [Description](#Description)
2. [Fonctionnalites](#fonctionnalites)
3. [Utilisations](#utilisations)
4. [Auteurs](#auteurs)

---

## Description
	Un logiciel simple pour permettre 
	Aux administrateurs de gérer les inscriptions en dominantes 
	Aux étudiants d'effectuer et de consulter leurs choix.

## Fonctionnalites  

* Ce que les étudiants peuvent faire :  

	 Faire les choix qui lui plait.   
	 Effectuer que lorqu'il est dans les délais paramétrés par l'administrateur. 
	 Voir les choix qui lui sont attribués une fois le traitement terminé.  
	 Modifier dans son profil uniquement son mot de passe.
	 Un étudiant classique peut faire 5 choix au maximum et un apprenti 2.  
    
  
* Ce que les administrateurs peuvent faire :  

	 Ajouter un nouvel étudiant ou créer une nouvelle dominante.    
	 Modifier les informations concernant les dominantes, les étudiants et les étapes de traitement.   
	 Supprimer une dominante ou un étudiant.  
	 Consulter la liste des étudiants, la liste des dominantes et la liste des étapes    
	 Lancer le traitement automatique pour la répartition des étudiants dans les dominantes  
	 Forcer l'inscription des étudiants dans une dominante  
   
## Utilisations  

	* Connection : A travers un identifiant et un mot de passe
	* Modification et déconnexion : A travers un clique sur l'icone en haut à gauche de l'interface
	
	* Etudiants
		- Choix des dominantes : 
			L'étudiant clique sur le bouton "Choix" depuis l'interface d'acceuil (acessible uniquement après connexion) 
			Ou depuis le menu de navigation de son interface
			Pour faire un choix,             -> appuie sur la dominante
			Pour faire reprendre un choix    -> appuie sur le bouton reprendre
			Pour valider ses choix           -> appuie sur le bouton valider
		- Voir ses choix : 
		    Une fois que l'étudiant a fait ses choix, il peut les consulter en cliquant sur le même bouton "Choix"
		- Voir sa dominante : 
		    L'étudiant clique sur le bouton "Dominante Finale" depuis l'interface d'acceuil (acessible uniquement après connexion) 
			Ou depuis le menu de navigation de son interface
			Si le traitement est déjà fait, il verra sa dominante sinon il lui sera demander de patienter
			
	* Administrateur
	    - Consulter les étudiants ou les dominantes ou les étapes :
	      L'administrateur clique sur le bouton "Etudiants" ou "Dominantes" ou "Etapes" depuis l'interface d'acceuil (accessible uniquement après connexion)
	      Ou depuis le menu de navigation de son interface
	    - Ajouter un étudiant (ou une dominante) :
	      Appuie sur le bouton + situé sur l'interface de consulter Etudiant (ou Dominante)
	      Remplir les champs de saisie
	      Appuyer sur le bouton "Valider"
	    - Supprimer un étudiant (ou une dominante) :
	      Selection de la ligne concernée par la suppression
	      Appuie sur le bouton "poubelle" situé sur l'interface de consulter Etudiant (ou Dominante)
	    - Modifier un étudiant (ou une dominante) :
	      Double clique sur la cellule à modifier
	      Mettre la nouvelle valeur et sortir du champ de saisie
	      Selectionner la ligne modifiée
	      Clique sur le bouton "v" pour valider
	    - Modifier la date d'une étape
	      Etre sur l'interface consulter Etape si ce n'est pas le cas
	      Double clique sur la cellule a modifier
	      Mettre la nouvelle valeur en respectant le format et sortir du champ
	      Selectionner la ligne modifier
	      Clique sur le bouton "v" pour valider
	       - Voir le positionnement en dominantes :
	      Etre sur l'interface consulter Dominante si ce n'est pas encore le cas
	      Selectionner la ligne de la dominante voulu
	      Clique sur le bouton "voir" 
	    - Forcer l'inscription en dominante :
	      Etre sur l'interface consulter Etudiant si ce n'est pas encore le cas
	      Appuie sur le bouton "Forcer inscription
	      Pour insérer un étudiant dans une dominante, il faut 
	      			-> Sélectionner sur la ligne de l'étudiant
	      			-> Sélectionner sur la ligne de la dominante
	      			-> Cliquer sur le bouton "insérer"
	     - Lancer le traitement automatique
	       Etre sur l'inteface consulter Etape si ce n'est pas encore le cas
	       Sélectionner 4 ou 7 selon le fait que l'on veut lancer le traitement pour les FISE ou les FISA
	       Appuyer sur le bouton "Lancer"
	       (Les détails du traitement est affiché en console)

	
## Auteurs 
 
	    Hilary BOCO - Gilbert TOBOSSI 
	
