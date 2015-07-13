import nltk
import itertools
import pandas
import sys
import unidecode


def is_valid_name(full_name):

	#parsing individual names from words and ignoring tokens which are just ','
	words = nltk.word_tokenize(full_name)
	if ',' in words :
		words.remove(',')

	#Single letter word can only occur once.
	one_letter_words = 0;
	for word in words:
		if (len(word) < 2 and word != ','):
			one_letter_words = one_letter_words + 1

	if (one_letter_words > 1 and len(words) == 2) :
		#print "Name " + full_name + " cannot be just 2 initials or blanks"
		return False


	#checking for alphabets and white space
	for word in words:
		for ch in word:
			if not ch == ',' :
				if (not ((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122) or ord(ch) == 32 or ord(ch) == 45 or ord(ch) == 46 or ord(ch) == 39)):
					#print "Found random character " + ch + " in " + full_name
					return False
	
	#if a word has a character repeated more than 2 times, it's not a valid name
	corrected_word = ''.join(''.join(s)[:3] for _, s in itertools.groupby(word))
	if corrected_word != word :
		#print "Word " + word + " in name " + full_name + " corrected as " + corrected_word
		return False

	return True

path = 'https://raw.githubusercontent.com/gchandru1/name-validation/master/Datasets/'

df1 = pandas.read_csv(path + 'CSV_Database_of_First_Names.csv')
for name in df1[df1.columns[0]] :
	name_ascii = unidecode.unidecode(name)
	if isinstance(name_ascii, str) : 
		is_valid_name(name_ascii)


df2 = pandas.read_csv(path + 'CSV_Database_of_Last_Names.csv')
for name in df2[df2.columns[0]] :
	name_ascii = unidecode.unidecode(name)
	if isinstance(name_ascii, str) : 
		is_valid_name(name_ascii)


df3 = pandas.read_csv(path + 'chicago_employees.csv')
for name in df3[df3.columns[0]] :
	name_ascii = unidecode.unidecode(name)
	if isinstance(name_ascii, str) : 
		is_valid_name(name_ascii)


df4 = pandas.read_csv(path + 'fifa_players_2012.csv')
for name in df4[df4.columns[1]] :
	name_ascii = unidecode.unidecode(name)
	if isinstance(name_ascii, str) : 
		is_valid_name(name_ascii)


df5 = pandas.read_csv(path + 'olympicathletes.csv')
for name in df5[df5.columns[0]] :
	name_ascii = unidecode.unidecode(name)
	if isinstance(name_ascii, str) : 
		is_valid_name(name_ascii)
