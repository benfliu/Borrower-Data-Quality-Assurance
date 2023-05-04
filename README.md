# Borrower-Data-Quality-Assurance
This project is intended to serve as a helpful tool for comparing a set of borrower PDF contract forms with a csv file intended to contain the contracts' tabulated data. If inconsistencies in the csv are detected, they should be flagged and corrected using the PDF data. Ultimately, the end result will be a sleek, drag-and-drop UI allowing for automated data quality assurance, saving your time and your sanity from trying to find the needle in the csv haystack!

### Update 5/3/23:
Just successfully implemented the *find_field_match* function, which takes in a field name, a string of extracted PDF text, and the PDF filename, and returns the key-value tuple associated with the field! Some notable edge cases include the following:

1. PDFs that contain the "smart" apostrophe (which looks like ’ instead of ')
2. Field names that contain special characters (either in Python or Regex), such as ", (), etc.

I also implemented two customized Exceptions that are thrown if multiple or zero instances of a desired field are found in the PDF text, implying improper PDF formatting. Excited about the progress so far!