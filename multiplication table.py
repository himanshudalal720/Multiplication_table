class tables(object):
    def __init__(self,n):
        self.n=n
    def GetTables(self):
        for i in range(1,self.n+1):
            for j in range(1,11):
                print(f'{i}\tx\t{j}\t=\t{i * j}')
            print('|-----------------|')
    def TablesHorizontal(self):
        for i in range(1,11):
            for j in range(1,self.n+1):
                print(f'{i} x {j} = {i * j} |'.center(15,' '),end='\t\t')
            print('\n')
obj=tables(int(input()))
obj.TablesHorizontal()
obj.GetTables()