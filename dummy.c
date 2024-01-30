# include <stdio.h>
# include <stdlib.h>
# include <string.h>

// groups and org linked indi. member. business indi. owners, customer. business member of group


struct node {
    int id;
    char name[20];
    char date[10];
    //int links;
    char type[20];
    char content[100];
};

struct link{
    struct node parent;
    struct node* childrens;
};

struct location{
    int x;
    int y;
};

struct individual{
    struct node* common;
    char birthday[10];
};

struct group{
    struct node* common;
    struct link member[10];
    struct link memberbuss[10];
};

struct business{
    struct node* common;
    struct location* loc;
    struct link owners[10];
    struct link customers[10];
};

struct organisation{
    struct node* common;
    struct location* loc;
    struct link members[10];
};