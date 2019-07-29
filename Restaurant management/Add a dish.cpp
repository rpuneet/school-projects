#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;
class food{
	private:
		float price;
		char f_name[50];
		int f_code;
	public:
		food(){
			price=0;
			f_code=0;
		}
		float getprice(){
	        return (price);
	    }
	    void input(){
	    	cout<<"\nEnter food name:";
	        gets(f_name);
	    	cout<<"Enter Price:";
	    	cin>>price;
	    	cout<<"Enter food code:";
	    	cin>>f_code;
		}
	    void display(){
	    	cout<<f_code<<"\t";
	    	cout<<price<<"\t";
	    	puts(f_name);
		}
        void copy(food ob){
        	price=ob.price;
        	strcpy(f_name,ob.f_name);
        	f_code=ob.f_code;
		}
};
int main(){
	food f;
	fstream file;
	
	file.open("Menu.txt",ios::out | ios::app);
	f.input();
	file.write((char*)&f,sizeof(f));
	file.close();
}
