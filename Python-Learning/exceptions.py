try:
    a = int(input())
    b = int(input())
    print(a + b)

except Exception as e:
    print("eexception",e)
finally:
    print("finally block printed")
