import sys
import math

def calcBinaryGap(decNum, gap2detect):
    '''
    This function finds all binary gaps in the binary representation of base10 decNum, and returns 
    maximum width for binary gap and its start bit position number (counting from bit#0).
    Binary gap can be intended as gap made of consecutive ones between zeros, or viceversa. 
    This can be set by gap2detect arg to be '1' or '0' respectively. 
    
    Args:
    
        decNum is the positive base10 number to be converted to binary and to be searched for gaps.
        It has to be within 1 and max integer number representable i.e. sys.maxsize if Python2 is in use
        
        gap2detect can be either '0' or '1' depending if looking for '0' gaps or '1' gaps
        
    Return:
    
        (max gap width, gap2detect, startbit) 
        
    '''
    zero = '0'
    one = '1'
    Python3 = 3
    decNumMin = 1
    if sys.version_info.major != Python3:
        decNumMax =  sys.maxsize  
    
    if sys.version_info.major == Python3:
        assert(type(decNum) == int and  decNumMin < decNum)
    else:
        assert(type(decNum) == int and  decNumMin < decNum < decNumMax)
        
    assert(type(gap2detect) == str and  (gap2detect == zero or gap2detect == one))

    ch2detect = one if (gap2detect == zero) else zero
    string = str(bin(decNum)).replace('0b','')
    listPos = [ el for el in (range(0,len(string))) if string[el] == ch2detect ]
    listDelta = [ (el-elPre, el) for elPre,el in zip(listPos,listPos[1:]) ] 
    sortedByGap = sorted(listDelta, key=lambda x: x[0], reverse = True)
    
    return (sortedByGap[0][0]-1), gap2detect,(sortedByGap[0][1]-(sortedByGap[0][0]-1))