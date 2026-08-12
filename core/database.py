import sqlite3
from datetime import datetime

DATABASE = "cyberaudit.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def init_database():
    conn = get_connection()
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()


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
        datetime.now().strftime("%d/%m/%Y %H:%M")
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


def delete_audit(audit_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM audits WHERE id = ?",
        (audit_id,)
    )

    conn.commit()
    conn.close()


# Initialiser automatiquement la base
init_database()