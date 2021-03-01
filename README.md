# P10_Deployez_votre_application_sur_un_serveur
La branche 'master' contient la version actuelle du site web en production  
[master](https://github.com/StephenAOGOLO/P10_Deployez_votre_application_sur_un_serveur/tree/master)

# Intégration Continue
## Travis
A chaque modification du projet, ajout de nouvelles fonctionnalités ou de corrections,  
le projet est envoyé sur la branche [stagging](https://github.com/StephenAOGOLO/P10_Deployez_votre_application_sur_un_serveur/tree/stagging). C'est à ce niveau que le service Travis entre en fonction.  
Ce service cree un environnement éphémère de production, proche de l'environnement du serveur hébergé.  
Il exécute deux campagnes de tests. Une campagne de tests unitaires/fonctionnels et une campagne de tests d'intégration.
Les tests unitaires utilisent les modules Django "TestCase" et "SimpleTestCase".  
Les tests d'intégration sont gérés par le module selenium couplé à un WebDriver.  
Ces derniers sont testés sur le navigateur Chrome.

# Déploiement
Le déploiement s'effectue en ligne de commandes, après la validation de l'intégration continue.  
La version finale du site est donc rappatriée depuis la branche [master](https://github.com/StephenAOGOLO/P10_Deployez_votre_application_sur_un_serveur/tree/master) du repo vers le serveur hébergé (Digital Ocean).  

# Monitoring
La surveillance du site est assurée par Sentry, Supervisor et le tableau de bord de Digital Ocean.
Chaque service remplit une fonction particulière, ce qui les rendent complémentaires.

## Sentry  
Sentry est une plateforme web permettant de concentrer et afficher les évènements et erreurs
prélevés depuis un site web.  

## Supervisor
Supervisor permet de centraliser la gestion des processus internes et externes qui sont utiles au
fonctionnement du site web. Ce service est notamment utilisé pour activer et désactiver
Gunicorn.  

## Digital Ocean  
Digital Ocean propose un tableau de bord permettant de surveiller l'activité du site  
en terme de consommation CPU, d'occupation mémoire et de bande-passante.  

# Automatisation
Suite au déploiement, Une certaine automatisation est dédiée à la maintenance du site,  
La mise à jour régulière de la base de données.
## Cron
Le module Crontab permet de planifier des exécutions.
La mise à jour de la base de données ainsi que l'enregistrement d'un journal d'évènement ont été planifiés.
Ces exécutions sont lancés une fois par semaine, le dimanche à 3h du matin.


# Trello
En Cours...

# Précision technique 
Les versions stagging et master ont désormais le même contenu

