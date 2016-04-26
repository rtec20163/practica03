#include <stdio.h>
#include <math.h> //para usar fabs(x) y exp(x)

double funcion(double x)
{
      return x*exp(x)-5;     
}

double error(double a, double b)
{
      return (fabs(a-b)/a)*100;
}


int main(int argc, char *argv[])
{
    double a=1.2,b=1.4,c,raiz=1.3267246652422,tolerancia=0.001;
    int i=1;
    
    printf("El programa implementa el algoritmo de biseccion para la funcion\n");
    printf("\t xe^x - 5");
 
    do
    {
     c=(a+b)/2;
     printf("\n\nIteracion %d \t Error relativo= %f",i,error(raiz,c));
     printf("\n\t a= %f \t\t f(a)= %f",a,funcion(a));
     printf("\n\t c= %f \t\t f(c)= %f",c,funcion(c));
     printf("\n\t b= %f \t\t f(b)= %f",b,funcion(b));
     

     if(funcion(a)*funcion(c)<0)
         b=c;
     else
         a=c;
     
     i = i+1;    
     
    }while(fabs(a-b)>tolerancia); 
     
    getchar();
    return 0;    
}
