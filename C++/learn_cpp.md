# Learing C++
## Basic Data Types
* char
* int
* float
* double
* void
> 2 additional
* bool
* wchar_t
> If a variable is unsigned, it only contains positive values and allows it to store numerically larger numbers
```
int main()
{
	float var = 5.5; //it is actually a double
	float var = 5.5f; //this is a float: after adding 'f'
	double variable = 5.3 ;
}
```
```
int main()
{
	bool = true; //output: 1
}
```
## Functions
```
#include <iostream>

int Multiply(int a, int b) //declaring a function, setting parameters within brackets
{
	return a * b;
}

int main()
{
	int result = Multiply(6, 7); //calling function and giving values for parameters
	
	std::cout << result <<std::endl;
	std::cin.get();
}
```
## Header Files
