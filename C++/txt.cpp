#include <iostream>
using namespace std;
int bin_dec(int num){
  int ans=0;
  int pow=1;
  while(num>0){
    int digit=num%10;
    num=num/10;
    ans+=digit*pow;
    pow*=2;
  }
  return ans;
}
int main(){
  int ans;
  
  ans=bin_dec(101);
  cout<<ans<<endl;
  return 0;


}