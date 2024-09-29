# settings.py
# Constants for the mock server

# settings.py
# Constants for the mock server

PORT = 5000

BASE_URLS = {
    'base1': {
        'base_url': '/welcome',
        'apis': [
            {
                'name': 'welcome',
                'url': '/welcome',
                'method': 'GET',
                'response_file': 'response_welcome.json'
            }
        ]
    },
    'base2': {
        'base_url': '/api/v2',
        'apis': [
            {
                'name': 'info',
                'url': '/info',
                'method': 'GET',
                'response_file': 'response_info.json'
            },
            {
                'name': 'status',
                'url': '/status',
                'method': 'GET',
                'response_file': 'response_status.json'
            }
        ]
    }
}
