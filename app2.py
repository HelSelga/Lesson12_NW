from flask import Flask, request, render_template
import json

CANDIDATES_PATH = 'candidates_info.json'
SETTINGS_PATH = 'settings.json'

app = Flask(__name__)


@app.route('/')
def page_app_work():
    settings = get_settings()
    online = settings.get('online', False)
    if online:
        return 'Приложение работает'
    else:
        return 'Приложение не работает'


@app.route('/candidate/<int:cid>')
def candidate_page(cid):
    with open(CANDIDATES_PATH, 'r', encoding='utf-8') as f:
        candidates = json.load(f)
    return render_template('candidate_profile.html', profiles=candidates, cid=cid)


@app.route('/list')
def page_list_of_candidates():
    with open(CANDIDATES_PATH, 'r', encoding='utf-8') as f:
        candidates = json.load(f)
    return render_template('list_of_profiles.html', profiles=candidates)


@app.route('/search')
def page_search_name():
    name = request.args.get('name', '')

    with open(SETTINGS_PATH, 'r', encoding='utf-8') as f:
        settings = json.load(f)
    case_sensitive = settings['case-sensitive']

    with open(CANDIDATES_PATH, 'r', encoding='utf-8') as f:
        candidates = json.load(f)

    return render_template('search_name.html', profiles=candidates, case_sensitive=case_sensitive, name=name)


@app.route('/skill/<skill_name>')
def page_search_skill(skill_name):
    with open(SETTINGS_PATH, 'r', encoding='utf-8') as f:
        settings = json.load(f)
    limit = settings.get('limit', 3)

    with open(CANDIDATES_PATH, 'r', encoding='utf-8') as f:
        candidates = json.load(f)

    candidates_match = []
    skill = skill_name.lower()

    for candidate in candidates:
        if skill in candidate['skills'].lower().split(", "):
            candidates_match.append(candidate)
    candidates_count = len(candidates_match[:limit])

    return render_template('search_skill.html', profiles=candidates, limit=limit, skill=skill, skill_name=skill_name,
                           candidates_count=candidates_count,
                           )


if __name__ == "__main__":
    app.run()
