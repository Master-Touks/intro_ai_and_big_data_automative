# LLM Adoption

- Problématique : Comment intégrer un LLM dans mon processus de livraison de features ?  

Quel LLM pour quel use case ? 
=> Quels outils est-ce que je peux utiliser ? (GitHub Copilot, Claude, GPT, Gemini, DeepSeek...) 

=> Comment les utiliser ?
- [] Open Source ? Cloud ?
- [] Centralisé ? Département ?
- [] Quel stratégie applique ? 

=> Créer un premier use case ? 
- [] Répondre à une spec tech, et générer le code le plus approprié de manière scalable 
- [] ... 
Output : un code auto-généré qui réponds aux specs et qui rentre dans mes contraintes métiers. 


## Qu'est-ce qu'un LLM ? 
- Un modèle d'IA Générative (Deep Learning) qui va me donner la réponse la plus probable à ma question.
- Points d'attentions : Hallucinations / Réécriture de code inutile / Implémentation de features inutiles / ...

### Comment ? 
- [] Quels sont mes outils ? [GitHub Copilot, Git, Jira, ...]
- [] Est-ce qu'il y a un LLM qui peut se connecter automatiquement à mes outils ? Tous d'un coup ou les uns après les autres ? 
- [] Qu'est-ce que je priorise ? [e.g mon use case]

#### Recherche 
- [] Chain of Thought (Comment lui dire ce que je veux de manière structuré, claire, et qu'il me donne l'output)
- [] Zero, One, Few Shot learning (Est-ce qu'il y a besoin/l'envie des exemples concrets ? En ai-je à disposition ?)
- [] MCP (Model Context Protocol) (Est-ce que je peux connecter mon LLM à mes outils et l'entrainé sur mes contraintes/contexte ?)
- [] RAG (Retrieval Augmented Generation) (Est-ce que j'ai besoin d'encoder mes documents historiques pour donner le contexte)
- [] J'implémente (j'applique, je test, je valide et je mets en production)

# Output : Résultat de mon PoC 
- [] Est-ce que le code qu'il m'a généré me permet de pouvoir juste faire : 
  -  []  une relecture simple, 
  -  [] valider, 
  -  [] mettre en prod
  -  [] Faire les unitaires
  - [] et livrer