#include <iostream>
#include <cmath>
using namespace std;

/*
S : Spot price at time = t
Su : Spot price in case of an up move
Sd : Spot price in case of a down move
E : Strike price 
r : Risk free rate
*/

double binomialPricing(double S, double Su, double Sd, double E, double r, double t, double T){
    double delta = (max(Su-E,0.0)-max(Sd-E,0.0))/(Su-Sd);
    double P = (max(Sd-E,0.0)-delta*Sd)*exp(-r*(T-t))+delta*S;
    return P;
}

int main(){
    cout<<binomialPricing(100,101,99,100,0.1,0,1);
    return 0;
}