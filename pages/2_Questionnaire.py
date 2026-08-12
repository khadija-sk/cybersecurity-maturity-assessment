import streamlit as st

from core.questions import questions
from core.scoring import calculate_score, maturity_level
from core.database import save_audit


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Questionnaire - CyberAudit",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# INITIALISATION DE LA SESSION
# ============================================================

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "questionnaire_started" not in st.session_state:
    st.session_state.questionnaire_started = False


# ============================================================
# FONCTION : EFFACER TOUT
# ============================================================

def clear_all():
    # Réinitialisation du questionnaire
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.questionnaire_started = False

    # Suppression des résultats précédents
    for key in [
        "score",
        "percentage",
        "theme_scores",
        "theme_totals",
        "level",
        "company"
    ]:
        if key in st.session_state:
            del st.session_state[key]


# ============================================================
# TITRE
# ============================================================

st.title("🛡️ CyberAudit")

st.subheader(
    "Assistant d'évaluation de la maturité cybersécurité"
)

st.markdown("---")


# ============================================================
# INFORMATIONS DE L'ENTREPRISE
# ============================================================

st.header("🏢 Informations de l'entreprise")

col1, col2 = st.columns(2)


with col1:

    entreprise = st.text_input(
        "🏢 Nom de l'entreprise",
        key="entreprise_input"
    )

    responsable = st.text_input(
        "👤 Responsable",
        key="responsable_input"
    )

    email = st.text_input(
        "📧 Email",
        key="email_input"
    )


with col2:

    secteur = st.selectbox(
        "🏭 Secteur d'activité",
        [
            "Industrie",
            "Commerce",
            "Services",
            "Santé",
            "Éducation",
            "Technologie",
            "Autre"
        ],
        key="secteur_input"
    )

    effectif = st.selectbox(
        "👥 Nombre d'employés",
        [
            "1 - 10",
            "11 - 50",
            "51 - 100",
            "Plus de 100"
        ],
        key="effectif_input"
    )


# ============================================================
# BOUTONS PRINCIPAUX
# ============================================================

st.markdown("---")

button_col1, button_col2 = st.columns(2)


with button_col1:

    if st.button(
        "🚀 Commencer le questionnaire",
        use_container_width=True
    ):

        # Vérification des informations

        if not entreprise.strip():

            st.error(
                "⚠️ Veuillez saisir le nom de l'entreprise."
            )

        elif not responsable.strip():

            st.error(
                "⚠️ Veuillez saisir le nom du responsable."
            )

        elif not email.strip():

            st.error(
                "⚠️ Veuillez saisir l'adresse email."
            )

        else:

            st.session_state.questionnaire_started = True

            st.session_state.company = {
                "entreprise": entreprise,
                "responsable": responsable,
                "email": email,
                "secteur": secteur,
                "effectif": effectif
            }

            st.success(
                "✅ Informations enregistrées avec succès !"
            )

            st.rerun()


with button_col2:

    if st.button(
        "🗑️ Effacer tout",
        use_container_width=True
    ):

        clear_all()

        st.rerun()


# ============================================================
# QUESTIONNAIRE
# ============================================================

if st.session_state.questionnaire_started:

    st.markdown("---")

    total_questions = len(questions)

    current = st.session_state.current_question


    # ========================================================
    # PROGRESSION
    # ========================================================

    progress = current / total_questions

    st.subheader("📋 Questionnaire")

    st.progress(progress)

    st.write(
        f"Question {current + 1} sur {total_questions}"
    )


    # ========================================================
    # QUESTION ACTUELLE
    # ========================================================

    question = questions[current]

    st.markdown(
        f"### 🔹 {question['theme']}"
    )

    answer = st.radio(
        question["question"],
        ["Oui", "Non"],
        key=f"question_{current}"
    )


    # ========================================================
    # NAVIGATION
    # ========================================================

    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # BOUTON PRÉCÉDENT
    # --------------------------------------------------------

    with col1:

        if st.button(
            "⬅️ Précédent",
            key="prev_btn",
            use_container_width=True
        ):

            if current > 0:

                st.session_state.current_question -= 1

                st.rerun()


    # --------------------------------------------------------
    # BOUTON SUIVANT
    # --------------------------------------------------------

    with col2:

        if st.button(
            "Suivant ➡️",
            key="next_btn",
            use_container_width=True
        ):

            # Sauvegarder la réponse

            st.session_state.answers[current] = answer


            # =================================================
            # QUESTION SUIVANTE
            # =================================================

            if current < total_questions - 1:

                st.session_state.current_question += 1

                st.rerun()


            # =================================================
            # DERNIÈRE QUESTION
            # =================================================

            else:

                # ---------------------------------------------
                # Calcul du score
                # ---------------------------------------------

                score, percentage, theme_scores, theme_totals = (
                    calculate_score(
                        st.session_state.answers
                    )
                )


                # ---------------------------------------------
                # Niveau de maturité
                # ---------------------------------------------

                level = maturity_level(score)


                # ---------------------------------------------
                # Sauvegarde des résultats
                # ---------------------------------------------

                st.session_state.score = score

                st.session_state.percentage = percentage

                st.session_state.theme_scores = theme_scores

                st.session_state.theme_totals = theme_totals

                st.session_state.level = level


                # ---------------------------------------------
                # Sauvegarde entreprise
                # ---------------------------------------------

                st.session_state.company = {
                    "entreprise": entreprise,
                    "responsable": responsable,
                    "email": email,
                    "secteur": secteur,
                    "effectif": effectif
                }


                # ---------------------------------------------
                # SAUVEGARDE DANS SQLITE
                # ---------------------------------------------

                save_audit(
                    entreprise=entreprise,
                    responsable=responsable,
                    email=email,
                    secteur=secteur,
                    effectif=effectif,
                    score=score,
                    percentage=percentage,
                    level=level
                )


                # ---------------------------------------------
                # Aller vers les résultats
                # ---------------------------------------------

                st.switch_page(
                    "pages/3_Resultats.py"
                )


# ============================================================
# MESSAGE SI QUESTIONNAIRE NON COMMENCÉ
# ============================================================

else:

    st.info(
        "👆 Remplissez les informations de l'entreprise "
        "puis cliquez sur **🚀 Commencer le questionnaire** "
        "pour démarrer l'évaluation."
    )