#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

long long int ways(int x,int *c,int m)
{  
    long long int dp[x+1];
    for(int i=0;i<=x;i++)
        dp[i]=0;
    dp[0]=1;
    for(int i=0;i<m;i++)
        for(int j=c[i];j<=x;j++)
            dp[j]+=dp[j-c[i]];
    return dp[x];
}

int main() {
     int n; 
     int m; 
    scanf("%d %d", &n, &m);
     int *c = malloc(sizeof(int) * (m+1));
    for(int c_i = 0; c_i < m; c_i++){
       scanf("%d",&c[c_i]);
    }
    // Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    long long int count = ways(n,c,m);
    printf("%lld",count);
    return 0;
}