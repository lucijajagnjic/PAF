#include <iostream>

void jednadzbaPravca(float x1, float y1, float x2, float y2)
{
    float k = (y2 - y1)/(x2 - x1);
    float l = y1 - k*x1;
    std::cout << "y = " << k << "x + " << l << std::endl;
}

int main()
{
    jednadzbaPravca(2,4,4,10);
    
    return 0;

}



