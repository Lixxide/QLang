![alt text](https://github.com/Lixxide/QuartzLang/blob/main/logo.png)

QuartzLang is 2D programing language with no (data) stacks, but with return, file commands, access to cmd, and some sort of recursion

QuartzLang uses a list of 10 numbers to store things (data[i]), you can also add and get data from the terrain/field

# Documentation

**Movement**

'^', 'v', '<', '>' : Changes the code pointer's direction

%   : Changes the code pointer's direction to a random one

wab : warps code pointer to x = data[a] y = data[b] (no return possible)

sab : warps code pointer to x = data[a] y = data[b] (return possible)

:   : returns

**Data in and out**

{ab : sets data[a] to the ascii/UTF-8/idk value of b

}a  : prints data[a] as a character

@a  : sets data[a] as the ascii/UTF-8/idk value of the character that the user inputed

Sab : sets data[a] to b as an int (since it can only be one digit you need to do math)

#a  : prints data[a] as an int

Ea  : sets data[a] to the user input as an int

gab : sets data[0] to the character at x = data[a] y = data[b]

Gab : sets data[1] to the character at x = data[a] y = data[b]

aab : writes data[0] as a character at x = data[a] y = data[b]

Aab : writes data[0] as a character at x = data[a] y = data[b]

**Math**

+ab : data[a] = data[a] + data[b]

-ab : data[a] = data[a] - data[b]

*ab : data[a] = data[a] * data[b]

/ab : data[a] = data[a] / data[b] (integer division)

!a  : if data[a] is 0, it is set to one, else data[a] is set to 0

'i','I' : increments data[0] (lowercase), or data[1] (uppercase)

'd','D' : decrements data[0] (lowercase), or data[1] (uppercase)


**Flow control**

;a  : skips next command if data[a] is 0

?ab : if data[a] = data[b], the code pointer doesn't turn, if data[a] > data[b] it turns left, and if data[a] < data[b] it turns right

=ab : same as '?', but b is a character (a stays the same)

Na  : if data[a] = 0, the code pointer doesn't turn, but turns right if data[a] > 0, and left if data[a] < 0


**Misc**

Pab : prints the string at x = data[a] y = data[b], the string is terminated by '§'

r   : recursion, upon exit, data[5 to 9] = new_data[0 to 4] (where new_data is the data of the new code pointer)

Q   : stops the program

cab : executes in the terminal/cmd the string at x = data[a] y = data[b], the string is terminated by '§'

**Moving Data**

(   : moves data left, with wrapping

)   : moves data right, with wrapping

]   : moves data right, without wrapping

[   : moves data left, without wrapping

xab : swaps data[a] and data[b]

**Files**

F : files

filename is the string at x = data[0] y = data[1], the string is terminated by '§'

the mode is data[2] (same modes as python, plus 'd' which deletes the file)

if the mode is 'a' or 'w', then the content is the string at x = data[3] y = data[4], the string is terminated by '§'

if the mode is 'r' then it sets data[5] as the UTF-8 of the data[6]th character of the file
