import sys
def check_nested_brackets(filename):

   with open(filename, 'r+') as myfile: 
       expressions = myfile.read()
   brackets = {} 
   brackets_list =[]
   left_brackets = ['(','[','{','<',]
   right_brackets = [')',']','}','>','*']
   for i, c in enumerate(expressions):
      current_exp=None 
      print i
      if c in left_brackets:
        if (c=='(' and expressions[i+1]=='*'  and i<len(expressions)-1):
            current_exp = c + expressions[i+1]   
        else:
            current_exp = c
 
      elif c in right_brackets:      
        if (c=='*' and expressions[i+1]==')' and expressions[i-1] != '(' and i<len(expressions)-1):  
            current_exp = c + expressions[i+1]   
        elif c!='*':
            current_exp = c
      if current_exp!=None:
          
        if current_exp in brackets:
            brackets[current_exp] += 1
        else:
            brackets[current_exp]  = 1
   print brackets
   print expressions    

  

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)
  dict = check_nested_brackets(sys.argv[1])

if __name__ == '__main__':
  main()
    