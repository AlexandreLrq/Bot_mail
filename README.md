# Bot Discord pour la gestion d'alias de mail
*********************
Ce bot Discord est un outil qui facilite la création d'alias de messagerie pour améliorer la gestion de vos e-mails. Il vous permet de générer des alias uniques pour chaque site internet ou application avec lesquels vous interagissez, et de rediriger ces alias vers votre adresse e-mail principale, que vous ne communiquez à personne.  

* **Génération d'alias de messagerie** : Le bot vous permet de créer facilement des alias de messagerie personnalisés pour chaque site internet ou application que vous utilisez. Par exemple, vous pouvez générer un alias "site_web_alias" pour le site web "example.com".


* **Redirection des e-mails** : Tous les e-mails reçus sur les alias générés sont automatiquement redirigés vers votre adresse e-mail principale. Vous n'avez plus besoin de fournir votre adresse e-mail réelle à chaque site ou application, ce qui améliore la confidentialité et la sécurité de vos communications.


* **Gestion des alias** : Vous pouvez gérer facilement vos alias de messagerie via des commandes spécifiques du bot. Vous pouvez créer de nouveaux alias, supprimer des alias existants ou afficher la liste de tous vos alias enregistrés.


* **Protection contre le spam** : En utilisant des alias de messagerie uniques pour chaque site ou application, vous pouvez limiter les risques de spam ou de courriers indésirables. Si vous commencez à recevoir des e-mails non sollicités sur un alias spécifique, vous pouvez simplement le supprimer sans affecter votre adresse principale.  


* **Protection contre le phishing** : L'utilisation d'alias spécifiques pour des services sensibles tels que votre banque permet de détecter les tentatives de phishing. Si vous recevez un e-mail prétendant provenir de votre banque mais qu'il n'est pas envoyé à l'alias que vous avez créé spécifiquement pour cette banque, il s'agit probablement d'une tentative de phishing. Vous pouvez ainsi identifier et éviter les attaques de phishing.

# Prérequis  
*********************
Avant d'installer et d'utiliser ce projet, assurez-vous de disposer des éléments suivants :

* Un compte OVH avec les clés API nécessaires pour accéder aux services OVH.
* Un nom de domaine configuré pour recevoir des e-mails.
* Un token d'un bot Discord. Vous pouvez créer un bot et obtenir son token en suivant les instructions de la documentation officielle de Discord.
* Un serveur privé sur Discord avec votre bot Discord ajouté.

# Installation
*********************
### Installation

* Assurez-vous d'avoir Python 3.10 installé sur votre machine. Vous pouvez le télécharger depuis le site officiel de Python : https://www.python.org/downloads/.  


* Clonez ce dépôt GitHub sur votre machine en utilisant la commande suivante :  
<pre><code>git clone https://github.com/AlexandreLrq/Bot_mail.git</code></pre>

* Accédez au répertoire du projet :  
<pre><code>cd Bot_mail</code></pre>

* Créez un fichier config.py dans le répertoire du projet et ouvrez-le avec un éditeur de texte. Copiez le contenu suivant dans le fichier config.py :
<pre><code># Clé API d'OVH
APPLICATION_KEY = "APPLICATION_KEY"
APPLICATION_SECRET = "APPLICATION_SECRET"
CONSUMER_KEY = "CONSUMER_KEY"

# Token du bot Discord
DISCORD_TOKEN = "DISCORD_TOKEN"

# Nom de domaine
DOMAINE = "DOMAINE"

# Adresse mail de destination
ADRESSE_MAIL = "ADRESSE_MAIL"
</code></pre>

* Remplacez les valeurs APPLICATION_KEY, APPLICATION_SECRET, CONSUMER_KEY, DISCORD_TOKEN, DOMAINE et ADRESSE_MAIL par les valeurs correspondantes. Enregistrez et fermez le fichier config.py.


* Installez les dépendances requises en exécutant la commande suivante :  
<pre><code>pip install -r requirements.txt</code></pre>

* Pour lancer le bot Discord, exécutez la commande suivante :
<pre><code>python main.py</code></pre>



### Installation avec Docker

* Assurez-vous d'avoir Docker installé sur votre machine. Vous pouvez le télécharger depuis le site officiel de Docker : https://www.docker.com/get-docker.


* Clonez ce dépôt GitHub sur votre machine en utilisant la commande suivante :
<pre><code>git clone https://github.com/AlexandreLrq/Bot_mail.git</code></pre>

* Accédez au répertoire du projet :  
<pre><code>cd Bot_mail</code></pre>

* Créez un fichier config.py dans le répertoire du projet et ouvrez-le avec un éditeur de texte. Copiez le contenu suivant dans le fichier config.py :
<pre><code># Clé API d'OVH
APPLICATION_KEY = "APPLICATION_KEY"
APPLICATION_SECRET = "APPLICATION_SECRET"
CONSUMER_KEY = "CONSUMER_KEY"

# Token du bot Discord
DISCORD_TOKEN = "DISCORD_TOKEN"

# Nom de domaine
DOMAINE = "DOMAINE"

# Adresse mail de destination
ADRESSE_MAIL = "ADRESSE_MAIL"
</code></pre>

* Remplacez les valeurs APPLICATION_KEY, APPLICATION_SECRET, CONSUMER_KEY, DISCORD_TOKEN, DOMAINE et ADRESSE_MAIL par les valeurs correspondantes. Enregistrez et fermez le fichier config.py.


* Créez une image Docker en exécutant la commande suivante :  
<pre><code>docker build -t bot_mail .</code></pre>

* Exécutez la commande suivante pour lancer un conteneur Docker du bot Discord :
<pre><code>docker run --restart always bot_mail</code></pre>

# Utilisation
*********************
Une fois le bot installé et configuré, vous pouvez interagir avec lui en utilisant les commandes suivantes :

* **!new** : Cette commande permet de créer un nouvel alias. Par exemple, en exécutant !new exemple, un nouvel alias nommé exemple@votredomaine.fr sera créé. Tous les e-mails envoyés à cet alias seront redirigés vers votre adresse e-mail principale.


* **!del** : Cette commande permet de supprimer un alias existant. Par exemple, en exécutant !del exemple, l'alias exemple@votredomaine.fr sera supprimé. Tous les e-mails envoyés à cet alias ne seront plus redirigés.


* **!maj** : Cette commande permet d'afficher la liste de tous les alias enregistrés, le bot affichera la liste des alias avec leurs noms correspondants.


* **!clear** : Cette commande permet d'effacer tous les messages du canal de discussion. Tous les messages présents dans le canal seront supprimés. Notez que cette action est irréversible.