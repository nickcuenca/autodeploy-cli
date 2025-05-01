import subprocess
import argparse
import sys

# Function to build the Docker image with versioning
def build_image(version="latest"):
    print(f"[+] Building Docker image {version}...")
    try:
        subprocess.run(["docker", "build", "-t", f"autodeploy-app:{version}", "."], check=True)
        # Save the successful version to a file
        with open("last_successful_version.txt", "w") as f:
            f.write(version)
        print(f"Image {version} built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Build failed: {e}")
        rollback()

# Function to run the container
def run_container():
    print("[+] Running container on http://localhost:8080 ...")
    try:
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("Container is running.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running container: {e}")
        sys.exit(1)

# Rollback to the last successful version if the current build fails
def rollback():
    print("[!] Rolling back to the last successful image...")
    try:
        with open("last_successful_version.txt", "r") as f:
            last_version = f.read().strip()
        if last_version:
            print(f"Rolling back to version {last_version}...")
            subprocess.run(["docker", "pull", f"autodeploy-app:{last_version}"], check=True)
            subprocess.run(["docker", "run", "-d", "-p", "8080:8080", f"autodeploy-app:{last_version}"], check=True)
            print(f"Rollback to {last_version} successful.")
        else:
            print("[!] No last successful version found for rollback.")
            sys.exit(1)
    except Exception as e:
        print(f"[!] Error during rollback: {e}")
        sys.exit(1)

# Mock deployment simulation
def deploy_mock():
    print("[+] 'Deploying' to mock server (this is a simulation)...")
    print("🎉 App deployed! Visit: http://localhost:5000")

# Adding arguments for handling commands
parser = argparse.ArgumentParser(description="AutoDeployCLI - Docker Build & Deploy Tool")
parser.add_argument("command", choices=["build", "run", "deploy"], help="Command to execute")
parser.add_argument("--version", type=str, help="Specify the version tag for the Docker image", default="latest")

args = parser.parse_args()

# Execute the respective functions based on the command
if args.command == "build":
    build_image(args.version)
elif args.command == "run":
    run_container()
elif args.command == "deploy":
    build_image(args.version)
    run_container()
    deploy_mock()