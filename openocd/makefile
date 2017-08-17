OPENOCD_PATH=C:\tools\OpenOCD-OLIMEX\openocd-0.9.0-rc1
OPENOCD_BIN_PATH=$(OPENOCD_PATH)\bin-x64
OPENOCD_SCRIPTS_PATH=$(OPENOCD_PATH)\scripts
OPENOCD=$(OPENOCD_BIN_PATH)\openocd.exe
OPENOCD_INT_CFG=$(OPENOCD_SCRIPTS_PATH)\interface\ftdi\olimex-jtag-tiny.cfg
OPENOCD_BOARD_CFG=$(OPENOCD_SCRIPTS_PATH)\board\olimex_stm32_h103.cfg

start:
	@echo Starting OpenOCD...
	cmd /C start "$(OPENOCD)" -f "$(OPENOCD_INT_CFG)" -f "$(OPENOCD_BOARD_CFG)"
	@echo Done.
	
stop:
	@echo Stopping OpenOCD...
	taskkill /IM openocd.exe
	@echo Done.
	
flash:
	@echo Flashing board with $(File)
	cmd /C start "$(OPENOCD)" -f "$(OPENOCD_INT_CFG)" -f "$(OPENOCD_BOARD_CFG)" -c init -c "reset halt" -c "stm32f1x mass_erase 0" -c "flash write_bank 0 $(File) 0" -c "reset init" -c "resume" -c "shutdown"
	@echo Done.