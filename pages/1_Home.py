import streamlit as st

st.set_page_config(
    page_title="CyberAudit",
    page_icon="🛡️",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main-title {
        font-size:48px;
        font-weight:700;
        color:#0B3D91;
        text-align:center;
    }
    .subtitle {
        font-size:22px;
        text-align:center;
        color:#444;
    }
    .card {
        background-color:#F5F7FA;
        padding:20px;
        border-radius:15px;
        border:1px solid #E0E0E0;
        text-align:center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-title'>🛡️ CyberAudit</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Plateforme d’évaluation de la maturité cybersécurité des PME marocaines</div>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='card'>✔ Conforme au guide CMRPI/AUSIM</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>✔ Évaluation simple</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>✔ Rapport PDF</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='card'>✔ Recommandations personnalisées</div>", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.button("🚀 Commencer l’évaluation", use_container_width=True)