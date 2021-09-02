#include <stdio.h>
#include <math.h>

main()
{
    double x;
    x = 30;
    x *= 3.141593 / 180.0;

    printf("The sin of 30 degrees is %f\n", sin(x));
    printf("The cos of 30 degrees is %f\n", cos(x));
    printf("The tan of 30 degrees is %f\n", tan(x));
    return 0;


}
