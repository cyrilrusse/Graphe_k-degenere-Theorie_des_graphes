#include <stdio.h>
#include <stdlib.h>

#include "graphe.h"


int main(){
    GRAPHE *test = malloc(sizeof(GRAPHE));
    if(!test)
        return -1;
    
    initialiserGraphe(test);
    lireFichier("graphe_test.txt", test);
    afficherGraphe(test);
    supprimerGraphe(test);



    return 0;
}