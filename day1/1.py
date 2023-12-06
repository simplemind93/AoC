import os

def decode(line: str) -> str:
    '''
    Decode a string item so that string representation of number in line
    \nAssumption is the max string representation of number in within a thousand

    \nArgument: 
        \n\tline : line item which represents a string
    If a string contains string representation of number like 'one', 'eleven', 'thirty'
    \n to 1,11,30 and sends back a string 

    \nReturn a decoded string
    '''

    # numdict = {'one': 1, 'two': 2,'three': 3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,\
    #             'ten':10,'twenty':20,'thirty':30,'fourty':40,'fifty':50,'sixty':60,'seventy':70,\
    #             'eighty':80,'ninety':90,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,\
    #             'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}
    numdict = {'one': 1, 'two': 2,'three': 3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,\
                'zero':0}

    lowline = line.lower()
    lisline = list(lowline)
    if lowline.rfind('hundred') != -1:
        lowline.replace('hundred','100')

    for wnum in numdict:
        if (ids :=lowline.rfind(wnum)) != -1: 
            lisline.insert(ids+1, str(numdict[wnum]))
            lowline = ''.join(lisline)
            # print(lowline, lisline)

    # if any(sd in lowline for sd in numdict):
    #     cont = [sd for sd in numdict if sd in lowline]
    #     for i in numdict:
    #         if i in lowline:
    #             lnum[lowline.rfind(i)]= numdict[i] 
    #     newls = list(lowline)
    #     for k in lnum: newls.insert(k,str(lnum[k]))
        # for i in cont :
        #     print(numdict[i]) 
        #     print(i)
        #     ind= lowline.rindex(i)
        #     newstr = lowline[:ind] +str(numdict[i]) + lowline[ind:]
    
    return lowline


def get_number(line, order) :
    '''
    Get a number from a string AoC Day 1:
    \nArguments:
        \nline : string which represents a string
        \norder : 
                \n\t0 : First to last
                \n\t1 : Last to first
    
    \nReturn a number from string
    '''
    strlen = len(line)
    if order == 0:
        iterrange = range(0,strlen,1)
    elif order == 1:
        iterrange = range(strlen-1, -1, -1)
    else:
        raise NotImplementedError
    for i in iterrange:
        if line[i].isdigit():
            return int(line[i])
    return 0



def main():
    print(os.getcwd())
    file = open('day1/input.txt')
    linetotal1 = 0
    linetotal2 = 0 
    for line in file:
        first_num = get_number(line, 0)
        last_num = get_number(line,1)
        linetotal1 += first_num*10 + last_num 
        line = decode(line)
        print(line)
        first_num2 = get_number(line, 0)
        last_num2 = get_number(line,1)

        print(first_num2,last_num2)
        linetotal2 += first_num2*10 + last_num2
        # print(linetotal)
    print(f'File Solution 1 =',linetotal1)
    print(f'File Solution 2 =',linetotal2)        


if __name__ == '__main__':
    main()