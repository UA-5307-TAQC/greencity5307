"""Module for testing partners buttons on UBSCourier page."""

import allure

from pages.common_pages.main_page import MainPage


@allure.title("Open partners pages by clicking on buttons")
@allure.description("This test verifies that the user can successfully "
                    "open partners pages. ")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "SidorovAI-224")
@allure.testcase("TC-6")
def test_open_partners_pages_by_clicking_on_buttons(driver):
    """TC-6"""

    main_page = MainPage(driver)

    with allure.step("User opens UBSCourier search page"):
        ubs_page = main_page.go_to_ubs_courier()

    with allure.step("User clicks 1st partner button"):
        ubs_page.click_nowaste_shop()
        assert "shop" in driver.current_url
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    with allure.step("User clicks 2nd partner button"):
        ubs_page.click_nowaste()
        assert "nowaste" in driver.current_url
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    with allure.step("User clicks 3rd partner button"):
        ubs_page.click_goto()
        assert "instagram" in driver.current_url
        driver.close()
        driver.switch_to.window(driver.window_handles[0])