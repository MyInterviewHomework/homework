import gdb

# This module is about breakpoint extension.

# This breakpoint is usefull to trigger
# actions on hits, such as value printing, 
# without giving control to gdb UI.
# The trick lies in the difference between
# the real program state (stopped) and the gdb
# internal breakpoint state given by the stop return value.
#
# Breakpoint is located according to expr.
# obs_handler is called on breakpoint hit with this object as argument.
# When obs_handler returns true, control is given to gdb UI.
# Else, it acts like a gdb continue.
# ObserverBreakpoint provides an obs_count attribute
# incremented each time obs_handler is called.
class ObserverBreakpoint (gdb.Breakpoint):
  def __init__(self, expr, obs_handler):
	self.obs_handler = obs_handler
	self.obs_count = 0
	gdb.Breakpoint.__init__(self, expr)
	
  def stop (self):
    self.obs_count += 1
    return self.obs_handler(self)
