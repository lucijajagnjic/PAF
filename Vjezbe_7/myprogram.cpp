#include <iostream>
#include  "Particle.h"

int main()
{
  Particle p1(100.0, 45.0, 0.0, 0.0, 0.01);
  p1.range();
  p1.tTime();

  Particle p2(10.0, 60.0, 0.0, 0.0, 0.01);
  p2.range();
  p2.tTime();

  return 0;
}