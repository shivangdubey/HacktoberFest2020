#include <iostream>
using namespace std;

class shape
{
  protected:
    float x, y,area;
  public:
    void set_value(float i, float j=0)
    {
      x = i;
      y = j;
    }
    virtual void show()
    {

    }
} ;

  class triangle : public shape
  {
    public:
      void show()
      {
      area=0.5*x*y;
      cout<<"Area of the triangle : "<<area<<" unit"<<endl;
      }
  };

  class square : public shape
  {
    public:
        void show()
        {
        area=x*x;
        cout<<"Area of the square : "<<area<<" unit"<<endl;
        }

  };

  class circle : public shape
{
  public:
      void show()
      {
      area=3.14*x*x;
      cout<<"Area of the circle : "<<area<<" unit"<<endl;
      }

} ;

int main()
{
shape *p;
triangle t;
square s;
circle c;
float b,h,a,r;
cout<<"Enter the radius of the circle : \n\n";
cin>>r;
p = &c;
p->set_value(r);
p->show();

cout<<"Enter the base and height of the triangle : \n";
cin>>b>>h;
p = &t;
p->set_value(b,h);
p->show();

cout<<"Enter the side of the square : \n\n";
cin>>a;
p = &s;
p->set_value(a);
p->show();
return 0;
}
