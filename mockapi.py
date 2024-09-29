from flask import Flask, jsonify, render_template_string
import json
import os
from settings import BASE_URLS, PORT

app = Flask(__name__)

def load_response(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)

# Template for listing APIs
api_list_template = """
<!DOCTYPE html>
<html>
<head>
    <title>API List</title>
</head>
<body>
    <a href="/">Back to Base URL List</a>
    <h1>API List for {{ base_url }}</h1>
    <ul>
    {% for api in apis %}
        <li><a href="{{ api.url }}">{{ api.name }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>
"""

# Template for listing base URLs
base_url_list_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Base URL List</title>
</head>
<body>
    <h1>Base URL List</h1>
    <ul>
    {% for base_url in base_urls %}
        <li><a href="{{ base_url.url }}">{{ base_url.name }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>
"""

# Route to list all base URLs
@app.route('/', methods=['GET'])
def list_base_urls():
    base_url_links = [{'name': base_name, 'url': base_config['base_url'] + '/'} for base_name, base_config in BASE_URLS.items()]
    return render_template_string(base_url_list_template, base_urls=base_url_links)

for base_name, base_config in BASE_URLS.items():
    base_url = base_config['base_url']
    
    # Route to list all APIs for the base URL
    def create_list_apis_route(base_url, apis):
        @app.route(base_url + '/', methods=['GET'], endpoint=f"list_apis_{base_name}")
        def list_apis():
            api_links = [{'name': api['name'], 'url': base_url + api['url']} for api in apis]
            return render_template_string(api_list_template, base_url=base_url, apis=api_links)
    
    create_list_apis_route(base_url, base_config['apis'])
    
    for api_config in base_config['apis']:
        url = base_url + api_config['url']
        method = api_config['method']
        response_file = api_config['response_file']
        
        # Define a route dynamically
        def create_route(response_file):
            def route():
                file_path = os.path.join(os.path.dirname(__file__),'api', response_file)
                response = load_response(file_path)
                return jsonify(response)
            return route
        
        # Use a unique endpoint name by combining base URL and API name
        endpoint = f"{base_url.strip('/')}_{api_config['name']}"
        app.route(url, methods=[method], endpoint=endpoint)(create_route(response_file))

if __name__ == '__main__':
    app.run(port=PORT, debug=True)