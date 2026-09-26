import requests
import csv

def get_github_profile(username):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:

        data = response.json()

        print("\n==============================")
        print("        GITHUB PROFILE")
        print("==============================")

        print("Username:", data["login"])

        if data["name"] is None:
            print("Name: Not Provided")
        else:
            print("Name:", data["name"])

        print("Followers:", data["followers"])
        print("Following:", data["following"])
        print("Public Repositories:", data["public_repos"])
        print("Public Gists:", data["public_gists"])

        if data["location"] is None:
            print("Location: Not Provided")
        else:
            print("Location:", data["location"])

        print("==============================")
        repo_url=f"https://api.github.com/users/{username}/repos"
        repo_response=requests.get(repo_url)
        print(repo_response.status_code)
        repos=repo_response.json()
        print("\n==============================")
        print("       REPOSITORIES")
        print("==============================")
        file=open("github_repositories.csv","w",newline="",encoding="utf-8")
        writer=csv.writer(file)
        writer.writerow(["Repository","Language","Starts","Forks","URL"])
        for repo in repos:
          print("Repository:", repo["name"])
          print("Language:", repo["language"])
          print("Stars:", repo["stargazers_count"])
          print("Forks:", repo["forks_count"])
          print("URL:", repo["html_url"])
          print("------------------------")
          writer.writerow([
              repo["name"],
              repo["language"],
              repo["stargazers_count"],
              repo["forks_count"],
              repo["html_url"]
          ])
        file.close()
          

    else:
        print("GitHub user not found")


username = input("Enter GitHub username: ")

get_github_profile(username)