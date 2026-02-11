project = "V2TextMail"
author = "Andrey Vyrlin"
release = "1.0"

extensions = [
    "sphinxcontrib.plantuml",
]

plantuml = r"java -jar C:\plantuml\plantuml-1.2026.1.jar"

templates_path = ["_templates"]
exclude_patterns = []

language = "ru"

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_logo = "_static/logo.png"

