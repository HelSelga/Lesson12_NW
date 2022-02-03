import json


def get_settings():
    """
    Получает и возвращает словарь из json-файла с настройками
    :return: словарь настроек
    """
    with open('settings.json', 'r', encoding='utf-8') as f:
        data_json = json.load(f)
    return data_json


def get_candidates():
    """
    Получает и возвращает список кандидатов из json-файла
    :return: список словарей с информацией о кандидатах
    """
    with open('candidates_info.json', 'r', encoding='utf-8') as f:
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


