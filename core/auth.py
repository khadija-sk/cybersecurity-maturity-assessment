import bcrypt
import streamlit as st

from core.database import (
    create_user,
    get_user_by_email,
)


# ============================================================
# PASSWORD
# ============================================================

def hash_password(password):
    """
    Hash the password securely with bcrypt.
    """

    password_bytes = password.encode("utf-8")

    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    return hashed.decode("utf-8")


def verify_password(password, password_hash):
    """
    Verify a password against its bcrypt hash.
    """

    password_bytes = password.encode("utf-8")
    hash_bytes = password_hash.encode("utf-8")

    return bcrypt.checkpw(
        password_bytes,
        hash_bytes
    )


# ============================================================
# REGISTER
# ============================================================

def register_user(
    username,
    email,
    password,
):
    """
    Create a new user.
    """

    username = username.strip()
    email = email.strip().lower()

    if not username or not email or not password:
        return False

    password_hash = hash_password(
        password
    )

    return create_user(
        username=username,
        email=email,
        password_hash=password_hash,
    )


# ============================================================
# LOGIN
# ============================================================

def authenticate_user(
    email,
    password,
):
    """
    Authenticate a user.

    Returns user information on success,
    otherwise None.
    """

    email = email.strip().lower()

    user = get_user_by_email(
        email
    )

    if not user:
        return None

    (
        user_id,
        username,
        user_email,
        password_hash,
        created_at,
    ) = user

    if not verify_password(
        password,
        password_hash,
    ):
        return None

    return {
        "id": user_id,
        "username": username,
        "email": user_email,
        "created_at": created_at,
    }


# ============================================================
# LOGIN SESSION
# ============================================================

def login_user(user):
    """
    Store the authenticated user in the Streamlit session.
    """

    st.session_state.authenticated = True

    st.session_state.user = user

    st.session_state.user_id = user["id"]

    st.session_state.username = user["username"]

    st.session_state.user_email = user["email"]


# ============================================================
# LOGOUT
# ============================================================

def logout_user():
    """
    Clear the authentication session.
    """

    auth_keys = [
        "authenticated",
        "user",
        "user_id",
        "username",
        "user_email",
    ]

    for key in auth_keys:
        st.session_state.pop(
            key,
            None
        )


# ============================================================
# AUTHENTICATION STATE
# ============================================================

def is_authenticated():
    """
    Return True when a user is authenticated.
    """

    return st.session_state.get(
        "authenticated",
        False
    )


# ============================================================
# PAGE PROTECTION
# ============================================================

def require_authentication():
    """
    Stop access to a page when the user is not authenticated.
    """

    if not is_authenticated():

        st.warning(
            "Vous devez être connecté pour "
            "accéder à cette page."
        )

        if st.button(
            "Se connecter",
            width="stretch",
        ):

            st.switch_page(
                "pages/0_Login.py"
            )

        st.stop()