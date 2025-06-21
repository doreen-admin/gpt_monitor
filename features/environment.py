import logging
import logging.handlers
from behave.model import Scenario
      
def before_all(context):
    context.log_handler = logging.handlers.BufferingHandler(1000)
    context.log_handler.setFormatter(logging.Formatter(context.config.logging_format, context.config.logging_datefmt))
    context.log_handler.setLevel(context.config.logging_level)
    userdata = context.config.userdata
    continue_after_failed = userdata.getbool("runner.continue_after_failed_step", False)
    Scenario.continue_after_failed_step = continue_after_failed

def before_step(context, step):
    context.log_handler.flush()
    root_logger = logging.getLogger()
    root_logger.addHandler(context.log_handler)

def after_step(context, step):
    root_logger = logging.getLogger()
    root_logger.removeHandler(context.log_handler)
    logstr = '\n'.join(context.log_handler.formatter.format(r) for r in context.log_handler.buffer)
