import streamlit as st

from core.questions import questions
from core.scoring import calculate_score, maturity_level
from core.database import save_audit


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Questionnaire - CyberAudit",
    page_icon=":material/checklist:",
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

    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.questionnaire_started = False

    for key in [
        "score",
        "percentage",
        "theme_scores",
        "theme_totals",
        "level",
        "company"
    ]:
        st.session_state.pop(key, None)

    for i in range(len(questions)):
        st.session_state.pop(
            f"question_{i}",
            None
        )

    for key in [
        "entreprise_input",
        "responsable_input",
        "email_input"
    ]:
        st.session_state.pop(key, None)


# ============================================================
# TITRE
# ============================================================

st.title("CyberAudit")

st.subheader(
    "Assistant d'évaluation de la maturité cybersécurité"
)

st.markdown("---")


# ============================================================
# INFORMATIONS DE L'ENTREPRISE
# ============================================================

st.header("Informations de l'entreprise")

col1, col2 = st.columns(2)


with col1:

    entreprise = st.text_input(
        "Nom de l'entreprise",
        key="entreprise_input"
    )

    responsable = st.text_input(
        "Responsable",
        key="responsable_input"
    )

    email = st.text_input(
        "Email",
        key="email_input"
    )


with col2:

    secteur = st.selectbox(
        "Secteur d'activité",
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
        "Nombre d'employés",
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
        "Commencer le questionnaire",
        width="stretch"
    ):

        if not entreprise.strip():

            st.error(
                "Veuillez saisir le nom de l'entreprise."
            )

        elif not responsable.strip():

            st.error(
                "Veuillez saisir le nom du responsable."
            )

        elif not email.strip():

            st.error(
                "Veuillez saisir l'adresse email."
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
                "Informations enregistrées avec succès."
            )

            st.rerun()


with button_col2:

    if st.button(
        "Effacer tout",
        width="stretch"
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

    progress = (
        (current + 1)
        / total_questions
    )

    st.subheader("Questionnaire")

    st.progress(progress)

    st.write(
        f"Question {current + 1} sur {total_questions}"
    )


    # ========================================================
    # QUESTION ACTUELLE
    # ========================================================

    question = questions[current]

    st.markdown(
        f"### {question['theme']}"
    )

    previous_answer = (
        st.session_state.answers.get(current)
    )

    if previous_answer is None:
        default_index = 0
    else:
        default_index = (
            0
            if previous_answer == "Oui"
            else 1
        )

    answer = st.radio(
        question["question"],
        ["Oui", "Non"],
        index=default_index,
        key=f"question_{current}"
    )


    # ========================================================
    # NAVIGATION
    # ========================================================

    col1, col2 = st.columns(2)


    # ========================================================
    # PRÉCÉDENT
    # ========================================================

    with col1:

        if st.button(
            "Précédent",
            key="prev_btn",
            width="stretch"
        ):

            st.session_state.answers[current] = answer

            if current > 0:

                st.session_state.current_question -= 1

                st.rerun()


    # ========================================================
    # SUIVANT
    # ========================================================

    with col2:

        if st.button(
            "Suivant",
            key="next_btn",
            width="stretch"
        ):

            st.session_state.answers[current] = answer


            if current < total_questions - 1:

                st.session_state.current_question += 1

                st.rerun()


            else:

                if (
                    len(st.session_state.answers)
                    < total_questions
                ):

                    st.error(
                        "Veuillez répondre à toutes les questions."
                    )

                else:

                    score, percentage, theme_scores, theme_totals = (
                        calculate_score(
                            st.session_state.answers
                        )
                    )

                    level = maturity_level(score)


                    st.session_state.score = score
                    st.session_state.percentage = percentage
                    st.session_state.theme_scores = theme_scores
                    st.session_state.theme_totals = theme_totals
                    st.session_state.level = level

                    st.session_state.company = {
                        "entreprise": entreprise,
                        "responsable": responsable,
                        "email": email,
                        "secteur": secteur,
                        "effectif": effectif
                    }


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


                    st.switch_page(
                        "pages/3_Resultats.py"
                    )


# ============================================================
# MESSAGE SI QUESTIONNAIRE NON COMMENCÉ
# ============================================================

else:

    st.info(
        "Remplissez les informations de l'entreprise "
        "puis cliquez sur « Commencer le questionnaire » "
        "pour démarrer l'évaluation."
    )