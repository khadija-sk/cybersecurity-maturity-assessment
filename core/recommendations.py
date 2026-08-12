from core.questions import questions


def generate_recommendations(answers):
    recommendations = []

    for i, q in enumerate(questions):

        if answers.get(i) == "Non":

            recommendations.append({
                "theme": q["theme"],
                "question": q["question"],
                "recommendation": q["recommendation"],
                "priority": q["priority"]
            })

    return recommendations