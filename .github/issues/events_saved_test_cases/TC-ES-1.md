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
Verify that the saved event disappears from the Saved Events page when the user deletes the event.

**Related Requirement/User Story:**<br>
None

**Date Created:**<br>
02-08-2026

**Author:**<br>
Osypenko Kostiantyn

**Priority:**<br>
Medium

**Preconditions:**<br>
 - User is logged in.
 - User has previously created an event with a unique title `{event_title}`.

**Test Steps:**

| Step # | Step Description | Test Data | Expected Result |
|:------:|:-----------------|:----------|:----------------|
| 1 | Navigate to the GreenCity URL. | `https://www.greencity.cx.ua/#/greenCity` | The Main page loads successfully. |
| 2 | Click on the **"Events"** button in the header. | N/A | The **"Events"** page loads successfully. |
| 3 | Click on the **Search** (magnifying glass) icon. | N/A | The search input field appears, replacing the icon. |
| 4 | Enter the title of the created event into the search field. | `{event_title}` | The list updates. The specific event card is found and displayed. |
| 5 | Click the **"Save"** (bookmark) icon on the found event card. | N/A | The **"Save"** icon turns green (indicating the event is saved). |
| 6 | Click the **"Saved"** icon in the header. | N/A | The **"Saved"** page loads successfully with the **"Eco-news"** section open by default. |
| 7 | Click on the **"Events"** tab. | N/A | The **"Saved Events"** section is displayed. The previously saved event card is visible in the list. |
| 8 | Click the **"More"** button on the event card. | N/A | The specific Event details page loads successfully. The **"Delete"** button is displayed in the upper right part of the page. |
| 9 | Click the **"Delete"** button. | N/A | The **"Event will be deleted"** confirmation modal appears. |
| 10 | Click the **"Yes"** button in the modal. | N/A | The modal closes. The user is redirected to the **"Events"** page with the list of all events. |
| 11 | Click the **"Saved"** icon in the header. | N/A | The **"Saved"** page loads successfully with the **"Eco-news"** section open by default. |
| 12 | Click on the **"Events"** tab. | N/A | The **"Saved Events"** section is displayed. The list is empty and the specific event is absent. |

**Postconditions:**<br>
N/A


**Environment:**
- Browser: Chrome


**Screenshots:**<br>
N/A

**Additional Context:**<br>
Test case fails on the step 4. The Search field functionality does not work.
