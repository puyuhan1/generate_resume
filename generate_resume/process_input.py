import re

def process_input(user_input):
    data = {
        "degree": None,
        "major": None,
        "university": None,
        "bachelor_degree": None,
        "bachelor_major": None,
        "bachelor_university": None,
        "experiences": [],
        "skills": [],
    }

    # Degree & Major (Master's)
    if "master" in user_input.lower():
        match = re.search(r"master.*?in ([\w\s]+)", user_input, re.IGNORECASE)
        if match:
            data["degree"] = "Master's"
            data["major"] = match.group(1).strip()

    # Degree & Major (Bachelor's)
    if "bachelor" in user_input.lower():
        match = re.search(r"bachelor.*?in ([\w\s]+)", user_input, re.IGNORECASE)
        if match:
            data["bachelor_degree"] = "Bachelor's"
            data["bachelor_major"] = match.group(1).strip()

    # University detection
    unis = ["Columbia University", "Harvard", "MIT", "Stanford", "Berkeley", "UCDavis"]
    for uni in unis:
        if uni.lower() in user_input.lower():
            if uni == "Columbia University":
                data["university"] = "Columbia University"
            elif uni == "Harvard":
                data["university"] = "Harvard University"
            elif uni == "MIT":
                data["university"] = "Massachusetts Institute of Technology"
            elif uni == "Stanford":
                data["university"] = "Stanford University"
            elif uni == "Berkeley":
                data["university"] = "UC Berkeley"
            elif uni == "UCDavis":
                data["university"] = "UC Davis"

    # Experience extraction
    exp_match = re.findall(r"(interned at .+?[\.!?])", user_input, re.IGNORECASE)
    for match in exp_match:
        data["experiences"].append(match.strip())

    # Skills extraction
    skills_match = re.search(r"skills? in ([\w\s,]+)", user_input, re.IGNORECASE)
    if skills_match:
        skills_str = skills_match.group(1)
        skills_list = [s.strip() for s in skills_str.split(",")]
        data["skills"] = skills_list

    return data