#include<iostream.h>
#include<conio.h>
class stu{ //First base Class//
	int id;
	char name[20];
	public: //If not declared, data members are by default defined as private//

	void getstu(){
		cout << "Enter stuid, name";
		cin >> id >> name;
	}
};

class marks: public stu{//derived class//
	protected: //without this command, data members will not be available next//
	int m, p, c;// without ‘protected:’ command, m1, m2, & m3 are private members//
	public:
	void getmarks(){
		cout << "Enter 3 subject marks:";
		cin >> m >> p >> c;
	}
};

class sports{//Second base class//
	protected:
	int spmarks;
	public:
	void getsports(){
		cout << "Enter sports marks:";
		cin >> spmarks;
	}
};

class result : public marks, public sports{//Derived class by hybrid inheritance//
	int tot;
	float avg;
	public :
	void show(){}
		tot=m+p+c;
		avg=tot/3.0;
		cout << "Total=" << tot << endl;
		cout << "Average=" << avg << endl;
		cout << "Average + Sports marks =" << avg+spmarks;
	}
};

void main(){
	result r;//object//
	r.getstu();
	r.getmarks();
	r.getsports();
	r.show();
	getch();
};
