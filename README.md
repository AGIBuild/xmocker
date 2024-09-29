# Mock Server

This mock server is built using Flask and serves predefined API responses for testing and development purposes. It allows you to define multiple base URLs, each with its own set of APIs, and navigate through them easily.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:

    ```sh
    pip install flask
    ```

## Configuration

The configuration for the mock server is defined in the `settings.py` file. Here is an example configuration:

```python
# settings.py
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
```

- [`PORT`]: The port on which the mock server will run.
- [`BASE_URLS`]: A dictionary defining the base URLs and their respective APIs.

## Running the Server

To start the mock server, run the following command:

```sh
python mockapi.py
```

The server will start on the specified port (default is 5000).

## Usage

### Accessing the Base URL List

Navigate to the root URL to see a list of all base URLs:

```
http://localhost:5000/
```

### Accessing API Lists

Click on any base URL link to see a list of all APIs under that base URL. For example:

```
http://localhost:5000/api/v1/
```

### Accessing API Endpoints

Click on any API link to access the predefined response for that API. For example:

```
http://localhost:5000/api/v1/user
```

## Adding New APIs

To add new APIs, update the [`BASE_URLS`] dictionary in the [`settings.py`] file with the new API details. Ensure that the `response_file` points to a valid JSON file containing the mock response.

## Example Response Files

Create JSON files for the responses in the `api` directory. For example:


```json
// response_user.json
{
    "user": "This is a mock response for the user endpoint."
}
```

## License

This project is licensed under the MIT License.
