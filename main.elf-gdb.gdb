set mem inaccessible-by-default off

# Connection
define connect
	target remote localhost:3333
	monitor halt reset
end

# Breakpoints
define set_breakpoints
	break main.c:58
	break main.c:76
	info break
end

# Led
define print_led_status
	# From stm32f10x.h:
	#
	# PERIPH_BASE     = ((uint32_t)0x40000000)
	# APB2PERIPH_BASE = (PERIPH_BASE + 0x10000)
	# GPIOC_BASE      = (APB2PERIPH_BASE + 0x1000)
	# GPIOC           = ((GPIO_TypeDef *) GPIOC_BASE)
    # GPIOC->ODR      = GPIOC + 0xC = 0x40011000+0xC 
	
	x /t 0x40011000+0xC
end

define switch_off_led
	# led is plugged on GPIOC PIN12
	set *(unsigned int *)(0x40011000+0xC) = 1<<12
end

define switch_on_led
	set *(unsigned int *)(0x40011000+0xC) ^= 1<<12
end

# Timer
define print_timer_count
    # From stm32f10x.h:
	#
	# PERIPH_BASE     = ((uint32_t)0x40000000)
	# APB1PERIPH_BASE = PERIPH_BASE
	# TIM2_BASE       = (APB1PERIPH_BASE + 0x0000)
	# TIM2            = ((TIM_TypeDef *) TIM2_BASE)
	# TIM2->CNT       = TIM2 + 0x24 = 0x40000000+0x24

	x /d 0x40000000+0x24
end