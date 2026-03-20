# what js a loop?

# A loop is a programming construct that repeats a block of code muliple times until a condtion is met 
# (or until the items to iterate are exhausted).
# loops let you automate repetitive tasks: processing every item in a list, scanning
# lines in a file, aggregating numbers, etc.

# python has two main loop types:

#for - iterate over an iterable (list, tuple, string, dict, generator, file, ...).

# while - repeat while a condition remains true.
#  for loop - concept & usage

# A for loop pulls items from an iterable one-by-one.
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)   #prints each fruit
    # Iterables bs Iterators (brief)
    
    # Iterable: an object tou can loop over (Implements_iter_or sequence protocol) - e.g., list, str, dict,
     
    # Iterator: an object with_next_() and_iter_(); calling next() advances tt until stopIteration.

    # You can manually use iterator protocol:
    it = iter([1,2,3])
    print(next(it))  # 1
    print(next(it))  # 2
    print(next(it))
    # next(it)...when exhausted stopIteration

    # range() - common with for

    # range(stop), range(start, stop), range(start, stop, step) - integer sequence generator (efficient for loop )
    for i in range(0, 10, 2):  # 0,2,4,6,8
        print(i)
        #helpful patterns

        #enumerate() to get index + value:
        for i, value in enumerate(["a", "b", "c"], start=1):
            print(i, value)
            #zip


# Q1 Print numbers from 1 to 10 using a for loop.
# print numbers from 10 down to 1 using a while loop. 
# print the multiplication table of using a for loop.
# write a program that prints only even numbers between 1 and 20 using a while loop.
# print a pattern using anested for loop.

# Ans:1
for i in range(1, 10):
    print(i)