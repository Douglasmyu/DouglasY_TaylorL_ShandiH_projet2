import dynamic
import exhaustive

def main():
    with open("input.txt", 'r') as f: #open file
        N= int(f.readline().strip()) 
        stocks_and_values = [list]
        amount = int(f.readline().strip())
        result_D = dynamic(N, stocks_and_values, amount)
        result_E = exhaustive(N, stocks_and_values, amount)
      
        for line in f:
            f_contents=f.readline(10)

            print(line, end='')

        file = open("output.txt", 'w')
        f.write 
    f.closed
