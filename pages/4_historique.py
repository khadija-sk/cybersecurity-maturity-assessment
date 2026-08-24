import streamlit as st
import plotly.express as px

from core.database import get_audits, delete_audit


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Historique - CyberAudit",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# TITRE
# ============================================================

st.title("Historique des audits")

st.caption(
    "Consultez les évaluations de cybersécurité réalisées précédemment "
    "et suivez l'évolution de la maturité d'une entreprise."
)

st.divider()


# ============================================================
# RÉCUPÉRATION DES AUDITS
# ============================================================

audits = get_audits()


# ============================================================
# AUCUN AUDIT
# ============================================================

if not audits:

    st.info(
        "Aucun audit enregistré pour le moment."
    )

    st.write(
        "Réalisez un questionnaire pour qu'il apparaisse ici."
    )

    st.stop()


# ============================================================
# STATISTIQUES GLOBALES
# ============================================================

total_audits = len(audits)

average_score = round(
    sum(audit[6] for audit in audits) / total_audits,
    1
)

average_percentage = round(
    sum(audit[7] for audit in audits) / total_audits,
    1
)


c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Nombre d'audits",
        total_audits
    )

with c2:

    st.metric(
        "Score moyen",
        f"{average_score}/25"
    )

with c3:

    st.metric(
        "Maturité moyenne",
        f"{average_percentage}%"
    )


st.divider()


# ============================================================
# ÉVOLUTION D'UNE ENTREPRISE
# ============================================================

st.subheader("Évolution de la maturité")


# Liste des entreprises uniques
companies = sorted(
    set(
        audit[1]
        for audit in audits
    )
)


selected_company = st.selectbox(
    "Sélectionner une entreprise",
    companies
)


# Audits de l'entreprise sélectionnée
company_audits = [
    audit
    for audit in audits
    if audit[1] == selected_company
]


# Tri chronologique
company_audits = sorted(
    company_audits,
    key=lambda audit: audit[0]
)


if len(company_audits) == 1:

    audit = company_audits[0]

    st.info(
        "Cette entreprise ne possède qu'un seul audit. "
        "Réalisez une nouvelle évaluation pour afficher "
        "son évolution dans le temps."
    )

else:

    evolution_data = []

    for index, audit in enumerate(
        company_audits,
        start=1
    ):

        evolution_data.append(
            {
                "Audit": f"Audit {index}",
                "Date": audit[9],
                "Maturité": audit[7],
                "Score": audit[6]
            }
        )


    # --------------------------------------------------------
    # Graphique évolution
    # --------------------------------------------------------

    fig = px.line(
        evolution_data,
        x="Audit",
        y="Maturité",
        markers=True,
        text="Maturité",
        labels={
            "Audit": "Évaluation",
            "Maturité": "Maturité (%)"
        }
    )

    fig.update_traces(
        texttemplate="%{text}%",
        textposition="top center"
    )

    fig.update_yaxes(
        range=[0, 100]
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


    # --------------------------------------------------------
    # Progression
    # --------------------------------------------------------

    first_audit = company_audits[0]
    last_audit = company_audits[-1]

    first_percentage = first_audit[7]
    last_percentage = last_audit[7]

    evolution = last_percentage - first_percentage


    p1, p2, p3 = st.columns(3)

    with p1:

        st.metric(
            "Premier audit",
            f"{first_percentage}%"
        )

    with p2:

        st.metric(
            "Dernier audit",
            f"{last_percentage}%"
        )

    with p3:

        st.metric(
            "Progression",
            f"{evolution:+d} points"
        )


    # --------------------------------------------------------
    # Tendance
    # --------------------------------------------------------

    if evolution > 0:

        st.success(
            f"Tendance positive : la maturité a progressé "
            f"de {evolution} points."
        )

    elif evolution < 0:

        st.error(
            f"Tendance négative : la maturité a diminué "
            f"de {abs(evolution)} points."
        )

    else:

        st.info(
            "Tendance stable : aucun changement entre "
            "le premier et le dernier audit."
        )


st.divider()


# ============================================================
# LISTE DES AUDITS
# ============================================================

st.subheader("Audits réalisés")


for audit in audits:

    (
        audit_id,
        entreprise,
        responsable,
        email,
        secteur,
        effectif,
        score,
        percentage,
        level,
        date
    ) = audit


    # ========================================================
    # NETTOYAGE DU NIVEAU
    # ========================================================

    clean_level = (
        str(level)
        .replace("🔴", "")
        .replace("🟡", "")
        .replace("🟢", "")
        .replace("🏆", "")
        .strip()
    )


    # ========================================================
    # COULEUR DU NIVEAU
    # ========================================================

    if clean_level == "Faible":

        level_color = "#C62828"

    elif clean_level == "Intermédiaire":

        level_color = "#EF6C00"

    elif clean_level == "Bon":

        level_color = "#2E7D32"

    else:

        level_color = "#1565C0"


    # ========================================================
    # CARTE AUDIT
    # ========================================================

    with st.container(border=True):

        col1, col2, col3, col4 = st.columns(
            [3, 2, 2, 2]
        )


        # ----------------------------------------------------
        # Entreprise
        # ----------------------------------------------------

        with col1:

            st.markdown(
                f"### {entreprise}"
            )

            st.write(
                f"**Responsable :** {responsable}"
            )

            st.write(
                f"**Date :** {date}"
            )


        # ----------------------------------------------------
        # Score
        # ----------------------------------------------------

        with col2:

            st.metric(
                "Score",
                f"{score}/25"
            )


        # ----------------------------------------------------
        # Pourcentage
        # ----------------------------------------------------

        with col3:

            st.metric(
                "Maturité",
                f"{percentage}%"
            )


        # ----------------------------------------------------
        # Niveau
        # ----------------------------------------------------

        with col4:

            st.write(
                "**Niveau**"
            )

            st.markdown(
                f"<span style='color:{level_color}; "
                f"font-weight:700; font-size:18px;'>"
                f"{clean_level}"
                f"</span>",
                unsafe_allow_html=True
            )


        st.divider()


        # ====================================================
        # DÉTAILS + SUPPRESSION
        # ====================================================

        detail_col, delete_col = st.columns(
            [4, 1]
        )


        # ----------------------------------------------------
        # Détails
        # ----------------------------------------------------

        with detail_col:

            with st.expander(
                "Voir les détails"
            ):

                d1, d2 = st.columns(2)

                with d1:

                    st.write(
                        f"**Entreprise :** {entreprise}"
                    )

                    st.write(
                        f"**Responsable :** {responsable}"
                    )

                    st.write(
                        f"**Email :** {email}"
                    )


                with d2:

                    st.write(
                        f"**Secteur :** {secteur}"
                    )

                    st.write(
                        f"**Effectif :** {effectif}"
                    )

                    st.write(
                        f"**Date :** {date}"
                    )


                st.write(
                    f"**Score :** {score}/25"
                )

                st.write(
                    f"**Pourcentage :** {percentage}%"
                )

                st.markdown(
                    f"**Niveau :** "
                    f"<span style='color:{level_color}; "
                    f"font-weight:700;'>"
                    f"{clean_level}"
                    f"</span>",
                    unsafe_allow_html=True
                )


        # ----------------------------------------------------
        # Suppression
        # ----------------------------------------------------

        with delete_col:

            if st.button(
                "Supprimer",
                key=f"delete_{audit_id}",
                width="stretch"
            ):

                delete_audit(
                    audit_id
                )

                st.success(
                    "Audit supprimé."
                )

                st.rerun()