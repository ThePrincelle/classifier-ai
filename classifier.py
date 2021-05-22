# python3
# classifier.py
# Machine Learning processing for classifier
# Created by Maxime Princelle
# --------------------------------------

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import linear_kernel
import os


def top_tfidf_features(row, features, top_n=20):
	topn_ids = np.argsort(row)[::-1][:top_n]
	top_feats = [(features[i], row[i]) for i in topn_ids]
	df = pd.DataFrame(top_feats, columns=['features', 'score'])
	return df


def top_features_in_doc(X, features, row_id, top_n=25):
	row = np.squeeze(X[row_id].toarray())
	return top_tfidf_features(row, features, top_n)


def classifier(mails_df):
	mails_df_copy = mails_df
 
	# Get path
	main_path = os.getenv('CLASSIFIER_AI_PATH', "./")
	stopwords_path = main_path + "stopwords_fr.txt"

	# Get stopwords
	stopwords_txt_fr = open(stopwords_path, "r")
	stopwords_fr = stopwords_txt_fr.read().split('\n')
	stopwords = ENGLISH_STOP_WORDS.union(stopwords_fr)
	#print(stopwords)

	# Remove newlines
	mails_df['text'].replace({r'\s+$': '', r'^\s+': ''}, regex=True, inplace=True)
	mails_df['text'].replace(r'\n',  ' ', regex=True, inplace=True)
	mails_df['text'].replace(r'\r', ' ', regex=True, inplace=True)

	#print(mails_df.text)

	vec = TfidfVectorizer(analyzer='word', stop_words=stopwords, max_df=0.3, min_df=3, max_features=30, token_pattern=r'(?u)\b[A-Za-z]+\b')
	vec_train = vec.fit_transform(mails_df["text"])

	features = vec.get_feature_names()
	#print(features)
	categories = top_features_in_doc(vec_train, features, 1, 100)

	#print(categories)
	categorised_mails = {}

	for idx, category in enumerate(categories.features):
		vec_query = vec.transform([category])
		cosine_sim = linear_kernel(vec_query, vec_train).flatten()
		related_email_indices = cosine_sim.argsort()
		category_emails = related_email_indices.tolist()

		# Remove first element
		category_emails.pop(0)

		emails = category_emails
		for idx, email_id in enumerate(category_emails):
			emails[idx] = mails_df.iloc[email_id]

		categorised_mails[category] = emails

	return categorised_mails
