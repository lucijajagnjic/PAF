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
    swap(lista[a], lista[b]);
    for(int i=0; i<7; i++)
    {
        cout << lista[i] << " " ;
    }
    cout << "\n";
}

void zamjenaElemenata(int lista[], int N)
{
    int skupljac[N];
    for(int i=N-1; i>=0; i--)
    {
        skupljac[N-1 - i] = lista[i] ;
    }
    for(int i=0; i<N-1; i++)
    {
        cout << skupljac[i] << " " ;
    }
    cout << "\n";
}

int main()
{
    int lista[7] = {2,3,4,5,6,7,8};
    poljeBrojeva(lista, 2, 7);
    zamjenaDvaElementa(lista, 4, 6);
    zamjenaElemenata(lista, 4);

    return 0;
}
