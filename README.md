# Github Learnings
I am currently learning Github & Git and in this demo-repo, you will see basic learnings & things that i have learned.

## Introduction & Basic Info
- ### Git
Git is a version-controlling system, in which you can store each and every version of a file or directory, and access each version enabling a history of changes, for example you can click 'history' of this file and you will be able to see all the changes made.
- ### Github
Github is a platform build on top of Git where you can store/share repositories and collabrate them. Github is the most popular & one of many ways on how you manage Git easily.

## 1. How to create a repo on Github?
To create a repository in GitHub (Web or Desktop):
### [Web](github.com): 
  - After logging in, in the main page. Click, ‘New’.
  - Scroll down to see, *'Add a README file'*, so checkmark it to create the file.
  - You can also make a license of the repo, if you click the dropdown below , 'Choose a License'. Then choose whichever license you like, most popular is `MIT license`, but choose based on your specific needs.\n
After that click, 'Create repository'.
  - #### README & License *(after repo-creation)*
	  - Alternatively to create a *README file* after repo creation:
	    - Create a file and only name it. `'README.md'`.
	  - Alternatively to create a *License file* after repo creation:
	    - Create a file and only name it. `'LICENSE.md'` or `'LICENSE'`.
	    - Click, 'Choose license template'.
	    - Then choose the template from the left column & click, 'Review and submit'.
	    - Then commit message. Then your License is successfully created.
### [Desktop](https://desktop.github.com/download/):
After opening GitHub Desktop.
  - Press `CTRL+N` or Click, File > New Repository.
  - Creating Repo panel will appear.
  - **README**: To make `README.md` click/checkmark, 'Initilize this repository with README'
  - **License**: To make license, you click the dropdown, and then choose your desired license.

## 2. How to Write Good Markdown-rich README's?
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
- To show an image is similar however before the [] brakets put exclaimation point(!). So, like this:\

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
> I have not shown all syntaxes for everything, to learn more: [GitHub Basic Syntaxes & Formatting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github).

- To make this it should start with > and then [!NOTE] and then in another line start with > and then write the message.
- [!NOTE] is not the only Alert, theres:
  - [!TIP], [!IMPORTANT], [!WARNING], [!CAUTION]
For another example:
> [!CAUTION]
> Do not use one syntax excessively or endlessly without reason.
