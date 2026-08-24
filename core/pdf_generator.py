from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
)

from core.iso_mapping import (
    calculate_iso_indicative_score,
    calculate_iso_global_score,
    iso_indicative_level,
)


# ============================================================
# COULEURS DU RAPPORT
# ============================================================

NAVY = colors.HexColor("#0B1F3A")
BLUE = colors.HexColor("#1565C0")
LIGHT_BLUE = colors.HexColor("#EAF3FF")

GREEN = colors.HexColor("#2E7D32")
LIGHT_GREEN = colors.HexColor("#E8F5E9")

ORANGE = colors.HexColor("#EF6C00")
LIGHT_ORANGE = colors.HexColor("#FFF3E0")

RED = colors.HexColor("#C62828")
LIGHT_RED = colors.HexColor("#FFEBEE")

YELLOW = colors.HexColor("#9E9D24")
LIGHT_YELLOW = colors.HexColor("#FFFDE7")

DARK_GRAY = colors.HexColor("#37474F")
GRAY = colors.HexColor("#78909C")
LIGHT_GRAY = colors.HexColor("#F5F7FA")

BORDER_GRAY = colors.HexColor("#D5DDE5")

WHITE = colors.white


# ============================================================
# FOOTER
# ============================================================

def add_page_footer(canvas, document):
    """
    Ajoute un footer professionnel sur chaque page.
    """

    canvas.saveState()

    width, height = A4

    canvas.setStrokeColor(BLUE)
    canvas.setLineWidth(0.7)

    canvas.line(
        1.5 * cm,
        1.25 * cm,
        width - 1.5 * cm,
        1.25 * cm,
    )

    canvas.setFont(
        "Helvetica",
        8,
    )

    canvas.setFillColor(GRAY)

    canvas.drawString(
        1.5 * cm,
        0.8 * cm,
        "CyberAudit — Évaluation de la maturité cybersécurité",
    )

    canvas.drawRightString(
        width - 1.5 * cm,
        0.8 * cm,
        f"Page {document.page}",
    )

    canvas.restoreState()


# ============================================================
# GÉNÉRATION DU PDF
# ============================================================

def generate_pdf(
    company,
    score,
    percentage,
    level,
    theme_scores,
    theme_totals,
    recommendations,
):
    """
    Génère un rapport PDF professionnel de l'audit CyberAudit.

    Retourne les données du PDF sous forme de bytes.
    """

    # ========================================================
    # DOCUMENT
    # ========================================================

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.7 * cm,
        title="Rapport CyberAudit",
        author="CyberAudit",
    )

    # Nombre total de questions
    total_questions = sum(
        theme_totals.values()
    )

    # ========================================================
    # CALCUL ISO INDICATIF
    # ========================================================

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

    # ========================================================
    # STYLES
    # ========================================================

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CyberAuditTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=NAVY,
        spaceAfter=8,
    )

    subtitle_style = ParagraphStyle(
        "CyberAuditSubtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontName="Helvetica",
        fontSize=11,
        leading=15,
        textColor=DARK_GRAY,
        spaceAfter=12,
    )

    date_style = ParagraphStyle(
        "DateStyle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=9,
        textColor=GRAY,
        spaceAfter=15,
    )

    section_style = ParagraphStyle(
        "SectionTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=NAVY,
        spaceBefore=14,
        spaceAfter=8,
    )

    normal_style = ParagraphStyle(
        "NormalText",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=14,
        textColor=DARK_GRAY,
    )

    small_style = ParagraphStyle(
        "SmallText",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=DARK_GRAY,
    )

    card_title_style = ParagraphStyle(
        "CardTitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=GRAY,
    )

    card_value_style = ParagraphStyle(
        "CardValue",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=20,
        textColor=NAVY,
    )

    recommendation_style = ParagraphStyle(
        "Recommendation",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=DARK_GRAY,
    )

    # ========================================================
    # ELEMENTS
    # ========================================================

    elements = []

    # ========================================================
    # HEADER
    # ========================================================

    logo_style = ParagraphStyle(
        "Logo",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=17,
        textColor=WHITE,
    )

    header_right_style = ParagraphStyle(
        "HeaderRight",
        parent=styles["Normal"],
        alignment=TA_LEFT,
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10,
        textColor=WHITE,
    )

    header_table = Table(
        [
            [
                Paragraph(
                    "<b>CYBER</b>AUDIT",
                    logo_style,
                ),
                Paragraph(
                    "RAPPORT D'AUDIT<br/>CYBERSÉCURITÉ",
                    header_right_style,
                ),
            ]
        ],
        colWidths=[
            9 * cm,
            7 * cm,
        ],
    )

    header_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    NAVY,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    12,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    12,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    10,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    10,
                ),
            ]
        )
    )

    elements.append(header_table)

    elements.append(
        Spacer(
            1,
            18,
        )
    )

    elements.append(
        Paragraph(
            "Rapport d'évaluation de la maturité cybersécurité",
            title_style,
        )
    )

    elements.append(
        Paragraph(
            "Évaluation des pratiques de cybersécurité de l'entreprise",
            subtitle_style,
        )
    )

    elements.append(
        Paragraph(
            f"Date de l'évaluation : "
            f"{datetime.now().strftime('%d/%m/%Y')}",
            date_style,
        )
    )

    # ========================================================
    # 1. INFORMATIONS DE L'ENTREPRISE
    # ========================================================

    elements.append(
        Paragraph(
            "1. Informations de l'entreprise",
            section_style,
        )
    )

    company_data = [
        [
            "Entreprise",
            company.get("entreprise", ""),
        ],
        [
            "Responsable",
            company.get("responsable", ""),
        ],
        [
            "Email",
            company.get("email", ""),
        ],
        [
            "Secteur",
            company.get("secteur", ""),
        ],
        [
            "Effectif",
            company.get("effectif", ""),
        ],
    ]

    company_table = Table(
        company_data,
        colWidths=[
            4.5 * cm,
            11.5 * cm,
        ],
    )

    company_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    BORDER_GRAY,
                ),
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    LIGHT_BLUE,
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (0, -1),
                    NAVY,
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold",
                ),
                (
                    "FONTNAME",
                    (1, 0),
                    (1, -1),
                    "Helvetica",
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
            ]
        )
    )

    elements.append(company_table)

    # ========================================================
    # 2. RÉSUMÉ DE L'AUDIT
    # ========================================================

    elements.append(
        Paragraph(
            "2. Résumé de l'audit",
            section_style,
        )
    )

    if score <= 8:

        level_color = RED
        level_background = LIGHT_RED

        interpretation = (
            "Maturité faible : plusieurs pratiques de "
            "cybersécurité nécessitent une amélioration prioritaire."
        )

    elif score <= 16:

        level_color = ORANGE
        level_background = LIGHT_ORANGE

        interpretation = (
            "Maturité intermédiaire : les principales pratiques "
            "sont présentes, mais plusieurs points doivent encore "
            "être renforcés."
        )

    elif score <= 21:

        level_color = GREEN
        level_background = LIGHT_GREEN

        interpretation = (
            "Bonne maturité : l'entreprise dispose d'un niveau "
            "de sécurité globalement satisfaisant."
        )

    else:

        level_color = BLUE
        level_background = LIGHT_BLUE

        interpretation = (
            "Excellente maturité : les bonnes pratiques évaluées "
            "sont largement mises en œuvre."
        )

    clean_level = (
        str(level)
        .replace("🔴", "")
        .replace("🟡", "")
        .replace("🟢", "")
        .replace("🏆", "")
        .strip()
    )

    # --------------------------------------------------------
    # Carte Score
    # --------------------------------------------------------

    score_card = Table(
        [
            [
                Paragraph(
                    "SCORE",
                    card_title_style,
                )
            ],
            [
                Paragraph(
                    f"{score}/{total_questions}",
                    card_value_style,
                )
            ],
        ],
        colWidths=[
            5 * cm
        ],
    )

    score_card.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    LIGHT_BLUE,
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    BLUE,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
            ]
        )
    )

    # --------------------------------------------------------
    # Carte Pourcentage
    # --------------------------------------------------------

    percentage_card = Table(
        [
            [
                Paragraph(
                    "TAUX DE MATURITÉ",
                    card_title_style,
                )
            ],
            [
                Paragraph(
                    f"{percentage}%",
                    card_value_style,
                )
            ],
        ],
        colWidths=[
            5 * cm
        ],
    )

    percentage_card.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    LIGHT_BLUE,
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    BLUE,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
            ]
        )
    )

    # --------------------------------------------------------
    # Carte Niveau
    # --------------------------------------------------------

    level_value_style = ParagraphStyle(
        "LevelValue",
        parent=card_value_style,
        textColor=level_color,
    )

    level_card = Table(
        [
            [
                Paragraph(
                    "NIVEAU",
                    card_title_style,
                )
            ],
            [
                Paragraph(
                    clean_level,
                    level_value_style,
                )
            ],
        ],
        colWidths=[
            5 * cm
        ],
    )

    level_card.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    level_background,
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    level_color,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
            ]
        )
    )

    # --------------------------------------------------------
    # KPI Table
    # --------------------------------------------------------

    kpi_table = Table(
        [
            [
                score_card,
                percentage_card,
                level_card,
            ]
        ],
        colWidths=[
            5.2 * cm,
            5.2 * cm,
            5.2 * cm,
        ],
    )

    kpi_table.setStyle(
        TableStyle(
            [
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    3,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    3,
                ),
            ]
        )
    )

    elements.append(kpi_table)

    elements.append(
        Spacer(
            1,
            10,
        )
    )

    # --------------------------------------------------------
    # Interprétation
    # --------------------------------------------------------

    interpretation_style = ParagraphStyle(
        "Interpretation",
        parent=normal_style,
        fontName="Helvetica-Bold",
        textColor=level_color,
    )

    interpretation_table = Table(
        [
            [
                Paragraph(
                    interpretation,
                    interpretation_style,
                )
            ]
        ],
        colWidths=[
            15.6 * cm
        ],
    )

    interpretation_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    level_background,
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.8,
                    level_color,
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    10,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    10,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
            ]
        )
    )

    elements.append(
        interpretation_table
    )

    # ========================================================
    # 3. SCORES PAR THÈME
    # ========================================================

    elements.append(
        Paragraph(
            "3. Scores par thème",
            section_style,
        )
    )

    theme_data = [
        [
            "Thème",
            "Score",
            "Total",
            "Pourcentage",
        ]
    ]

    for theme in theme_scores:

        score_theme = theme_scores[theme]
        total_theme = theme_totals[theme]

        percentage_theme = round(
            (score_theme / total_theme) * 100
        )

        theme_data.append(
            [
                Paragraph(
                    theme,
                    small_style,
                ),
                str(score_theme),
                str(total_theme),
                f"{percentage_theme}%",
            ]
        )

    theme_table = Table(
        theme_data,
        colWidths=[
            8 * cm,
            2.5 * cm,
            2.5 * cm,
            3 * cm,
        ],
        repeatRows=1,
    )

    theme_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    BORDER_GRAY,
                ),
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    NAVY,
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    WHITE,
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),
                (
                    "ALIGN",
                    (1, 1),
                    (-1, -1),
                    "CENTER",
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        WHITE,
                        LIGHT_GRAY,
                    ],
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
            ]
        )
    )

    elements.append(theme_table)

    # ========================================================
    # 4. ANALYSE DES DOMAINES
    # ========================================================

    elements.append(
        Paragraph(
            "4. Analyse des domaines",
            section_style,
        )
    )

    elements.append(
        Paragraph(
            "Performance par domaine",
            ParagraphStyle(
                "PerformanceTitle",
                parent=small_style,
                fontName="Helvetica-Bold",
                fontSize=10,
                textColor=NAVY,
                spaceAfter=8,
            ),
        )
    )

    theme_analysis_rows = []

    strong_points = []
    weak_points = []

    for theme in theme_scores:

        score_theme = theme_scores[theme]
        total_theme = theme_totals[theme]

        percentage_theme = round(
            (score_theme / total_theme) * 100
        )

        if percentage_theme >= 80:

            strong_points.append(
                (
                    theme,
                    percentage_theme,
                )
            )

        else:

            weak_points.append(
                (
                    theme,
                    percentage_theme,
                )
            )

        if percentage_theme >= 80:

            bar_color = GREEN

        elif percentage_theme >= 40:

            bar_color = ORANGE

        else:

            bar_color = RED

        bar_width = max(
            0.2,
            6 * percentage_theme / 100,
        )

        remaining_width = max(
            0.2,
            6 - bar_width,
        )

        bar_table = Table(
            [
                [
                    "",
                    "",
                ]
            ],
            colWidths=[
                bar_width * cm,
                remaining_width * cm,
            ],
            rowHeights=[
                0.35 * cm
            ],
        )

        bar_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, 0),
                        bar_color,
                    ),
                    (
                        "BACKGROUND",
                        (1, 0),
                        (1, 0),
                        colors.HexColor(
                            "#E5E9EF"
                        ),
                    ),
                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        0,
                        colors.white,
                    ),
                ]
            )
        )

        theme_analysis_rows.append(
            [
                Paragraph(
                    theme,
                    small_style,
                ),
                bar_table,
                Paragraph(
                    f"<b>{percentage_theme}%</b>",
                    ParagraphStyle(
                        "PercentageValue",
                        parent=small_style,
                        alignment=TA_CENTER,
                        fontName="Helvetica-Bold",
                        textColor=bar_color,
                    ),
                ),
            ]
        )

    theme_analysis_table = Table(
        theme_analysis_rows,
        colWidths=[
            7 * cm,
            7 * cm,
            1.6 * cm,
        ],
    )

    theme_analysis_table.setStyle(
        TableStyle(
            [
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    4,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
            ]
        )
    )

    elements.append(theme_analysis_table)

    elements.append(
        Spacer(
            1,
            10,
        )
    )

    # --------------------------------------------------------
    # Points forts / points à améliorer
    # --------------------------------------------------------

    strong_text = []

    for theme, theme_percentage in strong_points:

        strong_text.append(
            f"<b>{theme}</b> — "
            f"{theme_percentage}%"
        )

    weak_text = []

    for theme, theme_percentage in weak_points:

        weak_text.append(
            f"<b>{theme}</b> — "
            f"{theme_percentage}%"
        )

    if not strong_text:

        strong_text.append(
            "Aucun domaine n'atteint actuellement 80%."
        )

    if not weak_text:

        weak_text.append(
            "Aucun domaine majeur à améliorer."
        )

    strong_header_style = ParagraphStyle(
        "StrongHeader",
        parent=small_style,
        fontName="Helvetica-Bold",
        textColor=GREEN,
    )

    weak_header_style = ParagraphStyle(
        "WeakHeader",
        parent=small_style,
        fontName="Helvetica-Bold",
        textColor=ORANGE,
    )

    analysis_table = Table(
        [
            [
                Paragraph(
                    "POINTS FORTS",
                    strong_header_style,
                ),
                Paragraph(
                    "POINTS À AMÉLIORER",
                    weak_header_style,
                ),
            ],
            [
                Paragraph(
                    "<br/>".join(strong_text),
                    small_style,
                ),
                Paragraph(
                    "<br/>".join(weak_text),
                    small_style,
                ),
            ],
        ],
        colWidths=[
            8 * cm,
            8 * cm,
        ],
    )

    analysis_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    BORDER_GRAY,
                ),
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, 0),
                    LIGHT_GREEN,
                ),
                (
                    "BACKGROUND",
                    (1, 0),
                    (1, 0),
                    LIGHT_ORANGE,
                ),
                (
                    "BACKGROUND",
                    (0, 1),
                    (0, 1),
                    colors.HexColor(
                        "#F7FCF7"
                    ),
                ),
                (
                    "BACKGROUND",
                    (1, 1),
                    (1, 1),
                    colors.HexColor(
                        "#FFFAF3"
                    ),
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP",
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    9,
                ),
            ]
        )
    )

    elements.append(analysis_table)

    # ========================================================
    # 5. RECOMMANDATIONS PRIORITAIRES
    # ========================================================

    elements.append(
        Paragraph(
            "5. Recommandations prioritaires",
            section_style,
        )
    )

    priority_order = {
        "Critique": 1,
        "Élevée": 2,
        "Moyenne": 3,
    }

    sorted_recommendations = sorted(
        recommendations,
        key=lambda rec: priority_order.get(
            rec.get(
                "priority",
                "Moyenne",
            ),
            99,
        ),
    )

    top_recommendations = sorted_recommendations[:3]

    if not top_recommendations:

        elements.append(
            Paragraph(
                "Aucune recommandation prioritaire. "
                "Toutes les mesures évaluées sont conformes.",
                normal_style,
            )
        )

    else:

        for index, rec in enumerate(
            top_recommendations,
            start=1,
        ):

            priority = rec.get(
                "priority",
                "Moyenne",
            )

            theme = rec.get(
                "theme",
                "",
            )

            recommendation = rec.get(
                "recommendation",
                "",
            )

            question = rec.get(
                "question",
                "",
            )

            if priority == "Critique":

                priority_color = RED
                priority_background = LIGHT_RED

            elif priority == "Élevée":

                priority_color = ORANGE
                priority_background = LIGHT_ORANGE

            else:

                priority_color = YELLOW
                priority_background = LIGHT_YELLOW

            recommendation_content = (
                f"<b>{index}. {priority} — "
                f"{theme}</b><br/><br/>"
                f"<b>Point évalué :</b><br/>"
                f"{question}<br/><br/>"
                f"<b>Action recommandée :</b><br/>"
                f"{recommendation}"
            )

            recommendation_box = Table(
                [
                    [
                        Paragraph(
                            recommendation_content,
                            recommendation_style,
                        )
                    ]
                ],
                colWidths=[
                    15.6 * cm
                ],
            )

            recommendation_box.setStyle(
                TableStyle(
                    [
                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, -1),
                            priority_background,
                        ),
                        (
                            "BOX",
                            (0, 0),
                            (-1, -1),
                            0.8,
                            priority_color,
                        ),
                        (
                            "LINEBEFORE",
                            (0, 0),
                            (0, 0),
                            4,
                            priority_color,
                        ),
                        (
                            "LEFTPADDING",
                            (0, 0),
                            (-1, -1),
                            12,
                        ),
                        (
                            "RIGHTPADDING",
                            (0, 0),
                            (-1, -1),
                            10,
                        ),
                        (
                            "TOPPADDING",
                            (0, 0),
                            (-1, -1),
                            10,
                        ),
                        (
                            "BOTTOMPADDING",
                            (0, 0),
                            (-1, -1),
                            10,
                        ),
                    ]
                )
            )

            elements.append(
                KeepTogether(
                    [
                        recommendation_box,
                        Spacer(
                            1,
                            10,
                        ),
                    ]
                )
            )

    # ========================================================
    # 6. CONCLUSION
    # ========================================================

    elements.append(
        Paragraph(
            "6. Conclusion",
            section_style,
        )
    )

    conclusion = (
        f"L'évaluation réalisée pour "
        f"<b>{company.get('entreprise', '')}</b> "
        f"obtient un score de "
        f"<b>{score}/{total_questions}</b>, "
        f"soit un taux de maturité de "
        f"<b>{percentage}%</b>. "
        f"Le niveau de maturité évalué est : "
        f"<b>{clean_level}</b>."
    )

    elements.append(
        Paragraph(
            conclusion,
            normal_style,
        )
    )

    elements.append(
        Spacer(
            1,
            8,
        )
    )

    if recommendations:

        conclusion_text = (
            "Plusieurs actions d'amélioration ont été "
            "identifiées. Leur mise en œuvre permettra de "
            "renforcer progressivement la maturité "
            "cybersécurité de l'entreprise."
        )

    else:

        conclusion_text = (
            "Aucune recommandation prioritaire n'a été "
            "identifiée selon les critères évalués. "
            "Il est néanmoins recommandé de maintenir les "
            "mesures de sécurité en place et de réaliser "
            "régulièrement une nouvelle évaluation."
        )

    elements.append(
        Paragraph(
            conclusion_text,
            normal_style,
        )
    )

    # ========================================================
    # 7. COMPARAISON INDICATIVE ISO
    # ========================================================

    elements.append(
        Paragraph(
            "7. Comparaison indicative avec ISO/IEC 27001:2022",
            section_style,
        )
    )

    elements.append(
        Paragraph(
            "Cette comparaison est indicative et repose sur des "
            "domaines inspirés d'ISO/IEC 27001:2022. Elle ne "
            "constitue pas une évaluation de conformité ni une "
            "certification ISO 27001.",
            normal_style,
        )
    )

    elements.append(
        Spacer(
            1,
            8,
        )
    )

    # --------------------------------------------------------
    # Résumé ISO
    # --------------------------------------------------------

    iso_summary_data = [
        [
            "Score global indicatif",
            f"{iso_global_percentage}%",
        ],
        [
            "Niveau indicatif",
            iso_level,
        ],
    ]

    iso_summary_table = Table(
        iso_summary_data,
        colWidths=[
            7 * cm,
            9 * cm,
        ],
    )

    iso_summary_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    BORDER_GRAY,
                ),
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    LIGHT_BLUE,
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (0, -1),
                    NAVY,
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold",
                ),
                (
                    "FONTNAME",
                    (1, 0),
                    (1, -1),
                    "Helvetica-Bold",
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
            ]
        )
    )

    elements.append(
        iso_summary_table
    )

    elements.append(
        Spacer(
            1,
            10,
        )
    )

    # --------------------------------------------------------
    # Tableau des domaines
    # --------------------------------------------------------

    iso_table_data = [
        [
            "Domaine CyberAudit",
            "Domaine ISO-inspired",
            "Score",
        ]
    ]

    iso_domain_mapping = {
        "Gouvernance et sensibilisation":
            "Gouvernance et gestion des risques",

        "Gestion des accès et des incidents":
            "Contrôles d'accès et gestion des incidents",

        "Sécurité des systèmes et du réseau":
            "Sécurité technologique",

        "Protection des données":
            "Protection de l'information",
    }

    for cyberaudit_theme, iso_domain in iso_domain_mapping.items():

        iso_percentage = iso_results[
            iso_domain
        ]["percentage"]

        iso_table_data.append(
            [
                Paragraph(
                    cyberaudit_theme,
                    small_style,
                ),
                Paragraph(
                    iso_domain,
                    small_style,
                ),
                f"{iso_percentage}%",
            ]
        )

    iso_table = Table(
        iso_table_data,
        colWidths=[
            6 * cm,
            7 * cm,
            3 * cm,
        ],
        repeatRows=1,
    )

    iso_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    BORDER_GRAY,
                ),
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    NAVY,
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    WHITE,
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),
                (
                    "ALIGN",
                    (2, 1),
                    (2, -1),
                    "CENTER",
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        WHITE,
                        LIGHT_GRAY,
                    ],
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
            ]
        )
    )

    elements.append(
        iso_table
    )

    elements.append(
        Spacer(
            1,
            8,
        )
    )

    elements.append(
        Paragraph(
            "<b>Important :</b> ce résultat fournit une "
            "comparaison indicative basée sur les domaines "
            "retenus dans le prototype CyberAudit. Il ne "
            "constitue pas une mesure officielle de conformité "
            "à ISO/IEC 27001.",
            small_style,
        )
    )

    # ========================================================
    # BLOC FINAL
    # ========================================================

    elements.append(
        Spacer(
            1,
            18,
        )
    )

    final_box_style = ParagraphStyle(
        "FinalBox",
        parent=small_style,
        alignment=TA_CENTER,
        textColor=NAVY,
    )

    final_box = Table(
        [
            [
                Paragraph(
                    "<b>CyberAudit</b><br/>"
                    "Plateforme d'évaluation de la "
                    "maturité cybersécurité des PME marocaines",
                    final_box_style,
                )
            ]
        ],
        colWidths=[
            15.6 * cm
        ],
    )

    final_box.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    LIGHT_BLUE,
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.7,
                    BLUE,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    10,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    10,
                ),
            ]
        )
    )

    elements.append(
        final_box
    )

    # ========================================================
    # GÉNÉRATION
    # ========================================================

    document.build(
        elements,
        onFirstPage=add_page_footer,
        onLaterPages=add_page_footer,
    )

    buffer.seek(0)

    return buffer.getvalue()