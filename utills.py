import json

CANDIDATES_PATH = 'candidates_info.json'
SETTINGS_PATH = 'settings.json'

def get_settings():
    """
    Получает и возвращает словарь из json-файла с настройками
    :return: словарь настроек
    """
    with open(SETTINGS_PATH, 'r', encoding='utf-8') as f:
        data_json = json.load(f)
    return data_json


def get_candidates():
    """
    Получает и возвращает список кандидатов из json-файла
    :return: список словарей с информацией о кандидатах
    """
    with open(CANDIDATES_PATH, 'r', encoding='utf-8') as f:
        data_json = json.load(f)
    return data_json


def get_candidate_by_cid(cid):
    """
    :param cid: id кандидата
    :return: инфо-профиль кандидата
    """
    candidates = get_candidates()
    for candidate in candidates:
        if candidate.get('id') == cid:
            return candidate


def search_candidate_by_name(name):
    """
    :param name: имя для поиска
    :return: список найденных людей
    """
    settings = get_settings()
    case_sensitive = settings['case-sensitive']

    candidates = get_candidates()
    candidates_match = []

    for candidate in candidates:
        if name in candidate['name']:
            candidates_match.append(candidate)
            continue

        if not case_sensitive:
            if name.lower() in candidate['name'].lower():
                candidates_match.append(candidate)

    return candidates_match


def search_candidate_by_skill(skill_name):
    """
    :param skill: навык для поиска
    :return: список найденных людей
    """
    settings = get_settings()
    limit = settings.get('limit', 3)

    candidates = get_candidates()
    candidates_match = []

    skill = skill_name.lower()

    for candidate in candidates:
        skills = candidate['skills'].lower().split(", ")
        if skill in skills:
            candidates_match.append(candidate)

    return candidates_match[:limit]
