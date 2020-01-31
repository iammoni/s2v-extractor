class s2v:  #string to value
    col_list=[]
    df=None
    def __init__(self,df,col_list):
        self.df=df
        self.col_list=col_list
        print(self.df)
    def extract(self):
        rows=self.df.index.values.tolist();
        for col in self.col_list:
            for i in rows:
                if(self.df.at[i,col]):
                    self.df.at[i,col]=self.extract_no(self.df.at[i,col]);
        return self.df;
    def extract_no(self,str1):
        x=""
        if(str1==str1 and type(str1) == str):
            for i in range(len(str1)):
                if(str1[i].isdigit()):
                    x+=str1[i];
            return int(x);
        else:
            return str1;










