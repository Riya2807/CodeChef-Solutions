#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int n;
	while(t--){
	    cin>>n;
	    char result[n][n];
	    for(int i=0;i<n;i++){
	        for(int j=0;j<n;j++){
	            result[i][j]='.';
	        }
	    }
	    result[n-2][1]='Q';
	    int x=3;
	    for(int i=n-4;i>=0;i--){
	        result[i][x++]='Q';
	    }
	    
	    for(int i=0;i<n;i++){
	        for(int j=0; j<n; j++){
	            cout<<result[i][j];
	        }
	        cout<<endl;
	    }
	}
	return 0;
}
