from llm_utils import polish_experience_bullet

def generate_education(data):
    lines = []

    # Master's or higher
    if data.get("degree") and data.get("major"):
        edu_line = f"{data['degree']} in {data['major']}"
        if data.get("university"):
            edu_line += f", {data['university']}"
        lines.append(edu_line)

    # Bachelor's
    if data.get("bachelor_degree") and data.get("bachelor_major"):
        bachelor_line = f"{data['bachelor_degree']} in {data['bachelor_major']}"
        if data.get("bachelor_university"):
            bachelor_line += f", {data['bachelor_university']}"
        lines.append(bachelor_line)

    if not lines:
        return "Education:\n  - Education information not available."
    
    return "Education:\n" + "\n".join(f"  - {line}" for line in lines)


def generate_experience(data):
    if data.get("experiences") and any(data["experiences"]):
        print("📌 Polishing user-provided experience bullets...")
        polished = [
            polish_experience_bullet(exp, role="data analyst", skills=data.get("skills", []))
            for exp in data["experiences"]
        ]
        return "Experience:\n" + "\n".join(f"  - {b}" for b in polished)
    else:
        print("📌 Generating fake experience based on major and skills...")
        fake_bullets = generate_fake_achievements(data.get("major", ""), data.get("skills", []))
        polished = [
            polish_experience_bullet(bullet, role="data analyst", skills=data.get("skills", []))
            for bullet in fake_bullets
        ]
        return "Experience:\n" + "\n".join(polished)



def generate_skills(data):
    if data.get("skills"):
        return "Skills:\n  " + ", ".join(data["skills"])
    else:
        return "Skills:\n  - No skills listed."


def generate_resume(data):
    sections = [
        generate_education(data),
        generate_experience(data),
        generate_skills(data),
    ]
    return "\n\n".join(section for section in sections if section.strip())

def generate_fake_achievements(major, skills):
    bullets = []
    major = major.lower() if major else ""
    skills = [s.lower() for s in skills]

    # Data Science / Statistics / Analytics
    if any(kw in major for kw in ["data", "statistics", "analytics"]):
        if "python" in skills:
            bullets.append("  - Built data pipelines and analysis tools using Python and Pandas.")
        if "sql" in skills:
            bullets.append("  - Designed and executed complex SQL queries to extract actionable insights from databases.")
        if "machine learning" in skills:
            bullets.append("  - Developed predictive models to support data-driven decision-making.")
        if not bullets:
            bullets.append("  - Led end-to-end development of analytics projects using modern software tools to derive actionable insights.")
        return bullets

    # Computer Science / Software Engineering
    if any(kw in major for kw in ["computer", "software", "cs"]):
        if "java" in skills:
            bullets.append("  - Developed and maintained backend services using Java and Spring Boot.")
        if "cloud" in skills or "aws" in skills:
            bullets.append("  - Deployed scalable applications on cloud platforms such as AWS.")
        if "python" in skills:
            bullets.append("  - Created automation scripts and APIs using Python.")
        if not bullets:
            bullets.append("  - Led end-to-end development of technical projects using modern software tools to deliver robust solutions.")
        return bullets

    # Finance / Business
    if any(kw in major for kw in ["finance", "business", "economics"]):
        if "excel" in skills:
            bullets.append("  - Built financial models and dashboards in Excel to support strategic decision-making.")
        if "sql" in skills:
            bullets.append("  - Queried financial datasets to identify trends and performance metrics.")
        if not bullets:
            bullets.append("  - Led business-focused analytics projects using industry-standard tools to improve operations.")
        return bullets

    # Default fallback
    bullets.append("  - Led end-to-end development of analytics projects using modern software tools to derive actionable insights.")
    return bullets
