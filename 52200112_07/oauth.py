# Filename: oauth.py

from flask_dance.contrib.github import github, make_github_blueprint

github_blueprint = make_github_blueprint(
    client_id='Ov23liBwtCBxTEJxKEoP',
    client_secret='8cf23a17f3ad63fd92f2d00fa5809b8e8086d7b9',
)

