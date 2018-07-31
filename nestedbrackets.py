import sys
def check_nested_brackets(filename):
    with open(filename, 'r+') as myfile: 
       exp_list = myfile.read().split('\n')
    result =[]
    for exp in exp_list:
        result.append(check_brackets(exp))   
    return result             
     
def check_brackets( exp ):
    print exp
    brackets = {'(':')','[':']','{':'}','<':'>','(*':'*)'}
    brackets_list = []
    flag = False
    i=0
    pos=0
    while i<len(exp):  
        c=exp[i]
        if c == '(' and exp[i+1]=='*'  and i < len(exp)-1:
           c+=exp[i+1] 
           pos+=1
           i+=1
           flag=True 
        elif c == '*' and flag and i < len(exp)-1 and exp[i+1]==')' :  
           c+=exp[i+1] 
           pos+=1
           i+=1
           flag=False  

        if c in brackets:
            if c != '(*':
               pos+=1
            brackets_list.append(c)     
        elif c in brackets.values():  
            open_bracket= next((k for k, v in brackets.items() if v == c),None)
            if open_bracket and brackets_list[-1] != open_bracket:
                return 'NOooo' + str(pos)   
            else:
                brackets_list.pop()  
        else:
          pos+=1  
        i+=1
                     
    # Opening brackets but no closing
    if len(brackets_list)>0:
        # Find index of last item in brackets_list
        # Reverse search to find position
        pos=pos+1
        return 'NO ' + str(pos)
    return 'YES'    

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    sys.exit(1)
print(check_nested_brackets(sys.argv[1]))

if __name__ == '__main__':
  main()
    