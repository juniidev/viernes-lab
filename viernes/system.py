from datetime import datetime


class System:

    def get_time(self) -> str:
        now = datetime.now()
        return now.strftime("%H:%M:%S")