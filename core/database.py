import sqlite3
from datetime import datetime


DATABASE = "cyberaudit.db"


# ============================================================
# CONNEXION
# ============================================================

def get_connection():
    return sqlite3.connect(DATABASE)


# ============================================================
# INITIALISATION
# ============================================================

def init_database():

    conn = get_connection()
    cursor = conn.cursor()

    # --------------------------------------------------------
    # Table des audits
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entreprise TEXT NOT NULL,
            responsable TEXT NOT NULL,
            email TEXT NOT NULL,
            secteur TEXT NOT NULL,
            effectif TEXT NOT NULL,
            score INTEGER NOT NULL,
            percentage INTEGER NOT NULL,
            level TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    # --------------------------------------------------------
    # Table des utilisateurs
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ============================================================
# UTILISATEURS
# ============================================================

def create_user(
    username,
    email,
    password_hash
):
    """
    Crée un utilisateur.
    Retourne False si l'email existe déjà.
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users (
                username,
                email,
                password_hash,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                username.strip(),
                email.strip().lower(),
                password_hash,
                datetime.now().strftime(
                    "%d/%m/%Y %H:%M"
                )
            )
        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


def get_user_by_email(email):
    """
    Récupère un utilisateur grâce à son email.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            email,
            password_hash,
            created_at
        FROM users
        WHERE email = ?
        """,
        (email.strip().lower(),)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ============================================================
# AUDITS
# ============================================================

def save_audit(
    entreprise,
    responsable,
    email,
    secteur,
    effectif,
    score,
    percentage,
    level
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO audits (
            entreprise,
            responsable,
            email,
            secteur,
            effectif,
            score,
            percentage,
            level,
            date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entreprise,
        responsable,
        email,
        secteur,
        effectif,
        score,
        percentage,
        level,
        datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )
    ))

    conn.commit()
    conn.close()


def get_audits():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            entreprise,
            responsable,
            email,
            secteur,
            effectif,
            score,
            percentage,
            level,
            date
        FROM audits
        ORDER BY id DESC
    """)

    audits = cursor.fetchall()

    conn.close()

    return audits


def delete_audit(
    audit_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM audits
        WHERE id = ?
        """,
        (audit_id,)
    )

    conn.commit()
    conn.close()


# ============================================================
# INITIALISATION AUTOMATIQUE
# ============================================================

init_database()