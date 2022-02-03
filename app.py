from flask import Flask, render_template, request
from utills import get_settings, get_candidate_by_cid, get_candidates, search_candidate_by_name, search_candidate_by_skill

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
    candidate = get_candidate_by_cid(cid)
    page_content = f"""
    <h1>{candidate['name']}</h1>
    <p>{candidate['position']}</p>
    <img src="{candidate['picture']}" width=200/>
    <p>Навыки: {candidate['skills']}</p>
    """

    return page_content


@app.route('/list')
def page_list_of_candidates():
    candidates = get_candidates()
    page_content = "<h1>Все кандидаты</h1>"
    for candidate in candidates:
        page_content += f"""
            <p><a href="/candidate/{candidate['id']}">{candidate['name']}</a></p>
            """

    return page_content



@app.route('/search')
def page_search_name():
    name = request.args.get('name', '')

    candidates = search_candidate_by_name(name)
    candidates_count = len(candidates)

    page_content = f"<h2>Найдено кандидатов: {candidates_count}</h2>"

    for candidate in candidates:
        page_content += f"""
                <p><a href="/candidate/{candidate['id']}">{candidate['name']}</a></p>
                """

    return page_content


@app.route('/skill/<skill_name>')
def page_search_skill(skill_name):
    candidates = search_candidate_by_skill(skill_name)
    candidates_count = len(candidates)

    page_content = f"<h2>Найдено со скиллом {skill_name}: {candidates_count}</h2>"

    for candidate in candidates:
        page_content += f"""
                    <p><a href="/candidate/{candidate['id']}">{candidate['name']}</a></p>
                    """

    return page_content


if __name__ == "__main__":
    app.run()
