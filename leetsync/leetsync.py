import os
import requests
import json
import subprocess

LEETCODE_SESSION = os.getenv('LEETCODE_SESSION')  # User should set this as an environment variable
CSRF_TOKEN = os.getenv('LEETCODE_CSRF_TOKEN')  # User should set this as an environment variable (optional, but recommended)
HEADERS = {
    'cookie': f'LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRF_TOKEN}' if CSRF_TOKEN else f'LEETCODE_SESSION={LEETCODE_SESSION}',
    'referer': 'https://leetcode.com',
    'user-agent': 'Mozilla/5.0',
    'x-csrftoken': CSRF_TOKEN if CSRF_TOKEN else '',
}

# Directory to save submissions
SUBMISSIONS_DIR = 'submissions'

# GraphQL endpoint and query for fetching submissions
LEETCODE_GRAPHQL_URL = 'https://leetcode.com/graphql'
SUBMISSIONS_QUERY = '''
query submissionList($offset: Int!, $limit: Int!) {
  submissionList(offset: $offset, limit: $limit) {
    hasNext
    submissions {
      id
      title
      titleSlug
      statusDisplay
      lang
      timestamp
      url
    }
  }
}
'''

SUBMISSION_DETAIL_QUERY = '''
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    id
    code
    lang {
      name
    }
    runtime
    memory
    runtimeDisplay
    memoryDisplay
    timestamp
  }
}
'''

def fetch_submissions(offset=0, limit=20):
    variables = {"offset": offset, "limit": limit}
    payload = {"query": SUBMISSIONS_QUERY, "variables": variables}
    response = requests.post(LEETCODE_GRAPHQL_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()['data']['submissionList']
    else:
        print(f"Failed to fetch submissions: {response.status_code}")
        return None

def fetch_submission_code(submission_id):
    payload = {
        "query": SUBMISSION_DETAIL_QUERY,
        "variables": {"submissionId": int(submission_id)}
    }
    try:
        response = requests.post(LEETCODE_GRAPHQL_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get('data') and data['data'].get('submissionDetails'):
                details = data['data']['submissionDetails']
                if details and details.get('code'):
                    return details
                else:
                    print(f"No code found in details for submission {submission_id}. Full details: {details}")
                    return None
            else:
                print(f"No 'submissionDetails' found in response for submission {submission_id}: {data}")
                return None
        else:
            print(f"Failed to fetch code for submission {submission_id}: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Exception occurred while fetching code for submission {submission_id}: {e}")
        return None

def main():
    if not LEETCODE_SESSION:
        print("Please set your LEETCODE_SESSION cookie as an environment variable.")
        return
    os.makedirs(SUBMISSIONS_DIR, exist_ok=True)
    print("Fetching submissions from LeetCode...")
    all_submissions = []
    offset = 0
    limit = 20
    while True:
        submissions = fetch_submissions(offset=offset, limit=limit)
        if submissions and submissions['submissions']:
            all_submissions.extend(submissions['submissions'])
            print(f"Fetched {len(submissions['submissions'])} submissions (offset {offset}).")
            if submissions.get('hasNext'):
                offset += limit
            else:
                break
        else:
            break
    print(f"Total submissions fetched: {len(all_submissions)}")
    new_files = []
    for sub in all_submissions:
        if sub.get('statusDisplay') != 'Accepted':
            continue  # Skip non-accepted submissions
        detail = fetch_submission_code(sub['id'])
        if detail and detail['code']:
            # Create a filename: e.g., peak-element.py
            lang_ext = {
                'python': 'py', 'python3': 'py', 'cpp': 'cpp', 'java': 'java', 'c': 'c', 'csharp': 'cs',
                'javascript': 'js', 'typescript': 'ts', 'ruby': 'rb', 'swift': 'swift', 'go': 'go',
                'scala': 'scala', 'kotlin': 'kt', 'rust': 'rs', 'php': 'php', 'mysql': 'sql', 'bash': 'sh',
                'racket': 'rkt', 'erlang': 'erl', 'elixir': 'ex', 'dart': 'dart', 'perl': 'pl', 'haskell': 'hs',
                'lua': 'lua', 'shell': 'sh', 'pascal': 'pas', 'groovy': 'groovy', 'objective-c': 'm',
                'c++': 'cpp', 'c#': 'cs', 'f#': 'fs', 'vb': 'vb', 'matlab': 'm', 'plaintext': 'txt',
            }
            lang_name = detail['lang']['name'].lower() if detail.get('lang') and detail['lang'].get('name') else 'txt'
            ext = lang_ext.get(lang_name, lang_name)
            title_slug = sub.get('titleSlug', 'unknown-problem').replace('/', '_')
            filename = f"{title_slug}.{ext}"
            filepath = os.path.join(SUBMISSIONS_DIR, filename)
            # Only add if file is new or changed
            write_file = True
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    if f.read() == detail['code']:
                        write_file = False
            if write_file:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(detail['code'])
                print(f"Saved: {filename}")
                new_files.append(filepath)
        else:
            print(f"No code found for submission {sub['id']}")
    # Automate git add/commit/push for new files
    if new_files:
        try:
            subprocess.run(['git', 'add'] + new_files, check=True)
            subprocess.run(['git', 'commit', '-m', 'Add new accepted LeetCode solutions'], check=True)
            subprocess.run(['git', 'push'], check=True)
            print(f"Pushed {len(new_files)} new solutions to GitHub.")
        except subprocess.CalledProcessError as e:
            print(f"Git error: {e}")
    else:
        print("No new accepted solutions to push.")

if __name__ == "__main__":
    main() 