#include <iostream>
using namespace std;

void jednadzbaKruznice(float x, float y, float r, float p, float q)
{
    float d;
    d = sqrt(pow((x-p), 2.0) + pow((y - q), 2.0));
    if (d > r)
    {
        cout << "Tocka nije u kruznici." << endl;
    }
    else if (d <= r)
    {
        cout << "Tocka je u kruznici." << endl;
    }
}

int main()
{
    jednadzbaKruznice(5.0, 3.0, 4.0, 1.0, 1.0);
    return 0;
}
