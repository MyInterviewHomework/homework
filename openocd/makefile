# OpenOCD Makefile
#
# OpenOCD connects to the STM32-H103 board
# trough the ARM-USB-TINY debugger and 
# acts like a gdbserver, allowing therefore
# a GDB session.
# 
OPENOCD_PATH=C:\tools\OpenOCD-OLIMEX\openocd-0.9.0-rc1
OPENOCD_BIN_PATH=$(OPENOCD_PATH)\bin-x64
OPENOCD_SCRIPTS_PATH=$(OPENOCD_PATH)\scripts
OPENOCD=$(OPENOCD_BIN_PATH)\openocd.exe
OPENOCD_INT_CFG=$(OPENOCD_SCRIPTS_PATH)\interface\ftdi\olimex-jtag-tiny.cfg
OPENOCD_BOARD_CFG=$(OPENOCD_SCRIPTS_PATH)\board\olimex_stm32_h103.cfg

# Connect to the board and acts as a gdbserver
start:
	@echo Starting OpenOCD...
	cmd /C start "$(OPENOCD)" -f "$(OPENOCD_INT_CFG)" -f "$(OPENOCD_BOARD_CFG)"
	@echo Done.
	
# Stop / kill OpenOCD
stop:
	@echo Stopping OpenOCD...
	taskkill /IM openocd.exe
	@echo Done.
	
# Load a binary file to the board.
# Usage: make flash File="../myfile.bin" 
flash:
	@echo Flashing board with $(File)
	cmd /C start "$(OPENOCD)" -f "$(OPENOCD_INT_CFG)" -f "$(OPENOCD_BOARD_CFG)" -c init -c "reset halt" -c "stm32f1x mass_erase 0" -c "flash write_bank 0 $(File) 0" -c "reset init" -c "resume" -c "shutdown"
	@echo Done.