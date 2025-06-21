import json
import re
import logging
logger = logging.getLogger(__name__)

class MockHandler:
    def set_context(self, context):
        self.context = context

    def create_assistant(self, app, instructions):
        assistant = {}
        assistant["instructions"] = instructions
        return assistant
    
    def ask(self, query):
        return True
    
    def check_reply_contains(self, expected):
        # dummy. just check the content of json file
        if re.search(expected, expected.lower().replace("(", "")):
            assert True
        else:
            logger.warning(f"{expected} is not included in {expected}")
            assert False
