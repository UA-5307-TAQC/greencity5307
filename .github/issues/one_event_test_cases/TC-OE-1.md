---
type: "TestCase"
name: "Test Case"
about: "ISTQB-aligned template for test case creation"
title: "[Test Case]: "
labels: ["verification required"]
assignees: []
---

**Test Case ID:**<br>TC-OE-1

**Title:**<br>
Verify ability to post a comment on an Event page after logging in from the Header

**Related Requirement/User Story:**<br>
N/A

**Date Created:**<br>
02-08-2026

**Author:**<br>
Osypenko Kostiantyn

**Priority:**<br>
Medium

**Preconditions:**<br>
None

**Test Steps:**

| Step # | Step Description | Test Data | Expected Result |
|:------:|:-----------------|:----------|:----------------|
| 1 | Navigate to the GreenCity URL. | `https://www.greencity.cx.ua/#/greenCity` | The Home page loads successfully. |
| 2 | Click on the **"Events"** button in the header. | N/A | The **"Events"** page loads successfully. |
| 3 | Click the **"More"** button on the first event card. | N/A | The specific Event details page loads successfully. The comment input field and **"Comment"** button are **not** displayed. |
| 4 | Click the **"Sign in"** button in the header. | N/A | The **"Sign in"** modal window appears. |
| 5 | Enter a valid email address into the email field. | `{valid_email}` | The email field accepts the input. |
| 6 | Enter a valid password into the password field. | `{valid_password}` | The password field accepts the input. |
| 7 | Click the **"Sign in"** button. | N/A | The user is successfully logged in and redirected to the **Profile** page. |
| 8 | Navigate back to the previous page (Event details page). | N/A | The Event details page loads. The comment input field and **"Comment"** button are now displayed. |
| 9 | Enter a comment in the input field below the event information block. | `{comment_text}` | The input field is populated with the entered text. |
| 10 | Click the **"Comment"** button. | N/A | The comment appears in the comments block. The comment counter increments by 1. **"Edit"**, **"Delete"**, and **"Reply"** buttons appear under the posted comment. |

**Postconditions:**<br>
N/A


**Environment:**
- Browser: Chrome


**Screenshots:**<br>
N/A

**Additional Context:**<br>
N/A
