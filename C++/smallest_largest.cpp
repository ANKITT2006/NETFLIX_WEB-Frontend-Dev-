#include <iostream>
using namespace std;
int main(){
int marks[5]={15,5,10,16,2};
int size=5;
int smallest=INT_MAX;
int largest=INT_MIN;
int smallest_index=-1;
int largest_index=-1;
for(int i=0;i<=size-1;i++){
    smallest=min(marks[i],smallest);
    smallest_index=i;
    largest=max(marks[i],largest);
    largest_index=i;

}
cout<<"smallest number:"<<smallest <<"at index"<< smallest_index <<endl;
cout<<"largest number:"<<largest << "at index"<< largest_index<<endl;
    return 0;
}