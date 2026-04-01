"""Steps related to Edit Profile"""

from behave import when, then


@when('the user updates location privacy to "{value}"')
def step_set_location(context, value):
    """Set the location privacy to {value}"""
    context.profile_privacy.set_show_location_value(value)
    context.new_location = value


@when('the user updates eco places privacy to "{value}"')
def step_set_eco_places(context, value):
    """Set the eco places privacy to {value}"""
    context.profile_privacy.set_show_eco_places_value(value)
    context.new_eco_places = value


@when('the user updates to-do privacy to "{value}"')
def step_set_todo(context, value):
    """Set the to-do privacy to {value}"""
    context.profile_privacy.set_show_todo_value(value)
    context.new_todo = value


@then('the location privacy should be "{value}"')
def step_check_location(context, value):
    """The location privacy should be {value}"""
    actual = context.profile_privacy.get_show_location_value()
    assert actual == value, f"Expected '{value}', got '{actual}'"


@then('the eco places privacy should be "{value}"')
def step_check_eco_places(context, value):
    """The eco places privacy should be {value}"""
    actual = context.profile_privacy.get_show_eco_places_value()
    assert actual == value, f"Expected '{value}', got '{actual}'"


@then('the to-do privacy should be "{value}"')
def step_check_todo(context, value):
    """The to-do privacy should be {value}"""
    actual = context.profile_privacy.get_show_todo_value()
    assert actual == value, f"Expected '{value}', got '{actual}'"
