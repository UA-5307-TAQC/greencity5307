---
type: "TestCase"
name: "Test Case"
about: "ISTQB-aligned template for test case creation"
title: "[Test Case]: "
labels: ["verification required"]
assignees: []
---

**Test Case ID:**<br>TC-FF-2

**Title:**<br>
Verify Friend Request Persistence After User Logout and Login

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
| 6 | Click on the **User Profile** icon (dropdown) in the header. | N/A | The user menu dropdown opens. The **"Sign out"** option is visible. |
| 7 | Click the **"Sign out"** button. | N/A | The user is logged out successfully. The application redirects to the Main page. The **"Sign in"** button is visible in the header. |
| 8 | Click the **"Sign in"** button in the header. | N/A | The **"Sign in"** modal window appears. |
| 9 | Enter the valid email address into the email field. | `{valid_email}` | The email field accepts the input. |
| 10 | Enter the valid password into the password field. | `{valid_password}` | The password field accepts the input. |
| 11 | Click the **"Sign in"** button. | N/A | The user is successfully logged in. The Profile page loads successfully. |
| 12 | Click on the **"+"** (plus) icon in the **"My friends"** section within the profile information block. | N/A | The **"Find Friend"** page loads successfully. |
| 13 | Enter the same target user name into the **Search** input field. | `{target_user_name}` | The user list updates to display only the specific user. The button displays **"Cancel Request"** on the found user's card (indicating the request is still active).|


**Postconditions:**<br>
N/A


**Environment:**
- Browser: Chrome


**Screenshots:**<br>
N/A

**Additional Context:**<br>
N/A
