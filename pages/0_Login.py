
import streamlit as st

from core.auth import (
    register_user,
    authenticate_user,
    login_user,
)


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Connexion - CyberAudit",
    page_icon=":material/security:",
    layout="centered",
)


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
    <style>

    .login-container {
        max-width: 700px;
        margin: auto;
    }

    .brand {
        text-align: center;
        margin-top: 25px;
        margin-bottom: 8px;
    }

    .brand-title {
        font-size: 42px;
        font-weight: 800;
        color: #0B3D91;
        letter-spacing: -1px;
    }

    .brand-subtitle {
        text-align: center;
        color: #666666;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .security-note {
        text-align: center;
        padding: 12px 18px;
        margin-bottom: 25px;
        border: 1px solid #D9E2F2;
        border-radius: 10px;
        background-color: #F7F9FC;
        color: #4A5568;
        font-size: 14px;
    }

    .footer {
        text-align: center;
        color: #888888;
        font-size: 13px;
        margin-top: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SI DÉJÀ CONNECTÉ
# ============================================================

if st.session_state.get(
    "authenticated",
    False
):

    st.title("CyberAudit")

    st.success(
        f"Vous êtes déjà connecté en tant que "
        f"{st.session_state.get('username', '')}."
    )

    if st.button(
        "Accéder à CyberAudit",
        type="primary",
        width="stretch",
    ):

        st.switch_page(
            "app.py"
        )

    st.stop()


# ============================================================
# EN-TÊTE
# ============================================================

st.markdown(
    """
    <div class="brand">
        <div class="brand-title">
            CyberAudit
        </div>
    </div>

    <div class="brand-subtitle">
        Évaluation de la maturité cybersécurité des PME
    </div>

    <div class="security-note">
        Accédez à votre espace d'évaluation en toute sécurité.
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ONGLETS
# ============================================================

login_tab, register_tab = st.tabs(
    [
        "Connexion",
        "Créer un compte",
    ]
)


# ============================================================
# CONNEXION
# ============================================================

with login_tab:

    st.subheader(
        "Se connecter"
    )

    email = st.text_input(
        "Adresse email",
        placeholder="exemple@email.com",
        key="login_email",
    )

    password = st.text_input(
        "Mot de passe",
        type="password",
        placeholder="Votre mot de passe",
        key="login_password",
    )

    st.write("")

    if st.button(
        "Se connecter",
        type="primary",
        width="stretch",
    ):

        if not email.strip():

            st.error(
                "Veuillez saisir votre adresse email."
            )

        elif not password:

            st.error(
                "Veuillez saisir votre mot de passe."
            )

        else:

            user = authenticate_user(
                email=email,
                password=password,
            )

            if user:

                login_user(
                    user
                )

                st.success(
                    "Connexion réussie."
                )

                st.switch_page(
                    "app.py"
                )

            else:

                st.error(
                    "Adresse email ou mot de passe incorrect."
                )


# ============================================================
# CRÉATION DE COMPTE
# ============================================================

with register_tab:

    st.subheader(
        "Créer un compte"
    )

    username = st.text_input(
        "Nom d'utilisateur",
        placeholder="Votre nom",
        key="register_username",
    )

    register_email = st.text_input(
        "Adresse email",
        placeholder="exemple@email.com",
        key="register_email",
    )

    register_password = st.text_input(
        "Mot de passe",
        type="password",
        placeholder="Minimum 8 caractères",
        key="register_password",
    )

    confirm_password = st.text_input(
        "Confirmer le mot de passe",
        type="password",
        placeholder="Répétez votre mot de passe",
        key="register_confirm_password",
    )

    st.caption(
        "Le mot de passe doit contenir au moins 8 caractères."
    )

    st.write("")

    if st.button(
        "Créer mon compte",
        type="primary",
        width="stretch",
    ):

        if not username.strip():

            st.error(
                "Veuillez saisir votre nom d'utilisateur."
            )

        elif not register_email.strip():

            st.error(
                "Veuillez saisir votre adresse email."
            )

        elif not register_password:

            st.error(
                "Veuillez saisir un mot de passe."
            )

        elif len(register_password) < 8:

            st.error(
                "Le mot de passe doit contenir "
                "au moins 8 caractères."
            )

        elif register_password != confirm_password:

            st.error(
                "Les mots de passe ne correspondent pas."
            )

        else:

            created = register_user(
                username=username,
                email=register_email,
                password=register_password,
            )

            if created:

                st.success(
                    "Compte créé avec succès. "
                    "Vous pouvez maintenant vous connecter."
                )

            else:

                st.error(
                    "Cette adresse email est déjà utilisée."
                )


# ============================================================
# PIED DE PAGE
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        CyberAudit — Plateforme d'évaluation de la maturité
        cybersécurité des PME
    </div>
    """,
    unsafe_allow_html=True,
)