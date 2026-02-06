**Test Case ID**
TC-<ECO-NEWS-001>

**Title**
Create eco news with valid data

**Related Requirement/User Story** 
#101 – Create eco news

**Date Created**
02-06-2026

**Author**
Vitalina Kliuieva 

**Priority**
High 

**Preconditions**
1. User is logged in
2. CreateUpdateEcoNewsPage is opened

**Test Steps**
| Step # | Step Description | Test Data | Expected Result |
|:------:|:----------------|:----------|:---------------|
|   1    |Fill eco news form|Valid title, tags, source, image, content|All fields accept input|
|   2    |Click Submit button|    -      |Eco news is created|

**Postconditions**
Eco news is saved and visible in Eco News list


**Environment**
- Browser: [e.g. Chrome, Safari]


**Screenshots**


**Additional Context**
Uses fill_form() and submit_form() methods
