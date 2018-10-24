# Day 5

`touch Readme.md`
Gedit es como el Notepad de Windows y soporta .md
`gedit Readme.md`

### GitHub repository copy
* Fork it on GitHub - get it on your own GitHub space. 
* Click clone to get the link to have a local copy. 
* On terminal: 
	**`git clone https://github.com/ironhack-datalabs/madrid-oct-2018.git`**

## Exercise 
<span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> <u>Ex2:</u> `random_sample` vs **`sample`**. The later is shown [here](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.sample.html#numpy.random.sample), and [here](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html) but I can't find its syntax. <span style='color:grey; background-color:greenyellow; font-size:.60em'> learnt&solved.</span> ScyPy.org examples use "synonyms" for their examples, so they use `random_sample` for this and the others, as they have the same syntax. 

<span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> vsCode unexpected indent. <span style='color:grey; background-color:greenyellow; font-size:.60em'> solved</span>

**`rand`** creates the array from given numbers inside the function, so just **one parenthesis** (for the function) is enough. <span style='color:grey; background-color:greenyellow; font-size:.60em'> learnt</span>

<span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> See if there are more simple numpy `random`. <span style='color:grey; background-color:greenyellow; font-size:.60em'> learnt&solved.ConfirmationPending</span> [See scipy.org reference](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html). See also my .py and my Jupyter Lab.

<span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> vsCode keeps moving and deleting my code! <span style='color:grey; background-color:greenyellow; font-size:.60em'> patched</span> After too much time trying to find out what's going on (probably related with vsCode Git versioning), I verify that Windows version doesn't have that problem. 

<u>Ex9</u> <span style='color:grey; background-color:greenyellow; font-size:.60em'> learnt</span> `.T` is same as `transpose`.  <span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> I read this (ref pending), but it doesn't work. 

<u>Ex10</u> <span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> The exercise says to use `sum` , but many references point to use `+` or `add`. `+` works for me, but`sum` doesn't.  <span style='color:grey; background-color:greenyellow; font-size:.60em'> solved</span> The exercise didn't say that, or it's been changed (f&^%#!, where did that come from?). Now it makes sense.

<u>Ex15</u> `np.empty()`<span style='color:grey; background-color:greenyellow; font-size:.60em'> learnt</span> Use it with caution, as it doesn't initialize the values (unlike `np.ceros`)
<span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> In Jupyter, it is taking the values of the previous array! <span style='color:grey; background-color:greenyellow; font-size:.60em'> solved</span> In vsCode, print(f) doesn't print anything. Or just assign values afterwards.

<u>Ex16-17</u> <span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> `for x in f`, `print(x)` returns all values (without space), but 

​	` if x > d_min and x < d_mean:` returns

 `ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()`

<span style='color:grey; background-color:greenyellow; font-size:.60em'> learnt.</span> It is because it just iterates over each big group, rather than on each element (see tests on Jupyterlab)

<span style='color:grey; background-color:greenyellow; font-size:.60em'> solved</span> To visit all the elements use the **iterator object**: **`np.nditer`** 

<span style='color:grey; background-color:greenyellow; font-size:.60em'> learnt.</span> `f[d<d_mean]` returns all elements that are true for that condition. <span style='color:grey; background-color:yellow; font-size:.60em'> issue</span>  But I don't get why `f[d_min<d<d_mean]=25` returns an `"array with more than one element is ambiguous"` error, as it is an equally Boolean expression. What am I missing? 

<u>Ex 18</u> <span style='color:grey; background-color:greenyellow; font-size:.60em'> learnt.</span> `"%.2f" ` Specifies how many digits you want to print formatted as decimals. 

Example: 

```
"%.2f"
print("%.2f" % total)
```

`numpy.array2string` Returns a string representation of an array.  <span style='color:grey; background-color:yellow; font-size:.60em'> issue</span> But we want to cast each element...




