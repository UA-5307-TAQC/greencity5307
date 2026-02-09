---
type: "TestCase"
name: "Test Case"
about: "ISTQB-aligned template for test case creation"
title: "[Test Case]: "
labels: ["verification required"]
assignees: []
---

**Test Case ID:**<br>TC-ES-2

**Title:**<br>
Verify that saved events persist after the user logs out and logs back in.

**Related Requirement/User Story:**<br>
N/A

**Date Created:**<br>
02-08-2026

**Author:**<br>
Osypenko Kostiantyn

**Priority:**<br>
Medium

**Preconditions:**<br>
 - User is logged in.

**Test Steps:**

| Step # | Step Description | Test Data | Expected Result |
|:------:|:-----------------|:----------|:----------------|
| 1 | Navigate to the GreenCity URL. | `https://www.greencity.cx.ua/#/greenCity` | The Main page loads successfully. |
| 2 | Click on the **"Events"** button in the header. | N/A | The **"Events"** page loads successfully. |
| 3 | Click the **"Save"** (bookmark) icon on the first event card. | N/A | The **"Save"** icon turns green (indicating the event is saved). |
| 4 | Click the **"Saved"** icon in the header. | N/A | The **"Saved"** page loads successfully with the **"Eco-news"** section open by default. |
| 5 | Click on the **"Events"** tab/section. | N/A | The **"Saved Events"** section is displayed. The previously saved event card is visible in the list. |
| 6 | Click on the **User Profile** icon (dropdown) in the header. | N/A | A dropdown menu opens containing the **"Sign out"** option. |
| 7 | Click the **"Sign out"** button. | N/A | The user is logged out successfully. The main page loads. The **"Sign in"** button is visible in the header. |
| 8 | Click the **"Sign in"** button in the header. | N/A | The **"Sign in"** modal window appears. |
| 9 | Enter a valid email address into the email field. | `{valid_email}` | The email field accepts the input. |
| 10 | Enter a valid password into the password field. | `{valid_password}` | The password field accepts the input. |
| 11 | Click the **"Sign in"** button. | N/A | The user is successfully logged in. The **User Profile** page loads. |
| 12 | Click the **"Saved"** icon in the header. | N/A | The **"Saved"** page loads successfully with the **"Eco-news"** section open by default. |
| 13 | Click on the **"Events"** tab/section. | N/A | The **"Saved Events"** section is displayed. The previously saved event card is visible in the list. |

**Postconditions:**<br>
N/A


**Environment:**
- Browser: Chrome


**Screenshots:**<br>
N/A

**Additional Context:**<br>
N/A
