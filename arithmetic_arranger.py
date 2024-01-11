def arithmetic_arranger(problems, solve_problems=False):
  arranged_problems = ""
  operators = []
  operands = []
  row_1_str = ""
  row_2_str = ""
  row_3_str = ""
  row_4_str = ""

  # error if there are more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    operator = problem.split(" ")[1]

    # error if there are operators that are not addition or subtraction
    if (operator != "+" and operator != "-"):
      return "Error: Operator must be '+' or '-'."

    operators.append(operator)
    operand_1 = problem.split(" ")[0]
    operand_2 = problem.split(" ")[2]

    # error if there are non-digits in the operands
    if (not operand_1.isdigit() or not operand_2.isdigit()):
      return "Error: Numbers must only contain digits."
    # error if the operands are more than 4 digits
    elif (len(operand_1) > 4 or len(operand_2) > 4):
      return "Error: Numbers cannot be more than four digits."

    operands.append([operand_1, operand_2])

  for problem_index in range(len(problems)):
    operand_1 = operands[problem_index][0]
    operand_2 = operands[problem_index][1]
    operand_1_length = len(operand_1)
    operand_2_length = len(operand_2)

    if (operand_1_length > operand_2_length):
      longest_operand = 1
      longest_operand_length = len(operand_1)
    else:
      longest_operand = 2
      longest_operand_length = len(operand_2)

    operator = operators[problem_index]

    # format the problems
    if longest_operand == 1:
      row_1_str += (" " * 2) + operand_1
      row_2_str += operator + (" " * (operand_1_length - operand_2_length + 1))
      row_2_str += operand_2
    else:
      row_1_str += (" " *
                    (operand_2_length - operand_1_length + 2)) + operand_1
      row_2_str += operator + " " + operand_2

    # add the dashes
    row_3_str += ("-" * (longest_operand_length + 2))

    # solve the problems if solve_problems is True
    if solve_problems:
      if operator == "+":
        answer = int(operand_1) + int(operand_2)
      else:
        answer = int(operand_1) - int(operand_2)

      answer_str = str(answer)
      # add the answer
      row_4_str += (
          " " * (longest_operand_length + 2 - len(answer_str))) + answer_str

    # if the current problem is not the last problem in problems, make space
    if problem_index < len(problems) - 1:
      row_1_str += " " * 4
      row_2_str += " " * 4
      row_3_str += " " * 4
      row_4_str += " " * 4

  # combine all problems together
  if solve_problems:
    arranged_problems = row_1_str + "\n" + row_2_str + "\n" + row_3_str + "\n"
    arranged_problems += row_4_str
  else:
    arranged_problems = row_1_str + "\n" + row_2_str + "\n" + row_3_str

  return arranged_problems
