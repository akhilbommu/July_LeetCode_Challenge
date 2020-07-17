class AngleBetweenHandsOfClock:
    def angleClock(self, hrs: int, mins: int) -> float:
        hrs %= 12
        hours = hrs*30 + mins/2
        mins = 6 * mins
        return min(abs(hours-mins), 360-abs(mins-hours))


obj = AngleBetweenHandsOfClock()
print(obj.angleClock(12, 30))
print(obj.angleClock(3, 30))
print(obj.angleClock(3, 15))
print(obj.angleClock(4, 50))
print(obj.angleClock(12, 0))