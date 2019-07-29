#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
#include<dos.h>
#include<fstream>
#include<ctime>
using namespace std;

void initialise();

# define REST_NAME "HARD ROCK CAFE AND RESTAURANT"
# define PASSWORD "HARDROCK"

time_t now = time(0);
tm* str_time=localtime(&now);
void default_disp(int opt=0)
{   
    now= time(0);
	char *loc_time=ctime(&now);
	cout<<"\n";
	puts(loc_time);
    cout<<"\n\n\t\t       "<<REST_NAME;
    cout<<"\n\n\n\n";
    if(opt==1)
	{
    	cout<<"\tMENU :\n";
	}
}


int theme(int opt=0,const char *A=NULL,const char *B=NULL,const char *C=NULL,const char *D=NULL,const char *E=NULL,const char *F=NULL,const char *G=NULL,const char *H=NULL,const char *I=NULL,const char *J=NULL)
{   
    const char *List[11]={"\0",A,B,C,D,E,F,G,H,I,J};
    char ch;
	int pointer=1;
	int MAX=11;
	for(int k=1;k<MAX;k++)
	{
		if(List[k]==NULL)
		{
		    MAX=k;
			break;
		 }
	}
	while(1)
	{
	    system("cls");
	    default_disp(opt);
	    for(int i=1;i<MAX;i++)
        {
    	    if(i==pointer)
    	        cout<<"\t\t\t->"<<i<<".   "<<List[i]<<"\n";
    	    else
    	        cout<<"\t\t\t  "<<i<<".   "<<List[i]<<"\n";
	    }


		ch=getch();
		if(int(ch)<0)
		{
			ch=getch();
		}
		int flag=int(ch);
		switch(flag)
		{
			case 72:if(pointer>1) 
			            pointer--;
			        else 
					    pointer=MAX-1;
			        break;

			case 80:if(pointer<MAX-1) 
			            pointer++;
			        else 
					    pointer=1;
			        break;

			case 13:return(pointer);
		}
	}
}



struct customer
{
	char name[50],checkin_time[10],checkout_time[10];
	double totalbill;
};






class food
{
	private:
		float price;
		char f_name[50];
	    int f_code;
	public:
		food()
		{
			price=0;
			f_code=0;
		}
		float getprice()
		{
	        return (price);
	    }
	    int getf_code()
		{
	    	return f_code;
		}
	    void input()
		{
	    	cout<<"\nEnter food name:";
	        gets(f_name);
	    	cout<<"Enter Price:";
	    	cin>>price;
	    	cout<<"Enter food code:";
	    	cin>>f_code;
		}
	    void display()
		{
	    	cout<<f_code<<"\t";
	    	cout<<price<<"\t";
	    	puts(f_name);
		}
        void copy(food ob)
		{
        	price=ob.price;
        	strcpy(f_name,ob.f_name);
        	f_code=ob.f_code;
		}
} FNULL;

class table
{
	private:
		char status;//v for vacant o for occupied
		int no_of_seats;
		struct order
		{
			food f;
			order *next;
		} *orders;
		double bill;
        int tableno;
	public:
		double calc_bill();
		double totalbill;
		char name[50];
		char checkin_time[10];
		char checkout_time[10];
		table(int seats=2)
		{
			 bill=0.0;
			 status = 'v';
			 no_of_seats=seats;
			 tableno=-1;
			 orders=new order;
			 orders=NULL;
		}
		void deinitialise()
		{
			bill=0.0;
			status='v';
			orders=NULL;
			strcpy(name,"");
		}
		int isvacant()
		{
			int r = ((status=='v')?1:0);
			return (r);
		}
		void allot()
		{
			
			now = time(0);
            str_time=localtime(&now);
			
			cout<<"Customer Name:";
			cin>>name;
			status='o';
			int h,m,s;
			char temp[10];
			h=str_time->tm_hour;
			m=str_time->tm_min;
			s=str_time->tm_sec;
			itoa(h,checkin_time,10);
			strcat(checkin_time,":");
			itoa(m,temp,10);
			strcat(checkin_time,temp);
			strcat(checkin_time,":");
			itoa(s,temp,10);
			strcat(checkin_time,temp);
		}
		void seats(int s)
		{
			no_of_seats=s;
		}
		int getseats()
		{
			return no_of_seats;
		}
		void settableno(int n)
		{
			tableno=n;
		}
		int gettableno()
		{
			return tableno;
		}
		void put_details(customer *c)
		{
			strcpy(c->name,name);
			strcpy(c->checkin_time,checkin_time);
			strcpy(c->checkout_time,checkout_time);
	        c->totalbill=totalbill;
		}
		void write_on_file(customer c);
		void place_order(food o);
		void check_order();
		void show_bill(int);

};

double table::calc_bill()
{
	bill=0.0;
	order *temp;
	temp=orders;
	while(temp!=NULL)
	{
		bill+=temp->f.getprice();
		temp=temp->next;
	}
	return  bill;
}

void table::place_order(food o)
{
	order *temp,*ptr;
	temp=new order;
	ptr=new order;
	temp->f.copy(o);
	temp->next = NULL;
	if(orders==NULL)
	{
	    orders=temp;
	}
	else
	{
	    ptr =orders;
	    while(ptr->next!=NULL)
	        
	        ptr=ptr->next;
	    ptr->next=temp;
    }
}

void table::check_order()
{
	order *temp;
	temp=new order;
	temp=orders;
	while(temp!=NULL)
	{
		temp->f.display();
		temp=temp->next;
	}
	cout<<"\n";
}

void table::show_bill(int tn)
{
	calc_bill();
	system("cls");
	default_disp();
	cout<<"\n\n\n\t\t";
	cout<<"NAME:";
	puts(name);
	cout<<"\n\n\t\tTABLE NUMBER:"<<tn<<"\n\nS. No. Price     Item\n\n";
	check_order();
	cout<<"\nBill:              "<<bill;
	cout<<"\nVAT(14.5%):        "<<bill*14.5/100;
	cout<<"\nService Tax(5.8%): "<<bill*5.8/100;
	totalbill=bill*120.3/100;
	cout<<"\n\nTotal Bill:        "<<totalbill;
	
	
	
	now = time(0);
    str_time=localtime(&now);
	int h,m,s;
	char temp[10];
	h=str_time->tm_hour;
	m=str_time->tm_min;
	s=str_time->tm_sec;
	itoa(h,checkout_time,10);
	strcat(checkout_time,":");
	itoa(m,temp,10);
	strcat(checkout_time,temp);
	strcat(checkout_time,":");
	itoa(s,temp,10);
	strcat(checkout_time,temp);

    customer c;
    put_details(&c);
    write_on_file(c);
    
	deinitialise();
}

////////////  format of date  dd/mm/yyyy  /////////////

void table::write_on_file(customer c)
{
	now = time(0);
    str_time=localtime(&now);
    char temp;
	int flag2=1; 
	
	
	int y,m,d;
	char tmp[20],temp2[20],today[20];
	y=1900+str_time->tm_year;
	m=str_time->tm_mon+1;
	d=str_time->tm_mday;
	itoa(d,today,10);
	strcat(today,".");
	itoa(m,tmp,10);
	strcat(today,tmp);
	strcat(today,".");
	itoa(y,tmp,10);
	strcat(today,tmp);


	fstream fileindex,file;
	fileindex.open("FILEINDEX.TXT",ios::in | ios::app);
	while(!fileindex.eof())
	{
		fileindex>>temp2;
		if(strcmp(today,temp2)==0)
		{
			flag2=0;
			break;
		}
	}
	fileindex.close();
	if(flag2)
	{
		fileindex.open("FILEINDEX.TXT",ios::out | ios::app);
		fileindex<<today;
		fileindex<<" ";
		fileindex.close();
	}
	
	file.open(today,ios::out | ios::app);
	file.write((char*)&c,sizeof(c));;
}



int menu_theme(table t,int opt=1,food A=FNULL,food B=FNULL,food C=FNULL,food D=FNULL,food E=FNULL,food F=FNULL,food G=FNULL,food H=FNULL,food I=FNULL,food J=FNULL)
{   
    food fList[11]={FNULL,A,B,C,D,E,F,G,H,I};
    char ch;
	int pointer=1;
	int MAX=11;
	for(int k=1;k<MAX;k++)
	{
		if(fList[k].getprice()==0)
		{
		    MAX=k;
			break;
		 }
	}
	while(1)
	{
	    system("cls");
	    default_disp(opt);
	    cout<<"\n\t\t        S. No. Price     Item\n\n";
	    for(int i=1;i<MAX;i++)
        {
    	    if(i==pointer)
			{
    	        cout<<"\t\t\t->";
    	        fList[i].display();
    	   }
			else
    	    {
		        cout<<"\t\t\t  ";
    	        fList[i].display();
	        }
		}
		cout<<"\n\nPRESS SPACEBAR TO CONFIRM ORDER.";
		
		cout<<"\n\n\nYOUR ORDER:\n";
		t.check_order();


		ch=getch();
		if(int(ch)<0)
		{
			ch=getch();
		}
		int flag=int(ch);
		switch(flag)
		{
			case 72:if(pointer>1) 
			            pointer--;
			        else 
					    pointer=MAX-1;
			        break;

			case 80:if(pointer<MAX-1) 
			            pointer++;
			        else 
					    pointer=1;
			        break;
			        
			case 77:return(-2);//->
			        break;
			        
			case 75:return(-1);//<-
			        break;
            
            case 32:return(-3);//SPACEBAR
			        break;
			        
			case 13:return(fList[pointer].getf_code());
		}
	}
}




int value_for_k(int a,int choice,int i)
	{
		if(choice==-1 && a!=0)
			return(a-8);
		else if(choice==-2 && a<=i) 
		    return (a+8);
		else 
		    return(a);
		
	}
	
void menu(table &t)
{
	int i;
	int choice=0;
	food menu_item[50],temp;
	fstream menufile("Menu.txt",ios::in);
	for(i=0;!menufile.eof();i++)
	{
		menufile.read((char*)&temp,sizeof(temp));
		menu_item[i]=temp;
	}
	i--;
	menu_item[i]=FNULL;
	for(int k=0;choice!=-3;k=value_for_k(k,choice,i))
	{
		choice=menu_theme(t,1,menu_item[k],menu_item[k+1],menu_item[k+2],menu_item[k+3],menu_item[k+4],menu_item[k+5],menu_item[k+6],menu_item[k+7]);
		if(choice>0 && choice<1000)
		{
		    for(int m=0;m<i;m++)
			{
			    if(menu_item[m].getf_code()==choice)
				{
			    	t.place_order(menu_item[m]);
				}
		    }
	    }
	}
	
	
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void password()
{
	int f=0;
	start:
	system("cls");
	default_disp();
	cout<<"\n\n\t\t"<<(char)2<<"  WELCOME TO RESTAURANT MANAGEMENT SYSTEM  "<<(char)2;
	if(f) 
	    cout<<"\n\n\t\t\tWRONG PASSWORD";
	else 
	    cout<<"\n\n";
	cout<<"\n\n\n\n\n\t\t\tENTER PASSWORD : ";
	char inpt_pass[25],ch=0;
	int i=0;
	for(int j=0;j<25;j++)
	    inpt_pass[j]=0;
	do
	{  
		ch=getch();
		if(ch==8) goto start;
		else if(ch==13) continue;
		cout<<"*";
		inpt_pass[i]=ch;
		i++;
		
	}while(ch!=13);
	
	if(strcmp(inpt_pass,PASSWORD)==0) 
	    return;
	else
	{
		f=1;
		goto start;
	}
	    
}

/**************************************************************************************************************
************************************************  MAIN  *******************************************************
**************************************************************************************************************/

int main()
{
	password();
	
/************************************ INITIALISE  ***********************************************/

table table_array[20], *current_table;
current_table=new table;
int t,flag=0;
for(t=0;t<20;t++)
{
	table_array[t].settableno(t);
	if(t>=0 && t<5)  table_array[t].seats(2);
	else if(t>4 && t<15) table_array[t].seats(4);
    else table_array[t].seats(6);
}
int noofpeople,curtableno;

/////////////////////////

int flag3=0;
fstream fileindex,file;
int i=1;
customer c1;
double total_earning=0;

/////////////////////////////////////////////////////////////////////////////////////////////////////////
do
{ 
    int menu2;
    int menu1=theme(0,"Check In","Place Order","Check Out","Accounts","Exit");
	switch(menu1)
	{
		case 1: /* Check In */
		    flag=0;
		    system("cls");
		    default_disp();
            cout<<"\n\nNumber of people:";
            cin>>noofpeople;
			for(t=0;t<20;t++)
			{
		        if(table_array[t].isvacant() && table_array[t].getseats()>=noofpeople)
				{
		        	current_table=&table_array[t];
		        	flag=1;
		        	break;
				}
			}
			if(flag==0)
			{
			    cout<<"\n\n\t\t NO VACANCY.PLEASE WAIT FOR A WHILE";
			    getch();
			    break;
		    }
		    cout<<"\n";
		    current_table->allot();
		    cout<<"\nTABLE NUMBER:"<<current_table->gettableno();
		    cout<<"\n\n\t\tPRESS ANY KEY TO GO BACK.";
		    getch();
			break;
			
			
		case 2:/*Place order*/
		    system("cls");
		    default_disp();
		    flag=0;
		    cout<<"\n\nENTER TABLE NUMBER:";
		    cin>>curtableno;
		    if (curtableno>=20)
			{
		    	cout<<"\n\n\t\tTABLE DOES NOT EXIST";
				getch();
				break;
			}
		    for(t=0;t<20;t++)
			{
		    	if(table_array[t].gettableno()==curtableno && !table_array[t].isvacant())
				{
		    		current_table=&table_array[t];
		        	flag=1;
		        	break;
				}
		    }
			if(flag==0)
			{
				cout<<"\n\n\t\tTABLE IS VACANT";
				getch();
				break;
			}
			
			system("cls");
		    default_disp();
			menu(table_array[t]);
			system("cls");
			default_disp();
			cout<<"\n\nORDER SUMMARY:\n\nS. No. Price     Item\n\n";
			table_array[t].check_order();
			cout<<"\n\n\t\tPRESS ANY KEY TO CONTINUE.";
			getch();
			break;
			
		case 3:/*CHECK OUT*/
		    system("cls");
		    default_disp();
		    flag=0;
		    cout<<"\n\nENTER TABLE NUMBER:";
		    cin>>curtableno;
		    for(t=0;t<20;t++)
			{
		    	if(table_array[t].gettableno()==curtableno && !table_array[t].isvacant())
				{
		    		current_table=&table_array[t];
		        	flag=1;
		        	break;
				}
		    }
			if(flag==0)
			{
				cout<<"\n\n\t\tTABLE IS VACANT";
				getch();
				break;
			}
			system("cls");
		    default_disp();
			current_table->show_bill(curtableno);
			cout<<"\n\n\t\tPRESS ANY KEY TO CONTINUE.";
			getch();
			break;
			
			
		case 4:/*Accounts*/
		    menu2=theme(0,"History","Current Status","Back");
		    switch(menu2)
			{
		    	case 1:
		    		system("cls");
		            default_disp();
		            char date[20],temp3[20];
		    		cout<<"\n\nEnter Date.(dd.mm.yyyy):";
		    		cin>>date;
		    		/*int flag3;
		    		fstream fileindex,file;*/
	                fileindex.open("FILEINDEX.TXT",ios::in);
	                while(!fileindex.eof())
					{
	                	fileindex>>temp3;
                   		if(strcmp(date,temp3)==0)
						{
	                		flag3=1;
	                		break;
	                	}
                   	}
	                fileindex.close();
	                if(!flag3)
					{
	                	cout<<"\n\n\t\t\tNO RECORD PRESENT.";
	                	getch();
	                	break;
					}
					else
					    system("cls");
					    default_disp();
					    i=1;
					    cout<<"\tDATED : "<<date;
					    cout<<"\n\nS.No       Name       Check In Time      Check Out Time        Total Bill\n";
					    file.open(date,ios::in);
					    total_earning=0;
					/*   int i=1;
					    customer c1;
					    double total_earning=0;*/
					    while(file.read((char*)&c1,sizeof(c1)))
						{
					    	total_earning+=c1.totalbill;
					    	char final_string[100];
					    	
							itoa(i,final_string,10);
					    	if(i<10)
							    strcat(final_string,"   ");
							else if(i<100)
							    strcat(final_string,"  ");
					    	else if(i<1000)
							    strcat(final_string," ");
							else
							    strcat(final_string,"");
							    
					    	
					    	int l=strlen(c1.name),nmspace,f=0;
					    	nmspace=(18-l);
					    	if(nmspace%2!=0) f=1 ;
					    	nmspace/=2;
					    	for(int k=0;k<nmspace;k++) 
					    	    strcat(final_string," ");
					    	strcat(final_string,c1.name);
					    	for(int k=0;k<nmspace;k++) 
					    	    strcat(final_string," ");
					    	if(f) strcat(final_string," ");
					    	
					    	
					    	l=strlen(c1.checkin_time),nmspace,f=0;
					    	nmspace=(13-l);
					    	if(nmspace%2!=0) f=1 ;
					    	nmspace/=2;
					    	for(int k=0;k<nmspace;k++) 
					    	    strcat(final_string," ");
					    	strcat(final_string,c1.checkin_time);
					    	for(int k=0;k<nmspace;k++) 
					    	    strcat(final_string," ");
					    	if(f) strcat(final_string," ");
					    	
					    	
					    	strcat(final_string,"      ");
					    	
					    	l=strlen(c1.checkout_time),nmspace,f=0;
					    	nmspace=(14-l);
					    	if(nmspace%2!=0) f=1 ;
					    	nmspace/=2;
					    	for(int k=0;k<nmspace;k++) 
					    	    strcat(final_string," ");
					    	strcat(final_string,c1.checkout_time);
					    	for(int k=0;k<nmspace;k++) 
					    	    strcat(final_string," ");
					    	if(f) strcat(final_string," ");
					    
					        strcat(final_string,"          ");
					    	char billstr[20];
					    	itoa(c1.totalbill,billstr,10);
					    	strcat(final_string,billstr);
					    	cout<<"\n"<<final_string;
					    	i++;
						}
						cout<<"\n\n\t\tTotal Earnings:"<<total_earning;
						file.close();
						getch();
		    		
					break;
		    		
		    		
		    	case 2:
		    		system("cls");
		            default_disp();
		             for(t=0;t<20;t++)
					 {
		    	
		            	cout<<"\n\nTABLE NUMBER : "<<t;
		    	        if(table_array[t].isvacant())
						{
		    		        cout<<"\n\n\tVACANT.";
				        }
				        else
						{
				            cout<<"\n\tNAME : "<<table_array[t].name;
				            cout<<"\n\tCURRENT BILL : "<<table_array[t].calc_bill();
				        }
		                if(t%6==0 &&t!=0)
						{
				            getch();
		                    getch();
		                }
			        }
			        cout<<"\n\n\t\tPRESS ANY KEY.";
			        getch();
			        break;
			    case 3:
			    	break;
			}
		    break;
		case 5: exit(1);
	}
}while(1);
	
	return 0;

}
