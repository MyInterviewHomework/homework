# General Makefile
# Inspired by http://www.downloads.seng.de/HowTo_ToolChain_STM32_Ubuntu.pdf
#
# Usage:
# make OptLIB=0 OptSRC=0 all tshow
#
# See Makefile.common for parameters details

include Makefile.common
LDFLAGS=$(COMMONFLAGS) -fno-exceptions -ffunction-sections -fdata-sections -L$(LIBDIRWIN) -nostartfiles -Wl,--gc-sections,-Tlinker.ld

LDLIBS+=-lm
LDLIBS+=-lstm32

# Compile stm32 libs and src
# Produce:
# - a binary file ready to load to the board
# - an elf file with all symbols and code for debugging purposes
all: libs src
	$(CC) -o $(PROGRAM).elf $(LDFLAGS) \
		-Wl,--whole-archive \
		src/app.a \
		-Wl,--no-whole-archive \
			$(LDLIBS)
	$(OBJCOPY) -O ihex $(PROGRAM).elf $(PROGRAM).hex
	$(OBJCOPY) -O binary $(PROGRAM).elf $(PROGRAM).bin
	
	#Extract info contained in ELF to readable text-files:
	arm-none-eabi-readelf -a $(PROGRAM).elf > $(PROGRAM).info_elf
	arm-none-eabi-size -d -B -t $(PROGRAM).elf > $(PROGRAM).info_size
	arm-none-eabi-objdump -S $(PROGRAM).elf > $(PROGRAM).info_code
	arm-none-eabi-nm -t x -S --numeric-sort -s $(PROGRAM).elf > $(PROGRAM).info_symbol

.PHONY: libs src clean tshow

libs:
	$(MAKE) -C libs $@

src:
	$(MAKE) -C src $@

clean:
	$(MAKE) -C src $@
	$(MAKE) -C libs $@
	rm -f $(PROGRAM).elf $(PROGRAM).hex $(PROGRAM).bin $(PROGRAM).info_elf $(PROGRAM).info_size
	rm -f $(PROGRAM).info_code
	rm -f $(PROGRAM).info_symbol

tshow:
	@echo "######################################################################################################"
	@echo "######## optimize settings: $(InfoTextLib), $(InfoTextSrc)"
	@echo "######################################################################################################"
#flash:
# ./jtagprog.pl