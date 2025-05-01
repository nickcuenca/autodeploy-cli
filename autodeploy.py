import subprocess
import argparse

def build_image():
    print("[+] Building Docker image...")
    subprocess.run(["docker", "build", "-t", "autodeploy-app", "."], check=True)

def run_container():
    print("[+] Running container on http://localhost:5000 ...")
    subprocess.run(["docker", "run", "-p", "5000:5000", "autodeploy-app"], check=True)

def deploy_mock():
    print("[+] 'Deploying' to mock server (this is a simulation)...")
    print("🎉 App deployed! Visit: http://localhost:5000")

parser = argparse.ArgumentParser(description="AutoDeployCLI - Docker Build & Deploy Tool")
parser.add_argument("command", choices=["build", "run", "deploy"], help="Command to execute")

args = parser.parse_args()

if args.command == "build":
    build_image()
elif args.command == "run":
    run_container()
elif args.command == "deploy":
    build_image()
    run_container()
    deploy_mock()