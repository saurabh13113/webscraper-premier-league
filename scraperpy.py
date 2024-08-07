import time
from io import StringIO
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL for the Premier League stats on FBref
standin_url = "https://fbref.com/en/comps/9/2023-2024/2023-2024-Premier-League-Stats"

# List of years to iterate over, representing seasons (2023-2024, 2022-2023, etc.)
years = list(range(24, 22, -1))

# Initialize a list to store match data for all teams and seasons
all_matches = []

# Loop over the defined years to scrape data for each season
for year in years:
    # Fetch the webpage content for the current season's standings
    data = requests.get(standin_url)
    soup = BeautifulSoup(data.text, features="lxml")

    # Select the table containing the standings information
    standings_table = soup.select('table.stats_table')[0]

    # Extract team URLs from the standings table
    links = [l.get("href") for l in standings_table.find_all('a')]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in links]

    # Prepare the URL for the previous season for the next loop iteration
    prev_season = soup.select("a.prev")[0].get("href")
    standin_url = f"https://fbref.com{prev_season}"

    # Loop over each team URL to fetch and merge match and shooting data
    for team_url in team_urls:
        # Extract and format the team name from the URL
        team_name = team_url.split("/")[-1].replace("-Stats", " ").replace("-", " ")

        # Fetch the webpage content for the current team's stats
        data = requests.get(team_url)
        matches = pd.read_html(StringIO(data.text), match="Scores & Fixtures")[0]

        # Extract the shooting data link and fetch the corresponding data
        soup = BeautifulSoup(data.text, features="lxml")
        links = [l.get("href") for l in soup.find_all('a')]
        links = [l for l in links if l and 'all_comps/shooting/' in l]
        data = requests.get(f"https://fbref.com{links[0]}")
        shooting = pd.read_html(data.text, match="Shooting")[0]
        shooting.columns = shooting.columns.droplevel()

        # Merge the match data with the shooting data based on the match date
        try:
            team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")
        except ValueError:
            continue

        # Filter the data to only include Premier League matches
        team_data = team_data[team_data["Comp"] == "Premier League"]

        # Add season and team information to the dataset
        team_data["Season"] = year
        team_data["Team"] = team_name

        # Append the team's data for the current season to the list
        all_matches.append(team_data)

        # Sleep for 1 second to avoid overwhelming the server
        time.sleep(1)
        print("done")

# Combine all the match data into a single DataFrame
match_df = pd.concat(all_matches)

# Save the combined match data to a CSV file for later use
match_df.to_csv("matches.csv")

# Print the team URLs and the final DataFrame for verification
print(team_urls)
print(match_df)
