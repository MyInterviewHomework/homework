#
# GDB extension for main.c debugging purposes. 
# Automatically place a breakpoint and 
# display led and timer status on the four first breakpoint hits.
#
# Author: Sebastien Morvan
# Version: 1.0
#
# Usage:
# - Copy this file and 'pyks' into the directory of main.elf
# - Check your gdb auto-load policy, especially in $HOME/.gdbinit
# - Connect the board, load the program, start openOCD
# - From the shell, run: arm-none-eabi-gdb-py main.elf  
#

import gdb
import datetime
from pyks.gdb import *

################################################################################
#
# Printing functions to render the application status
#
################################################################################

# Print board LED status in hexa and binary
# by reading the GPIOC value
def print_led_status():
  print "LED status:"
  pr.print_memory(0x4001100c, 2)
  print ""

# Print timer 2 hardware counter value in hexa and binary
def print_timer_count():
  print "Timer count:"
  pr.print_memory(0x40000024, 2)
  print ""

# Print the value of timerValue defined in main.c
def print_timer_value():
  pr.print_value("timerValue")

# Print application status by combining
# - current date time 
# - above defined print functions
# - call stack

def print_status():
  print "\n#### Status at", datetime.datetime.now(), "####\n"
  print_led_status()
  print_timer_count()
  pr.print_value("timerValue")
  print("")
  pr.print_call_stack()
  print("")

################################################################################
#
# Breakpoint and command handler to print the application status
#
################################################################################

# This handler is used by the ObserverBreakpoint
# to print the application status on the four first breakpoint hits
def print_status_obs_bp_handler(breakpoint):
  print_status()
  return breakpoint.obs_count > 3

# This handler is used by the user defined GDB command
# 'print_status'
def print_status_cmd_handler(argv):
  print_status()  

################################################################################
#
# Main
#
################################################################################

# Define a new breakpoint and delegate the hit event action to a dedicated handler
bp.ObserverBreakpoint("main.c:95", print_status_obs_bp_handler)
# Define a new GDB command to print the application status 
cmd.create_command("print_status", print_status_cmd_handler)

# Connect to the target
gdb.execute("target remote localhost:3333")
gdb.execute("monitor halt reset")
# Continue until the next breakpoint
gdb.execute("c")