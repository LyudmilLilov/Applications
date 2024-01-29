from datetime import date, timedelta

class Calendar:
    def __init__(self):
        self.events = {}

    def add_event(self, event_date, event_description):
        if event_date in self.events:
            self.events[event_date].append(event_description)
        else:
            self.events[event_date] = [event_description]

    def view_events(self, event_date):
        if event_date in self.events:
            print(f"Events on {event_date}:")
            for event in self.events[event_date]:
                print(f"- {event}")
        else:
            print(f"No events on {event_date}")

def main():
    my_calendar = Calendar()

    while True:
        print("\n1. Add Event")
        print("2. View Events for a Date")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            event_date = input("Enter the date (YYYY-MM-DD): ")
            event_description = input("Enter event description: ")
            my_calendar.add_event(event_date, event_description)
        elif choice == "2":
            event_date = input("Enter the date to view events (YYYY-MM-DD): ")
            my_calendar.view_events(event_date)
        elif choice == "3":
            print("Exiting the calendar program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
