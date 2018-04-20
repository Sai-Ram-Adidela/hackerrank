"""
Title     : String Validators
Subdomain : Challenges/Strings
Domain    : Python
Author    : Sai Ram Adidela
Created   : 20 April 2018
"""
if __name__ == '__main__':
    s = input()

    # THIS Code is not working for 1, 2, 4, 5 test cases for input 'qA2'.
    #     isalnum = lambda s: print('True') if s.isalnum else print('False')
    #     isalpha = lambda s: print('True') if s.isalpha else print('False')
    #     isdigit = lambda s: print('True') if s.isdigit else print('False')
    #     islower = lambda s: print('True') if s.islower else print('False')
    #     isupper = lambda s: print('True') if s.isupper else print('False')
    #     isalnum(s)
    #     isalpha(s)
    #     isdigit(s)
    #     islower(s)
    #     isupper(s)

    # THIS Code is not working for 0, 3, 5 test cases for input 'qA2'.
    # print(s.isalnum())
    # print(s.isalpha())
    # print(s.isdigit())
    # print(s.islower())
    # print(s.isupper())

    # This working fine but any body correct my above codes.
    for i in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(getattr(c, i)() for c in s))
