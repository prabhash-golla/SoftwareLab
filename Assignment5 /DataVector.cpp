#include<iostream>
#include<vector>
#include<cmath>
#include "DataVector.h"
using namespace std;

//Constructor that optionally takes the dimension of the vector.
DataVector::DataVector(int dimension)
{
    // cout << "DataVector has been constructed\n";
    if(dimension==0)
        v={};
    else
        v.resize(dimension);
}


// Destructor to release any allocated resources to v.
DataVector::~DataVector()
{
    // cout << "DataVector has been destructed\n";
}

//Copy constructor to create a new instance by copying another DataVector other into v.
DataVector::DataVector(const DataVector& other)
{
    // cout << "DataVector has been constructed\n";
    v=other.v;
}

bool DataVector :: operator==(const DataVector& other) const
{
    if(v.size()!=other.v.size())
    {
        return false;
    }
    else
    {
        for(int i=0;i<v.size();i++)
        {
            if(v[i]!=other.v[i])
            {
                return false;
            }
        }
        return true;
    }
}
// Assignment operator to assign the values of other DataVector to this instance.
DataVector& DataVector:: operator=(const DataVector &other)
{
    v.resize(other.v.size());
    for(int i=0;i<v.size();i++)
    {
        v[i]=other.v[i];
    }
    return *this;
}

// Overloaded addition operator for vector addition.
// This function add the respective coordinates of the other and this vector.
DataVector DataVector:: operator+(const DataVector &other)
{
    if(v.size()==other.v.size())
    {
        DataVector newvec(v.size());
        for(int i=0;i<v.size();i++)
        {
            newvec.v[i]=v[i]+other.v[i];
        }
        return newvec;
    }
    else
    {
        cerr << "The size of vectors are not equal";
        return DataVector();
    }
}

// Overloaded subtraction operator for vector addition.
// This function subtract the respective coordinates of the other and this vector.
DataVector DataVector:: operator-(const DataVector &other) const
{
    if(v.size()==other.v.size())
    {
        DataVector newvec(v.size());
        for(int i=0;i<v.size();i++)
        {
            newvec.v[i]=v[i]-other.v[i];
        }
        return newvec;
    }
    else
    {
        cerr << "The size of vectors are not equal";
        return DataVector();
    }
}

// Overloaded dot product operator for vector multiplication.
// Thsi function givess the dot product of the other and this vector.
double DataVector:: operator*(const DataVector &other)
{
    if(v.size()==other.v.size())
    {
        double dotproduct=0;
        for(int i=0;i<v.size();i++)
        {
            dotproduct=dotproduct+v[i]*other.v[i];
        }
        return dotproduct;
    }
    else
    {
        cerr << "The size of vectors are not equal";
        return 0;
    }
}

// Calculate the Euclidean norm of the vector using the operator * on this and this.
double DataVector::norm()
{
    return sqrt((*this) * (*this));
}

// Calculate the Euclidean distance between this vector and other vector.
// This function uses operator- and norm in it.
double DataVector::dist(const DataVector &other) const
{
    if (v.size() == other.v.size()) 
    {
        DataVector diff = *this - other;
        return diff.norm();
    } 
    else 
    {
        cerr << "The size of vectors are not equal";
        return 0;
    }
}

// Get the element at a specific index in the vector.
double DataVector::getElement(int index) 
{
    if (index >= 0 && index < v.size()) {
        return v[index];
    } else {
        cerr << "Invalid index for getElement()" << endl;
        return 0.0; // or some default value
    }
}

// push the element in this vector.
void DataVector::pushElement(double value) 
{
    v.push_back(value);
}

// Get the dimension of this vector.
int DataVector::getDimension()
{
    return v.size();
}

// Print all the elements of the this vector.
int DataVector::pri()
{
    for(int j=0;j<v.size();j++)
    {
       cout << v[j] << " ";
    }
    cout << endl;
    return 0;
}

// Set the dimension of the vector.
void DataVector::setDimension(int dimension)
{
    v.resize(dimension);
    return;
}