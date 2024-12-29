### How to use github actions to update a schedule from google sheet/s on github readme

#### Step 1: Create a GitHub Repository

* Log in to your GitHub account.
* Navigate to the top-right corner and click New Repository.
* Provide a name for your repository (e.g., **ScheduleMeet**) and configure other options (public/private).
* Click Create Repository.

#### Step 2: Clone the Repository on your local machine

* To work on your local system:
* Copy the repository’s HTTPS link from GitHub (highlighted in the GitHub UI).
* Clone the repository using your terminal or VS Code (my preference).
* VS Code Users: Use the "Clone Repository" button in the Source Control menu and paste the link.

#### Step 3: Add Required Files

* You need two new files to set up the automation:**update_markdown.py**
* Create this file in the root of your repository.
* Paste the following code and replace the CSV_URL in the script with the CSV export link for your Google Sheet (see more detailed instructions below).

```
import pandas as pd
import requests
import io

def fetch_google_sheet_csv(url, sheet_name=None):
    """Fetch CSV data from a specific sheet in a Google Sheet."""
    if sheet_name:
        sheet_url = f"{url}&sheet={sheet_name}"
    else:
        sheet_url = url
    response = requests.get(sheet_url)
    response.raise_for_status()
    return pd.read_csv(io.StringIO(response.text))

def update_markdown(df, filename="README.md"):
    """Convert DataFrame to Markdown and update README.md."""
    with open(filename, 'w') as f:
        f.write("# 2025\n\n")
        f.write(df.to_markdown(index=False))
    print("README.md has been updated.")

if __name__ == "__main__":
    #actual copy link of google sheet would look like thuis : https://docs.google.com/spreadsheets/d/1cGfIostiPJAxmo_zINnHGHSthbUZ8x9R90-C4oZvTt0/edit?usp=sharing
    # Use the CSV export link for your Google Sheet
    #Solution: Update the URL to include the /export?format=csv parameter:
    CSV_URL = "https://docs.google.com/spreadsheets/d/1cGfIostiPJAxmo_zINnHGHSthbUZ8x9R90-C4oZvTt0/export?format=csv"
    df = fetch_google_sheet_csv(CSV_URL, sheet_name='Sheet1')

    update_markdown(df)

```

**Workflow Configuration:**

* Create the directories .github/workflows/ in the root of your repository.
* Within workflows/, create a file named update_readme.yml.
* Add the following code to the file:

#### Step 4:

Update Changes on Remote by pushing changes. You should be able to see your all files there that you just created.

#### Step 5: Set Workflow Permissions

* Go to your GitHub repository.
* Navigate to Settings > Actions > General.
* Scroll to the Workflow Permissions section and enable Read and write permissions.
* Click Save.

#### Step 6: Run the Workflow

* Go to the Actions tab in your GitHub repository.
* Select the Update README with Google Sheet Data workflow.
* Click Run Workflow to trigger the workflow manually for the first time.
* Once executed, the workflow will fetch data from your Google Sheet and update the README.md file with the schedule.

#### Note: Customizing the Script for Your Google Sheet

* Get the Google Sheet Link
* Open your Google Sheet.
* Click Share and make the sheet accessible to "Anyone with the link."

**Modify the link:**

Replace /edit?usp=sharing with /export?format=csv.

**Example:**

**Original:**
https://docs.google.com/spreadsheets/d/1cGfIostiPJAxmo_zINnHGHSthbUZ8x9R90-C4oZvTt0/**edit?usp=sharing**

**CSV Export Link:**
https://docs.google.com/spreadsheets/d/1cGfIostiPJAxmo_zINnHGHSthbUZ8x9R90-C4oZvTt0/**export?format=csv**

Paste the updated CSV export link into the CSV_URL variable in update_markdown.py.
