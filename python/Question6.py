# modify this function, and create other functions below as you wish
import requests

def question06(portfolio):
   
    dict = {}
    string = ''
    portfolio = portfolio.replace("[","").replace("]","").replace('\"','')
    tokens = portfolio.split(",")
    
    for port in tokens:
        port = port.lstrip().rstrip()
        string = str(port[0])+str(port[-1])
        if not (string in dict.keys()):
            dict[string] = 1
        else:
            dict[string] += 1
            
    curr_max = 0
    if(len(set(dict.values()))== 1):
        return 0
    
    for key,value in dict.items():
        if(value > curr_max):
            curr_max = value
            strings = key
   
    for index,port in enumerate(tokens):
        port = port.lstrip().rstrip()
        if(strings == str(port[0])+str(port[-1])):
            value = index
                
    return value


'''
if __name__ == '__main__':
    url = "https://cscc-gl.herokuapp.com/tests/run/6/"
    tests = requests.get(url=url).json()
    for testnumber in range(0, len(tests)):
        
        test = tests[testnumber]
        q6input = test["input"]
        output = test["output"]
        #print(q6input)
        result = question06(q6input)
        print(result,output)
        break
'''
