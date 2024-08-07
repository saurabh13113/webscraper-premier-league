# webscraper-premier-league-🕸️
Summer Project that uses BeautifulSoup and pandas to obtain premier league data for the past few seasons using web-scraping

# Premier League Match Data Scraper

This project is designed to scrape and aggregate match data for Premier League football teams from the FBref website. The data includes detailed match statistics for each team, covering multiple seasons. The project uses Python, along with libraries such as `requests`, `BeautifulSoup`, and `pandas`, to perform the web scraping and data processing.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Data Fields](#data-fields)
- [Usage](#usage)
- [Output](#output)
- [Notes](#notes)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Contributing](#contributing)

## Features

- **Web Scraping**: Extracts match data and shooting statistics for each team in the Premier League across multiple seasons.
- **Data Processing**: Merges match data with shooting statistics and filters the data to include only Premier League matches.
- **Seasonal Data Collection**: Iterates over multiple seasons to collect comprehensive data for analysis.
- **CSV Output**: Saves the final aggregated dataset as a CSV file for easy analysis and further processing.

## Requirements

To run this project, you need to have the following Python libraries installed:

- `requests`: For making HTTP requests to retrieve web pages.
- `beautifulsoup4`: For parsing HTML content and extracting data.
- `pandas`: For data manipulation and analysis.

## Installation

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## How It Works
1. Sending Requests: The scraper sends HTTP requests to the FBref website to fetch the HTML content of the Premier League match pages.
2. Parsing HTML: The BeautifulSoup library is used to parse the HTML content and extract relevant match and shooting statistics.
3. Data Extraction: Data is extracted from the parsed HTML and structured into a format suitable for analysis.
4. Data Aggregation: The extracted data is aggregated into a comprehensive dataset covering multiple seasons.
5. CSV Export: The final dataset is saved as a CSV file, which can be used for further analysis or reporting.

### Data Fields
The dataset includes the following fields:

- Team: The name of the football team.
- Season: The season of the Premier League.
- Match Date: The date of the match.
- Opponent: The name of the opposing team.
- Match Statistics: Various match statistics such as goals, shots, possession, etc.
- Shooting Statistics: Detailed shooting statistics including shots on target, shot accuracy, etc.

## Usage
To use the scraper, run the main script:

```
bash
python scraper.py
```
The script will scrape the data, process it, and save the results as premier_league_data.csv in the current directory.

### Output
The output of the scraper is a CSV file named premier_league_data.csv, which contains the aggregated match and shooting statistics for Premier League teams across multiple seasons. The file will have the following columns:

- Team
- Season
- Match Date
- Opponent
- Match Statistics
- Shooting Statistics

## Notes
- Ensure that you comply with FBref's terms of service when scraping data from their website.
- The scraper may need adjustments if the structure of the FBref website changes.
- Data scraping can be subject to rate limits; be considerate of the frequency of requests to avoid being blocked.

### Future Improvements
1. Error Handling: Add robust error handling to manage issues such as network failures or changes in webpage structure.
2. Data Visualization: Implement functionality to visualize the data using charts or graphs.
3. API Integration: Explore using an API for data retrieval instead of web scraping.
4. Real-Time Updates: Implement functionality to scrape and update data in real-time or on a regular schedule.

License: This project is licensed under the MIT License. See the LICENSE file for details.

Contributing: Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue to discuss what you would like to change before submitting a pull request.
