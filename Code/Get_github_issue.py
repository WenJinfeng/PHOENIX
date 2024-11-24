import requests
import pandas as pd
import time
import os

SEARCH_KEYWORD = "AWS serverless configuration"  # Define your search keyword here
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # GitHub Token for authentication
output_file = "XXXX.xlsx"


if not GITHUB_TOKEN:
    raise ValueError("Please set the GITHUB_TOKEN environment variable.")

url = "https://api.github.com/search/issues"

issue_data = []

per_page = 100  
page = 1

while True:
    params = {
        'q': SEARCH_KEYWORD,
        'per_page': per_page,
        'page': page
    }
    
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(url, headers=headers, params=params)
    
    print(f"Fetching page {page}...")
    
    if response.status_code == 200:
        data = response.json()
        
        issues = data.get("items", [])
        
        if not issues:
            print("No more issues found.")
            break
        
        for issue in issues:
            issue_data.append({
                "Issue Title": issue.get("title"),
                "Issue Number": issue.get("number"),
                "Repository Name": issue.get("repository_url").split('/')[-2] + "/" + issue.get("repository_url").split('/')[-1],
                "State": issue.get("state"),
                "Created At": issue.get("created_at"),
                "Updated At": issue.get("updated_at"),
                "Comments Count": issue.get("comments"),
                "Issue URL": issue.get("html_url"),
                "User": issue.get("user", {}).get("login")
            })
        
        if len(issues) < per_page:
            print("Reached the last page of results.")
            break
        
        page += 1
        time.sleep(10)
    
    elif response.status_code == 403:
        print("API rate limit exceeded. Please try again later.")
        break
    elif response.status_code == 401:
        print("Authentication failed. Please check if your GitHub token is correct.")
        break
    else:
        print(f"Request failed with status code: {response.status_code}, response: {response.text}")
        break

df = pd.DataFrame(issue_data)

# Sort the DataFrame by Comments Count in descending order (optional)
df = df.sort_values(by="Comments Count", ascending=False)

df.to_excel(output_file, index=False, engine="openpyxl")

print(f"Data has been sorted by comments count and saved to '{output_file}'.")
