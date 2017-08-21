![Krono-Safe](http://krono-safe.com/wp-content/uploads/2014/08/Logo2.png)
# Homework
This homework consists in using and creating an extension to gdb in order to debug an applicatin running on a board.
It contains:
- an application that blinks the status led based on hardware timer
- a set of gdb and Python scripts for gdb
- a convenient script launching OpenOCD with the right configuration to debug the STM32-H103 board with the Olime debugger ARM-USB-TINY

# Installing on Windows
  - Install the [GNU ARM Embedded Toolchain](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads)
  - Install [Cygwin](https://www.cygwin.com/install.html) and its devtool package (you will need make and bash)
  - Install [Olimex OpenOCD](https://www.olimex.com/Products/ARM/JTAG/_resources/OpenOCD/)
  - Install [Python 2.7](https://www.python.org/downloads/)
  - Update your PATH to include ARM toolchain commands and python
  - Check the installation by typing the following commands in Cygwin shell
 ```
$ arm-none-eabi-gcc --version
$ python --version
```
  - Retrieve the project with Git

# Compiling
  - Start a Cygwin session
  - Go to your project directory
```
$ cd /cygdrive/c/ws/ks
```
  - Run make
 ```
 $ make OptLIB=0 OptSRC=0
 ```
  - To removed produced files, run clean
 ```
 $ make clean
 ```
 # Programming the board
  - Plug your board to an USB power supply
  - Plug the USB debugger to the board and to your PC
  - Start a Cygwin session
  - Go to your project directory
```
$ cd /cygdrive/c/ws/ks
```
  - Check the file main.bin
```
$ ls -l main.bin
```
  - Just run
 ```
 $ cd openocd
 $ make flash File=../main.bin
```
  - Do you see the status led blinking? Good job!
 # Debugging with gdb and Python
  - Plug your board to an USB power supply
  - Plug the USB debugger to the board and to your PC
  - Start a Cygwin session
  - Go to your project directory
 ```
$ cd /cygdrive/c/ws/ks
```
  - Start OpenOCD gdbserver
 ```
 $ make -C openocd start
 ```
  - Note: to stop OpenOCD, just run
 ```
 $ make -C openocd stop
```
  - Check gdb Python auto-load policy, especially in your $HOME/.gdbinit file
  - Start gdb and auto-load python scripts
 ```
 $ arm-none-eabi-gdb-py main.elf
```
  - Auto loaded debugging Python scripts should produce outputs like this:
```
#### Status at 2017-08-21 23:45:21.669000 ####

LED status:
hex: 0x00, 0x00
bin: 00000000, 00000000

Timer count:
hex: 0x04, 0xba
bin: 00000100, 10111010

timerValue = 995

Call stack:
#0 main() at main.c line 95
```
  - To print this application status, you could type
```
(gdb) print_status
```
# Coding
  - Main application code is located in the file src/main.c
  - Python scripts can be modified in
    - main.elf-gdb.py for application specific script
    - pyks/gdb for gdb general purposes
 # Todos
   - Write some/more tests
 
