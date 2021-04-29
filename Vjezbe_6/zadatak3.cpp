#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

void poljeBrojeva(int lista[], int a, int b)
{
    for(int i=a; i<b; i++)
    {
        cout << lista[i] << " " ;
    }
    cout << "\n";
}

void zamjenaDvaElementa(int lista[], int a, int b)
{
    for(int i=a; i<b; i++)
    {
        cout << lista[i] << " " ;
    }
    cout << "\n" ;
}

int main()
{
    int lista[7] = {2,3,4,5,6,7,8};
    poljeBrojeva(lista, 2, 7);
    zamjenaDvaElementa(lista, 4, 6);
    return 0;
}
