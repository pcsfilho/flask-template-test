# Flask Starter Test

A simple Flask app starter template to testing.

## Features

Here is a list of the available features:

- **Tests**: Unit tests are included to ensure the application's functionality and robustness.

## Getting Started

### Running The Application

1.Clone the repository to your local machine:

```bash
git clone https://github.com/riad-azz/flask-template && cd flask-template
```

2.Install the required dependencies:

```bash
pip install -r requirements.txt
```

3.The application can be run with the following command:

```bash
python server.py
```

4.To enable env file make sure to copy the `.env.example` content and create a `.env` file:

```.env
# Flask Variables
SECRET_KEY="YOUR-SECRET-KEY"
```

**Note**: for development you need to create a `.env.dev` file.

### Running Tests

You can write tests in `flask-template/tests`, where you will also find some examples.

To run the tests simply use the command:

```bash
python -m pytest
```

You can switch between running the tests from `.env.dev` _(development environment)_ or `.env` _(production environment)_ by going to `flask-template/tests/__init__.py` and changing the value of `FLASK_DEBUG`:

```python
import os

# Set 'False' to test with .env
# Set 'True' to test with .env.dev
os.environ["FLASK_DEBUG"] = "True"
```

## License

This project is licensed under the terms of the MIT license. For more details, see the LICENSE file in the repository.
