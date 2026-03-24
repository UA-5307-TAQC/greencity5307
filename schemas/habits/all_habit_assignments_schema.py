"""Schema for the current user's habit assignments"""

from schemas.habits.habit_assignment_schema import habit_assignment_schema

all_habit_assignments_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": habit_assignment_schema
}
