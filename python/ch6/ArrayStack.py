"""This module contains class ArrayStack and ArrayStackStatic
   There are also some application function using ArrayStack class in this module.
   For example: 'is_matched_html' 'is_matched_html_new' etc.
"""

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """Error attempting to access an element from an full container"""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self,maxlen=None):
        """Create an empty stack."""
        self._data = []
        self._maxlen=maxlen

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data)==0

    def push(self,e):
        """Add element e to the top of the stack"""
        if self._maxlen!=None:
            if len(self._data)==self._maxlen:
                raise Full('The stack is full')
        self._data.append(e)

    def top(self):
        """Return(but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the pop of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

class ArrayStackStatic:
    """LIFO Stack implementation using a Python list as underlying storage,but has a static lenth"""

    def __init__(self,n):
        """Create an empty stack."""
        self._data = [None]*n
        self._n=n
        self._top=0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._n

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._top==0

    def push(self,e):
        """Add element e to the top of the stack"""
        if self._top==(self._n):
            raise Full("Stack is full")
        self._top+=1
        self._data[self._top-1]=e

    def top(self):
        """Return(but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._top-1]

    def pop(self):
        """Remove and return the element from the pop of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        self._top-=1
        return self._data[self._top]

def is_matched_html(raw):
    """Return True if all HTML tags are properly match; 
       False otherwise.
    """
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>',j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop( ):
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

def is_matched_html_new(raw):
    """Return True if all HTML tags are properly match; 
       False otherwise.
       Much better than is_matched_html when there are attributes in opening tags
    """
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>',j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if not tag[1:] in S.pop( ):
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty ='({['# opening delimiters
    righty =')}]'# respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c) # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False # mismatched
    return S.is_empty() # were all symbols matched?

def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        print type(line)
        S.push(line.rstrip('\n')) # we will re-insert newlines when writing
    original.close()
    # now we overwrite with contents in LIFO order
    output = open(filename, 'w') # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n') # re-insert newline characters
    output.close()

"""test code"""
if __name__ == '__main__':    
    #test on is_matched_html and is_matched_html_new
    print 'test on is_matched_html and is_matched_html_new......'
    str_a="<body> \
    <center> \
    <h1> The Little Boat </h1> \
    </center> \
    <p> The storm tossed the little\
    boat like a cheap sneaker in an\
    old washing machine. The three\
    drunken fishermen were used to\
    such treatment, of course, but\
    not the tree salesman, who even as\
    a stowaway now felt that he\
    had overpaid for the voyage. </p>\
    <ol>\
    <li> Will the salesman die? </li>\
    <li> What color is the boat? </li>\
    <li> And what about Naomi? </li>\
    </ol>\
    </body>"
    str_b="<name></name>"
    str_c="<name attr='hehe' attr2=1>ctxrr test</name>"
    print is_matched_html(str_a)
    print is_matched_html(str_b)
    print is_matched_html(str_c)
    print ''
    print is_matched_html_new(str_a)
    print is_matched_html_new(str_b)
    print is_matched_html_new(str_c)  
    print '-------------------------'
    #test on is_matched
    print 'test on is_matched......'
    str_m='(abcd(e[])'
    str_n='(abcde[])'
    print is_matched(str_m)
    print is_matched(str_n)
    #test on reverse_file
    #reverse_file('a')