class Zoom:
    def __init__(self, time, meeting_description, attendees_dictionary, the_frequency, duration):
        self.time = time
        self.description = meeting_description
        self.attendees = attendees_dictionary
        self.frequency = the_frequency
        self.duration = duration

    def set_time(self, time):
        self.time = time

    def set_description(self, description):
        self.description = description

    def set_attendees(self, attendees):
        self.attendees = attendees

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_duration(self, duration):
        self.duration = duration

    def get_time(self):
        return self.time

    def get_description(self):
        return self.description

    def get_attendees(self):
        return self.attendees

    def get_email(self, name):
        for attendee in self.attendees:
            if attendee['name'] == name:
                return attendee['email']
        return None

    def get_frequency(self):
        return self.frequency

    def get_duration(self):
        return self.duration

    def get_all_info(self):
        only_names = [attendee['name'] for attendee in self.attendees]

        all_information = {
            'Meeting Time': self.time,
            'Meeting Description': self.description,
            'All Attendees': only_names,
            'The Frequency': self.frequency,
            'The Duration': self.duration
        }
        return all_information

    def print_info(self):
        info = self.get_all_info()
        print(info)
