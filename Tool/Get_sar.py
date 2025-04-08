import requests
import json

# Using the base API URL
base_url = "https://shr32taah3.execute-api.us-east-1.amazonaws.com/Prod/applications/search"

# Set request headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
    'Accept': 'application/json',  # Expect JSON data
    'Content-Type': 'application/json'
}

# Initialize variables for pagination
page_number = 1
page_size = 100
has_more_pages = True

# Create an empty list to store all applications
all_applications = []

while has_more_pages:
    # Set the request parameters
    params = {
        'searchText': 'helper-macro-elastic-serverless-forwarder',
        'pageSize': page_size,
        'pageNumber': page_number,
        'includeAppsWithCapabilities': 'CAPABILITY_IAM,CAPABILITY_NAMED_IAM,CAPABILITY_RESOURCE_POLICY,CAPABILITY_AUTO_EXPAND'
    }

    try:
        # Make the GET request
        response = requests.get(base_url, headers=headers, params=params)

        # Ensure the request was successful
        response.raise_for_status()

        # Attempt to parse the JSON data
        data = response.json()

        # Extract the list of applications
        applications = data.get('applications', [])

        # If no applications are returned, there are no more pages
        if not applications:
            has_more_pages = False
            break

        # Iterate over the list of applications and store required information
        for app in applications:
            app_name = app.get('name', 'No application name')
            deployment_count = app.get('deploymentCount', 0)  # Default to 0 if missing
            home_page_url = app.get('homePageUrl', 'No homepage URL')

            # Append the application information to the list if deployment_count > 0
            if deployment_count > 0:
                all_applications.append({
                    "name": app_name,
                    "deployment_count": deployment_count,
                    "home_page_url": home_page_url
                })

        # Move to the next page
        page_number += 1

    except requests.exceptions.ConnectionError:
        print("Network connection error. Could not reach the target server. Please check your internet connection or if the target server is reachable.")
        break
    except requests.exceptions.HTTPError as e:
        print(f"HTTP request failed with status code: {e.response.status_code}")
        print(e.response.text)
        break
    except json.JSONDecodeError:
        print("Failed to parse the returned data as JSON.")
        break

# Print all applications information with deployment_count > 0
for app in all_applications:
    print(f"Application Name: {app['name']}")
    print(f"Deployment Count: {app['deployment_count']}")
    print(f"Homepage URL: {app['home_page_url']}")
    print('-' * 50)

# Print the total number of applications found with deployment_count > 0
print(f"Total number of applications found with deployment_count > 0: {len(all_applications)}")
