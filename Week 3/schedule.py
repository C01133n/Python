import datetime

class Schedule:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name, event_date):
        if event_name in self.events:
            print(f"Event '{event_name}' already exists.")
        else:
            self.events[event_name] = event_date
            print(f"Event '{event_name}' added on {event_date}.")

    def view_events(self):
        if self.events:
            print("Scheduled Events:")
            for event, date in self.events.items():
                print(f"{event}: {date}")
        else:
            print("No events scheduled.")

    def delete_event(self, event_name):
        if event_name in self.events:
            del self.events[event_name]
            print(f"Event '{event_name}' deleted.")
        else:
            print(f"Event '{event_name}' not found.")

# Example usage
schedule = Schedule()

schedule.add_event("Meeting", datetime.datetime(2024, 4, 1, 14, 30))
schedule.add_event("Conference", datetime.datetime(2024, 4, 15, 9, 0))

schedule.view_events()

schedule.delete_event("Meeting")

schedule.view_events()
