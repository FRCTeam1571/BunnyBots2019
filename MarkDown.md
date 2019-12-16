Basic Syntax
===
<p>These are the elements outlined in John Gruber’s original design document. All Markdown applications support these  elements.</p>

Element Markdown Syntax
---

Heading
# H1
## H2
### H3

- Bold **bold text**
- Italic *italicized text*  
Italicized text is the _cat's meow_.

Blockquote  
> blockquote   

Ordered List
1. First item
2. Second item
3. Third item 

 Unordered List
- First item
- Second item
- Third item  

Code `code`  
Code Blocks  
    Code blocks are normally indented four spaces or one tab.   
    When they’re in a list, indent them eight spaces or two tabs.

Horizontal Rule
---
Link  
[title](https://www.example.com)  
Image  
![alt text](image.jpg)  

URLs and Email Addresses  
To quickly turn a URL or email address into a link, enclose it in angle brackets.  
<https://www.markdownguide.org>
<fake@example.com>

----
# Extended Syntax  
<p>These elements extend the basic syntax by adding additional features. Not all Markdown applications support these elements.</p>

Element     Markdown Syntax  
Table  
| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text | 

Fenced Code Block
```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
``` 

Footnote  
Here's a sentence with a footnote. [^1]

[^1]: This is the footnote. 

Heading ID  
### My Great Heading {#custom-id}  

Definition List  
term
: definition  

Strikethrough
~~The world is flat.~~  

Task List  
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media 

---
Escaping Characters
<p>To display a literal character that would otherwise be used to format text in a Markdown document, add a backslash (\) in front of the character.</p>
\* Without the backslash, this would be a bullet in an unordered list.  

The rendered output looks like this:
* Without the backslash, this would be a bullet in an unordered list.  

Characters You Can Escape
You can use a backslash to escape the following characters.

| Character | Name |
| ----------- | ----------- |
| \\ | backslash |
| \` | backtick (see also escaping backticks in code) |
| \* | asterisk |
| \_ | underscore |
| \{ \} | curly braces |
| \[ \] | brackets |
| \( \) | parentheses |
| \# | pound sign |
| \+ | plus sign |
| \- | minus sign (hyphen) |
| \. | dot |
| \! | exclamation mark |
| \| | pipe (see also escaping pipe in tables) |