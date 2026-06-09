import os
import re
from datetime import datetime

from typing import Any

from flask import Flask, render_template_string, render_template, request, Blueprint
from jinja2 import ChoiceLoader, PackageLoader, FileSystemLoader, PrefixLoader
from jinja2.runtime import Macro
from markupsafe import Markup

from dmutils.external import external as external_blueprint
from dmutils.formats import datetimeformat


def parse_document_upload_time(data):
    match = re.search(r'(\d{4}-\d{2}-\d{2}-\d{2}\d{2})\..{2,3}$', data)
    if match:
        return datetime.strptime(match.group(1), '%Y-%m-%d-%H%M')


# This is needed because of compliance communications attachments
# When really in use the form field will have the hidden_tag method
class hidden_tag_dict(dict):
    def hidden_tag(self):
        return Markup(
            f'<input type="hidden" name="{self["file"]["name"].replace("file", "hidden_tag")}" value="hidden-tag">'
        )


def transform_dict_to_hidden_tag_dict(obj):
    return hidden_tag_dict(
        **{
            key: transform_dict_to_hidden_tag_dict(value) if isinstance(value, dict) else value
            for key, value in obj.items()
        }
    )


def _invoke(self, arguments, autoescape):
    if self._environment.is_async:
        return self._async_invoke(arguments, autoescape)

    arguments = [
        transform_dict_to_hidden_tag_dict(argument) if isinstance(argument, dict) else argument
        for argument in arguments
    ]

    rv = self._func(*arguments)

    if autoescape:
        rv = Markup(rv)

    return rv


Macro._invoke = _invoke  # type: ignore


def create_app():
    app = Flask(__name__)

    app.jinja_loader = ChoiceLoader(
        [
            PrefixLoader(
                {
                    'govuk_frontend_jinja': PackageLoader('govuk_frontend_jinja'),
                    'digitalmarketplace_frontend_jinja': FileSystemLoader(
                        searchpath=os.path.join(
                            os.path.dirname(__file__), '../../digitalmarketplace_frontend_jinja/templates'
                        )
                    ),
                }
            ),
            FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), 'templates')),
        ]
    )
    app.jinja_env.globals['govukRebrand'] = False

    # For the urls in the header and footer
    app.register_blueprint(external_blueprint)

    # Filters for some of the components
    app.add_template_filter(datetimeformat)
    app.add_template_filter(parse_document_upload_time)

    main = Blueprint('main', __name__)

    @main.get('/')
    def index() -> str:
        return 'Hello there'

    @main.get('/suppliers/add-item/<section_id>/<question_id>/<item_number>')
    def add_item(section_id, question_id, item_number) -> str:
        return 'Hello there'

    @main.get('/suppliers/remove-item/<section_id>/<question_id>/<item_number>')
    def remove_item(section_id, question_id, item_number) -> str:
        return 'Hello there'

    app.register_blueprint(main)

    @app.post('/component/<string:component>')
    def component(component: str) -> Any:
        data: Any = request.get_json()
        # Render the component using the data provided
        # component is the hyphenated component name e.g. character-count
        # data['macro_name'] is the camelcased name e.g. CharacterCount
        # data['params] are the params that will be passed to the macro
        # Returns an html response that is just the template in question - no wrapping <html>, <body> elements etc
        return render_template_string(
            f"""
            {{% from "digitalmarketplace_frontend_jinja/components/{component}/macro.html" import digitalmarketplace{data['macro_name']} %}}
            {{{{ digitalmarketplace{data['macro_name']}({data['params']}) }}}}
            """
        )

    @app.post('/layout/<string:layout>')
    def layout(layout: str) -> Any:
        data: Any = request.get_json()
        # Render the layout template using the data provided
        return render_template(f'digitalmarketplace_frontend_jinja/layouts/{layout}.html', **data.get('params', {}))

    @app.post('/error/<string:error>')
    def error_page(error: str) -> Any:
        data: Any = request.get_json()
        # Render the error template using the data provided
        return render_template(f'digitalmarketplace_frontend_jinja/errors/{error}.html', **data.get('params', {}))

    return app
