import sys
def check_nested_brackets(filename):
    with open(filename, 'r+') as myfile: 
       exp_list = myfile.read().split('\n')
    result =[]
 
    for expressions in exp_list:
        result.append(check_brackets(expressions))   
    return result             
     

def check_brackets( expressions ):
    print expressions
    brackets = {'(':')','[':']','{':'}','<':'>','(*':'*)'}
    brackets_list =[]
    pos=0
    for i, c in enumerate(expressions):
        pos=i+1         
        if c in brackets:
            brackets_list.append(c)  
        elif c in brackets.values():
            open_bracket= next((k for k, v in brackets.items() if v == c),None)
            print(c, ' - ', open_bracket)
            print brackets_list[-1],open_bracket
            if open_bracket and brackets_list[-1] != open_bracket:
                return 'NOo '+ str(i)     
            else:
                brackets_list.pop()    
    if len(brackets_list)>0:
        return 'NO ' + str(pos+1)  
    return 'YES'    

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    sys.exit(1)
print(check_nested_brackets(sys.argv[1]))

if __name__ == '__main__':
  main()
    