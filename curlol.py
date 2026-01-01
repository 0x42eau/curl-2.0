import subprocess
import sys

def basic_curl(url):
    try:
        # Run curl with the URL provided
        return subprocess.check_output(["curl", url]).decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Check if the user provided an argument
    if len(sys.argv) < 2:
        print("Usage: python curlol.py <URL>")
    else:
        # sys.argv[1] is the first positional argument
        target_url = sys.argv[1]
        print(basic_curl(target_url))
