#ifndef TREEINDEX_H
#define TREEINDEX_H

#include<bits/stdc++.h>
#include "DataVector.h"
#include "VectorDataset.h"
using namespace std;

class TreeIndex 
{
    protected:
        static TreeIndex *instance;
        static VectorDataset Data;
        TreeIndex();
        virtual ~TreeIndex();
        vector<int> Set;
        TreeIndex* left;
        TreeIndex* right;
        DataVector unit_vector;
        double median;
    public:
        static void assignData(VectorDataset& Data);
        void assignIndex();
        static  TreeIndex& GetInstance();
        virtual TreeIndex* MakeTree(int Dimension=0) = 0;
        priority_queue<pair<double,int>> Search( DataVector& target, int k,priority_queue<pair<double,int>>& neighbors);
        void k_nearest_neighbors(DataVector& target, int k, vector<pair<double,int>>& neighbors);
};

class KDTreeIndex : public TreeIndex 
{
    public:
        static  KDTreeIndex& GetInstance();
        KDTreeIndex* MakeTree(int Dimension = 0) override;
        double ChooseRule(VectorDataset b,int Dimension);
        ~KDTreeIndex() {}
    private:
        static KDTreeIndex *instance;
        KDTreeIndex();
};

class RPTreeIndex : public TreeIndex 
{
    public:
        static  RPTreeIndex& GetInstance();
        RPTreeIndex* MakeTree(int Dimension=0);
        double ChooseRule(VectorDataset b);
        ~RPTreeIndex() {}
    private:
        static RPTreeIndex *instance;
        RPTreeIndex() {}
};

#endif