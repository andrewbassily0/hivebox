import sys

def print_version_and_exit(version):
    print(f"Current app version: {version}")
    sys.exit()

# Example usage
app_version = ['0.0.1']
print_version_and_exit(app_version)