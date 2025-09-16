## How to Write Good Markdown-rich README's?
Writing Good Markdown is essential in Github to do documentation, explaination, wiki etc effectively as it provides human readibility along with stylying it. Along with this you will come to know that syntax is not the only thing but something more crucial is how to use it.

This is simple introduction on how to write good markdown-rich README's.

For tha we need to know:
- how it works.
- what are special characters to format.
- where to use it.

This is specially necessary to make a good __customizable__ README's

## Structures
Do not use any of the syntaxes excessivily and only use them when they are needed.
- __ [text] __ and ** [text] ** for **bold**.\
Only use **bold** to show really important words or to stress words.
- `_text_` and `*text*` for *italic*
Only use *italic* to show some emphasis or to differentiate from bold: so to categorize emphasis.
- combine both to make ***Italic-Bold***:
`***Italic-Bold***`\
- Add '#' to make a heading and increasing the hashes leads to lower heading sizies. e.g.,
# heading 1
## heading 2
### heading 3
The reasoning of heading is pretty straightforward, one tips for headings is start with one `#` for main title and increase the hash like `##` for sub-heading and `##` for sub-sections and you can go further down the rabbit hole. This adds textual symmetry and structure.

The following are pretty straightforward and do not need such explainations:
- `~text~` for ~strikethrough~
- >  for a quote, `>` text
- [Github](www.github.com) - To make a hyperlink, add [text] then without space, (url) like `[Github](www.github.com)`.
![This is github logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhcVrL5XiyI9tM5z8mYG9oSL76qEIV-JRH_A&s)
- To show an image is similar however before the [] brakets put exclaimation point(!). So, like this:

`![This is github logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhcVrL5XiyI9tM5z8mYG9oSL76qEIV-JRH_A&s)`

- To make code block like shown above it,  there should be ` three times sign one line before and one after the code for multiple lines.
```
// C++ header file
#include <iostream>
```


alternatively you can also use, only one ` to make code block as wells ` however that will be limited to only one line.

`
// C++ header file
#include <iostream>
` 
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
> I have not shown all syntaxes for everything, to learn more: [GitHub Basic Syntaxes & Formatting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github) or [Markdown Style Guide](https://google.github.io/styleguide/docguide/style.html)

- The syntax for above `note` is:
```
> [!NOTE]
> I have not shown all syntaxes for everything, to learn more: [GitHub Basic Syntaxes & Formatting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github).
```
- `!NOTE` is not the only Alert, theres:
  - `!TIP, !IMPORTANT, !WARNING, !CAUTION`
For another example:
> [!CAUTION]
> Do not use one syntax excessively or endlessly without reason.
