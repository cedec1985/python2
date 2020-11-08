#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <cstdlib> // voir lignes 50 et suivantes
#include <cstdio>
#include <ctime>//voir ligne 61
#include <algorithm>
using namespace std;

int main(){
    int i =5;
    float f;
    char s[80];
cout<<"entrer une valeur entière:"<<endl;
cin>>i;
cout<<"entrer une valeur flottante:"<<endl;
cin>>f;
cout<<"entrer un nom:"<<endl;
cin>>s;
cout<<"vous avez entré:"<<endl;
cout<<"entier"<<i<<'\n'<<"float"<<f<<endl;
cout<<"nom"<<s<<endl;
for(int j=0;j<5;j++){
    for (int i=0; i<10;i++)
        cout<<setw(3)<<rand()%100;
    cout<<endl;
}
for(int j=0;j<5;j++)
    for (int i=0;i<10;i++)
{
    cout<<setw(4)<<setiosflags(ios::left)<<setfill('.');
    cout<<rand()%100;
}
    cout<<endl;
cout<<setiosflags(ios::showpoint);
cout<<setiosflags(ios::showbase);
for (int i=0;i<10;i++){
    float f=rand()%10;
    cout<<f<<endl;
}
cout<<setiosflags(ios::showpos);
for (int i=0; i<10;i++){
    cout<<rand()%100<<endl;
}
printf("estbngiuzqgjn\nvkjd1234567890");
int test=0;
printf("%d",50);
printf("%d",test);
printf("val1=%d, val2=%c, val3=%d, val4=%f",66,66,231,30.333);
printf("test=%.2f\n",1.234567);
printf("[%4d][%-4d]\n",10,20);
printf("[%5.2f][%-5.2s]\n",1.567,"2.896");
char maChaine[256];
int val=50;
sprintf(maChaine, "%d\n", val);
printf("%s",maChaine);
snprintf(maChaine,256,"%d\n", val);
printf("%s",maChaine);
int rec;
scanf("%d",&rec);
srand(time(NULL));
int arr=345;
int brr=678;
printf("arr:%d,brr:%d\n,arr,brr");
printf("brr:%d,brr:%d\n,arr,brr");
enum Dir{NORD, EST, SUD,OUEST};
const int TX = 20;
const float M = 5.77f;
enum Dir d;
d = NORD;
#define TX 80 //remplacé par const int TX = 80
int g;
int k;
double m;
char c;
printf("taille en mémoire de g :%d\n",sizeof(g));
printf("taille en mémoire de k :%d\n",sizeof(k));
printf("taille en mémoire de m :%d\n",sizeof(m));
printf("taille en mémoire de c :%d\n",sizeof(c));
long long l;
unsigned long long p;
cout<<sizeof(l)<<sizeof(p)<<endl;
wchar_t e = 'a';
cout<<sizeof(e)<<":"<<e<<endl;
wchar_t es[]=L"012345678"; //L=16 bits
char*ptr = (char*)es; //chaîne = nombre d'octets
for (int i=0;i<18;i++)// 9 caractères 16 bits = 18 octets
cout<<*(ptr+i);
cout<<endl;
struct testif {int x,y;};
testif t1;
auto t = t1;
t.x=1;
t.y=2;
do {
 int sum = t.x+t.y;
 cin>>t.x>>t.y;
 cout<<sum<<endl;}
while (t.x < t.y);
// Get the array
    int array[] = { 1, 45, 54, 71, 76, 12 };

    // Compute the sizes
    int n = sizeof(array) / sizeof(array[0]);

    // Print the array
    cout << "Array: ";
    for (int i = 0; i < n; i++)
        cout << array[i] << " ";

    // Reverse the array
    reverse(array, array + n);

    // Print the reversed array
    cout << "\nReversed Array: ";
    for (int i = 0; i < n; i++)
        cout << array[i] << " "<<endl;
int array_2 =[];
array_2.append(6,2,5,4,5);



//#define NORD  0
//#define EST   1
//...
//remplacé par enum Dir{NORD,EST,...}
enum gir {sORD,fST};
gir di;
di = gir::sORD;
string prefix("->"), middle(), suffix("<-");
cout << "Test: " << prefix << middle << suffix <<endl;


return 0;

}