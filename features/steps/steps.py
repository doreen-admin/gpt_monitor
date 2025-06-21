# steps/login_steps.py
import json
from src.mock_handler import MockHandler
from src.openai_handler import OpenAIHandler
from openai import OpenAI
from behave import given, when, then

def get_handler(key): 
    kv = {
            "mock": MockHandler(),
            "openai": OpenAIHandler()
        }
    return kv[key]

@given('Assistant Instructions of {app}')
def step_impl(context, app):
    #handler = OpenAIHandler()
    handler = get_handler(context.config.userdata["handler"])
    handler.set_context(context)
    with open("features/steps/resource/instructions.json", 'r') as file:
        data = json.load(file)
    
    handler.create_assistant(app, data[app])
    context.handler = handler
    context.app = app

@when('User asks the Assistant a Query of {query}')
def step_impl(context, query):
    with open("features/steps/resource/queries.json", 'r') as file:
        data = json.load(file)[context.app]
    retval = context.handler.ask(data[query])
    if retval == False:
        assert False

@then('the Reply contains reference to {contents}')
def step_impl(context, contents):
    context.handler.check_reply_contains(contents)
