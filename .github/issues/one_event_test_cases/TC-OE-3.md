---
type: "TestCase"
name: "Test Case"
about: "ISTQB-aligned template for test case creation"
title: "[Test Case]: "
labels: ["verification required"]
assignees: []
---

**Test Case ID:**<br>TC-OE-3

**Title:**<br>
Verify Event Joining, Profile Counter Update, and Cancellation

**Related Requirement/User Story:**<br>
N/A

**Date Created:**<br>
02-08-2026

**Author:**<br>
Osypenko Kostiantyn

**Priority:**<br>
Medium

**Preconditions:**
 - User is not logged in.
 - User account has 0 organized or attended events

**Test Steps:**

| Step # | Step Description | Test Data | Expected Result |
|:------:|:-----------------|:----------|:----------------|
| 1 | Navigate to the GreenCity URL. | `https://www.greencity.cx.ua/#/greenCity` | The Home page loads successfully. |
| 2 | Click on the **"Events"** button in the header. | N/A | The **"Events"** page loads successfully. |
| 3 | Click the **"More"** button on the first event card. | N/A | The specific Event details page loads successfully. |
| 4 | Click the **"Join Event"** button below the event information block. | N/A | The **"Sign in"** modal window appears. |
| 5 | Enter a valid email address into the email field. | `{valid_email}` | The email field accepts the input. |
| 6 | Enter a valid password into the password field. | `{valid_password}` | The password field accepts the input. |
| 7 | Click the **"Sign in"** button. | N/A | The user is successfully logged in. |
| 8 | Click on the **"My Space"** button in the header. | N/A | The **User Profile** page loads successfully. The **"Organized and attended events"** counter in the profile information block displays **0**. |
| 9 | Navigate back to the previous page (Event details page). | N/A | The Event details page loads successfully. |
| 10 | Click the **"Join Event"** button below the event information block. | N/A | The button style changes to transparent, and the label changes to **"Cancel Request"**. A success message **"You have successfully joined the event"** appears at the top of the page. |
| 11 | Click on the **"My Space"** button in the header. | N/A | The **User Profile** page loads successfully. The **"Organized and attended events"** counter increments by 1. |
| 12 | Navigate back to the previous page (Event details page). | N/A | The Event details page loads successfully. |
| 13 | Click the **"Cancel Request"** button below the event information block. | N/A | The confirmation modal **"Are you sure that you don't want to join this event?"** appears. |
| 14 | Click the **"Yes"** button in the modal. | N/A | The modal closes. The **"Cancel Request"** button reverts to **"Join Event"**. |
| 15 | Click on the **"My Space"** button in the header. | N/A | The **User Profile** page loads successfully. The **"Organized and attended events"** counter decrements by 1 (returns to **0**). |

**Postconditions:**<br>
N/A


**Environment:**
- Browser: Chrome


**Screenshots:**<br>
N/A

**Additional Context:**<br>
Test case fails on 13 Step. Cancel Request button after reloading **is not** displayed.
