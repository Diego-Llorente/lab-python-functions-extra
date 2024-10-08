{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8bce5313",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_unique_list_f(lst):\n",
    "    \"\"\"\n",
    "    Takes a list as an argument and returns a new list with unique elements from the first list.\n",
    "\n",
    "    Parameters:\n",
    "    lst (list): The input list.\n",
    "\n",
    "    Returns:\n",
    "    list: A new list with unique elements from the input list.\n",
    "    \"\"\"\n",
    "    # your code goes here\n",
    "    turn_set = set(lst)\n",
    "    turn_list = list(turn_set)\n",
    "    return turn_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "19521f96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Uppercase count: 2, Lowercase count: 8'}"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def count_case_f(string):\n",
    "    \"\"\"\n",
    "    Returns the number of uppercase and lowercase letters in the given string.\n",
    "\n",
    "    Parameters:\n",
    "    string (str): The string to count uppercase and lowercase letters in.\n",
    "\n",
    "    Returns:\n",
    "    A tuple containing the count of uppercase and lowercase letters in the string.\n",
    "    \"\"\"\n",
    "    # your code goes here\n",
    "    lower_count = 0\n",
    "    upper_count = 0\n",
    "    \n",
    "    for letter in string:\n",
    "        if letter == \" \":\n",
    "            pass\n",
    "        elif letter == letter.upper():\n",
    "            upper_count += 1\n",
    "        else:\n",
    "            lower_count += 1\n",
    "            \n",
    "    return {f\"Uppercase count: {upper_count}, Lowercase count: {lower_count}\"}\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1c614ebd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note this is an example Good day\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import string\n",
    "\n",
    "def remove_punctuation_f(sentence):\n",
    "    \"\"\"\n",
    "    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.\n",
    "\n",
    "    Parameters:\n",
    "    sentence (str): A string representing a sentence.\n",
    "\n",
    "    Returns:\n",
    "    str: The sentence without any punctuation marks.\n",
    "    \"\"\"\n",
    "    # your code goes here\n",
    "    \n",
    "    new_sentence = \"\"\n",
    "    \n",
    "    for letter in sentence:\n",
    "        if letter == \",\" or letter == \".\" or letter == \"!\" or letter == \":\" or letter == \"!\" or letter == \"?\" or letter == (\")\"):\n",
    "            pass\n",
    "        else:\n",
    "            new_sentence += letter\n",
    "    \n",
    "    new_sentence = \" \".join(new_sentence.split())\n",
    "    \n",
    "    return new_sentence\n",
    "    \n",
    "my_sentence = remove_punctuation_f(\"Note : this is an example !!! Good day : )\")\n",
    "    \n",
    "\n",
    "\n",
    "def word_count_f(sentence):\n",
    "    \"\"\"\n",
    "    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.\n",
    "    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.\n",
    "    \n",
    "    Parameters:\n",
    "    sentence (str): A string representing a sentence.\n",
    "\n",
    "    Returns:\n",
    "    int: The number of words in the sentence.\n",
    "    \"\"\"\n",
    "    # your code goes here\n",
    "    words = sentence.split(\" \")\n",
    "\n",
    "    return len(words)\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a665250e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17305b5d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f3e429a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
