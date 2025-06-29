
# How To Write Markdown-rich README's?
## Introduction

This is simple introduction on how to write markdown-rich README's.

For tha we need to know:
- how it works
- what are special characters to format.

This is specially necessary to make a good __customizable__ README's

## Structures
- __ [text] __ and ** [text] ** for **bold**
- _ [text] _ and * [text] * for *italic*
- combine both to make ***Italic-Bold***.
- add '#' to make a heading and increasing the hashes leads to lower heading sizies. e.g.,
# heading 1
## heading 2

### heading 3

- ~ [text] ~ for ~strikethrough~
- >  for a quote, > text
- [Github](www.github.com) - To make a hyperlink, add [text] then without space, (url).
- To show an image is similar however before the [] brakets put exclaimation point(!).
![This is github logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhcVrL5XiyI9tM5z8mYG9oSL76qEIV-JRH_A&s)

```
// C++ header file
#include <iostream>
```
- To make code block like shown above it,  there should be ``` sign one line before and one after the code.

 
- Now to make tables:
```
| Header 1 | Header 2 |  
| --- |  --- |  
| content cell | content cell |  
| content cell | content cell |  
```
This is the result:

| Header 1 | Header 2 |  
| --- |  --- |  
| content cell | content cell |  
| content cell | content cell |  


> [!NOTE]
> I have not shown all syntaxes for everything, to learn more: [GitHub Basic Syntaxes & Formatting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github).

- To make this it should start with > and then [!NOTE] and then in another line start with > and then write the message.
- [!NOTE] is not the only Alert, theres:
  - [!TIP], [!IMPORTANT], [!WARNING], [!CAUTION]
