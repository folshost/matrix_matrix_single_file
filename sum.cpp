#include <iostream>
#include <stdio.h>
#include <stdlib.h>



int main(int argc, char* argv[]){
  long long int s;
  char* end;
  const int f = strtol(argv[1], &end,10);
  for(int i = 0; i<f;i++){
    s += i*i;
  }
  std::cout << s << std::endl;
}
