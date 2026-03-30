#include <iostream>
using namespace std;

int main(){
    int n=6;
    bool is_prime=true;
    if(n<=1){
        is_prime=false;
    }
    else{
        for(int i=2;i<=n-1;i++){
            if(n%i==0){
                is_prime=false;
                break;
            }
        }
    }
    if(is_prime){
        cout<<n<<" is a prime number"<<endl;
    }
    else{
        cout<<n<<" is not a prime number"<<endl;
    }
}