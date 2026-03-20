"""File to test email api client."""

import allure
import pytest
from clients.email_client import EmailClient
from data.config import Config
from utils.logger import logger

pytestmark = [
    allure.epic("GreenCity API"),
    allure.feature("Email API")
]


@pytest.fixture
def email_client(access_token):
    """Fixture to initialize and return the EmailClient."""
    with allure.step("Step 1: Initialize Email client with USER base url"):
        return EmailClient(base_url=Config.BASE_USER_API_URL, access_token=access_token)


def verify_403_forbidden(response, endpoint_name: str):
    """Helper function to verify 403 Forbidden status and log the result."""
    with allure.step(f"Step 3: Verify status code is 403 Forbidden ({endpoint_name})"):
        if response.status_code != 403:
            logger.error(
                f"SECURITY VULNERABILITY! Expected 403, but got {response.status_code}. "
                f"Response: {response.text}"
            )

        assert response.status_code == 403, \
            f"Expected 403 Forbidden, but got {response.status_code}. Response: {response.text}"

        logger.info(f"Security check passed successfully for {endpoint_name}.")


@pytest.mark.parametrize(
    "method_name,payload,endpoint_name,story,title",
    [
        (
            "send_telegram_feedback",
            {
                "chatId": "123456789",
                "name": "Oleksandr",
                "rating": 5,
                "comment": "Telegram feedback test.",
                "subject": "New feedback from Telegram Bot.",
            },
            "Telegram feedback endpoint",
            "Telegram feedback",
            "Security: Verify regular user gets 403 when trying to send Telegram feedback email",
        ),
        (
            "send_user_violation",
            {
                "name": "Oleksandr",
                "email": "greencitytest69@hotmail.com",
                "language": "en",
                "violationDescription": "Spamming the eco-news comments.",
            },
            "User Violation endpoint",
            "User Violation Notifications",
            "Security: Verify regular user gets 403 when trying to send user violation email",
        ),
        (
            "send_report",
            {
                "subscribers": [
                    {
                        "name": "Oleksandr",
                        "email": "greencitytest69@hotmail.com",
                        "language": "en",
                        "unsubscribeToken": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    }
                ],
                "categoriesDtoWithPlacesDtoMap": {
                    "Recycling": [
                        {
                            "name": "Lviv Plastic Recycling Point.",
                            "category": {
                                "name": "Plastic",
                                "parentCategoryId": 1,
                            },
                        }
                    ],
                    "Eco Shops": [
                        {
                            "name": "SoftServe Green Store",
                            "category": {
                                "name": "Eco Products",
                                "parentCategoryId": 2,
                            },
                        }
                    ],
                },
                "periodicity": "IMMEDIATELY",
            },
            "Report endpoint",
            "Report Notifications",
            "Security: Verify regular user gets 403 when trying to send report email",
        ),
        (
            "send_reason_of_deactivation",
            {
                "email": "greencitytest69@hotmail.com",
                "name": "Oleksandr",
                "deactivationReason": "User too long inactive.",
                "lang": "en",
            },
            "Reason of deactivation endpoint",
            "Account Deactivation Notifications",
            "Security: Verify regular user gets 403 when trying to send deactivation reason email",
        ),
        (
            "send_place_status_change",
            {
                "placeName": "Lviv Plastic Recycling Point.",
                "newStatus": "PROPOSED",
                "userName": "Oleksandr",
                "email": "greencitytest69@hotmail.com"
            },
            "Place status change endpoint",
            "Place Status Notifications",
            "Security: Verify regular user gets 403 when trying to send place status change email",
        ),
        (
            "send_message_of_account_activation",
            {
                "email": "greencitytest69@hotmail.com",
                "name": "Oleksandr",
                "lang": "en"
            },
            "Message of account activation endpoint",
            "Account Activation Notifications",
            "Security: Verify regular user gets 403 when trying to send activation message email",
        ),
        (
            "send_interesting_eco_news",
            {
                "ecoNewsList": [
                    {
                        "ecoNewsId": 101,
                        "imagePath": "https://greencity.cx.ua/assets/img/eco-news-1.jpg",
                        "title": "Масове висадження дерев у Львові",
                        "text": "Приєднуйтесь до нас цими вихідними, щоб висадити понад 500 дерев у центрі міста."
                    }
                ],
                "subscribers": [
                    {
                        "name": "Denys",
                        "email": "greencitytest69@hotmail.com",
                        "language": "uk",
                        "unsubscribeToken": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                    }
                ]
            },
            "Eco News endpoint",
            "Eco News Notifications",
            "Security: Verify regular user gets 403 when trying to send interesting Eco News email",
        ),
        (
            "send_habit_notification",
            {
                "name": "Oleksandr",
                "email": "greencitytest69@hotmail.com",
            },
            "Habit notifications endpoint",
            "Habit Notifications",
            "Security: Verify regular user gets 403 when trying to send habit notification email",
        ),
        (
            "send_scheduled_notifications",
            {
                "username": "Oleksandr",
                "userId": 1205,
                "userUuid": "123e4567-e89b-12d3-a456-426614174000",
                "baseLink": "https://greencity.cx.ua/",
                "subject": "Important Notification from GreenCity",
                "body": "This is a test notification body text.",
                "language": "en",
                "ubs": True
            },
            "Scheduled notification endpoint",
            "Scheduled Notifications",
            "Security: Verify regular user gets 403 when trying to trigger scheduled email notification",
        ),
        (
            "send_green_office_notifications",
            {
                "username": "Oleksandr",
                "userId": 1205,
                "userUuid": "123e4567-e89b-12d3-a456-426614174000",
                "baseLink": "https://greencity.cx.ua/",
                "subject": "Important Notification from GreenCity",
                "body": "This is a test notification body text.",
                "language": "en",
                "ubs": True
            },
            "Green office notification endpoint",
            "Green Office Notifications",
            "Security: Verify regular user gets 403 when trying to send Green Office notification",
        )
    ],
)
def test_user_cannot_send_email_endpoints(
    email_client, method_name, payload, endpoint_name, story, title
):
    """Negative security tests: verify regular user receives 403 on restricted email endpoints."""
    # Set Allure metadata dynamically per endpoint
    allure.dynamic.story(story)
    allure.dynamic.title(title)
    logger.info(
        "Starting security test: verifying regular user cannot access %s.",
        endpoint_name,
    )
    with allure.step("Step 2: Prepare payload and send POST request"):
        client_method = getattr(email_client, method_name)
        response = client_method(payload=payload)
    verify_403_forbidden(response, endpoint_name)
