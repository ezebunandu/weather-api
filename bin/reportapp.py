import requests


def report_event():
    desc = input("What event do you want to report? ")
    city = input("What city? ")
    country = input("What country is the city? ")

    data = {
        "description": desc,
        "location": {
            "city": city,
            "country": country
        }
    }

    url = "http://127.0.0.1:8080/api/reports"
    resp = requests.post(url, json=data)
    resp.raise_for_status()

    result = resp.json()
    print(f"Reported new event: {result.get('id')}")


def see_events():
    url = "http://127.0.0.1:8080/api/reports"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    for r in data:
        print(f"{r.get('location').get('city')}: {r.get('description')}")


def main():
    choice = input("[R]eport weather or [S]ee reports? ")
    while choice:
        if choice.lower().strip() == 'r':
            report_event()
        elif choice.lower().strip() == 's':
            see_events()
        else:
            print(f"Invalid option {choice}.")

        choice = input("[R]eport weather or [S]ee reports? ")


if __name__ == "__main__":
    main()