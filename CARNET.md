# 📒 Mon carnet de bord

**Nom :** 

**Prénom :** 

**Adresse de mon site :** https://______.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Le code est sur GitHub, puis il est envoyé sur PythonAnywhere pour être exécuté en ligne.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que le site est hébergé sur un serveur distant, et le navigateur de mon voisin demande simplement la page à ce serveur. Son ordinateur n’a pas besoin d’avoir le site installé.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le nom de domaine est `www.google.com` et le chemin est `/maps`.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ *Not Found* veut dire que la ressource demandée n’existe pas. C’est le serveur qui envoie ce message.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Flask a du mal à choisir quelle fonction correspond à quelle route. Il peut provoquer une erreur et le serveur renvoie une erreur 500. En pratique, chaque route doit avoir un nom unique.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie du code HTML brut, avec des balises comme `<h1>Bonjour</h1>`. Le navigateur lit ces balises et les transforme en page visible, sans montrer les balises elles-mêmes.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_
   - `<h1>` : sert à créer un titre principal.
   - `<p>` : sert à créer un paragraphe de texte.
   - `<ul>` : sert à créer une liste non ordonnée.
   - `<li>` : sert à créer un élément de liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ Parce que le navigateur va la télécharger directement depuis l’autre serveur où elle est hébergée. Mon site n’a pas besoin de l’héberger lui-même pour l’afficher.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Parce que le code Python sert à gérer la logique et les données, tandis que le HTML sert à afficher le contenu. Séparer les deux rend le travail plus simple, plus lisible et plus facile à modifier sans tout casser.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Ils sont remplacés par le serveur, avant que la page ne soit envoyée au navigateur. J’ai vérifié ça parce que Flask remplit ces variables avec les valeurs Python avant d’envoyer le HTML final.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML donne la structure de la page, par exemple les titres, paragraphes et images. Le CSS donne le style, comme les couleurs, les tailles, les marges et le placement.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Le navigateur télécharge au moins le fichier HTML principal, puis les fichiers CSS associés, et éventuellement d’autres ressources comme des images ou des polices si la page en contient.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Parce que le navigateur garde parfois une copie en cache du CSS. Avec Ctrl + F5, on force le rechargement complet pour voir la version la plus récente.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. Le navigateur envoie la requête, et le serveur envoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ Elle déclenche plusieurs requêtes : au moins une pour la page HTML, puis une ou plusieurs pour les fichiers CSS, et éventuellement pour les images ou autres ressources.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ Le code `200` veut dire que la ressource a bien été trouvée et envoyée. Le code `404` veut dire que la ressource demandée n’a pas été trouvée, donc la favicon est absente ou inaccessible.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Parce que ces changements sont uniquement dans le navigateur de la personne qui les fait. Ils n’altèrent pas le vrai fichier du serveur, donc les autres visiteurs ne les voient pas.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le paramètre est `search_query` et sa valeur est `chat`.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Parce que le serveur essaie de convertir `bonjour` en nombre entier, et ça ne marche pas. Il faut vérifier que la valeur est bien un nombre avant de la convertir, et gérer l’erreur proprement.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Parce que l’utilisateur peut envoyer du HTML ou du JavaScript, et si on l’affiche sans filtrer, ça peut créer une faille de sécurité. C’est ce qu’on appelle une injection.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ Avec GET, les données apparaissent dans l’URL. Avec POST, elles sont envoyées dans le corps de la requête, donc elles ne sont pas visibles dans l’adresse.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour une recherche, je choisirais GET, car c’est simple et les paramètres sont visibles dans l’URL. Pour une connexion avec mot de passe, je choisirais POST, car les données sont plus sensibles et on ne veut pas les afficher dans l’URL.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Pas complètement. Elles ne sont pas visibles dans l’URL, mais elles peuvent quand même être observées dans l’onglet Réseau si le navigateur est inspecté ou si la sécurité du site est faible. POST est plus sûr que GET, mais il ne garantit pas une confidentialité totale.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Un `4xx` est une erreur du client : la requête envoyée est mauvaise ou invalide. Un `5xx` est une erreur du serveur : le serveur a eu un problème pour traiter la demande. En gros, 4xx = erreur de l’utilisateur, 5xx = erreur du site.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur répond avec un code de redirection, comme 301 ou 302. Ensuite, le navigateur lit ce code et fait automatiquement une deuxième requête vers la bonne URL. Donc la deuxième requête est faite par le navigateur.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Quand une page a changé d’URL, le site redirige automatiquement l’ancienne adresse vers la nouvelle. On voit aussi souvent une redirection vers la version sécurisée `https` au lieu de `http`.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Le serveur connaît souvent votre adresse IP, votre navigateur et son type, ainsi que la langue que vous préférez, comme la langue indiquée dans `Accept-Language`.

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ Il peut servir à afficher la page dans la langue du visiteur, par exemple en français si c’est la langue principale du navigateur.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ Une requête 404 correspond souvent à une page qui n’existe pas ou à une URL mal écrite. Par exemple, une page demandée comme `/page-inconnue` ou une favicon absente.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ Je pense que la navigation n’est pas vraiment anonyme. Même sans remplir de formulaire, le navigateur envoie beaucoup d’informations techniques au serveur, et ces infos peuvent révéler des choses sur nous.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Une page HTML est destinée à un humain, pour être affichée dans un navigateur. Une réponse JSON est destinée à une machine, par exemple un script JavaScript ou une application, qui l’utilise automatiquement.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Sur le serveur, le code Python calcule l’heure et prépare la réponse. Dans le navigateur, le code JavaScript récupère les données et affiche l’horloge à l’écran.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ Une application météo utilise une API. Elle échange des informations comme la ville, la température, les prévisions et les conditions météorologiques.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Quand on tape une adresse dans le navigateur, celui-ci envoie une requête au serveur qui héberge le site. Le serveur regarde quelle page est demandée, exécute le code nécessaire et renvoie une réponse. Le navigateur reçoit cette réponse, interprète les fichiers HTML/CSS/JS et affiche la page à l’écran. En résumé, le serveur prépare les données, et le navigateur les transforme en page visible.
