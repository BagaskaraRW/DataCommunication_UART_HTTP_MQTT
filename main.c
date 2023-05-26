#include <project.h>
#include <stdio.h>
#include <math.h>

/* Project Defines */
#define TRANSMIT_BUFFER_SIZE  1

int main()
{
    /* Variable to store ADC result */
    uint16 Output;
    uint16 Input;
    uint16 R_FSR;
    uint16 Vcc;
    uint16 Vmeas;
    uint16 mass;
    uint16 R0 = 4700;
    /* Transmit Buffer */
    char TransmitBuffer[TRANSMIT_BUFFER_SIZE];
    
    /* Start the components */
    ADC_DelSig_1_Start();
    UART_1_Start();
    
    /* Start the ADC conversion */
    ADC_DelSig_1_StartConvert();
    
    for(;;)
    {        
        if(ADC_DelSig_1_IsEndConversion(ADC_DelSig_1_RETURN_STATUS))
        {
            Input = ADC_DelSig_1_CountsTo_mVolts(ADC_DelSig_1_GetResult16());
            R_FSR = R0*((Vcc/Vmeas)-1);
            Output = 271.0/(R0*((Vcc/Vmeas)-1));
            mass = pow(Output,(1/0.69));
            sprintf(TransmitBuffer, "%u\n", Output);
                /* Send out the data */
            UART_1_PutString(TransmitBuffer);
            CyDelay(50);
        }
    }
}


/* [] END OF FILE */
