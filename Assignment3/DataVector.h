#ifndef DATAVECTOR_H
#define DATAVECTOR_H
#include<iostream>
#include<vector>

/*
this is the class defined for a Vector in multi dimensional space.
It has a Private member variable v to store the vector.
There are 14 member functions intoto.
1)DataVector(int dimension=0):-
     Constructor that optionally takes the dimension of the vector.
2)~DataVector():-
     Destructor to release any allocated resources to v.
3)DataVector(const DataVector& other):-
     Copy constructor to create a new instance by copying another DataVector other into v.
4)DataVector & operator=(const DataVector &other):-
     Assignment operator to assign the values of other DataVector to this instance.
5)DataVector operator+(const DataVector& other):-
     Overloaded addition operator for vector addition.
     This function add the respective coordinates of the other and this vector.
6)DataVector operator-(const DataVector& other):-
     Overloaded subtraction operator for vector addition.
     This function subtract the respective coordinates of the other and this vector.
7)double operator*(const DataVector& other):-
     Overloaded dot product operator for vector multiplication.
     Thsi function givess the dot product of the other and this vector.
8)double norm():-
     Calculate the Euclidean norm of the vector using the operator * on this and this.
9)double dist(const DataVector& other) const;
     Calculate the Euclidean distance between this vector and other vector.
     This function uses operator- and norm in it.
10)double getElement(int index):-
     Get the element at a specific index in the vector.
11)void pushElement(double value):-
     push the element in this vector.
12)int getDimension():-
     Get the dimension of this vector.
13)int pri();
     Print all the elements of the this vector.
14)void setDimension(int dimension = 0);
     Set the dimension of the vector.
*/
class DataVector{
     std::vector<double> v;
     public:
     DataVector(int dimension=0);
     ~DataVector();
     DataVector(const DataVector& other);
     DataVector & operator=(const DataVector &other);
     void setDimension(int dimension=0);
     DataVector operator+(const DataVector &other);
     DataVector operator-(const DataVector &other) const;
     double operator*(const DataVector &other);
     double norm();
     int pri();
     double dist(const DataVector &other) const;
     double getElement(int index); 
     void pushElement(double value); 
     int getDimension(); 
};

#endif