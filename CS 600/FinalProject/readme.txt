I have created a function called get_links_from_webpage() which returns a list of links from a webpage. I have used the beautifulsoup library to find all the links in the webpage. I have passed the html of the webpage to the beautifulsoup library and it returns all the links in the webpage.

I have also created a function called get_pages_from_file() which returns a list of pages from a file. I have opened the file in read mode and split each page into a list. I have returned the list of pages.

I have also created a function called get_terms_from_file() which returns a list of terms from a file. I have opened the file in read mode and split each term into a list. I have returned the list of terms.

I have also created a function called remove_html_tags() which removes html tags from a string. I have used regular expressions to remove the html tags from the string.

I have also created a function called get_stop_words() which returns a list of stop words. I have hardcoded the stop words in the function.

I have also created a function called get_words_from_text() which returns a list of words from a string of text. I have first removed the html tags from the string using the remove_html_tags() function. I have then converted the string to lowercase and removed the punctuations from the string. I have then split the string into a list of words. I have then removed the stop words from the list of words.

I have also created a function called get_words_from_webpage() which returns a list of words from a webpage. I have passed the url of the webpage to the get_words_from_text() function and it returns a list of words from the webpage.

I have also created a function called search_engine() which returns a list of pages containing the given terms. I have looped through all the pages and for each page, I have passed the url to the get_words_from_webpage() function. This function returns a list of words from the webpage. I have then checked if the list of terms is a subset of the list of words from the webpage. If it is, then I have added the page to the result list. I have returned the result list.

# Search Engine

I have created a search engine which returns a list of pages containing the given terms.

## Algorithms and Data Structure Used

I have used the beautifulsoup library to find all the links in the webpage.

I have also used regular expressions to remove the html tags from the string.

I have hardcoded the stop words in the function.

## Approach

I have first created a function called get_links_from_webpage() which returns a list of links from a webpage.

I have then created a function called get_pages_from_file() which returns a list of pages from a file.

I have then created a function called get_terms_from_file() which returns a list of terms from a file.

I have then created a function called remove_html_tags() which removes html tags from a string.

I have then created a function called get_stop_words() which returns a list of stop words.

I have then created a function called get_words_from_text() which returns a list of words from a string of text.

I have then created a function called get_words_from_webpage() which returns a list of words from a webpage.

I have then created a function called search_engine() which returns a list of pages containing the given terms.

## Working

The term we search is stored in terms.txt and their search result is stored in output.txt. This is always overwritten by the most recent search.