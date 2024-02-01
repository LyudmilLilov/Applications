import requests


def fetch_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f"Error fetching repositories for user {username}. Status code: {response.status_code}")
        return []


def display_repository_info(repositories):
    for repo in repositories:
        print("\nRepository Name:", repo["name"])
        print("Description:", repo["description"])
        print("Language:", repo["language"])
        print("Stars:", repo["stargazers_count"])


def main():
    pass


if __name__ == "__main__":
    main()
