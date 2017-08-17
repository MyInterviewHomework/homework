import ks

ks.Breakpoints()
ks.PrintValue()
ks.PrintStack()

gdb.execute("ks-set-breakpoints")
gdb.execute("run")
gdb.execute("ks-print-stack")
