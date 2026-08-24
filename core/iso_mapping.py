# ============================================================
# MAPPING INDICATIF CYBERAUDIT / ISO IEC 27001
# ============================================================
#
# Ce fichier fournit une comparaison indicative entre les
# domaines CyberAudit et des domaines de sécurité inspirés
# d'ISO/IEC 27001:2022.
#
# Ce n'est PAS une évaluation de conformité ISO 27001 et
# ne constitue pas une certification.
#
# ============================================================


# ============================================================
# DOMAINES DE COMPARAISON
# ============================================================

ISO_DOMAINS = {
    "Gouvernance et sensibilisation": {
        "name": "Gouvernance et gestion des risques",
        "description": (
            "Organisation de la sécurité, responsabilités, "
            "politiques et gestion des risques."
        ),
    },

    "Gestion des accès et des incidents": {
        "name": "Contrôles d'accès et gestion des incidents",
        "description": (
            "Gestion des accès, authentification, droits "
            "utilisateurs et traitement des incidents."
        ),
    },

    "Sécurité des systèmes et du réseau": {
        "name": "Sécurité technologique",
        "description": (
            "Protection des systèmes, réseaux, équipements "
            "et mesures de sécurité techniques."
        ),
    },

    "Protection des données": {
        "name": "Protection de l'information",
        "description": (
            "Protection des informations, sauvegardes, accès "
            "aux données et préservation de leur sécurité."
        ),
    },
}


# ============================================================
# CORRESPONDANCE CYBERAUDIT → DOMAINE ISO-INSPIRED
# ============================================================

CYBERAUDIT_TO_ISO = {

    "Gouvernance et sensibilisation":
        "Gouvernance et gestion des risques",

    "Gestion des accès et des incidents":
        "Contrôles d'accès et gestion des incidents",

    "Sécurité des systèmes et du réseau":
        "Sécurité technologique",

    "Protection des données":
        "Protection de l'information",
}


# ============================================================
# CALCUL DU SCORE INDICATIF
# ============================================================

def calculate_iso_indicative_score(
    theme_scores,
    theme_totals,
):
    """
    Calcule un score indicatif inspiré de domaines ISO/IEC 27001.

    Le calcul repose sur les mêmes réponses que CyberAudit,
    mais les résultats sont regroupés selon les domaines
    définis dans ce mapping.

    Retourne :

        {
            "nom_du_domaine": {
                "score": ...,
                "total": ...,
                "percentage": ...
            }
        }
    """

    results = {}

    for cyberaudit_theme, iso_domain in CYBERAUDIT_TO_ISO.items():

        score = theme_scores.get(
            cyberaudit_theme,
            0
        )

        total = theme_totals.get(
            cyberaudit_theme,
            0
        )

        if total > 0:

            percentage = round(
                (score / total) * 100
            )

        else:

            percentage = 0

        results[iso_domain] = {
            "score": score,
            "total": total,
            "percentage": percentage,
        }

    return results


# ============================================================
# SCORE GLOBAL INDICATIF
# ============================================================

def calculate_iso_global_score(
    iso_results,
):
    """
    Calcule le score global indicatif du référentiel.
    """

    total_score = 0
    total_questions = 0

    for domain in iso_results.values():

        total_score += domain["score"]
        total_questions += domain["total"]

    if total_questions == 0:

        return 0

    return round(
        (total_score / total_questions) * 100
    )


# ============================================================
# NIVEAU INDICATIF
# ============================================================

def iso_indicative_level(percentage):
    """
    Détermine un niveau indicatif pour l'affichage.

    Ces seuils sont propres au prototype CyberAudit et
    ne représentent pas des seuils officiels ISO/IEC 27001.
    """

    if percentage < 32:

        return "Faible"

    elif percentage < 64:

        return "Intermédiaire"

    elif percentage < 84:

        return "Bon"

    else:

        return "Excellent"