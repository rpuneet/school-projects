#include<allegro.h>
BITMAP *buffer;
double curx=20;
double tempx;
double dir[]={1,1};
double x=100,y=100,ball_tx,ball_ty;
double pl2lx=0,pl2ly=8,pl2rx=80,pl2ry=18,tlx,trx;
int pl1scr=0,pl2scr=0;
int flag;
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////   MENU  /////////////////////////////////////////////////////////////////////////////

void menu(){
	clear_keybuf();
	textout_ex(buffer,font,".. vs PLAYER ..",248,220,makecol(0,255,255),makecol(255,255,255));
	textout_ex(buffer,font,".. vs COMPUTER ..",245,200,makecol(0,255,0),makecol(255,255,255));
	flag=0;//vs computer
	draw_sprite(screen,buffer,0,0);
	while(!key[KEY_ENTER]){
		clear_keybuf();
		readkey();
		if(key[KEY_UP] || key[KEY_DOWN]){
			if(flag==0){
				textout_ex(buffer,font,".. vs PLAYER ..",248,220,makecol(0,255,0),makecol(255,255,255));
	            textout_ex(buffer,font,".. vs COMPUTER ..",245,200,makecol(0,255,255),makecol(255,255,255));	
			    flag=1;
			}
			else if(flag==1){
				textout_ex(buffer,font,".. vs PLAYER ..",248,220,makecol(0,255,255),makecol(255,255,255));
	            textout_ex(buffer,font,".. vs COMPUTER ..",245,200,makecol(0,255,0),makecol(255,255,255));	
			    flag=0;
			}
			
		}
	    draw_sprite(screen,buffer,0,0);	
	}
	textout_ex(buffer,font,"                    ",248,220,makecol(0,0,0),makecol(255,255,255));
	textout_ex(buffer,font,"                     ",245,200,makecol(0,0,0),makecol(255,255,255));
	clear_keybuf();
}
////////////////////////////////////////////////////////////////  BALL  /////////////////////////////////////////////////////////////////
void rebound(){
	
	if(x<5) dir[1]+=(dir[1]*-2);
	if(x>635)  dir[1]-=(dir[1]*2);
	if (y<5)  dir[0]+=2;
	if (y>475) dir[0]-=2;
}
void move(){
	ball_tx=x;
	ball_ty=y;
	if(x<5 || y<5 || x>635 || y>475){
		rebound();
	}
	else if(x>curx-40 && x<curx+40 && y==460){
		dir[0]=-1;
		dir[1]=(x-curx)/40;
	}
	else if(x>pl2lx && x<pl2rx && y==23 ){
		double t=(pl2lx+pl2rx)/2;
		dir[0]=1;
		dir[1]=(x-t)/80;
	}
	x+=dir[1];
	y+=dir[0];
	circlefill(buffer,ball_tx,ball_ty,5,makecol(255,255,255));
	circlefill(buffer,x,y,5,makecol(0,0,0));
	//rest(1);
	//draw_sprite(screen,buffer,0,0);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////// PLAYER 2 /////////////////////////////////////////////////////////////////////////////

void pl2(){
	tlx=pl2lx;
	
	trx=pl2rx;
	
	if(key[KEY_RIGHT] && pl2rx<=640){
		++pl2rx;
		++pl2lx;
	}
	else if(key[KEY_LEFT] && pl2lx>=0){
		--pl2rx;
		--pl2lx;
	}
	//acquire_screen();
	rectfill(buffer,tlx,pl2ly,trx,pl2ry,makecol(255,255,255));
	rectfill(buffer,pl2lx,pl2ly,pl2rx,pl2ry,makecol(0,0,255));
	//draw_sprite(screen,buffer,0,0);
	//release_screen();
	
}
///////////////////////////////////////// CPU /////////////////////////////////////////////////////////////////////////////////////////////
void cpu(){
	tlx=pl2lx;
	
	trx=pl2rx;
	
	if(y<360){
		if(pl2lx+10<x){
		       pl2lx++;
		        pl2rx++;
	        }
	    if(pl2rx-10>x){
		       pl2lx--;
		        pl2rx--;
	        }
		}
	//acquire_screen();
	rectfill(buffer,tlx,pl2ly,trx,pl2ry,makecol(255,255,255));
	rectfill(buffer,pl2lx,pl2ly,pl2rx,pl2ry,makecol(0,0,255));
	//draw_sprite(screen,buffer,0,0);
	//release_screen();
	
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////// PLAYER 1 ///////////////////////////////////////////////////////////////////

void get_info(){
	tempx=curx;
	curx=mouse_x;
}

void pl1(){
	get_info();
	rectfill(buffer,tempx-40,465,tempx+40,475,makecol(255,255,255));
	rectfill(buffer,curx-40,465,curx+40,475,makecol(255,0,0));
	//draw_sprite(screen, buffer,0,0);
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////CHECK SCORE/////////////////////////////////////////

void check_score(){
	if(y==475){
	pl2scr++;
	}
	if(y==5){
	pl1scr+=1;
	}
	textout_ex(buffer,font,":",330,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=0)
	    textout_ex(buffer,font,"00",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=1)
	    textout_ex(buffer,font,"01",310,240,makecol(0,0,0),makecol(255,255,255));
    if(pl1scr/2>=2)
	    textout_ex(buffer,font,"02",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=3)
	    textout_ex(buffer,font,"03",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=4)
	    textout_ex(buffer,font,"04",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=5)
	    textout_ex(buffer,font,"05",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=6)
	    textout_ex(buffer,font,"06",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=7)
	    textout_ex(buffer,font,"07",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=8)
	    textout_ex(buffer,font,"08",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=9)
	    textout_ex(buffer,font,"09",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=10)
	    textout_ex(buffer,font,"10",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=11)
	    textout_ex(buffer,font,"11",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=12)
	    textout_ex(buffer,font,"12",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=13)
	    textout_ex(buffer,font,"13",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=14)
	    textout_ex(buffer,font,"14",310,240,makecol(0,0,0),makecol(255,255,255));
	if(pl1scr/2>=15)
	    textout_ex(buffer,font,"15",310,240,makecol(0,0,0),makecol(255,255,255));
	
	if(pl2scr/2>=0)
	    textout_ex(buffer,font,"00",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=1)
	    textout_ex(buffer,font,"01",340,240,makecol(0,0,0),makecol(255,255,255));
    if(pl2scr/2>=2)
	    textout_ex(buffer,font,"02",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=3)
	    textout_ex(buffer,font,"03",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=4)
	    textout_ex(buffer,font,"04",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=5)
	    textout_ex(buffer,font,"05",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=6)
	    textout_ex(buffer,font,"06",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=7)
	    textout_ex(buffer,font,"07",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=8)
	    textout_ex(buffer,font,"08",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=9)
	    textout_ex(buffer,font,"09",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=10)
	    textout_ex(buffer,font,"10",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=11)
	    textout_ex(buffer,font,"11",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=12)
	    textout_ex(buffer,font,"12",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=13)
	    textout_ex(buffer,font,"13",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=14)
	    textout_ex(buffer,font,"14",340,240,makecol(0,0,0),makecol(255,255,255));
	if(pl2scr/2>=15)
	    textout_ex(buffer,font,"15",340,240,makecol(0,0,0),makecol(255,255,255));
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void check_win(){
	if(pl1scr/2==10)
	    textout_ex(buffer,font,"..PLAYER 1 WINS..",260,280,makecol(0,255,0),makecol(255,255,255));
		
	if(pl2scr/2==10)
	    if(flag==1)
	        textout_ex(buffer,font,"..PLAYER 2 WINS..",260,280,makecol(0,255,0),makecol(255,255,255));
	    else if(flag==0)
	        textout_ex(buffer,font,"..COMPUTER WINS..",260,280,makecol(0,255,0),makecol(255,255,255));
}


/******************************************************************************************************************************************************************
*******************************************************************  MAIN *****************************************************************************************
**************************************************************************************************************************************************************/
int main(){
	allegro_init();
	install_mouse();
	install_keyboard();
	set_color_depth(16);
	set_gfx_mode(GFX_AUTODETECT,640,480,0,0);
	
	buffer = create_bitmap(640,480);
	rectfill(buffer,0,0,640,480,makecol(255,255,255));
	draw_sprite(screen,buffer,0,0);
	menu();
	textout_ex(buffer,font,"PRESS SPACEBAR TO START THE GAME",180,240,makecol(0,255,255),makecol(255,255,255));
	draw_sprite(screen,buffer,0,0);
	readkey();
	if(key[KEY_SPACE]){
    textout_ex(buffer,font,"                                    ",180,240,makecol(255,255,255),makecol(255,255,255));
	while(!key[KEY_ESC]){
		
		clear_keybuf();
		pl1();
		move();
		if(flag==1)
		    pl2();
		else if(flag==0)
		    cpu();
		check_score();
		draw_sprite(screen,buffer,0,0);
		check_win();
		draw_sprite(screen,buffer,0,0);
			
		}
}
	return 0;
}
END_OF_MAIN();

