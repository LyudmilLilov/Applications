from datetime import date, timedelta

class Calendar:
    def __init__(self):
        self.events = {}

    def add_event(self, event_date, event_description):
        pass

    def view_events(self, event_date):
        pass

def main():
    my_calendar = Calendar()

    while True:
        print("\n1. Add Event")
        print("2. View Events for a Date")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")



if __name__ == "__main__":
    main()
