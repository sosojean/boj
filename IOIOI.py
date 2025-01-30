import sys 

n = int(sys.stdin.readline()) 
m = int(sys.stdin.readline()) 
s = sys.stdin.readline().strip()  # 개행 문자 제거

def find_target():
    count_target = 0
    pattern_count = 0
    i = 0  

    while i < m - 1:  
        if s[i] == "I":   
            pattern_count = 0  
            
            while i + 2 < m and s[i+1] == "O" and s[i+2] == "I":
                pattern_count += 1   
                if pattern_count >= n:
                    count_target += 1
                i += 2   
        i += 1  

    print(count_target)

find_target()
