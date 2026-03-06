from datetime import datetime

import allure

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage

@allure.title("Check that calendar highlights current system date on My Space page")
def test_calendar_current_day(driver_with_login):
    """Test that calendar highlights current system date."""

    with allure.step("Go to My Space page"):
        driver = driver_with_login
        my_habit_page = MyHabitPage(driver)

    with allure.step("Check if the current day on the calendar is correct"):
        now = datetime.now()
        date = my_habit_page.calendar.get_current_date()
        day, month, year = date["day"], date["month"], date["year"]
        assert day == now.strftime("%d"), f"Wrong current day on calendar: {day}"
        assert month == now.strftime("%m"), f"Wrong current month on calendar: {month}"
        assert year == now.strftime("%Y"), f"Wrong current year on calendar: {year}"
