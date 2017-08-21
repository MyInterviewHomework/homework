import gdb

# This module is about gdb user defined commands.

# FunctionCommand associates a user defined function_handler
# with a gdb command name.
# function_handler is called with an argument array from the UI inputs.
class FunctionCommand(gdb.Command):
  def __init__ (self, name, function_handler):
    self.function_handler = function_handler
    super (FunctionCommand, self).__init__ (name, gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
    argv = gdb.string_to_argv(arg)
    self.function_handler(argv)

# create_command is a convenient way to build
# a FunctionCommand object.	
def create_command(name, handler):
  FunctionCommand(name, handler)
