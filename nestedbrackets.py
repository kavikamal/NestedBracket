import sys
def check_nested_brackets(filename):
    with open(filename, 'r+') as myfile: 
       exp_list = myfile.read().split('\n')
    result = " "
    for exp in exp_list:
        result+=(check_brackets(exp)) + "\n"   
    return result             
     
def check_brackets( exp ):
    brackets = {'(':')','[':']','{':'}','<':'>','(*':'*)'}
    brackets_list = []
    i=0
    pos=0
    while i<len(exp): 
        pos+=1 
        c=exp[i]
        if c == '(' and exp[i+1]=='*'  and i < len(exp)-1:
           c+=exp[i+1] 
           i+=1       
        elif c == '*' and i < len(exp)-1 and exp[i+1]==')' :  
           c+=exp[i+1] 
           i+=1
     
        if c in brackets:
            brackets_list.append(c)     
        elif c in brackets.values():  
            open_bracket= next((k for k, v in brackets.items() if v == c),None)
            if open_bracket and brackets_list[-1] != open_bracket:
                return 'NO ' + str(pos)   
            else:
                brackets_list.pop()      
        i+=1
                     
    # Opening brackets but no closing
    if len(brackets_list)>0:
        pos=pos+1
        return 'NO ' + str(pos)
    return 'YES'    

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    sys.exit(1)
result = check_nested_brackets(sys.argv[1])
file = open("nestedbracketoutput.txt","w") 
file.write(result)
file.close()

if __name__ == '__main__':
  main()
    