#include <stdio.h>
#include <stdlib.h>
#include "graphe.h"

void initialiserGraphe(GRAPHE *g){
	g->nbS=0;        
	g->nbA=0;
	g->maxS=0;
	g->premierSommet=NULL;
	g->dernierSommet=NULL;
}

int ajouterSommet(GRAPHE *g, int info){
	SOMMET *pointeur = malloc(sizeof(SOMMET));
	g->maxS++;
	if (pointeur == NULL){
		printf("Erreur! Memoire insuffisante pour creer un sommet\n");
		return -1; 
	}
	pointeur->label=g->maxS;
	pointeur->info=info;
	pointeur->suivant=NULL;
	pointeur->adj=NULL;
	if (!g->nbS){
		g->premierSommet=pointeur;
		g->dernierSommet=pointeur;
	}
	else{
		g->dernierSommet->suivant=pointeur;
		g->dernierSommet=pointeur;
	}
	g->nbS++;

	return pointeur->label;
}

int ajouterArc(GRAPHE *g, int a, int b, int info)
{
	SOMMET *psommet, *psommet2;
	ELTADJ *padj, *precedent;
	psommet=g->premierSommet;

	/* on parcourt les sommets jusqu'a trouver a */
	while (psommet && psommet->label != a)
		psommet=psommet->suivant;

	if (!psommet){
		printf("Erreur! Creation d'un arc dont l'origine n'existe pas\n");
		return -1;
	}/* on a trouvé a */

	padj=psommet->adj;

	/* on parcourt les sommets pour trouver b */
	psommet2=g->premierSommet;
	while (psommet2 && psommet2->label != b)
		psommet2 = psommet2->suivant;

	if (!psommet2){
		printf("Erreur! Creation d'un arc dont l'extremite n'existe pas\n");
		return -2;
	}
	/* on a trouvé a et b */
	if (!padj){ /* la liste d'adjacence est vide */
		padj= malloc(sizeof(ELTADJ));
		if (!padj){
			printf("Erreur! Memoire insuffisante pour creer un sommet\n");
			return -3; 
		}
		psommet->adj=padj; /* premier element de la liste d'adjacence */
		padj->suivant=NULL;

		padj->dest = b;
		padj->info = info;
		g->nbA++;
		return 0;
	}
	/* la liste d'adjacence est non vide, on la parcourt pour voir si b s'y trouve */
	if (padj->dest > b){
		padj= malloc(sizeof(ELTADJ));
		if (!padj){
			printf("Erreur! Memoire insuffisante pour creer un sommet\n");
			return -3; 
		}
		padj->suivant=psommet->adj;
		psommet->adj=padj;
	}
	else{
		while (padj){
			if (padj->dest == b) {padj->info=info; break;} /* l'arc existe, update info */
			if (padj->dest > b) {padj=NULL; break;} /* on depasse b sans le trouver */
			precedent=padj;
			padj=padj->suivant;
		}
		if (!padj) /* l'arc n'existe pas, il faut le creer */{
			padj = malloc(sizeof(ELTADJ));
			if (!padj){
				printf("Erreur! Memoire insuffisante pour creer un sommet\n");
				return -3; 
			}
			if (!precedent->suivant) /* element ajouté a la fin */{
				precedent->suivant=padj;
				padj->suivant=NULL; 
			}
			else /* element ajouté "au milieu" pour garder ordre */{
				padj->suivant=precedent->suivant;
				precedent->suivant=padj; 
			}
		}
	}


	padj->dest=b;
	padj->info=info;
	g->nbA++;

	return 0;
}
	

int supprimerSommet(GRAPHE *g, int a){
	SOMMET *psommet, *precedent;
	ELTADJ *padj, *suivant, *precedent_adj;
	int flag_premier_sommet, flag_premier_arc;
	if (!g->premierSommet){
		printf("Erreur! Graphe vide, suppression impossible\n");
		return -1;
	}
	psommet=g->premierSommet;
	flag_premier_sommet=1;
	while (psommet && psommet->label != a){
		flag_premier_sommet=0;
		precedent=psommet;
		psommet=psommet->suivant;
	}
	if (!psommet){
		printf("Erreur! Le sommet a supprimer n'existe pas\n");
		return -1;
	}

	if (!psommet->suivant) 
		g->dernierSommet=precedent;
	
	if (flag_premier_sommet == 1) 
		g->premierSommet=psommet->suivant;
	else 
		precedent->suivant=psommet->suivant;
	padj=psommet->adj;
	free(psommet);
	g->nbS--;
	while (padj){
		suivant=padj->suivant;
		free(padj);
		g->nbA--;
		padj=suivant;
	}
	
	/* il faut aussi supprimer les arcs ayant le sommet a supprimer comme extremite */
	psommet=g->premierSommet;
	while (psommet){
		padj=psommet->adj;
		flag_premier_arc=1;
		while (padj && padj->dest != a){
			flag_premier_arc=0;
			precedent_adj=padj;
			padj=padj->suivant; 
		}
		if (padj){
			if (flag_premier_arc == 1) 
				psommet->adj=padj->suivant;
			else 
				precedent_adj->suivant=padj->suivant;
			free(padj);
			g->nbA--;
		}
		psommet=psommet->suivant;
	}
	return 0;
}

int supprimerArc(GRAPHE *g, int a, int b){
	SOMMET *psommet;
	ELTADJ *padj, *precedent_adj;
	int flag_premier_arc;

	if (!g->premierSommet){
		printf("Erreur! Graphe vide, suppression impossible\n");
		return -1;
	}
	psommet=g->premierSommet;
	while (psommet && psommet->label != a)
		psommet=psommet->suivant;

	if (!psommet){
		printf("Erreur! L'extremite de l'arc a supprimer n'existe pas\n");
		return -1;
	}

	padj=psommet->adj;
	flag_premier_arc=1;
	while (padj && padj->dest != b){
		flag_premier_arc=0;
		precedent_adj=padj;
		padj=padj->suivant; 
	}
	if (!padj){
		printf("Erreur! L'extremite de l'arc a supprimer n'existe pas\n");
		return -1;
	}

	if (flag_premier_arc == 1) 
		psommet->adj=padj->suivant;
	else 
		precedent_adj->suivant=padj->suivant;
	free(padj);
	g->nbA--;

	return 0;
}

void supprimerGraphe(GRAPHE *g){
	SOMMET *psommet,*temps;
	ELTADJ *padj,*tempadj;

	psommet=g->premierSommet;
	while (psommet){
		padj = psommet->adj;
		while (padj){
			tempadj=padj;
			padj=padj->suivant;
			free(tempadj);
		}
		temps=psommet;
		psommet=psommet->suivant;
		free(temps);
	}
	initialiserGraphe(g);
}

void afficherGraphe(GRAPHE *g){
	SOMMET *psommet;
	ELTADJ *padj;
	if (!g->premierSommet){ 
		printf("graphe vide\n");
		return ;
	}
	printf("nbS=%d , nbA=%d, label max.=%d\n", g->nbS, g->nbA, g->maxS);
	psommet=g->premierSommet;
	while (psommet){
		printf("\nSommet de label: %d , info: %d\n", psommet->label, psommet->info);
		if (!psommet->adj)
			printf(" -> ce sommet n'a aucun arc sortant\n ");
		else{
			padj = psommet->adj;
			while (padj){
				printf(" -> arc de %d vers %d avec l'info. %d \n", psommet->label, padj->dest, padj->info);
				padj = padj->suivant;
			}
		}
		printf("\n");
		psommet = psommet->suivant;
	}
	
}

int lireFichier(char *nomf, GRAPHE *g)
{
  FILE *fp;
  char ligne[MAX+1]; 
  int temp,i,j,nbS1,nbLigne,sommet,nbElt,creerArc;

	initialiserGraphe(g);
  fp=fopen(nomf,"r"); /* ouvre un fichier en lecture */
  nbLigne=0; /* compte les lignes du fichier */
  sommet=0; /* label du sommet en cours */
  nbS1=0; /* compte les sommets de la 1ere ligne */
  while (fgets(ligne,MAX,fp) != NULL){ 
	nbLigne++; /* compte le nombre de lignes du fichier */

	if (ligne[0] != '\n') /* on passe les lignes vides */
		{
			i=0; 
			if (nbS1 == 0) /* compte les sommets de la 1ere ligne */
			{
				nbS1=1; 
				while (ligne[i] != '\n'){
					if (ligne[i] == ',') 
						nbS1++;
					i++;
				}
				for (j=1; j<=nbS1; j++) 
					{
						ajouterSommet(g,0);
					}
				i=0; /* on relit la 1ere ligne */
			}
			
			sommet++; /* origine des arcs */
			nbElt=0; /* controle le nombre d'arcs crees */
			while (ligne[i] != '\n')
				{
					temp=0; /* va contenir l'extremite */
					creerArc=1;
					while (ligne[i] != ',' && ligne[i] != '\n')
						{
							while (ligne[i]==' ' || ligne[i]=='\t') {i++;}
							if ((ligne[i]>'9' || ligne[i]<'0') && ligne[i]!='x') 
								{
									printf("Erreur à la ligne %d !\n",nbLigne);
									supprimerGraphe(g);
									return -1; /* pas des chiffres ! */
								}
							if (ligne[i]=='x') creerArc=0;
							temp=10*temp+ligne[i]-'0';
							i++; 
							while (ligne[i]==' ' || ligne[i]=='\t') {i++;}
						}
					if (ligne[i] == ',') i++; 
					nbElt++;
					if (nbElt<=nbS1 && creerArc==1) ajouterArc(g,sommet,nbElt,temp); /* ligne pas trop longue */
				} 
			if (nbElt != nbS1) /* pas le bon nombre de champs sur ligne */
				{
					printf("Erreur à la ligne %d !\n",nbLigne);
					supprimerGraphe(g);
					return -1; /* pas le bon nombre de champs */
				}
		}
		}
  fclose(fp);
	return 0;
}

