#from art import logo

def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2
  
def multiply(n1,n2):
  return n1 * n2
  
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  #print(logo)
  num1 = float(input("What's the first number?: "))
  for system in operations:
    print(system)
  
  
  """if operation_symbol == "+":
    answer = add(num1, num2)
  elif operation_symbol == "-":
    answer = subtract(num1, num2)
  elif operation_symbol == "*":
    answer = multiply(num1, num2)
  elif operation_symbol == "/":
    answer = divide(num1, num2)"""
  
  
  
  #To add calculate an additional operation
  continue_calculation = False
  while continue_calculation == False:
    operation_symbol = input("Pick an operation: ")
    next_num = float(input("What's the next number?: "))
    calculating_functions = operations[operation_symbol]
    answer = calculating_functions(num1, next_num)
  
    print(f"{num1} {operation_symbol} {next_num} = {answer}")
    
    calculate_more = input("Do you want to calculate more?: enter Yes or No ").title()
    if calculate_more == "Yes":
      num1 = answer
    elif calculate_more == "No":
      continue_calculation = True
      #clear()
      calculator()


calculator()