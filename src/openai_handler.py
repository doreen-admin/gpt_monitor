import json
import re
from openai import OpenAI
from logging import getLogger
import os

class OpenAIHandler:
    def set_context(self, context):
        self.context = context
        self.logger = getLogger(__name__)
        self.err = False

    def create_assistant(self, app, instructions):
        OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
        self.context.client = OpenAI(api_key=OPENAI_API_KEY)

        # Create an Assistant
        self.context.assistant = self.context.client.beta.assistants.create(
            name=app,
            instructions=instructions,
            model=self.context.config.userdata["model"]
        )
    
    def ask(self, query):
        # Create a thread
        self.context.thread = self.context.client.beta.threads.create()

        # Add a user message to the thread
        message = self.context.client.beta.threads.messages.create(
            thread_id=self.context.thread.id,
            role="user",
            content=query
            #content="Hello, how can I integrate GPT with my app?"
        )
        # Run the Assistant
        run = self.context.client.beta.threads.runs.create(
            thread_id=self.context.thread.id,
            assistant_id=self.context.assistant.id
        )
        # Wait for the run to complete, then retrieve the response
        import time
        while True:
            run_status = self.context.client.beta.threads.runs.retrieve(
                thread_id=self.context.thread.id,
                run_id=run.id
            )
            if run_status.status == "completed":
                return True
            elif run_status.status == "failed":
                return False
            #print("waiting")
            time.sleep(1)
    
    def check_reply_contains(self, expected):
        # Get the messages
        messages = self.context.client.beta.threads.messages.list(thread_id=self.context.thread.id)
        for msg in messages.data:
            actual = msg.content[0].text.value
            #print(f"{msg.role}: {actual}")    
            if msg.role == "assistant":
                if re.search(expected.lower(), actual.lower()):
                    assert True
                else:
                    if not self.err:
                        self.err = True
                        print(f"Role: {msg.role}. {expected} is not included in {actual}")
                    assert False
