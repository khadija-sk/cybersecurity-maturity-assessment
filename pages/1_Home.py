import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CyberAudit",
    page_icon=":material/security:",
    layout="wide"
)


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 48px;
        font-weight: 700;
        color: #0B3D91;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #444444;
        margin-bottom: 30px;
    }

    .card {
        background-color: #F5F7FA;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #E0E0E0;
        text-align: center;
        min-height: 90px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TITRE
# ============================================================

st.markdown(
    "<div class='main-title'>CyberAudit</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='subtitle'>
        Plateforme d'évaluation de la maturité cybersécurité
        des PME marocaines
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")


# ============================================================
# CARACTÉRISTIQUES
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        """
        <div class='card'>
            Conforme au guide CMRPI/AUSIM
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class='card'>
            Évaluation simple et rapide
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class='card'>
            Rapport PDF professionnel
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        """
        <div class='card'>
            Recommandations personnalisées
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")
st.write("")
st.write("")


# ============================================================
# BOUTON PRINCIPAL
# ============================================================

if st.button(
    "Commencer l'évaluation",
    width="stretch"
):

    st.switch_page(
        "pages/2_Questionnaire.py"
    )