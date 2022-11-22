#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:36:50 2020

@author: robert.trypuz
"""

import os
import json
import pandas as pd
import nltk
nltk.download('stopwords',quiet=True)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


from nltk.tokenize import word_tokenize
from collections import Counter

root_folder_path = '/Volumes/Transcend/CORD-19-research-challenge2/noncomm_use_subset/noncomm_use_subset/pmc_json'

papers_dict = {}
for root, dirnames, filenames in os.walk(root_folder_path):
    for filename in filenames:
        if filename != '.DS_Store':           
            with open(os.path.join(root, filename)) as file:
yde                paper_in_json = json.load(file)
                papers_dict[paper_in_json['paper_id']] = pd.json_normalize(paper_in_json['body_text']) 

corpus = []
tokens = []
for paper_key in papers_dict.keys():
    if 'text' in papers_dict[paper_key].keys():
        for index, value in papers_dict[paper_key]['text'].items():
            corpus.append(value)
            tokens.extend(word_tokenize(value))


stopwords = nltk.corpus.stopwords.words('english')
sw_tokens = [token for token in tokens if token not in stopwords]         

lexicon = sorted(set(sw_tokens))
    
bag_of_words = Counter(sw_tokens)

bag_of_words.most_common(50)

bag_of_words['depends']


count_vectorizer = CountVectorizer()
word_count_vector = count_vectorizer.fit_transform(corpus)


NUM_TOPICS = 20
NUM_TOPICS_ELEMENTS = 50



def print_topics(model, count_vectorizer, top_n=50):
    lda_dict = {}
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        topic_members_weights = [(count_vectorizer.get_feature_names()[i], topic[i])
                        for i in topic.argsort()[:-top_n - 1:-1]]
        print(topic_members_weights)   

        topic_members = []
        for element in topic_members_weights[:NUM_TOPICS_ELEMENTS]:
            topic_members.append(element[0])
        lda_dict[idx] = topic_members                   
        print()
    return lda_dict
        
# Build a Latent Dirichlet Allocation Model
lda_model = LatentDirichletAllocation(n_components=NUM_TOPICS, 
                                      max_iter=15, 
                                      learning_method='online')
lda_Z = lda_model.fit_transform(word_count_vector)
# print(lda_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)

print("LDA Model:")
# print_topics(lda_model, count_vectorizer)

lda_dict = print_topics(lda_model, count_vectorizer)
print_topics(lda_model, count_vectorizer)

papers_dict2 = {}
for root, dirnames, filenames in os.walk(root_folder_path):
    for filename in filenames:
        if filename != '.DS_Store':           
            with open(os.path.join(root, filename)) as file:
                paper_in_json = json.load(file)
                papers_dict2[paper_in_json['paper_id']] = paper_in_json['body_text']