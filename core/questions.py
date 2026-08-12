questions = [
    {
        "theme": "Gouvernance et sensibilisation",
        "question": "Existe-t-il une politique de cybersécurité écrite ?",
        "recommendation": "Rédiger, faire valider par la direction et diffuser une politique de cybersécurité adaptée à l'entreprise.",
        "priority": "Élevée"
    },
    {
        "theme": "Gouvernance et sensibilisation",
        "question": "Une personne est-elle responsable de la cybersécurité ?",
        "recommendation": "Désigner officiellement un responsable de la cybersécurité chargé de coordonner les mesures de sécurité.",
        "priority": "Critique"
    },
    {
        "theme": "Gouvernance et sensibilisation",
        "question": "Les employés reçoivent-ils une sensibilisation à la cybersécurité ?",
        "recommendation": "Mettre en place des sessions régulières de sensibilisation aux risques : phishing, mots de passe, logiciels malveillants et protection des données.",
        "priority": "Élevée"
    },
    {
        "theme": "Gouvernance et sensibilisation",
        "question": "Les nouveaux employés sont-ils informés des bonnes pratiques de sécurité ?",
        "recommendation": "Intégrer une sensibilisation à la cybersécurité dans le processus d'intégration de chaque nouvel employé.",
        "priority": "Moyenne"
    },
    {
        "theme": "Gouvernance et sensibilisation",
        "question": "Les risques liés à la cybersécurité sont-ils évalués régulièrement ?",
        "recommendation": "Mettre en place une analyse périodique des risques afin d'identifier les menaces, vulnérabilités et impacts potentiels.",
        "priority": "Critique"
    },

    {
        "theme": "Gestion des accès et des incidents",
        "question": "Chaque employé possède-t-il un compte utilisateur personnel ?",
        "recommendation": "Attribuer un compte individuel à chaque utilisateur afin d'assurer la traçabilité des accès et des actions.",
        "priority": "Élevée"
    },
    {
        "theme": "Gestion des accès et des incidents",
        "question": "Les mots de passe respectent-ils des règles de complexité ?",
        "recommendation": "Mettre en place une politique de mots de passe robustes et sensibiliser les utilisateurs à leur protection.",
        "priority": "Élevée"
    },
    {
        "theme": "Gestion des accès et des incidents",
        "question": "L'authentification à deux facteurs est-elle utilisée ?",
        "recommendation": "Déployer l'authentification multifacteur (MFA), en priorité pour les comptes administrateurs et les accès distants.",
        "priority": "Critique"
    },
    {
        "theme": "Gestion des accès et des incidents",
        "question": "Les accès des anciens employés sont-ils supprimés rapidement ?",
        "recommendation": "Mettre en place une procédure de départ permettant de désactiver rapidement tous les comptes et accès d'un ancien employé.",
        "priority": "Critique"
    },
    {
        "theme": "Gestion des accès et des incidents",
        "question": "Les droits d'accès sont-ils révisés régulièrement ?",
        "recommendation": "Effectuer régulièrement une revue des droits afin de supprimer les privilèges devenus inutiles.",
        "priority": "Élevée"
    },

    {
        "theme": "Gestion des accès et des incidents",
        "question": "Une procédure de gestion des incidents existe-t-elle ?",
        "recommendation": "Formaliser une procédure décrivant la détection, le signalement, l'analyse, le traitement et le suivi des incidents de cybersécurité.",
        "priority": "Critique"
    },
    {
        "theme": "Gestion des accès et des incidents",
        "question": "Les employés savent-ils signaler un incident ?",
        "recommendation": "Informer les employés sur la procédure et le canal à utiliser pour signaler rapidement tout incident de sécurité.",
        "priority": "Élevée"
    },
    {
        "theme": "Gestion des accès et des incidents",
        "question": "Les incidents sont-ils enregistrés ?",
        "recommendation": "Mettre en place un registre des incidents permettant de conserver les informations importantes et d'assurer leur suivi.",
        "priority": "Élevée"
    },
    {
        "theme": "Gestion des accès et des incidents",
        "question": "Des exercices de cybersécurité sont-ils réalisés ?",
        "recommendation": "Organiser régulièrement des exercices ou simulations afin de tester la capacité de l'entreprise à réagir à un incident.",
        "priority": "Moyenne"
    },
    {
        "theme": "Gestion des accès et des incidents",
        "question": "Les mesures sont-elles améliorées après chaque incident ?",
        "recommendation": "Réaliser un retour d'expérience après chaque incident et mettre à jour les mesures de sécurité en fonction des enseignements tirés.",
        "priority": "Élevée"
    },

    {
        "theme": "Sécurité des systèmes et du réseau",
        "question": "Tous les ordinateurs disposent-ils d'un antivirus à jour ?",
        "recommendation": "Déployer une solution de protection adaptée et vérifier régulièrement que les signatures et logiciels de sécurité sont à jour.",
        "priority": "Élevée"
    },
    {
        "theme": "Sécurité des systèmes et du réseau",
        "question": "Les logiciels sont-ils régulièrement mis à jour ?",
        "recommendation": "Mettre en place une procédure de gestion des mises à jour et appliquer rapidement les correctifs de sécurité importants.",
        "priority": "Critique"
    },
    {
        "theme": "Sécurité des systèmes et du réseau",
        "question": "Le réseau Wi-Fi est-il protégé ?",
        "recommendation": "Sécuriser le réseau Wi-Fi avec un chiffrement approprié, des mots de passe robustes et une configuration séparant si possible les réseaux internes et invités.",
        "priority": "Élevée"
    },
    {
        "theme": "Sécurité des systèmes et du réseau",
        "question": "Un pare-feu est-il installé ?",
        "recommendation": "Déployer et configurer correctement un pare-feu afin de contrôler les communications réseau entrantes et sortantes.",
        "priority": "Critique"
    },
    {
        "theme": "Sécurité des systèmes et du réseau",
        "question": "Les équipements sont-ils protégés contre les accès non autorisés ?",
        "recommendation": "Renforcer la protection physique et logique des équipements et limiter leur accès aux personnes autorisées.",
        "priority": "Élevée"
    },

    {
        "theme": "Protection des données",
        "question": "Les données importantes sont-elles sauvegardées régulièrement ?",
        "recommendation": "Mettre en place une stratégie de sauvegarde régulière des données importantes et conserver des copies protégées.",
        "priority": "Critique"
    },
    {
        "theme": "Protection des données",
        "question": "Les sauvegardes sont-elles testées ?",
        "recommendation": "Effectuer régulièrement des tests de restauration afin de vérifier que les sauvegardes peuvent réellement être récupérées en cas d'incident.",
        "priority": "Critique"
    },
    {
        "theme": "Protection des données",
        "question": "Les données sensibles sont-elles accessibles uniquement aux personnes autorisées ?",
        "recommendation": "Appliquer le principe du moindre privilège et contrôler régulièrement les accès aux données sensibles.",
        "priority": "Critique"
    },
    {
        "theme": "Protection des données",
        "question": "Les postes de travail sont-ils verrouillés lorsqu'ils sont laissés sans surveillance ?",
        "recommendation": "Activer le verrouillage automatique des postes et sensibiliser les utilisateurs à verrouiller leur session lorsqu'ils s'absentent.",
        "priority": "Moyenne"
    },
    {
        "theme": "Protection des données",
        "question": "Les informations confidentielles sont-elles protégées contre les pertes ou les fuites ?",
        "recommendation": "Mettre en place des mesures de protection adaptées aux informations confidentielles, notamment le contrôle des accès, le chiffrement lorsque nécessaire et la sensibilisation des utilisateurs.",
        "priority": "Critique"
    }
]