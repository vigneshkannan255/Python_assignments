/*This problem was asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number. N lies in the range: [1, 1000].
For example, given 1, you should return 19. Given 2, you should return 28.*/
#include<bits/stdc++.h>
using namespace std;
int main() {

	// Write your code here
    int n,n1,sum=0,d=0,re=0,c=0;
    cin>>n;
    for(int i=18;i<=100036;i++){
        n1=i;
    while(n1>0)
    {
        d=n1%10;
        sum+=d;
        n1=n1/10;
    }
        if(sum==10)
            c++;
            re=i;
        if(c==n)
            break;
        sum=0;
    }
    printf("%d",re);
    return 0;
        
}
