import streamlit as st

from core.auth import (
    is_authenticated,
    logout_user,
)


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CyberAudit",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# AUTHENTIFICATION
# ============================================================

if not is_authenticated():

    st.title("🛡️ CyberAudit")

    st.subheader(
        "Plateforme d'évaluation de la maturité cybersécurité"
    )

    st.write(
        "Connectez-vous pour accéder à votre espace CyberAudit."
    )

    if st.button(
        "Se connecter",
        type="primary",
        width="stretch",
    ):

        st.switch_page(
            "pages/0_Login.py"
        )

    st.stop()


# ============================================================
# UTILISATEUR
# ============================================================

username = st.session_state.get(
    "username",
    "Utilisateur"
)


# ============================================================
# HERO
# ============================================================

st.title(
    "🛡️ CyberAudit"
)

st.subheader(
    f"Bienvenue, {username}."
)

st.write(
    "Évaluez la maturité cybersécurité de votre entreprise, "
    "identifiez les points à améliorer et obtenez des "
    "recommandations personnalisées."
)


# ============================================================
# ACTIONS PRINCIPALES
# ============================================================

st.write("")

action_col1, action_col2 = st.columns(2)

with action_col1:

    if st.button(
        "🚀 Commencer un nouvel audit",
        type="primary",
        width="stretch",
    ):

        st.switch_page(
            "pages/2_Questionnaire.py"
        )


with action_col2:

    if st.button(
        "📊 Voir l'historique",
        width="stretch",
    ):

        st.switch_page(
            "pages/4_historique.py"
        )


st.divider()


# ============================================================
# PRÉSENTATION
# ============================================================

st.header(
    "Une évaluation simple et structurée"
)

st.write(
    "CyberAudit analyse plusieurs domaines essentiels "
    "de la cybersécurité afin de fournir une vision claire "
    "du niveau de maturité de l'entreprise."
)


# ============================================================
# INDICATEURS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Contrôles",
        "25",
        "Questions"
    )

with col2:

    st.metric(
        "Domaines",
        "4",
        "Sécurité"
    )

with col3:

    st.metric(
        "Niveaux",
        "4",
        "Maturité"
    )

with col4:

    st.metric(
        "Rapport",
        "PDF",
        "Exportable"
    )


st.divider()


# ============================================================
# COMMENT ÇA FONCTIONNE
# ============================================================

st.header(
    "Comment ça fonctionne ?"
)

step1, step2, step3 = st.columns(3)

with step1:

    st.subheader(
        "01 — Évaluer"
    )

    st.write(
        "Répondez aux 25 questions portant sur "
        "les principales pratiques de cybersécurité."
    )


with step2:

    st.subheader(
        "02 — Analyser"
    )

    st.write(
        "CyberAudit calcule automatiquement votre "
        "score global et vos scores par domaine."
    )


with step3:

    st.subheader(
        "03 — Améliorer"
    )

    st.write(
        "Identifiez les points faibles et consultez "
        "les recommandations adaptées à votre situation."
    )


st.divider()


# ============================================================
# FONCTIONNALITÉS
# ============================================================

st.header(
    "Fonctionnalités"
)


feature1, feature2 = st.columns(2)

with feature1:

    with st.container(border=True):

        st.subheader(
            "📊 Analyse de maturité"
        )

        st.write(
            "Visualisez votre niveau global et les "
            "performances de chaque domaine."
        )


with feature2:

    with st.container(border=True):

        st.subheader(
            "💡 Recommandations personnalisées"
        )

        st.write(
            "Identifiez les mesures de sécurité "
            "qui nécessitent une amélioration."
        )


feature3, feature4 = st.columns(2)

with feature3:

    with st.container(border=True):

        st.subheader(
            "📄 Rapport PDF"
        )

        st.write(
            "Générez un rapport professionnel contenant "
            "les résultats et recommandations."
        )


with feature4:

    with st.container(border=True):

        st.subheader(
            "📈 Historique"
        )

        st.write(
            "Suivez l'évolution de la maturité "
            "au fil des différentes évaluations."
        )


st.divider()


# ============================================================
# APPEL À L'ACTION
# ============================================================

st.header(
    "Prêt à évaluer votre cybersécurité ?"
)

st.write(
    "Lancez une nouvelle évaluation et obtenez "
    "une vision claire de votre posture actuelle."
)


if st.button(
    "🚀 Lancer mon évaluation",
    type="primary",
    width="stretch",
):

    st.switch_page(
        "pages/2_Questionnaire.py"
    )


# ============================================================
# INFORMATIONS UTILISATEUR
# ============================================================

st.divider()

st.caption(
    f"Connecté en tant que : {username}"
)


# ============================================================
# DÉCONNEXION
# ============================================================

if st.button(
    "Se déconnecter",
    width="stretch",
):

    logout_user()

    st.switch_page(
        "pages/0_Login.py"
    )