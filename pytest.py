typedef struct list_node {
    int value;
    struct list_node *next;
} *node;

typedef struct list_struct{
    node head;
    node tail;
} *list;


list makelist(void);
/*adding related functions*/
void addvalue(list,int);
int insertvalue(list,int,int);
/*getting related functions*/
int getindex_byvalue(list,int);
int getvalue_byindex(list,int);
/* removing related functions */
int removevalue_byvalue(list,int);
int removevalue_byindex(list,int);

void printlist(list);

list makelist(){
    list l = malloc(sizeof(struct list_struct));
    l->head = NULL;
    l->tail = NULL;
    return l;
}

void addvalue(list list,int node_data){
    node n = malloc(sizeof(struct list_node));
    n->value = node_data;
    n->next = NULL;
    if(list->tail != NULL){
        list->tail->next = n;
    }
    if(list->head == NULL){
        list->head = n;
    }
    list->tail = n;
}

int insertvalue(list list,int index,int data){
    /*if failed to insert value,return 1*/
    node n = list->head;
    /*to change b.next*/
    node b = NULL;
    node new_node = malloc(sizeof(node));
    new_node->value = data;

    int count=0;
    for(count=0;n!=NULL;n=n->next,count++){
        if(count==index){
            new_node->next = n;
            if(n==list->head){
                list->head = new_node;
            }else{
                b->next = new_node;
            }
            return 0;
        }
        b = n;
    }
    return 1;
}


int getindex_byvalue(list list,int value){
    /*return index of value.
     * if there is no value,return -1*/
    node n = list->head;
    int count;
    for(count=0;n!=NULL;n=n->next,count++){
        if(n->value == value){
            return count;
        }
    }
    return -1;
}

int getvalue_byindex(list list,int index){
    node n = list->head;
    int count;
    for(count=0;n!=NULL;n=n->next,count++){
        if(count==index){
            return n->value;
        }
    }
    return -1;
}

int removevalue_byvalue(list list,int value){
    node n;
    node b = NULL;
    for(n=list->head;n!=NULL;n=n->next){
        if(n->value==value){
            if(n==list->head){
                list->head = n->next;
                if(n==list->tail){
                    /*it's only one node in list*/
                    list->tail = NULL;
                }
            }else if(n==list->tail){
                list->tail = b;
                b->next = NULL;
            }else{
                b->next = n->next;
            }
            return 0;
        }
        b = n;
    }
    return 1;
}

int removevalue_byindex(list list,int index){
    node n;
    node b = NULL;
    int count = 0;
    for(n=list->head;n!=NULL;n=n->next,count++){
        if(count==index){
            if(n==list->head){
                list->head = n->next;
                if(n==list->tail){
                    /*it's only one node in list*/
                    list->tail = NULL;
                }
            }else if(n==list->tail){
                list->tail = b;
                b->next = NULL;
            }else{
                b->next = n->next;
            }
            return 0;
        }
        b = n;
    }
    return 1;
}

void printlist(list list){
    node n = list->head;
    int count;
    printf("head:%p,tail:%p\n",list->head,list->tail);
    for(count=0;n!=NULL;count++){
        printf("Node %d's value = %d,addr = %p\n",
                count,n->value,n);
        n = n->next;
    }
    printf("\n");
}

int main(){
    list l = makelist();
    int cont = 1;
    while(cont){
        int command = 0;
        int value;
        int index;
        printlist(l);
        printf("-1:quit,1:add,2:insert\n");
        printf("3:getindex,4:getvalue\n");
        printf("5:remove_byvalue,6:remove_byindex\n");
        printf("command:");
        scanf("%d",&command);
        switch(command){
            /*add*/
            case 1:
                printf("value?:");
                scanf("%d",&value);
                addvalue(l,value);
                printf("\n");
                break;
            /*insert*/
            case 2:
                printf("index?:");
                scanf("%d",&index);
                printf("value?:");
                scanf("%d",&value);
                if(insertvalue(l,index,value)){
                    printf("failed to insert(%d,%d)",index,value);
                }
                printf("\n\n");
                break;
            /*getindex*/
            case 3:
                printf("value?:");
                scanf("%d",&value);
                printf("index is %d\n",
                        getindex_byvalue(l,value));
                printf("\n");
                break;
            /*getvalue*/
            case 4:
                printf("index?:");
                scanf("%d",&index);
                printf("value is %d\n",
                        getvalue_byindex(l,index));
                printf("\n");
                break;
            /*remove_byvalue*/
            case 5:
                printf("value?:");
                scanf("%d",&value);
                removevalue_byvalue(l,value);
                printf("\n");
                break;
            /*remove_byindex*/
            case 6:
                printf("index?:");
                scanf("%d",&index);
                removevalue_byindex(l,index);
                printf("\n");
                break;
            /*quit*/
            case -1:
                cont = 0;
                break;
            default:
                break;
        }
    }
    return 0;
}
