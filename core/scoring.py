from core.questions import questions

def calculate_score(answers):
    total_questions = len(questions)

    score = 0
    theme_scores = {}
    theme_totals = {}

    for i, q in enumerate(questions):
        theme = q["theme"]

        if theme not in theme_scores:
            theme_scores[theme] = 0
            theme_totals[theme] = 0

        theme_totals[theme] += 1

        if answers.get(i) == "Oui":
            score += 1
            theme_scores[theme] += 1

    percentage = round((score / total_questions) * 100)

    return score, percentage, theme_scores, theme_totals


def maturity_level(score):
    if score <= 8:
        return "🔴 Faible"
    elif score <= 16:
        return "🟡 Intermédiaire"
    elif score <= 21:
        return "🟢 Bon"
    else:
        return "🏆 Excellent"