import streamlit as st

from core.database import get_audits, delete_audit


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Historique - CyberAudit",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# TITRE
# ============================================================

st.title("📚 Historique des audits")

st.caption(
    "Consultez les évaluations de cybersécurité réalisées précédemment."
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
        "📭 Aucun audit enregistré pour le moment."
    )

    st.write(
        "Réalisez un questionnaire pour qu'il apparaisse ici."
    )

    st.stop()


# ============================================================
# STATISTIQUES
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
        "📋 Nombre d'audits",
        total_audits
    )

with c2:

    st.metric(
        "📊 Score moyen",
        f"{average_score}/25"
    )

with c3:

    st.metric(
        "📈 Maturité moyenne",
        f"{average_percentage}%"
    )


st.divider()


# ============================================================
# LISTE DES AUDITS
# ============================================================

st.subheader("📋 Audits réalisés")


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


    # --------------------------------------------------------
    # Couleur / icône du niveau
    # --------------------------------------------------------

    if "Faible" in level:

        level_icon = "🔴"

    elif "Intermédiaire" in level:

        level_icon = "🟡"

    elif "Bon" in level:

        level_icon = "🟢"

    else:

        level_icon = "🏆"


    # --------------------------------------------------------
    # Carte de l'audit
    # --------------------------------------------------------

    with st.container(border=True):

        col1, col2, col3, col4 = st.columns(
            [3, 2, 2, 2]
        )


        # ----------------------------------------------------
        # Entreprise
        # ----------------------------------------------------

        with col1:

            st.markdown(
                f"### 🏢 {entreprise}"
            )

            st.write(
                f"👤 **Responsable :** {responsable}"
            )

            st.write(
                f"📅 **Date :** {date}"
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

            st.write("**Niveau**")

            st.write(
                f"{level_icon} {level}"
            )


        st.divider()


        # ----------------------------------------------------
        # Détails
        # ----------------------------------------------------

        detail_col, delete_col = st.columns(
            [4, 1]
        )


        with detail_col:

            with st.expander("🔍 Voir les détails"):

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

                st.write(
                    f"**Niveau :** {level_icon} {level}"
                )


        # ----------------------------------------------------
        # Suppression
        # ----------------------------------------------------

        with delete_col:

            if st.button(
                "🗑️ Supprimer",
                key=f"delete_{audit_id}",
                use_container_width=True
            ):

                delete_audit(audit_id)

                st.success(
                    "Audit supprimé."
                )

                st.rerun()