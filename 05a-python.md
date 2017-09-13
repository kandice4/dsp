# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both are containers for elements like strings, integers, floats. Tuples are immutable while lists are mutable. This means that you cannot change tuples. Tuples are used in dictionaries. Lists cannot be used in dictionaries. As stated before, lists are mutable. Only immutable objects can be used as keys in a dictionary.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both are a collection of elements. Elements are separated by commas. Lists are ordered but sets are not. Sets cannot have duplicate elements. I might create a list to hold the values for number of streams per day by day of the week. Each element would be indexed and each index would map to a day of the week. Sets are more typical for membership testing or to remove duplicate values. Both can use `in` to check if element exists in the list/set. List can use index to find the position of the element but since sets are unordered we can't determine an index.
>>Both can use `in` to check if element exists in the list/set. Tuples are faster for membership testing and also use less memory because of their immutability. However, if you are iterating over the elements a list is faster.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a keyword used for creating anonymous functions. They are used to return the result of an expression without having to program a separate function. One example is to use lambda within the first argument of the filter() function to check for a condition. For example: filter(lambda x: x%2==0, my_list) will return only elements of my_list that are divisible by 2 (even).

>> The key argument requires a function. It is helpful to use lambda for arguments that require a function. This works similarly to the use in filter because the function is called for each list element. Lambda can be used to sort by index for complex objects. For example: sorted(tuples_list, key=lambda tuple: tuple[1]) will sort a list of tuples by the 2nd element in the tuple. For user data, this could be a DOB, age, name, zip code, etc.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow you to quickly create a list in one line of code by performing operations on a sequence. The list comprehension uses `for` `in` and `if`, essentially looping and testing conditions in one statement. List comprehensions can be used to map and filter at the same time or do one or the other. For example, the list comprehension `[x**2 for x in range(1,11) if x%2 == 0]` does the job of a map function taking in a number and returning its square and also filtering for only even inputs. The list comprehension is supposed to run faster and is clearly simplier to code for simple expressions.

>> A dictionary comprehension is created by `{key: value for (key, value) in iterable}`. Set comprehensions are formed using the same syntax as list comprehension except using curly braces instead of brackets. For example `{x**2 for x in range(1,11)}`.

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>>  
>>    ```
>>    date_start = '01-02-2013'
>>    date_stop = '07-28-2015'
>>    from datetime import datetime
>>    date_format = '%m-%d-%Y'
>>    a = datetime.strptime(date_start,date_format)
>>    b = datetime.strptime(date_stop, date_format)
>>    c = b - a
>>    days_between = c.days
>>    ```

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>>  
>>    ```
>>    date_start = '12312013'
>>    date_stop = '05282015'
>>    from datetime import datetime
>>    date_format = '%m%d%Y'
>>    a = datetime.strptime(date_start,date_format)
>>    b = datetime.strptime(date_stop, date_format)
>>    c = b - a
>>    days_between = c.days
>>    ```

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>>  
>>    ```
>>    date_start = '15-Jan-1994'
>>    date_stop = '14-Jul-2015'
>>    from datetime import datetime
>>    date_format = '%d-%b-%Y'
>>    a = datetime.strptime(date_start,date_format)
>>    b = datetime.strptime(date_stop, date_format)
>>    c = b - a
>>    days_between = c.days
>>    ```
Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





