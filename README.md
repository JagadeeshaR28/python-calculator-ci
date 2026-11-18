# Python Calculator CI

[![CI](https://github.com/YOUR_USERNAME/python-calculator-ci/actions/workflows/ci.yml/badge.svg)](https://github.com/JagadeeshaR28/python-calculator-ci/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-TBD-lightgrey.svg)](LICENSE)

A simple Python calculator application demonstrating automated testing, code quality validation, and Continuous Integration using GitHub Actions.

## Overview

Python Calculator CI is a lightweight Python application that performs basic arithmetic operations.

The project demonstrates engineering practices used in modern software development, including:

- Modular Python application structure.
- Automated unit testing using Pytest.
- Code quality validation using Flake8.
- Automated CI pipeline using GitHub Actions.
- Git-based source code management.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero exception handling.
- Automated unit testing.
- Automated code quality checks.

## Architecture

The project follows a simple modular architecture.

```text
python-calculator-ci/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── tests/
│   └── test_calculator.py
│
├── calculator.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### CI Workflow Architecture

```text
Developer
    |
    v
Git Repository
    |
    v
GitHub Repository
    |
    v
GitHub Actions Trigger
    |
    v
Python Environment Setup
    |
    v
Install Dependencies
    |
    v
Flake8 Code Quality Check
    |
    v
Pytest Automated Tests
    |
    v
CI Result
(Pass / Fail)
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Application development |
| Pytest | Automated testing |
| Flake8 | Code quality validation |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | Continuous Integration |

## Prerequisites

Ensure the following tools are installed:

- Python 3.11 or compatible version.
- Git.
- pip (Python package installer).

Verify the installations:

```bash
python3 --version
git --version
pip3 --version
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-calculator-ci.git

cd python-calculator-ci
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

## Usage

The calculator supports four basic arithmetic operations.

Example:

```python
from calculator import add, subtract, multiply, divide

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
```

Expected output:

```text
15
5
50
2.0
```

Division by zero raises a `ValueError` to prevent invalid calculations.

## Testing

Run the automated test suite:

```bash
python -m pytest -v
```

The test suite validates the calculator's arithmetic operations and exception handling.

## Code Quality

Run Flake8 to check Python code quality:

```bash
flake8 .
```

## Continuous Integration

The project uses GitHub Actions to automatically validate code changes.

The workflow is triggered by:

- Push events to the `main` branch.
- Pull requests targeting the `main` branch.

The pipeline performs:

1. Repository checkout.
2. Python environment setup.
3. Dependency installation.
4. Flake8 code quality validation.
5. Pytest automated testing.

A failed validation prevents the workflow from reporting a successful build.

Workflow configuration:

`.github/workflows/ci.yml`

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.

   ```bash
   git checkout -b feature/your-feature
   ```

3. Implement your changes.
4. Run automated tests.

   ```bash
   python -m pytest -v
   ```

5. Run code quality checks.

   ```bash
   flake8 .
   ```

6. Commit your changes with a meaningful commit message.

   ```bash
   git add .
   git commit -m "feat: add new calculator functionality"
   ```

7. Push your branch and create a Pull Request.

All contributions should pass the project's automated CI checks.

## Code of Conduct

All contributors are expected to follow the project's Code of Conduct.

Reference: [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/)

## Versioning

This project follows Semantic Versioning (SemVer).

Version format:

`MAJOR.MINOR.PATCH`

For example: `1.0.0`

See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

The licensing terms will be defined in the repository's `LICENSE` file.

## Maintainer

See the repository's GitHub page for project ownership and maintenance information.
