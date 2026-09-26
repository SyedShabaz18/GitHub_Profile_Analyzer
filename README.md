GitHub Profile Analyzer

A Python project that uses the GitHub REST API to fetch public GitHub profile and repository information and export repository data to a CSV file.

Features

- Search for a GitHub user by username
- Fetch public profile information
- Display followers and following
- Display public repository and gist counts
- Handle users who do not have a public name or location
- Handle invalid GitHub usernames
- Fetch public repositories
- Display repository name, programming language, stars, forks, and URL
- Export repository information to a CSV file

Technologies Used

- Python
- Requests
- GitHub REST API
- CSV

How It Works

The project follows this workflow:

GitHub Username
       ↓
GitHub REST API
       ↓
Fetch Profile Information
       ↓
Fetch Repository Information
       ↓
Display Results
       ↓
Export Repository Data to CSV

Example

The program asks for a GitHub username:

Enter GitHub username: SyedShabaz18

It then displays profile information such as:

GITHUB PROFILE

Username: SyedShabaz18
Name: Not Provided
Followers: 0
Following: 0
Public Repositories: 1
Public Gists: 0
Location: Not Provided

It also displays repository information:

REPOSITORIES

Repository: My-Project
Language: Python
Stars: 0
Forks: 0
URL: https://github.com/...

The repository information is also saved to:

github_repositories.csv

How to Run

1. Install Python

Make sure Python is installed on your computer.

2. Install Requests

Open the terminal and run:

python -m pip install requests

3. Run the program

python api_day1.py

4. Enter a GitHub username

Enter GitHub username: octocat

The program will fetch and display the public GitHub information.

Project Structure

GitHub-Profile-Analyzer/
│
├── github_profile_analyzer.py
├── github_repositories.csv
└── README.md

What I Learned

Through this project, I practiced:

- Making REST API requests using Python
- Working with HTTP status codes
- Parsing JSON responses
- Working with Python dictionaries and lists
- Using functions and loops
- Handling missing data
- Handling API errors
- Extracting useful information from API responses
- Writing API data into CSV files

Future Improvements

Possible future improvements include:

- Add language usage statistics
- Calculate total repository stars
- Identify the most-starred repository
- Add better error handling
- Generate a more detailed analytics report
- Add a simple user interface

Author

Syed Shabaz Banu

B.Tech Computer Science Engineering (AI & ML)

GitHub: "SyedShabaz18"