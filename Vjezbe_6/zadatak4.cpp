#include <iostream>
using namespace std;

void jednadzba(float a1, float b1, float c1, float a2, float b2, float c2)
{
    float x;
    x = (b1*c2 - b2*c1) / (b1*a2 -a1*b2);
    float y;
    y = (c1 - a1*x) / b1;
    cout << "X je: " << x << " Y je: " << y << endl;
}

int main()
{
    jednadzba(2.0, 5.0, 7.0, -12.0, 9.0, 4.0);
    return 0;
}