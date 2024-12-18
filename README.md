# **Python Project: Generate Quotes Based on Category**

This Quotes Generator Projec is used to Generated the Quotes based on the user Sugestion. Its Basically work by fetching the content from json file which work as a data set to Model

---

## **Features**

- **Search Quotes by Category**: It suggest the quotes based on category
- **Author-Sorted Output**: It also display the detail of author of quotes.

---

## **Requirements**

- **Python 3.x**
- A **JSON file** named `quotes.json` containing the qoute dataset . The structure of file should be like shown below:-

```json
[
  {
    "quote": "Your inspirational quote here.",
    "author": "Author Name",
    "category": ["tag1", "tag2", "tag3"]
  }
]
```

---

## **How to Run the Script**

1. Make sure you have Python 3 installed on your system.
2. Ensure the `quotes.json` file is in the same directory as the script and formatted correctly.
3. Run the script:

```bash
python main.py
```

4. Enter a tag or category when prompted:

```css
Enter a tag: motivation
```

The model will display quotes that match the entered tag, sorted by author names in reverse order. For each quote:

- The author's name is displayed as "Popularity".
- The corresponding quote is displayed.
- You can choose to see the next quote or stop by entering **Y** (Yes) or **N** (No).