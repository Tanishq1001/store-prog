# Learing C++
## How it Works:
```#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
   vector<string> msg {"hello", "Worlds"};

   for (const string& word : msg){
       cout << word << " ";
   }
   cout << endl;
}
```
> \#include <>: imports files which have declarations for functions used in the program
> int main(): it is the main fuction of the program
> endl: ends the line