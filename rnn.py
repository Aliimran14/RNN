# -*- coding: utf-8 -*-
"""RNN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o0gqF82Si0Zl0GHBcd_AJQG8yg0BlPqh

Buid a Recurrent Neural Network
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

"""sample data from training"""

# Sample data
sentences = [
    "Machine learning algorithms are powerful tools."
    "I enjoy exploring new algorithms."
    "Learning about AI is captivating."
    "Deep learning models can be complex."
    "I love understanding how neural networks work."
    "The field of data science is evolving rapidly."
    "I find artificial intelligence intriguing."
    "Studying computer vision is exciting."
    "Natural language processing is a fascinating domain."
    "I enjoy coding in Python for data science projects."
    "Building models is a creative process."
    "I love experimenting with different machine learning techniques."
    "The potential of AI to transform industries is amazing."
    "I enjoy staying updated with the latest tech trends."
    "Learning about reinforcement learning is interesting."
    "I find predictive modeling to be very useful."
    "I love solving problems with data analysis."
    "Data preprocessing is a crucial step in machine learning."
    "I enjoy reading research papers on deep learning."
    "I find optimization techniques fascinating."
    "Understanding algorithms helps in developing better solutions."
    "I love the challenge of debugging code."
    "Machine learning applications are diverse and impactful."
    "I enjoy collaborating with others on tech projects."
    "Learning new programming languages is fun."
    "I love working with large datasets."
    "I find feature engineering to be an art."
    "Model evaluation is an essential part of machine learning."
    "I enjoy attending tech conferences."
    "Learning about big data technologies is exciting."
    "I love experimenting with neural network architectures."
    "I find the theory behind machine learning algorithms interesting."
    "I enjoy visualizing data insights."
    "Machine learning models can make accurate predictions."
    "I love the creativity involved in data storytelling."
    "I find unsupervised learning techniques intriguing."
    "I enjoy automating tasks with AI."
    "Learning about AI ethics is important."
    "I love the problem-solving aspect of machine learning."
    "I find cloud computing technologies fascinating."
    "I enjoy using machine learning for real-world applications."
    "I love experimenting with different data preprocessing techniques."
    "I find transfer learning to be a powerful approach."
    "I enjoy working on machine learning projects."
    "Learning about data privacy is crucial."
    "I love the innovation happening in the AI field."
    "I find data visualization tools useful."
    "I enjoy testing and validating machine learning models."
    "I love discovering new machine learning applications."
    "I find ensemble methods to be effective."
    "I enjoy learning from data."
    "Machine learning can provide valuable insights."
    "I love the interdisciplinary nature of AI."
    "I find recommendation systems interesting."
    "I enjoy participating in hackathons."
    "Learning about neural networks is fascinating."
    "I love the potential of AI to solve complex problems."
    "I find sentiment analysis intriguing."
    "I enjoy implementing machine learning algorithms."
    "I love the excitement of discovering patterns in data."
    "I find time series analysis challenging."
    "I enjoy exploring different types of data."
    "Machine learning is transforming various industries."
    "I love working on predictive analytics."
    "I find anomaly detection to be useful."
    "I enjoy studying the mathematics behind machine learning."
    "I love the hands-on experience of building models."
    "I find clustering techniques interesting."
    "I enjoy exploring open-source machine learning libraries."
    "Machine learning can automate complex tasks."
    "I love the flexibility of machine learning models."
    "I find computer vision applications fascinating."
    "I enjoy solving real-world problems with AI."
    "I love the continuous learning aspect of AI."
    "I find reinforcement learning to be challenging."
    "I enjoy experimenting with hyperparameter tuning."
    "Machine learning can improve decision-making processes."
    "I love the creativity involved in feature selection."
    "I find generative models to be fascinating."
    "I enjoy reading about the latest AI advancements."
    "Machine learning can enhance user experiences."
    "I love the diversity of machine learning applications."
    "I find natural language generation intriguing."
    "I enjoy working with text data."
    "Machine learning can optimize business processes."
    "I love the innovation in AI research."
    "I find the concept of machine learning interpretability interesting."
    "I enjoy creating machine learning workflows."
    "Machine learning can uncover hidden patterns."
    "I love the impact of AI on society."
    "I find deep reinforcement learning fascinating."
    "I enjoy developing custom machine learning solutions."
    "Machine learning can improve customer experiences."
    "I love the potential of AI in healthcare."
    "I find the scalability of machine learning models intriguing."
    "I enjoy applying machine learning to finance."
    "Machine learning can enhance security measures."
    "I love the possibilities of AI in creative industries."
    "I find the ethical implications of AI important."
    "I enjoy sharing knowledge about machine learning."
    "This Free Advance AI Course that is helping alot of students to learn the concepts of AI and provides the detailed guideline on how to learn AI. This course enables the students to make their own projects. Updates them with the state of the art technologies and provide all the necessary knowlegde so that they should not be dependend on anyone to be able to learn anything."
]

"""Tokenization and preprocessing data"""

# Initialize the tokenizer
tokenizer = Tokenizer()

# Fit the tokenizer on the provided sentences
tokenizer.fit_on_texts(sentences)

# Get the total number of unique words (plus one for padding)
total_words = len(tokenizer.word_index) + 1
print(total_words)
print(tokenizer.word_index)

# Initialize a list to hold input sequences
input_sequences = []

# Iterate over each sentence
for line in sentences:
    # Convert the sentence to a sequence of integers
    token_list = tokenizer.texts_to_sequences([line])[0]
    # print(token_list)
    # Create n-gram sequences
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)




# Determine the maximum sequence length
max_sequence_len = max([len(x) for x in input_sequences])

# Pad sequences to ensure they are all the same length
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
print(input_sequences)

#initialize the tokenizer
tokennizer = Tokenizer()
#fit the tokenizer on the provided sentencess
tokenizer.fit_on_texts(sentences)
#get the total number of uniqe (plus one for padding)
total_words = len(tokenizer.word_index) + 1
print(total_words)
print(tokenizer.word_index)
#initialize a list to hold input sequence
input_sequences = []
#itrate over each sentences
for line in sentences:
  #convert the sentence to a sequence of integers
  token_list = tokenizer.texts_to_sequences([line])[0]
  #print(token_list)
  #create n-gram sequences
  for i in range(1, len(token_list)):
    n_gram_sequence = token_list[:i+1]
    input_sequences.append(n_gram_sequence)



#Determine the maximum the text lenght
max_sequence_len = max([len(x) for x in input_sequences])

#pad sequences to ensure they are all the same length
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
print(input_sequences)

"""Data preparation"""

# Split data into inputs and labels

# Inputs: All elements of the sequences except the last one
X = input_sequences[:, :-1]
print("Input Data: ",X)

# Labels: The last element of each sequence (the word to predict)
y = input_sequences[:, -1]
print("Labels: ",y)

# Convert labels to one-hot encoded format
y = tf.keras.utils.to_categorical(y, num_classes=total_words)
# print("one hot encoded Vector: ", y)

"""Define the model architecture"""

# Define the RNN model

# Sequential model allows stacking layers in a linear fashion
model = Sequential([
    # Embedding layer to convert word indices to dense vectors of fixed size
    # Input dimension: total number of words, Output dimension: size of embedding vectors
    # Input length: length of input sequences (excluding the last word)
    Embedding(total_words, 10, input_length=max_sequence_len-1),

    # SimpleRNN layer with 30 units, which processes the sequence data
    SimpleRNN(30),

    # Dense output layer with a softmax activation function
    # Output dimension: total number of words (for multi-class classification)
    Dense(total_words, activation='softmax')
])

#compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#train the model
model.fit(X, y, epochs=100, verbose=1)

"""Next word prediction"""

# Function to predict the next word(s) given a seed text
def predict_next_word(seed_text, next_words=10):
    for _ in range(next_words):
        # Convert the seed text to a sequence of integers
        token_list = tokenizer.texts_to_sequences([seed_text])[0]

        # Pad the sequence to match the input length required by the model
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')

        # Predict the probabilities of the next word in the sequence
        predicted = model.predict(token_list, verbose=0)

        # Get the index of the word with the highest probability
        predicted_word_index = np.argmax(predicted, axis=-1)[0]

        # Retrieve the word corresponding to the predicted index
        predicted_word = tokenizer.index_word[predicted_word_index]

        # Append the predicted word to the seed text
        seed_text += " " + predicted_word

    # Return the updated seed text with the predicted word(s)
    return seed_text

# Test the prediction function with a sample input
print(predict_next_word("machine lEARNING algorithms are powerful tools i enjoy exploring new the latest ai advancements machine learning can enhance user experiences i love the potential of ai in data machine learning can enhance"))