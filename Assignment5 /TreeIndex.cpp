#include "TreeIndex.h"
#include<bits/stdc++.h>
using namespace std;

VectorDataset TreeIndex::Data = VectorDataset(0);
TreeIndex *TreeIndex::instance = NULL;
KDTreeIndex *KDTreeIndex::instance = NULL;
RPTreeIndex *RPTreeIndex::instance = NULL;

void TreeIndex :: assignData(VectorDataset& data)
{
   TreeIndex :: Data=data;
}

void TreeIndex:: assignIndex()
{
    for(int i=0;i<TreeIndex :: Data.getDimension() && i ;i++)
    {
        Set[i]=i;
    }
}

TreeIndex :: TreeIndex()
{
    left = nullptr;
    right = nullptr;
}

TreeIndex :: ~TreeIndex()
{
    if(left) delete left;
    if(right) delete right;
}

// TreeIndex& TreeIndex :: GetInstance()
// {
//     if(!instance) instance = new TreeIndex();
//     return *instance; 
// }

KDTreeIndex :: KDTreeIndex()
{
    
}

KDTreeIndex& KDTreeIndex :: GetInstance()
{
    // static KDTreeIndex& MakeTree();
    if(!instance) instance = new KDTreeIndex();
    return *instance; 
}

RPTreeIndex& RPTreeIndex :: GetInstance()
{
    if(!instance) instance = new RPTreeIndex();
    return *instance;
}

double KDTreeIndex :: ChooseRule(VectorDataset b,int p)
{
    // If size of the arr[] is even 
    int n = b.getDimension();
    vector<int> a;
    for(int i=0;i<n;i++)
    {
        a.push_back(b.getElement(i).getElement(p));
    }
    sort(a.begin(),a.end());
    if (n % 2 == 0) 
    {         
        return (double)(a[n/2 - 1]+ a[n/2])/ 2.0; 
    } 
    // If size of the arr[] is odd 
    else
    { 
        return (double)(a[(n-1)/2])/2.0; 
    } 
}

KDTreeIndex* KDTreeIndex :: MakeTree(int Dimension)
{
    if(Set.size() < 100)
    {
        return this;
    }
    VectorDataset S;
    for(int i=0;i<Set.size();i++)
    {
        S.AddData(TreeIndex :: Data.getElement(Set[i]));
    }    

    for(int i=0;i<S.getElement(0).getDimension();i++)
    {
        if(i!=Dimension)
        unit_vector.pushElement(0);
        else
        unit_vector.pushElement(1);
    }

    KDTreeIndex* Right = new KDTreeIndex();
    KDTreeIndex* Left = new KDTreeIndex();
    vector<int> A,B;
    median = ChooseRule(S,Dimension);
    for(int i=0;i<S.getDimension();i++)
    {
        if(S.getElement(i).getElement(Dimension)<=median)
        {
            A.push_back(i);
        }
        else
        {
            B.push_back(i);
        }
    }
    Left->Set=A;
    Right->Set=B;

    left = (Left->MakeTree((Dimension+1)%S.getElement(0).getDimension()));
    right = (Right->MakeTree((Dimension+1)%S.getElement(0).getDimension()));

    return this;
}

// void TreeIndex::k_nearest_neighbors(DataVector& target, int k, vector<pair<double,int>>& neighbors)
// {
//    priority_queue<pair<double,int>> Queue(neighbors.begin(),neighbors.end());
//    for(int i=0;i<Set.size();i++)
//    {
//         double distance = target.dist(TreeIndex::Data.getElement(Set[i]));
//         if(Queue.size()<k) Queue.push({distance,Set[i]});
//         else if(Queue.top().first > distance) 
//         {
//             Queue.pop();
//             Queue.push({distance,Set[i]});
//         }
//    }
//    neighbors.clear();
//    while(!Queue.empty())
//    {
//         neighbors.push_back(Queue.top());
//         Queue.pop();
//    }
//     cout << neighbors.size() << endl;
// }

priority_queue<pair<double,int>> TreeIndex::Search(DataVector &target,int k,priority_queue<pair<double,int>>& neighbors)
{
    // if(this == NULL)
    // {
    //     return false;
    // }
    // if(this->Set.size()<100) 
    // {
    //     this->k_nearest_neighbors(target,k,neighbors);
    //     return false;
    // }
    // else
    // {
    //     if(target * unit_vector <=median)
    //     {
    //         if(left->Search(target,k,neighbors)) return true;
    //         if(neighbors.size()==k && abs(target*unit_vector - median) > neighbors[0].first) return true;
    //         else if(right != NULL) right->k_nearest_neighbors(target,k,neighbors);
    //         return false;
    //     }

    //     if(right->Search(target,k,neighbors)) return true;
    //     if(neighbors.size()==k && abs(target*unit_vector - median) > neighbors[0].first) return true; 
    //     else if(left!=NULL) left->k_nearest_neighbors(target,k,neighbors);
    //     return false;

    // }

    if(left==NULL && right == NULL)
    {
        for(auto it : this ->Set )
        {
            neighbors.push({target.dist(Data.getElement(it)),it});
            if(neighbors.size() > k){
                neighbors.pop();
            }
        }
        return neighbors;
    }
    int dimension = dimension % Data.getDimension();
    if(target.getElement(dimension) <  median){
        if( left != nullptr){
            neighbors = left->Search(target,k,neighbors);
        }
        if(neighbors.size() < k || abs(target.getElement(dimension) - median) < neighbors.top().second){
            if( right != nullptr){
                neighbors = right -> Search(target,k,neighbors);
            }
        }
    }
    else{
        if(right != nullptr){
            neighbors = right ->Search(target,k,neighbors);
        }
        if(neighbors.size() < k || abs(target.getElement(dimension) - median) < neighbors.top().second){
            if(left != nullptr){
                neighbors = left -> Search(target,k,neighbors);
            }
        }
    }
    return neighbors;
}

double RPTreeIndex :: ChooseRule(VectorDataset b)
{
    srand(time(0));
    vector<double> unit;
    int Dim = b.getDimension();
    for(int i=0;i<Dim;i++)
    {
        unit.push_back(static_cast<double>(rand()));
    }
    double Dis=0;
    for(int i=0;i<Dim;i++)
    {
        Dis = Dis + unit[i]*unit[i];
    }
    Dis = sqrt(Dis);
    for(int i=0;i<Dim;i++)
    {
        unit_vector.pushElement(unit[i]/Dis);
    }
    int x_ = static_cast<int>(rand()%Dim);
    DataVector Y,X = b.getElement(x_);
    double max_dist=0;
    for(int i =0;i<Dim;i++)
    {
        double dist = X.dist(b.getElement(i));
        if(max_dist<dist)
        {
            max_dist = dist;
            Y = b.getElement(i);
        }
    }
    double delta = (static_cast<double>(rand()/RAND_MAX*2)-1)*6*max_dist/sqrt(Dim);
    vector<double> Dot_prod;
    for(int i=0;i<Dim;i++)
    {
        Dot_prod.push_back(b.getElement(i)*unit_vector);
    }
    sort(Dot_prod.begin(),Dot_prod.end());
    if(Dim%2==0) median = (double)((Dot_prod[Dim/2]+Dot_prod[(Dim/2)-1])/2.0)+delta;
    else median = (double) Dot_prod[(Dim-1)/2] + delta;
    return median;
}

RPTreeIndex* RPTreeIndex :: MakeTree(int Dimension)
{
    if(Set.size() < 100)
    {
        return this;
    }
    VectorDataset S;
    for(int i=0;i<Set.size();i++)
    {
        S.AddData(TreeIndex :: Data.getElement(Set[i]));
    }    


    RPTreeIndex* Right = new RPTreeIndex();
    RPTreeIndex* Left = new RPTreeIndex();
    vector<int> A,B;
    median = ChooseRule(S);
    for(int i=0;i<S.getDimension();i++)
    {
        if(S.getElement(i).getElement(Dimension)<=median)
        {
            A.push_back(i);
        }
        else
        {
            B.push_back(i);
        }
    }
    Left->Set=A;
    Right->Set=B;

    left = (Left->MakeTree((Dimension+1)%S.getElement(0).getDimension()));
    right = (Right->MakeTree((Dimension+1)%S.getElement(0).getDimension()));

    return this;
}