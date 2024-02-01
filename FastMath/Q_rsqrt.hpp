#include <iostream>
#include <limits>
#include <cstring>
using namespace std;

// the answer may be wrong according to the os platform
// float Q_rsqrt(float number) {
//     long i;
//     float x2, y;
//     const float three_half = 1.5F;
    
//     x2 = number * 0.5F;
//     y  = number;
//     i = *(long *) &y;
//     i = 0x5f3759df - (i>>1);
//     y = *(float *)&i;
//     y = y*(three_half - (x2*y*y));
//     // y = y*(three_half - (x2*y*y)); // for more precise
//     return y;
// }
    

// prevent c++ undefined action
float Q_rsqrt(float number)
{
    static_assert(numeric_limits<float>::is_iec559,  "fast inverse square root requires IEEE-comliant 'float'");
    static_assert(sizeof(float)==sizeof(uint32_t),  "fast inverse square root requires 'float' to be 32-bit");
    float x2 = number * 0.5F, y = number;
    uint32_t i;
    memcpy(&i, &y, sizeof(float));
    i  = 0x5f3759df - ( i >> 1 );
    memcpy(&y, &i, sizeof(float));
    return y * ( 1.5F - ( x2 * y * y ) );
}

// g++ Qrsqrt.hpp -o main.exe
int main() {
    cout << 1/Q_rsqrt(2) << "==" << "1/sqrt(2)"  << "==" << "1.414" <<endl;
}