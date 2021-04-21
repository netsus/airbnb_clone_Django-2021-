from django.utils import timezone
import calendar


class Day:
    def __init__(self, number, past, month, year):
        self.number = number
        self.past = past
        self.month = month
        self.year = year

    def __str__(self):
        return str(self.number)


class Calendar(calendar.Calendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.day_names = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
        self.months = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    def get_days(self):
        weeks = self.monthdays2calendar(self.year, self.month)
        now = timezone.now()
        today = now.day
        month = now.month
        days = [
            Day(
                number=day,
                past=(month == self.month) and (day < today),
                month=self.month,
                year=self.year,
            )
            for week in weeks
            for day, _ in week
        ]
        # ## class 없이 딕셔너리로도 가능하다.
        # days = [
        #     {"day": day, "past": (month == self.month) and (day < today)}
        #     for week in weeks
        #     for day, _ in week
        # ]
        return days

    def get_month(self):
        return self.months[self.month - 1]
