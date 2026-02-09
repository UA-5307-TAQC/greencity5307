---
type: "TestCase"
name: "Test Case"
about: "ISTQB-aligned template for test case creation"
title: "[Test Case]: "
labels: ["verification required"]
assignees: []
---

**Test Case ID:**<br>TC-FF-1

**Title:**<br>
Verify User Search, Friend Request Sending, Persistence, and Cancellation

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
 - A target user exists in the system who is not yet in the user's friend list.

**Test Steps:**

| Step # | Step Description | Test Data | Expected Result |
|:------:|:-----------------|:----------|:----------------|
| 1 | Navigate to the GreenCity URL. | `https://www.greencity.cx.ua/#/greenCity` | The Home page loads successfully. |
| 2 | Click on the **"My Space"** section in the header. | N/A | The **"My Space"** page loads successfully. |
| 3 | Click on the **"+"** (plus) icon in the **"My friends"** section within the profile information block. | N/A | The **"Find Friend"** page loads successfully. |
| 4 | Enter the target user name into the **Search** input field. | `{target_user_name}` | The user list updates to display only the specific user matching the input. |
| 5 | Click the **"Add Friend"** button on the found user's card. | N/A | The button label changes to **"Cancel Request"**. A notification message **"Friend request sent"** appears at the top of the page. |
| 6 | Refresh the page. | N/A | The **"Find Friend"** page reloads successfully. The **Search** input field is cleared, and the full list of users is displayed. |
| 7 | Enter the same target user name into the **Search** input field. | `{target_user_name}` | The user list updates to display only the specific user. The **"Cancel Request"** button is displayed on the user card. |
| 8 | Click on the user card. | N/A | The specific **User Profile** page loads successfully. The **"Cancel Request"** button is displayed in the profile information block. |
| 9 | Click the **"Cancel Request"** button. | N/A | The button label changes to **"Add Friend"**. A notification message **"Your friend request has been canceled"** appears at the top of the page. |
| 10 | Navigate back to the previous page (**"Find Friend"**). | N/A | The **"Find Friend"** page loads successfully. The **Search** input field is cleared, and the full list of users is displayed. |
| 11 | Enter the same target user name into the **Search** input field. | `{target_user_name}` | The user list updates to display only the specific user. The **"Add Friend"** button is displayed on the user card. |

**Postconditions:**<br>
N/A


**Environment:**
- Browser: Chrome


**Screenshots:**<br>
N/A

**Additional Context:**<br>
N/A
