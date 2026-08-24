import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from core.questions import questions
from core.recommendations import generate_recommendations
from core.pdf_generator import generate_pdf
from core.iso_mapping import (
    calculate_iso_indicative_score,
    calculate_iso_global_score,
    iso_indicative_level,
)


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Résultats - CyberAudit",
    page_icon=":material/analytics:",
    layout="wide"
)


# ============================================================
# VÉRIFICATION
# ============================================================

if "score" not in st.session_state:

    st.warning(
        "Aucun audit disponible. "
        "Veuillez commencer un questionnaire."
    )

    st.stop()


# ============================================================
# DONNÉES
# ============================================================

company = st.session_state.company
score = st.session_state.score
percentage = st.session_state.percentage
level = st.session_state.level

theme_scores = st.session_state.theme_scores
theme_totals = st.session_state.theme_totals

answers = st.session_state.answers

total_questions = len(questions)


# ============================================================
# RECOMMANDATIONS
# ============================================================

recommendations = generate_recommendations(
    answers
)


# ============================================================
# CALCUL ISO INDICATIF
# ============================================================

iso_results = calculate_iso_indicative_score(
    theme_scores=theme_scores,
    theme_totals=theme_totals
)

iso_global_percentage = calculate_iso_global_score(
    iso_results
)

iso_level = iso_indicative_level(
    iso_global_percentage
)


# ============================================================
# TITRE
# ============================================================

st.title("Tableau de bord CyberAudit")

st.caption(
    "Évaluation de la maturité cybersécurité de l'entreprise"
)


# ============================================================
# INFORMATIONS
# ============================================================

st.subheader("Informations de l'entreprise")

c1, c2 = st.columns(2)

with c1:

    st.write(
        f"**Entreprise :** {company['entreprise']}"
    )

    st.write(
        f"**Responsable :** {company['responsable']}"
    )

    st.write(
        f"**Email :** {company['email']}"
    )


with c2:

    st.write(
        f"**Secteur :** {company['secteur']}"
    )

    st.write(
        f"**Effectif :** {company['effectif']}"
    )


st.divider()


# ============================================================
# RÉSUMÉ
# ============================================================

st.subheader("Résumé de l'audit")

k1, k2, k3 = st.columns(3)

with k1:

    st.metric(
        "Score",
        f"{score}/{total_questions}"
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
# COULEUR DU NIVEAU
# ============================================================

if level == "Faible":

    level_color = "#C62828"

elif level == "Intermédiaire":

    level_color = "#EF6C00"

elif level == "Bon":

    level_color = "#2E7D32"

else:

    level_color = "#1565C0"


# ============================================================
# INTERPRÉTATION
# ============================================================

if level == "Faible":

    interpretation = (
        "Plusieurs pratiques de cybersécurité "
        "nécessitent une amélioration prioritaire."
    )

elif level == "Intermédiaire":

    interpretation = (
        "Les principales pratiques sont présentes, "
        "mais plusieurs points doivent encore être renforcés."
    )

elif level == "Bon":

    interpretation = (
        "L'entreprise dispose d'un niveau de sécurité "
        "globalement satisfaisant."
    )

else:

    interpretation = (
        "Les bonnes pratiques évaluées sont largement "
        "mises en œuvre."
    )


st.markdown(
    f"""
    <div style="
        padding: 15px;
        border-radius: 10px;
        background-color: #F5F7FA;
        border-left: 5px solid {level_color};
        margin-bottom: 20px;
    ">
        <strong style="color:{level_color};">
            {level}
        </strong>
        <br>
        {interpretation}
    </div>
    """,
    unsafe_allow_html=True
)


st.divider()


# ============================================================
# JAUGE
# ============================================================

st.subheader("Niveau de maturité")

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
                "color": "#0B3D91"
            },
            "steps": [
                {
                    "range": [0, 32],
                    "color": "#FFCDD2"
                },
                {
                    "range": [32, 64],
                    "color": "#FFE0B2"
                },
                {
                    "range": [64, 84],
                    "color": "#FFF9C4"
                },
                {
                    "range": [84, 100],
                    "color": "#C8E6C9"
                }
            ]
        }
    )
)

st.plotly_chart(
    fig,
    width="stretch"
)


# ============================================================
# OUI / NON
# ============================================================

st.subheader("Répartition des réponses")

oui = score
non = total_questions - score

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
        "#2E7D32",
        "#C62828"
    ]
)

st.plotly_chart(
    fig,
    width="stretch"
)


# ============================================================
# SCORES PAR THÈME
# ============================================================

st.subheader("Scores par thème")

themes = []
scores = []

for theme in theme_scores:

    themes.append(theme)

    theme_percentage = round(
        (
            theme_scores[theme]
            / theme_totals[theme]
        ) * 100
    )

    scores.append(theme_percentage)


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
    texttemplate="%{text}%",
    textposition="outside"
)

fig.update_yaxes(
    range=[0, 100]
)

st.plotly_chart(
    fig,
    width="stretch"
)


# ============================================================
# COMPARAISON INDICATIVE ISO
# ============================================================

st.divider()

st.subheader(
    "Comparaison indicative avec ISO/IEC 27001:2022"
)

st.info(
    "Cette comparaison est indicative et repose sur des "
    "domaines inspirés d'ISO/IEC 27001:2022. "
    "Elle ne constitue pas une évaluation de conformité "
    "ni une certification ISO 27001."
)


# ------------------------------------------------------------
# Score global ISO indicatif
# ------------------------------------------------------------

iso_level_color = {
    "Faible": "#C62828",
    "Intermédiaire": "#EF6C00",
    "Bon": "#2E7D32",
    "Excellent": "#1565C0",
}.get(
    iso_level,
    "#1565C0"
)


iso_col1, iso_col2 = st.columns(2)

with iso_col1:

    st.metric(
        "Score global indicatif",
        f"{iso_global_percentage}%"
    )

with iso_col2:

    st.markdown(
        f"""
        <div style="
            padding: 10px;
            border-radius: 8px;
            background-color: #F5F7FA;
            border-left: 4px solid {iso_level_color};
        ">
            <strong>Niveau indicatif</strong><br>
            <span style="
                color:{iso_level_color};
                font-weight:700;
                font-size:18px;
            ">
                {iso_level}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")

# ------------------------------------------------------------
# Tableau de comparaison
# ------------------------------------------------------------

iso_table_data = []

for cyberaudit_theme, iso_domain in {
    "Gouvernance et sensibilisation":
        "Gouvernance et gestion des risques",

    "Gestion des accès et des incidents":
        "Contrôles d'accès et gestion des incidents",

    "Sécurité des systèmes et du réseau":
        "Sécurité technologique",

    "Protection des données":
        "Protection de l'information",
}.items():

    cyberaudit_percentage = round(
        (
            theme_scores[cyberaudit_theme]
            / theme_totals[cyberaudit_theme]
        ) * 100
    )

    iso_percentage = iso_results[
        iso_domain
    ]["percentage"]

    iso_table_data.append(
        {
            "Domaine CyberAudit": cyberaudit_theme,
            "Domaine ISO-inspired": iso_domain,
            "CyberAudit": cyberaudit_percentage,
            "ISO-inspired": iso_percentage,
        }
    )


iso_table = []

for row in iso_table_data:

    iso_table.append(
        {
            "Domaine CyberAudit":
                row["Domaine CyberAudit"],

            "Domaine ISO-inspired":
                row["Domaine ISO-inspired"],

            "CyberAudit (%)":
                row["CyberAudit"],

            "ISO-inspired (%)":
                row["ISO-inspired"],
        }
    )


st.dataframe(
    iso_table,
    width="stretch",
    hide_index=True,
)


# ------------------------------------------------------------
# Graphique comparatif
# ------------------------------------------------------------

comparison_data = []

for row in iso_table_data:

    comparison_data.append(
        {
            "Domaine":
                row["Domaine ISO-inspired"],

            "Référentiel":
                "CyberAudit",

            "Score":
                row["CyberAudit"],
        }
    )

    comparison_data.append(
        {
            "Domaine":
                row["Domaine ISO-inspired"],

            "Référentiel":
                "ISO-inspired",

            "Score":
                row["ISO-inspired"],
        }
    )


comparison_fig = px.bar(
    comparison_data,
    x="Domaine",
    y="Score",
    color="Référentiel",
    barmode="group",
    text="Score",
    labels={
        "Domaine": "Domaine de sécurité",
        "Score": "Score (%)"
    }
)

comparison_fig.update_traces(
    texttemplate="%{text}%",
    textposition="outside"
)

comparison_fig.update_yaxes(
    range=[0, 100]
)

st.plotly_chart(
    comparison_fig,
    width="stretch"
)


# ============================================================
# ANALYSE DES DOMAINES
# ============================================================

st.divider()

st.subheader("Analyse des domaines")

strong_points = []
weak_points = []

for theme in theme_scores:

    theme_percentage = round(
        (
            theme_scores[theme]
            / theme_totals[theme]
        ) * 100
    )

    if theme_percentage >= 80:

        strong_points.append(
            (theme, theme_percentage)
        )

    else:

        weak_points.append(
            (theme, theme_percentage)
        )


col_strong, col_weak = st.columns(2)


# ============================================================
# POINTS FORTS
# ============================================================

with col_strong:

    st.markdown(
        "### Points forts"
    )

    if not strong_points:

        st.info(
            "Aucun domaine n'atteint actuellement 80% ou plus."
        )

    else:

        for theme, theme_percentage in strong_points:

            st.write(
                f"**{theme}** — {theme_percentage}%"
            )

            st.progress(
                theme_percentage / 100
            )


# ============================================================
# POINTS À AMÉLIORER
# ============================================================

with col_weak:

    st.markdown(
        "### Points à améliorer"
    )

    if not weak_points:

        st.success(
            "Aucun domaine majeur à améliorer."
        )

    else:

        for theme, theme_percentage in weak_points:

            st.write(
                f"**{theme}** — {theme_percentage}%"
            )

            st.progress(
                theme_percentage / 100
            )


# ============================================================
# PRIORITÉS
# ============================================================

st.divider()

st.subheader("Priorité des actions")

priority_counts = {
    "Critique": 0,
    "Élevée": 0,
    "Moyenne": 0
}


for rec in recommendations:

    priority = rec.get(
        "priority",
        "Moyenne"
    )

    if priority in priority_counts:

        priority_counts[priority] += 1


p1, p2, p3 = st.columns(3)


with p1:

    st.metric(
        "Critiques",
        priority_counts["Critique"]
    )


with p2:

    st.metric(
        "Élevées",
        priority_counts["Élevée"]
    )


with p3:

    st.metric(
        "Moyennes",
        priority_counts["Moyenne"]
    )


# ============================================================
# RECOMMANDATIONS
# ============================================================

st.divider()

st.header(
    "Recommandations personnalisées"
)


if not recommendations:

    st.success(
        "Toutes les mesures évaluées sont conformes."
    )

else:

    st.write(
        f"{len(recommendations)} "
        f"recommandation(s) identifiée(s)."
    )

    priority_order = {
        "Critique": 1,
        "Élevée": 2,
        "Moyenne": 3
    }

    recommendations = sorted(
        recommendations,
        key=lambda rec:
        priority_order.get(
            rec.get(
                "priority",
                "Moyenne"
            ),
            99
        )
    )

    for rec in recommendations:

        priority = rec.get(
            "priority",
            "Moyenne"
        )

        if priority == "Critique":

            priority_color = "#C62828"

        elif priority == "Élevée":

            priority_color = "#EF6C00"

        else:

            priority_color = "#9E9D24"


        with st.expander(
            f"{priority} — "
            f"{rec.get('theme', '')}"
        ):

            st.markdown(
                f"""
                <div style="
                    border-left: 4px solid {priority_color};
                    padding-left: 12px;
                ">
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                "**Question évaluée:**"
            )

            st.write(
                rec.get(
                    "question",
                    ""
                )
            )

            st.write(
                "**Action recommandée:**"
            )

            st.info(
                rec.get(
                    "recommendation",
                    ""
                )
            )


# ============================================================
# RAPPORT PDF
# ============================================================

st.divider()

st.subheader("Rapport PDF")

st.write(
    "Générez et téléchargez le rapport complet "
    "de l'audit avec les résultats et les recommandations."
)

pdf_bytes = generate_pdf(
    company=company,
    score=score,
    percentage=percentage,
    level=level,
    theme_scores=theme_scores,
    theme_totals=theme_totals,
    recommendations=recommendations
)

st.download_button(
    label="Télécharger le rapport PDF",
    data=pdf_bytes,
    file_name="rapport_cyberaudit.pdf",
    mime="application/pdf",
    width="stretch"
)


# ============================================================
# NOUVEL AUDIT
# ============================================================

st.divider()

st.subheader("Nouvel audit")

st.write(
    "Vous pouvez effacer l'audit actuel et "
    "commencer une nouvelle évaluation."
)


if st.button(
    "Refaire l'audit",
    width="stretch"
):

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

    st.switch_page(
        "pages/2_Questionnaire.py"
    )