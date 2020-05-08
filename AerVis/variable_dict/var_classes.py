'''
Varialbe Calsses
'''


class Attributes:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class VariableReference(dict):
    '''
    A variable class mapping data two keys acting as pointers to the data. The keys are stash_name and stash_code - written as name and code. When data is updated on either variable, it updates for both
    
    Inputs:
        as_class :: bool- convert var dictionarys to allow for . access using the attributes class (dictionaries are faster)
    
    Usage:
        vars = VariableReference()
        vars.add(<key1>,<key2>,<data dictionary>)
    '''
    # bikey dictionary - updates data independantly
    # myDict = {
    #   **dict.fromkeys(['a', 'b', 'c'], 10), 
    #   **dict.fromkeys(['b', 'e'], 20)
    # }
    
    def __init__(self,as_class=False):
        self.as_class = as_class
        self.index = 0
        
        self.classdescription = '''
        AerVis Variable Attributes Class
        --------------------------------
        
        
        Methods:
           -   To get attributes run <this>.keys()
           -   To access articles with invalid python names (e.g. begining with \% or -) use getattr(<this>,"$£%$_unconventional_var_name")
       '''
        
    def keys(self):
        return dir(self)
    def __repr__(self):
         return self.classdescription
    def __str__(self):
         return self.classdescription        
        
    def add(self,data):
        
        assert type(data) == dict
        
        # Add Mandatory keys as blanks
        for n in 'stash_code,name,short_name,long_name,units,description'.split(','):
            try:data[n]
            except KeyError: data[n] = ''
        
        name = data['name']
        code = data['stash_code']
        
        if self.as_class:
            data = Attributes(data)
        self.index+=1
        setattr(self, 'var_id_%i'%self.index, data)
        setattr(self, name ,getattr(self,  'var_id_%i'%self.index))
        setattr(self, code ,getattr(self,  'var_id_%i'%self.index))
        
    # def fromVarName(self,varstr):
    #     self.add(dict(( (i,globals()[i]) for i in varstr.split(','))) )
