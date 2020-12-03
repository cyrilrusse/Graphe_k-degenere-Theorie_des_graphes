### 
## Makefile
## MATH0499: Projet
## RANDAXHE Martin && RUSSE Cyril
## 
### 

## Variables

# Tools & flags
CC = gcc
CFLAGS = --std=c99 --pedantic -Wall -Wextra -Wmissing-prototypes -DNDEBUG 
LD = gcc
LDFLAGS =

# Files
EXEC = exec_tdg

MODULES_LISTESET = main.c graphe.c
OBJECTS_LISTESET = main.o graphe.o



## Rules

#compilation

make: $(OBJECTS_LISTESET)
	$(LD) -o $(EXEC) $(OBJECTS_LISTESET) $(LDFLAGS) -lm



main.o: main.c
	$(CC) -c main.c -o main.o $(CFLAGS)

graphe.o: graphe.c
	$(CC) -c graphe.c -o graphe.o $(CFLAGS)



#rapport
rapport:all_rapport clean_log_aux

all_rapport:
	cd ../rapport && pdflatex tad-RusseCyril.tex

clean_log_aux:
	cd ../rapport && rm -f tad-RusseCyril.aux tad-RusseCyril.log tad-RusseCyril.toc

clean_rapport: clean_log_aux
	cd ../rapport && rm -f tad-RusseCyril.pdf

#création archive
archive:
	cd .. && tar -zcvf demineur_01.tar.gz source rapport doc

#supp fichiers objets + executable
clean:
	rm -f *.o $(EXEC)