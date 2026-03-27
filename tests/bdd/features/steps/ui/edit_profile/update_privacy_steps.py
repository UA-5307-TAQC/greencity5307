"""Steps related to Edit Profile"""

from behave import when, then


@when('the user updates location privacy to "{value}"')
def step_set_location(context, value):
    """Set location privacy to "{value}"""
    context.profile_privacy.set_show_location_value(value)
    context.new_location = value


@when('the user updates eco places privacy to "{value}"')
def step_set_eco_places(context, value):
    """Set eco places privacy to "{value}"""
    context.profile_privacy.set_show_eco_places_value(value)
    context.new_eco_places = value


@when('the user sets to-do list visibility to "{value}"')
def step_set_todo(context, value):
    """Set to-do list visibility to "{value}"""
    context.profile_privacy.set_show_todo_value(value)
    context.new_todo = value


@when('the user updates to-do privacy to "{value}"')
def step_check_location(context, value):
    """Check if privacy is set to "{value}"""
    actual = context.profile_privacy.get_show_location_value()
    assert actual == value, f"Expected '{value}', got '{actual}'"


@then('the eco places visibility should be "{value}"')
def step_check_eco_places(context, value):
    """Check if privacy is set to "{value}"""
    actual = context.profile_privacy.get_show_eco_places_value()
    assert actual == value, f"Expected '{value}', got '{actual}'"


@then('the to-do list visibility should be "{value}"')
def step_check_todo(context, value):
    """Check if privacy is set to "{value}"""
    actual = context.profile_privacy.get_show_todo_value()
    assert actual == value, f"Expected '{value}', got '{actual}'"
