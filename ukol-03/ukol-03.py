# Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.
# Soubor si ulož a načti do slovníku.
# Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".
# Výsledný slovník ulož jako JSON do souboru prospech.json.

import json

def pass_or_fail(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


with open("ukol-03\\body.json", mode="r", encoding="utf-8") as file_scores:
    scores = json.load(file_scores)

pass_or_fail_dict = {}
for student, score in scores.items():
    result = pass_or_fail(score)
    pass_or_fail_dict[student] = result

with open("ukol-03\\prospech.json", mode="w", encoding="utf-8") as json_file:
    json.dump(pass_or_fail_dict, json_file, indent=4, ensure_ascii=False)



# BONUS
# Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.
# Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:
#1: 90 a více
#2: 70-89
#3: 50-69
#4: 30-49
#5: 29 a méně

def grade(score):
    if score >= 90:
        return 1
    elif score >= 70 and score < 90:
        return 2
    elif score >= 50 and score < 70:
        return 3
    elif score >= 30 and score < 50:
        return 4
    else:
        return 5

def create_nested_dict(dictionary):
    new_dict = {}
    for key,value in dictionary.items():
        grade_from_value = grade(value)
        new_dict[key] = {"score": value, "grade": grade_from_value}
    return new_dict


with open("ukol-03\\bonusy.json", mode="r", encoding="utf-8") as file_bonuses:
    bonuses = json.load(file_bonuses)

scores_with_bonus = scores
for student, score in scores_with_bonus.items():   
    if student in bonuses:
        scores_with_bonus[student] += bonuses[student]

final_dict_with_grades = create_nested_dict(scores_with_bonus)

with open("ukol-03\\body_znamky.json", mode="w", encoding="utf-8") as json_file:
    json.dump(final_dict_with_grades, json_file, indent=4, ensure_ascii=False)

