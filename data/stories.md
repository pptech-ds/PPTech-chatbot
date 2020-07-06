### CATALOGUE ###

## demarrer
* demarrer
    - utter_demarrer

## aider
* aide
    - utter_aider

## bonjour
* bonjour
    - utter_bonjour

## aurevoir
* aurevoir
    - utter_aurevoir

## hors_sujet
* hors_sujet
    - utter_hors_sujet

## definition
* definition
    - action_definition

## traduction
* traduction
    - action_traduction

## wikipedia
* wikipedia
    - action_wikipedia

## conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation


### RECHERCHER STANDALONE ###

## trouver
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"reussie"}
    - slot{"recherche":"reussie"}
    - slot{"relance":"false"}

## ne pas trouver
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"echouee"}
    - slot{"recherche":"echouee"}
    - slot{"relance":"false"}


### RECHERCHE COMBOS ###

### demarrer

## demarrer + trouver
* demarrer
    - utter_demarrer
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"reussie"}
    - slot{"recherche":"reussie"}
    - slot{"relance":"false"}

## demarrer + ne pas trouver
* demarrer
    - utter_demarrer
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"echouee"}
    - slot{"recherche":"echouee"}
    - slot{"relance":"false"}

### aider

## aider + trouver
* aide
    - utter_aider
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"reussie"}
    - slot{"recherche":"reussie"}
    - slot{"relance":"false"}

## aider + ne pas trouver
* aide
    - utter_aider
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"echouee"}
    - slot{"recherche":"echouee"}
    - slot{"relance":"false"}

### bonjour

## bonjour + trouver
* bonjour
    - utter_bonjour
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"reussie"}
    - slot{"recherche":"reussie"}
    - slot{"relance":"false"}

## bonjour + ne pas trouver
* bonjour
    - utter_bonjour
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"echouee"}
    - slot{"recherche":"echouee"}
    - slot{"relance":"false"}

### traduction

## traduction + trouver
* traduction
    - action_traduction
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"reussie"}
    - slot{"recherche":"reussie"}
    - slot{"relance":"false"}

## traduction + ne pas trouver
* traduction
    - action_traduction
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"echouee"}
    - slot{"recherche":"echouee"}
    - slot{"relance":"false"}

### wikipedia

## wikipedia + trouver
* wikipedia
    - action_wikipedia
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"reussie"}
    - slot{"recherche":"reussie"}
    - slot{"relance":"false"}

## wikipedia + ne pas trouver
* wikipedia
    - action_wikipedia
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"reussie"}
    - slot{"recherche":"reussie"}
    - slot{"relance":"false"}

### conversation

## conversation + trouver
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"reussie"}
    - slot{"recherche":"reussie"}
    - slot{"relance":"false"}

## conversation + ne pas trouver
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* recherche
    - utter_recherche
    - action_rechercher{"recherche":"echouee"}
    - slot{"recherche":"echouee"}
    - slot{"relance":"false"}


### DEMARRER ###

## demarrer + aider
* demarrer
    - utter_demarrer
* aide
    - utter_aider

## demarrer + bonjour
* demarrer
    - utter_demarrer
* bonjour
    - utter_bonjour

## demarrer + aurevoir
* demarrer
    - utter_demarrer
* aurevoir
    - utter_aurevoir

## demarrer + conversation
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## demarrer + hors_sujet
* demarrer
    - utter_demarrer
* hors_sujet
    - utter_hors_sujet

## demarrer + traduction
* demarrer
    - utter_demarrer
* traduction
    - action_traduction

## demarrer + wikipedia
* demarrer
    - utter_demarrer
* wikipedia
    - action_wikipedia

## demarrer + aider + bonjour
* demarrer
    - utter_demarrer
* aide
    - utter_aider
* bonjour
    - utter_bonjour

## demarrer + aider + aurevoir
* demarrer
    - utter_demarrer
* aide
    - utter_aider
* aurevoir
    - utter_aurevoir

## demarrer + aider + conversation
* demarrer
    - utter_demarrer
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## demarrer + aider + hors_sujet
* demarrer
    - utter_demarrer
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet

## demarrer + aider + traduction
* demarrer
    - utter_demarrer
* aide
    - utter_aider
* traduction
    - action_traduction

## demarrer + aider + wikipedia
* demarrer
    - utter_demarrer
* aide
    - utter_aider
* wikipedia
    - action_wikipedia

## demarrer + bonjour + aider
* demarrer
    - utter_demarrer
* bonjour
    - utter_bonjour
* aide
    - utter_aider

## demarrer + bonjour + aurevoir
* demarrer
    - utter_demarrer
* bonjour
    - utter_bonjour
* aurevoir
    - utter_aurevoir

## demarrer + bonjour + conversation
* demarrer
    - utter_demarrer
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## demarrer + bonjour + hors_sujet
* demarrer
    - utter_demarrer
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet

## demarrer + bonjour + traduction
* demarrer
    - utter_demarrer
* bonjour
    - utter_bonjour
* traduction
    - action_traduction

## demarrer + bonjour + wikipedia
* demarrer
    - utter_demarrer
* bonjour
    - utter_bonjour
* wikipedia
    - action_wikipedia

## demarrer + conversation + aider
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## demarrer + conversation + bonjour
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## demarrer + conversation + aurevoir
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## demarrer + conversation + conversation
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## demarrer + conversation + hors_sujet
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## demarrer + conversation + aider
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## demarrer + conversation + bonjour
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## demarrer + conversation + aurevoir
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## demarrer + conversation + conversation
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## demarrer + conversation + hors_sujet
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## demarrer + conversation + traduction
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## demarrer + conversation + wikipedia
* demarrer
    - utter_demarrer
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## demarrer + hors_sujet + aider
* demarrer
    - utter_demarrer
* hors_sujet
    - utter_hors_sujet
* aide
    - utter_aider

## demarrer + hors_sujet + bonjour
* demarrer
    - utter_demarrer
* hors_sujet
    - utter_hors_sujet
* bonjour
    - utter_bonjour

## demarrer + hors_sujet + aurevoir
* demarrer
    - utter_demarrer
* hors_sujet
    - utter_hors_sujet
* aurevoir
    - utter_aurevoir

## demarrer + hors_sujet + conversation
* demarrer
    - utter_demarrer
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## demarrer + hors_sujet + conversation
* demarrer
    - utter_demarrer
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## demarrer + hors_sujet + traduction
* demarrer
    - utter_demarrer
* hors_sujet
    - utter_hors_sujet
* traduction
    - action_traduction

## demarrer + hors_sujet + wikipedia
* demarrer
    - utter_demarrer
* hors_sujet
    - utter_hors_sujet
* wikipedia
    - action_wikipedia


### AIDER ###

## aider + bonjour
* aide
    - utter_aider
* bonjour
    - utter_bonjour

## aider + aurevoir
* aide
    - utter_aider
* aurevoir
    - utter_aurevoir

## aider + conversation
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## aider + hors_sujet
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet

## aider + traduction
* aide
    - utter_aider
* traduction
    - action_traduction

## aider + wikipedia
* aide
    - utter_aider
* wikipedia
    - action_wikipedia

## aider + bonjour + aurevoir
* aide
    - utter_aider
* bonjour
    - utter_bonjour
* aurevoir
    - utter_aurevoir

## aider + bonjour + conversation
* aide
    - utter_aider
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## aider + bonjour + hors_sujet
* aide
    - utter_aider
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet

## aider + bonjour + traduction
* aide
    - utter_aider
* bonjour
    - utter_bonjour
* traduction
    - action_traduction

## aider + bonjour + wikipedia
* aide
    - utter_aider
* bonjour
    - utter_bonjour
* wikipedia
    - action_wikipedia

## aider + conversation + bonjour
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## aider + conversation + aurevoir
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## aider + conversation + conversation
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## aider + conversation + hors_sujet
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## aider + conversation + bonjour
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## aider + conversation + aurevoir
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## aider + conversation + conversation
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## aider + conversation + hors_sujet
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## aider + conversation + traduction
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## aider + conversation + wikipedia
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## aider + hors_sujet + bonjour
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet
* bonjour
    - utter_bonjour

## aider + hors_sujet + aurevoir
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet
* aurevoir
    - utter_aurevoir

## aider + hors_sujet + conversation
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## aider + hors_sujet + traduction
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet
* traduction
    - action_traduction

## aider + hors_sujet + wikipedia
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet
* wikipedia
    - action_wikipedia


### BONJOUR ###

## bonjour + aider
* bonjour
    - utter_bonjour
* aide
    - utter_aider

## bonjour + aurevoir
* bonjour
    - utter_bonjour
* aurevoir
    - utter_aurevoir

## bonjour + conversation
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## bonjour + hors_sujet
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet

## bonjour + traduction
* bonjour
    - utter_bonjour
* traduction
    - action_traduction

## bonjour + wikipedia
* bonjour
    - utter_bonjour
* wikipedia
    - action_wikipedia

## bonjour + aider + aurevoir
* bonjour
    - utter_bonjour
* aide
    - utter_aider
* aurevoir
    - utter_aurevoir

## bonjour + aider + saluer
* bonjour
    - utter_bonjour
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## bonjour + aider + hors_sujet
* bonjour
    - utter_bonjour
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet

## bonjour + aider + traduction
* bonjour
    - utter_bonjour
* aide
    - utter_aider
* traduction
    - action_traduction

## bonjour + aider + wikipedia
* bonjour
    - utter_bonjour
* aide
    - utter_aider
* wikipedia
    - action_wikipedia

## bonjour + conversation + aider
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## bonjour + conversation + aurevoir
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## bonjour + conversation + conversation
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## bonjour + conversation + hors_sujet
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## bonjour + conversation + aider
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## bonjour + conversation + aurevoir
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## bonjour + conversation + saluer
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer
    - utter_saluer

## bonjour + conversation + hors_sujet
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## bonjour + conversation + traduction
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## bonjour + conversation + wikipedia
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## bonjour + hors_sujet + aider
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet
* aide
    - utter_aider

## bonjour + hors_sujet + aurevoir
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet
* aurevoir
    - utter_aurevoir

## bonjour + hors_sujet + conversation
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## bonjour + hors_sujet + traduction
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet
* traduction
    - action_traduction

## bonjour + hors_sujet + wikipedia
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet
* wikipedia
    - action_wikipedia


### CONVERSATION ###

## conversation + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## conversation + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## conversation + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## conversation + insulter
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* insulter
    - utter_insulter

## conversation + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## conversation + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## conversation + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## conversation + aider + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* bonjour
    - utter_bonjour

## conversation + aider + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* aurevoir
    - utter_aurevoir

## conversation + aider + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + aider + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet

## conversation + aider + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* traduction
    - action_traduction

## conversation + aider + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* wikipedia
    - action_wikipedia

## conversation + bonjour + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* aide
    - utter_aider

## conversation + bonjour + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* aurevoir
    - utter_aurevoir

## conversation + bonjour + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + bonjour + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet

## conversation + bonjour + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* traduction
    - action_traduction

## conversation + bonjour + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* wikipedia
    - action_wikipedia

## conversation + conversation + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## conversation + conversation + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## conversation + conversation + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## conversation + conversation + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## conversation + conversation + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## conversation + conversation + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## conversation + hors_sujet + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* aide
    - utter_aider

## conversation + hors_sujet + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* bonjour
    - utter_bonjour

## conversation + hors_sujet + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* aurevoir
    - utter_aurevoir

## conversation + hors_sujet + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + hors_sujet + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* traduction
    - action_traduction

## conversation + hors_sujet + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* wikipedia
    - action_wikipedia


### IDENTITE ###

## conversation + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## conversation + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## conversation + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## conversation + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## conversation + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## conversation + wikiepdia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## conversation + aider + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* bonjour
    - utter_bonjour

## conversation + aider + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* aurevoir
    - utter_aurevoir

## conversation + aider + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + aider + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet

## conversation + aider + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* traduction
    - action_traduction

## conversation + aider + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider
* wikipedia
    - action_wikipedia

## conversation + bonjour + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* aide
    - utter_aider

## conversation + bonjour + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* aurevoir
    - utter_aurevoir

## conversation + bonjour + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + bonjour + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet

## conversation + bonjour + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* traduction
    - action_traduction

## conversation + bonjour + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour
* wikipedia
    - action_wikipedia

## conversation + conversation + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## conversation + conversation + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## conversation + conversation + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## conversation + conversation + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + conversation + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## conversation + conversation + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## conversation + conversation + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## conversation + conversation + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## conversation + conversation + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## converastion + conversation + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## conversation + conversation + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + conversation + hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## conversation + conversation + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## conversation + conversation + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## conversation + hors_sujet + aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* aide
    - utter_aider

## conversation + hors_sujet + bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* bonjour
    - utter_bonjour

## conversation + hors_sujet + aurevoir
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* aurevoir
    - utter_aurevoir

## conversation + hors_sujet + conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## conversation + hors_sujet + traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* traduction
    - action_traduction

## conversation + hors_sujet + wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet
* wikipedia
    - action_wikipedia


### TRADUCTION ###

## traduction + aider
* traduction
    - action_traduction
* aide
    - utter_aider

## traduction + bonjour
* traduction
    - action_traduction
* bonjour
    - utter_bonjour

## traduction + aurevoir
* traduction
    - action_traduction
* aurevoir
    - utter_aurevoir

## traduction + conversation
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## traduction + hors_sujet
* traduction
    - action_traduction
* hors_sujet
    - utter_hors_sujet

## traduction + wikipedia
* traduction
    - action_traduction
* wikipedia
    - action_wikipedia

## traduction + aider + bonjour
* traduction
    - action_traduction
* aide
    - utter_aider
* bonjour
    - utter_bonjour

## traduction + aider + aurevoir
* traduction
    - action_traduction
* aide
    - utter_aider
* aurevoir
    - utter_aurevoir

## traduction + aider + conversation
* traduction
    - action_traduction
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## traduction + aider + hors_sujet
* traduction
    - action_traduction
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet

## traduction + aider + wikipedia
* traduction
    - action_traduction
* aide
    - utter_aider
* wikipedia
    - action_wikipedia

## traduction + bonjour + aider
* traduction
    - action_traduction
* bonjour
    - utter_bonjour
* aide
    - utter_aider

## traduction + bonjour + aurevoir
* traduction
    - action_traduction
* bonjour
    - utter_bonjour
* aurevoir
    - utter_aurevoir

## traduction + bonjour + conversation
* traduction
    - action_traduction
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## traduction + bonjour + hors_sujet
* traduction
    - action_traduction
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet

## traduction + bonjour + wikipedia
* traduction
    - action_traduction
* bonjour
    - utter_bonjour
* wikipedia
    - action_wikipedia

## traduction + conversation + aider
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## traduction + conversation + bonjour
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## traduction + conversation + aurevoir
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## traduction + conversation + conversation
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## traduction + conversation + hors_sujet
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## traduction + conversation + wikipedia
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## traduction + conversation + aider
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## traduction + conversation + bonjour
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## traduction + conversation + aurevoir
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## traduction + conversation + conversation
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## traduction + conversation + hors_sujet
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## traduction + conversation + wikipedia
* traduction
    - action_traduction
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* wikipedia
    - action_wikipedia

## traduction + hors_sujet + aider
* traduction
    - action_traduction
* hors_sujet
    - utter_hors_sujet
* aide
    - utter_aider

## traduction + hors_sujet + bonjour
* traduction
    - action_traduction
* hors_sujet
    - utter_hors_sujet
* bonjour
    - utter_bonjour

## traduction + hors_sujet + aurevoir
* traduction
    - action_traduction
* hors_sujet
    - utter_hors_sujet
* aurevoir
    - utter_aurevoir

## traduction + hors_sujet + conversation
* traduction
    - action_traduction
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## traduction + hors_sujet + conversation
* traduction
    - action_traduction
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## traduction + hors_sujet + wikipedia
* traduction
    - action_traduction
* hors_sujet
    - utter_hors_sujet
* wikipedia
    - action_wikipedia


### WIKIPEDIA ###

## wikipedia + aider
* wikipedia
    - action_wikipedia
* aide
    - utter_aider

## wikipedia + bonjour
* wikipedia
    - action_wikipedia
* bonjour
    - utter_bonjour

## wikipedia + aurevoir
* wikipedia
    - action_wikipedia
* aurevoir
    - utter_aurevoir

## wikipedia + conversation
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## wikipedia + hors_sujet
* wikipedia
    - action_wikipedia
* hors_sujet
    - utter_hors_sujet

## wikipedia + traduction
* wikipedia
    - action_wikipedia
* traduction
    - action_traduction

## wikipedia + aider + bonjour
* wikipedia
    - action_wikipedia
* aide
    - utter_aider
* bonjour
    - utter_bonjour

## wikipedia + aider + aurevoir
* wikipedia
    - action_wikipedia
* aide
    - utter_aider
* aurevoir
    - utter_aurevoir

## wikipedia + aider + conversation
* wikipedia
    - action_wikipedia
* aide
    - utter_aider
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## wikipedia + aider + hors_sujet
* wikipedia
    - action_wikipedia
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet

## wikipedia + aider + traduction
* wikipedia
    - action_wikipedia
* aide
    - utter_aider
* traduction
    - action_traduction

## wikipedia + bonjour + aider
* wikipedia
    - action_wikipedia
* bonjour
    - utter_bonjour
* aide
    - utter_aider

## wikipedia + bonjour + aurevoir
* wikipedia
    - action_wikipedia
* bonjour
    - utter_bonjour
* aurevoir
    - utter_aurevoir

## wikipedia + bonjour + conversation
* wikipedia
    - action_wikipedia
* bonjour
    - utter_bonjour
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## wikipedia + bonjour + hors_sujet
* wikipedia
    - action_wikipedia
* bonjour
    - utter_bonjour
* hors_sujet
    - utter_hors_sujet

## wikipedia + bonjour + traduction
* wikipedia
    - action_wikipedia
* bonjour
    - utter_bonjour
* traduction
    - action_traduction

## wikipedia + conversation + aider
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## wikipedia + conversation + bonjour
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## wikipedia + conversation + aurevoir
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## wikipedia + conversation + conversation
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## wikipedia + conversation + hors_sujet
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## wikipedia + conversation + traduction
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## wikipedia + conversation + aider
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aide
    - utter_aider

## wikipedia + conversation + bonjour
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* bonjour
    - utter_bonjour

## wikipedia + conversation + aurevoir
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* aurevoir
    - utter_aurevoir

## wikipedia + conversation + conversation
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## wikipedia + conversation + hors_sujet
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* hors_sujet
    - utter_hors_sujet

## wikipedia + conversation + traduction
* wikipedia
    - action_wikipedia
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation
* traduction
    - action_traduction

## wikipedia + hors_sujet + aider
* wikipedia
    - action_wikipedia
* hors_sujet
    - utter_hors_sujet
* aide
    - utter_aider

## wikipedia + hors_sujet + bonjour
* wikipedia
    - action_wikipedia
* hors_sujet
    - utter_hors_sujet
* bonjour
    - utter_bonjour

## wikipedia + hors_sujet + aurevoir
* wikipedia
    - action_wikipedia
* hors_sujet
    - utter_hors_sujet
* aurevoir
    - utter_aurevoir

## wikipedia + hors_sujet + conversation
* wikipedia
    - action_wikipedia
* hors_sujet
    - utter_hors_sujet
* saluer OR identite OR insulter OR createur OR meteo OR possibilites OR isbot OR quel_age OR quelle_langue OR quelle_heure OR qui_suis_je OR quel_nom OR origine_lieu OR origine_construction OR faire_connaissance OR faire_blague OR quel_genre OR merci OR affirmer OR infirmer OR complimenter
    - action_conversation

## wikipedia + hors_sujet + traduction
* wikipedia
    - action_wikipedia
* hors_sujet
    - utter_hors_sujet
* traduction
    - action_traduction


### STORIES INTERACTIVES ###

## story 1
* bonjour
    - utter_bonjour
* saluer
    - utter_saluer
* aide
    - utter_aider
* hors_sujet
    - utter_hors_sujet