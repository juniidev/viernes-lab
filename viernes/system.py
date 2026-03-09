from datetime import datetime


class System:

    def get_time(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")