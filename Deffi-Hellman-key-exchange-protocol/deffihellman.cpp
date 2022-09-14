#include<iostream>
#include<math.h>
long long int power(long long int a, long long int b,long long int P)
{
	if (b == 1)
		return a;

	else
		return (((long long int)pow(a, b)) % P);
}
int main()
{
	long long int p, g, x, a, y, b, ka, kb;
	std::cout<<"enter value of p: ";
	std::cin>>p;
	std::cout<<"enter value of g: ";
	std::cin>>g;
	std::cout<<"enter alice private key: ";
	std::cin>>a;
	std::cout<<"The private key a for Alice : "<<a;
	x = power(g, a, p);
	std::cout<<"\n enter bob private key: ";
	std::cin>>b;
	std::cout<<"The private key a for bob : "<<b;
	y = power(g, b, p);
	ka = power(y, a, p);
	kb = power(x, b, p);
	std::cout<<"\n Secret key for the Alice is : "<<ka;
	std::cout<<"\n Secret Key for the Bob is : "<<kb;
	return 0;
}
