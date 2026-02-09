---
type: "TestCase"
name: "Test Case"
about: "ISTQB-aligned template for test case creation"
title: "[Test Case]: "
labels: ["verification required"]
assignees: []
---

**Test Case ID:**<br>TC-OE-2

**Title:**<br>
Verify Comment Creation, Counter Update, and Deletion

**Related Requirement/User Story:**<br>
N/A

**Date Created:**<br>
02-08-2026

**Author:**<br>
Osypenko Kostiantyn

**Priority:**<br>
Medium

**Preconditions:**<br>
User is logged in

**Test Steps:**

| Step # | Step Description | Test Data | Expected Result |
|:------:|:-----------------|:----------|:----------------|
| 1 | Navigate to the GreenCity URL. | `https://www.greencity.cx.ua/#/greenCity` | The Home page loads successfully. |
| 2 | Click on the **"Events"** button in the header. | N/A | The **"Events"** page loads successfully. |
| 3 | Click the **"More"** button on the first event card. | N/A | The specific Event details page loads successfully. The comment input field and **"Comment"** button are displayed below the event information block. |
| 4 | Enter a comment in the input field below the event information block. | `{comment_text}` | The input field is populated with the entered text. |
| 5 | Click the **"Comment"** button. | N/A | The comment appears in the comments block. The comment counter increments by 1. **"Edit"**, **"Delete"**, and **"Reply"** buttons appear under the posted comment. |
| 6 | Navigate back to the **"Events"** page. | N/A | The **"Events"** page loads successfully. The comment counter icon on the corresponding event card increments by 1. |
| 7 | Click the **"More"** button on the same event card used in Step 3. | N/A | The specific Event details page loads successfully. The comment input field and **"Comment"** button are displayed. The previously posted comment is displayed in the comments list. |
| 8 | Click the **"Delete"** button under the previously posted comment. | N/A | The **"Are you sure you want to delete the comment?"** confirmation modal appears. |
| 9 | Click the **"Yes, delete"** button in the modal. | N/A | The modal closes, and the comment is deleted. The comment counter on the page decrements by 1. |
| 10 | Navigate back to the **"Events"** page. | N/A | The **"Events"** page loads successfully. The comment counter icon on the corresponding event card decrements by 1. |

**Postconditions:**<br>
N/A


**Environment:**
- Browser: Chrome


**Screenshots:**<br>
N/A

**Additional Context:**<br>
N/A
