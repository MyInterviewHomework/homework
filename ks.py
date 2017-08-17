import gdb

class Breakpoints(gdb.Command):
  def __init__ (self):
    super (Breakpoints, self).__init__ ("ks-set-breakpoints", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
    print("Setting breakpoints...")
    gdb.Breakpoint("main.c:58")
    gdb.Breakpoint("main.c:76")
	gdb.execute("info break")
    print("Done.")

class PrintValue(gdb.Command):
  def __init__ (self):
    super (PrintValue, self).__init__ ("ks-print-value", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
    argv = gdb.string_to_argv(arg)
    value_expr = argv[0]    
    value = gdb.parse_and_eval(value_expr)
    print("%s = %s" % (value_expr, value))

class PrintStack(gdb.Command):
  def __init__ (self):
    super (PrintStack, self).__init__ ("ks-print-stack", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
    print("Printing call stack...")
    frame = gdb.newest_frame()
    i = 0
    while(frame):
      symtab_and_line = frame.find_sal()
      result = (i, frame.function(), symtab_and_line.symtab, symtab_and_line.line)
      print("#%d %s() at %s line %s" % result)
      frame = frame.older()
      i+=1

