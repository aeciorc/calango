# Calango   
### Intro   

I've created this repo to document my process of learning how to design a simple programming language and implemening a source-to-source compiler. I'll be taking an incremental approach, starting with a small subset of the language and ending each iteration with a working program.

### The language:  
  
I like writing bash scripts, but the syntax really puts me off. So for this exercise I'm designing a pythonic command language that compiles to bash. I'll call it **Calango**. Here is a sample of Calango:
 
```
for n in [1..4]:
	res= ps(a) | grep(-i n) | head(-1)
	echo(res)
 ```
 
- *[1..4]* is a range of numbers from 1 to 4.  
- *ps*, *grep*, *head* and *echo* are of course shell commands. The brackets are used for passing any number of arguments to these commands. 
- "|" is your usual pipeline symbol. 
- Whitespace is used to denote blocks, exactly as in python. However, Calango restricts it to tabs.

Here's the bash code our compiler should output:
``` bash  
for i in {1..4}  
do  
res= ps a | grep -i $n  | head  
echo $res  
done  
```  
 
 We'll start with a simple subset of Calango:  
 ``` 
echo([1..4])
echo(1-1+4)
   ```  
 for which our compiler would output:
 ``` bash
echo {1..4}  
echo $((1-1+4))  
 ``` 
 which should output:  
 
 ``1 2 3 4``  
 ``4``  
 
### Tokenization  
The first step is to build a program that reads Calango code returns lists of the tokens found in it, along with their kinds
