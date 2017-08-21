import gdb

# This module contains convenient functions 
# to print call stack, variable and memory values.
 
# Print the call stack from the newest frame in current inferior.
# Display level, function name, file and line.
def print_call_stack():
  print("Call stack:")
  frame = gdb.newest_frame()
  i = 0
  while(frame):
    symtab_and_line = frame.find_sal()
    result = (i, frame.function(), symtab_and_line.symtab, symtab_and_line.line)
    print "#%d %s() at %s line %s" % result
    frame = frame.older()
    i+=1

# Print value computed by expr.
def print_value(expr):
  value = gdb.parse_and_eval(expr)
  print("%s = %s" % (expr, value))

# Print byte_count bytes read from the address addr.
# For each byte, values are formated in hexa and binary.
def print_memory(addr, byte_count):
  inf = gdb.selected_inferior()
  value = inf.read_memory(addr, byte_count)
  print "hex:", ', '.join('%#.2x' % ord(value[i]) for i in reversed(range(len(value))))
  print "bin:", ', '.join('%s' % bin(ord(value[i]))[2:].zfill(8) for i in reversed(range(len(value))))
