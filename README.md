
# AutoDeployCLI - Docker Build & Deploy Tool

## Overview
AutoDeployCLI is a command-line tool that automates the building, running, and deployment of Docker containers. It simplifies the process of setting up Docker containers with the ability to rollback to previous versions if a build fails.

## Features
- Build Docker images with versioning.
- Run Docker containers with specified ports.
- Simulate deployment to a mock server.
- Rollback to the last successful Docker image.

## Requirements
- Docker
- Python 3.x

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/nickcuenca/autodeploy-cli.git
cd autodeploy-cli
pip install -r requirements.txt
```

## Usage
- **Build Docker Image**:
    ```bash
    python3 autodeploy.py build --version v1
    ```
- **Run Container**:
    ```bash
    python3 autodeploy.py run
    ```
- **Deploy (Build + Run + Mock Deployment)**:
    ```bash
    python3 autodeploy.py deploy --version v1
    ```

## License
MIT License. See [LICENSE](LICENSE) for more details.