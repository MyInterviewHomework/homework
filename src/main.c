/************************************************************************************************************
* Test-program for Olimex “STM32-H103”, header board for “STM32F103RBT6”.
* After program start, green LED (STAT) will blink based on the hardware timer TIM2 interruption.
*
************************************************************************************************************/

#include "stm32f10x.h"
#include "stm32f10x_rcc.h"
#include "stm32f10x_gpio.h"
#include "stm32f10x_tim.h"
#include "misc.h"

/*
	The board status LED is connected to the GPIOC Pin 12.
	Enable the port in push pull output mode.
*/
void InitializeLEDs()
{
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);

	GPIO_InitTypeDef gpioStructure;
    gpioStructure.GPIO_Pin = GPIO_Pin_12;
    gpioStructure.GPIO_Mode = GPIO_Mode_Out_PP;
    gpioStructure.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIOC, &gpioStructure);

    GPIO_WriteBit(GPIOC, GPIO_Pin_12, Bit_RESET);
}

/*
	Initialize the timer (TIM2) to generate an
	update event each second.
	Period value = (1 / 72Mhz) * 40000 * 1800
*/
void InitializeTimer()
{
    RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);

    TIM_TimeBaseInitTypeDef timerInitStructure;
    timerInitStructure.TIM_Prescaler = 40000;
    timerInitStructure.TIM_CounterMode = TIM_CounterMode_Up;
    timerInitStructure.TIM_Period = 1800;
    timerInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;
    timerInitStructure.TIM_RepetitionCounter = 0;
    TIM_TimeBaseInit(TIM2, &timerInitStructure);
    TIM_Cmd(TIM2, ENABLE);
	TIM_ITConfig(TIM2, TIM_IT_Update, ENABLE);
}

/*
	Enable timer interrupt for TIM2 
*/
void EnableTimerInterrupt()
{
    NVIC_InitTypeDef nvicStructure;
    nvicStructure.NVIC_IRQChannel = TIM2_IRQn;
    nvicStructure.NVIC_IRQChannelPreemptionPriority = 0;
    nvicStructure.NVIC_IRQChannelSubPriority = 1;
    nvicStructure.NVIC_IRQChannelCmd = ENABLE;
    NVIC_Init(&nvicStructure);
}

/*
	Timer interrupt handler.
	Just: 
	- clear interrupt pending bits
	- toggle the led status by XOR on bit 12
*/
void TIM2_IRQHandler(void)
{
    if (TIM_GetITStatus(TIM2, TIM_IT_Update) != RESET)
    {
        TIM_ClearITPendingBit(TIM2, TIM_IT_Update);
        GPIOC->ODR ^=(1 << 12 );
    }
}

/*
	Main: where the application starts
*/
int main()
{
    InitializeLEDs();
    InitializeTimer();
	EnableTimerInterrupt();
    
	int timerValue;
    for (;;)
    {
		for (int i = 0; i < 1000000; i++)
		{
			/* Create a opportunity to put a breakpoint */
			timerValue = TIM_GetCounter(TIM2);
			if (timerValue == 200)
				asm("nop");
		}
	}
}
