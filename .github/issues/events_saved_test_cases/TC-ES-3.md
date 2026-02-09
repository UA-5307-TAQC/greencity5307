---
type: "TestCase"
name: "Test Case"
about: "ISTQB-aligned template for test case creation"
title: "[Test Case]: "
labels: ["verification required"]
assignees: []
---

**Test Case ID:**<br>TC-ES-3

**Title:**<br>
Verify Event Saving Functionality and Saved Items Management

**Related Requirement/User Story:**<br>
None

**Date Created:**<br>
02-08-2026

**Author:**<br>
Osypenko Kostiantyn

**Priority:**<br>
Medium

**Preconditions:**<br>
N/A

**Test Steps:**

| Step # | Step Description | Test Data | Expected Result |
|:------:|:-----------------|:----------|:----------------|
| 1 | Navigate to the GreenCity URL. | `https://www.greencity.cx.ua/#/greenCity` | The Home page loads successfully. |
| 2 | Click on the **"Events"** button in the header. | N/A | The **"Events"** page loads successfully. |
| 3 | Click the **"Save"** (bookmark) icon in the upper-right corner of the first event card. | N/A | The **"Sign in"** modal window appears. |
| 4 | Enter a valid email address into the email field. | `{valid_email}` | The email field accepts the input. |
| 5 | Enter a valid password into the password field. | `{valid_password}` | The password field accepts the input. |
| 6 | Click the **"Sign in"** button. | N/A | The user is successfully logged in and redirected to the **Profile** page. |
| 7 | Navigate back to the **"Events"** page. | N/A | The **"Events"** page loads successfully. |
| 8 | Click the **"Save"** (bookmark) icon in the upper-right corner of the first event card. | N/A | The **"Save"** icon turns green (indicating the event is saved). |
| 9 | Click the **"Saved"** icon in the header. | N/A | The **"Saved"** page loads successfully with the **"Eco-news"** section open by default. |
| 10 | Click on the **"Events"** tab. | N/A | The **"Saved Events"** section is displayed. The event card saved in Step 8 is present in the list. |
| 11 | Click the **"Save"** (bookmark) icon in the upper-right corner of this event card. | N/A | The **"Save"** icon turns white (indicating the event is removed from saved). |
| 12 | Refresh the page. | N/A | The event card disappears from the **"Saved Events"** page. |

**Postconditions:**<br>
N/A


**Environment:**
- Browser: Chrome


**Screenshots:**<br>
N/A

**Additional Context:**<br>
N/A
