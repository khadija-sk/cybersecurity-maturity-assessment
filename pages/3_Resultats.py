import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from core.recommendations import generate_recommendations


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Résultats - CyberAudit",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# VÉRIFICATION DE L'AUDIT
# ============================================================

if "score" not in st.session_state:

    st.warning(
        "⚠️ Aucun audit disponible. "
        "Veuillez commencer un questionnaire."
    )

    st.stop()


# ============================================================
# RÉCUPÉRATION DES DONNÉES
# ============================================================

company = st.session_state.company

score = st.session_state.score

percentage = st.session_state.percentage

level = st.session_state.level

theme_scores = st.session_state.theme_scores

theme_totals = st.session_state.theme_totals

answers = st.session_state.answers


# ============================================================
# RECOMMANDATIONS
# ============================================================

recommendations = generate_recommendations(
    answers
)


# ============================================================
# TITRE
# ============================================================

st.title("📊 Tableau de bord CyberAudit")

st.caption(
    "Évaluation de la maturité cybersécurité de l'entreprise"
)


# ============================================================
# INFORMATIONS DE L'ENTREPRISE
# ============================================================

st.subheader("🏢 Informations de l'entreprise")

c1, c2 = st.columns(2)

with c1:

    st.write(
        f"**Entreprise :** "
        f"{company['entreprise']}"
    )

    st.write(
        f"**Responsable :** "
        f"{company['responsable']}"
    )

    st.write(
        f"**Email :** "
        f"{company['email']}"
    )


with c2:

    st.write(
        f"**Secteur :** "
        f"{company['secteur']}"
    )

    st.write(
        f"**Effectif :** "
        f"{company['effectif']}"
    )


st.divider()


# ============================================================
# RÉSUMÉ DE L'AUDIT
# ============================================================

st.subheader("🎯 Résumé de l'audit")

k1, k2, k3 = st.columns(3)

with k1:

    st.metric(
        "Score",
        f"{score}/25"
    )


with k2:

    st.metric(
        "Taux de maturité",
        f"{percentage}%"
    )


with k3:

    st.metric(
        "Niveau",
        level
    )


# ============================================================
# MESSAGE D'INTERPRÉTATION
# ============================================================

if score <= 8:

    st.error(
        "🔴 **Maturité faible** : "
        "plusieurs pratiques de cybersécurité "
        "nécessitent une amélioration prioritaire."
    )

elif score <= 16:

    st.warning(
        "🟡 **Maturité intermédiaire** : "
        "les principales pratiques sont présentes, "
        "mais plusieurs points doivent encore être renforcés."
    )

elif score <= 21:

    st.success(
        "🟢 **Bonne maturité** : "
        "l'entreprise dispose d'un niveau de sécurité "
        "globalement satisfaisant."
    )

else:

    st.success(
        "🏆 **Excellente maturité** : "
        "les bonnes pratiques évaluées sont largement "
        "mises en œuvre."
    )


st.divider()


# ============================================================
# NIVEAU DE MATURITÉ
# ============================================================

st.subheader("🎯 Niveau de maturité")

fig = go.Figure(
    go.Indicator(

        mode="gauge+number",

        value=percentage,

        title={
            "text": "Maturité cybersécurité"
        },

        gauge={

            "axis": {
                "range": [0, 100]
            },

            "bar": {
                "color": "darkblue"
            },

            "steps": [

                {
                    "range": [0, 30],
                    "color": "#ff4b4b"
                },

                {
                    "range": [30, 60],
                    "color": "orange"
                },

                {
                    "range": [60, 80],
                    "color": "yellow"
                },

                {
                    "range": [80, 100],
                    "color": "green"
                }

            ]
        }
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# RÉPARTITION OUI / NON
# ============================================================

st.subheader("📈 Répartition des réponses")

oui = score

non = 25 - oui

fig = px.pie(

    values=[
        oui,
        non
    ],

    names=[
        "Oui",
        "Non"
    ],

    hole=0.55,

    color_discrete_sequence=[
        "#2ecc71",
        "#e74c3c"
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# SCORES PAR THÈME
# ============================================================

st.subheader("📊 Scores par thème")

themes = []

scores = []

for theme in theme_scores:

    themes.append(theme)

    theme_percentage = round(
        (
            theme_scores[theme]
            /
            theme_totals[theme]
        ) * 100
    )

    scores.append(
        theme_percentage
    )


fig = px.bar(

    x=themes,

    y=scores,

    text=scores,

    labels={
        "x": "Thème",
        "y": "Score (%)"
    }
)

fig.update_traces(
    textposition="outside"
)

fig.update_yaxes(
    range=[0, 100]
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# POINTS FORTS / POINTS À AMÉLIORER
# ============================================================

st.divider()

st.subheader("💪 Analyse des domaines")

strong_points = []

weak_points = []


for theme in theme_scores:

    theme_percentage = round(
        (
            theme_scores[theme]
            /
            theme_totals[theme]
        ) * 100
    )


    if theme_percentage >= 70:

        strong_points.append(
            (
                theme,
                theme_percentage
            )
        )

    else:

        weak_points.append(
            (
                theme,
                theme_percentage
            )
        )


col_strong, col_weak = st.columns(2)


# ============================================================
# POINTS FORTS
# ============================================================

with col_strong:

    st.markdown(
        "### 🟢 Points forts"
    )

    if len(strong_points) == 0:

        st.info(
            "Aucun domaine n'atteint actuellement "
            "70% ou plus."
        )

    else:

        for theme, percentage_theme in strong_points:

            st.write(
                f"✅ **{theme}** — "
                f"{percentage_theme}%"
            )

            st.progress(
                percentage_theme / 100
            )


# ============================================================
# POINTS À AMÉLIORER
# ============================================================

with col_weak:

    st.markdown(
        "### 🟠 Points à améliorer"
    )

    if len(weak_points) == 0:

        st.success(
            "🎉 Aucun domaine majeur à améliorer."
        )

    else:

        for theme, percentage_theme in weak_points:

            st.write(
                f"⚠️ **{theme}** — "
                f"{percentage_theme}%"
            )

            st.progress(
                percentage_theme / 100
            )


# ============================================================
# PRIORITÉ DES ACTIONS
# ============================================================

st.divider()

st.subheader("🚨 Priorité des actions")

priority_counts = {

    "Critique": 0,

    "Élevée": 0,

    "Moyenne": 0

}


for rec in recommendations:

    priority = rec["priority"]

    if priority in priority_counts:

        priority_counts[priority] += 1


p1, p2, p3 = st.columns(3)


with p1:

    st.metric(
        "🔴 Critiques",
        priority_counts["Critique"]
    )


with p2:

    st.metric(
        "🟢 Élevées",
        priority_counts["Élevée"]
    )


with p3:

    st.metric(
        "🟡 Moyennes",
        priority_counts["Moyenne"]
    )


# ============================================================
# RECOMMANDATIONS
# ============================================================

st.divider()

st.header(
    "💡 Recommandations personnalisées"
)


if len(recommendations) == 0:

    st.success(
        "🎉 Excellent ! "
        "Toutes les mesures évaluées sont conformes."
    )


else:

    st.write(
        f"**{len(recommendations)} "
        f"recommandation(s) identifiée(s).**"
    )


    # ========================================================
    # ORDRE DES PRIORITÉS
    # ========================================================

    priority_order = {

        "Critique": 1,

        "Élevée": 2,

        "Moyenne": 3

    }


    recommendations = sorted(

        recommendations,

        key=lambda rec:
        priority_order.get(
            rec["priority"],
            99
        )
    )


    # ========================================================
    # AFFICHAGE
    # ========================================================

    for rec in recommendations:

        priority = rec["priority"]


        if priority == "Critique":

            icon = "🔴"

        elif priority == "Élevée":

            icon = "🟢"

        else:

            icon = "🟡"


        with st.expander(

            f"{icon} "
            f"{priority} — "
            f"{rec['theme']}"

        ):

            st.write(
                "**Question évaluée :**"
            )

            st.write(
                rec["question"]
            )


            st.write(
                "**Action recommandée :**"
            )

            st.info(
                rec["recommendation"]
            )


# ============================================================
# REFAIRE L'AUDIT
# ============================================================

st.divider()

st.subheader("🔄 Nouvel audit")

st.write(
    "Vous pouvez effacer l'audit actuel et "
    "commencer une nouvelle évaluation."
)


if st.button(
    "🔄 Refaire l'audit",
    use_container_width=True
):

    # Réinitialiser les données de l'audit

    keys_to_remove = [

        "score",

        "percentage",

        "theme_scores",

        "theme_totals",

        "level",

        "company",

        "answers",

        "current_question",

        "questionnaire_started",

        "reset_form"

    ]


    for key in keys_to_remove:

        st.session_state.pop(
            key,
            None
        )


    # Retour au questionnaire

    st.switch_page(
        "pages/2_Questionnaire.py"
    )