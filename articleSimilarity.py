# -*- coding: utf-8 -*-
'''
    This class provides us with the similarity probability of students work and an article 
'''
from polyglot.mapping import Embedding
import numpy as np

class ArticleSimilarity:
    def __init__(self, student_summary=[]):
        self.punctuations = ['.', ',', '[', ']', '(', ')']
        self.stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
        self.student_summary = [ self.clean_doc(s) for s in student_summary ]
        self.embeddings = Embedding.load("data/embeddings_pkl.tar.bz2")
        self.summary_vetors = []
        for summary in self.student_summary:
            self.summary_vetors.append(self.calculate_doc2vec(summary))
        
    def similarity(self, article=""):
        article = self.clean_doc(article)
        article_vector = self.calculate_doc2vec(article)
        similarities = []
        for sv in self.summary_vetors:
            similarities.append(np.linalg.norm(sv - article_vector))
        return reduce(lambda x, y: x + y, similarities) / len(similarities)

    def calculate_doc2vec(self, doc):
        embeddings = []
        for word in doc.split():            
            emb = self.get_word_embeddings(word)
            if emb is not None:
                embeddings.append(emb)
        embeddings_numpy = np.array(embeddings)
        return np.mean(embeddings_numpy, axis=0)
    
    # remove common stop words from doc
    def remove_stop_words(self, doc):
        cleaned_doc = []
        for word in doc.split():
            if word in self.stop_words:
                continue
            cleaned_doc.append(word)
        return ' '.join(cleaned_doc)

    # remove punctuations from doc
    def remove_punctuations(self, doc):
        cleaned_doc = ""
        for c in doc:
            if c in self.punctuations:
                continue
            cleaned_doc += c
        return cleaned_doc
    
    def clean_doc(self, doc):
        return self.remove_stop_words(self.remove_punctuations(doc))

    def get_word_embeddings(self, word):
        return self.embeddings.get(word)


'''
    To find the overall similarity between a professor research and a student work
'''
class OverAllSimilarity:
    def __init__(self, student_summary=[]):
        self.student_summary = student_summary
        self.arsim = ArticleSimilarity(self.student_summary)
        
    def calculate_overall_similarity(self, articles=[]):
        articles_similarities = []
        for article in articles:
            articles_similarities.append(self.arsim.similarity(article))
        return articles_similarities


def main():
    # test ArticleSimilarity class
    summary = ["Automatic speech recognition has been a challenging task for many decades. With the advent of deep learning algorithms and availability of large speech datasets along with exponentially growth of computational power in the past decade, we are now closer than anytime to conquer this challenging task. However, we are far away from a language independent speech recognition system and yet state-of-the-art ASRs are trained for a specific language.In this thesis we focus on building an automatic speech recognition system for Persian language. Language dependent ASR systems causes’ language related challenges due to the fact that different languages have their own underlying structure, including different set of phones, different vocabulary, different grammar and etc. Another challenge, language dependent ASR systems face with is the need for a training speech dataset in that specific language. Throughout this thesis we will indicate Persian language ASR system challenges and the way we tried to resolve these obstacles."]
    articles = ["Recurrent neural networks (RNNs) are a powerful model for sequential data. End-to-end training methods such as Connectionist Temporal Classification make it possible to train RNNs for sequence labelling problems where the input-output alignment is unknown. The combination of these methods with the Long Short-term Memory RNN architecture has proved particularly fruitful, delivering state-of-the-art results in cursive handwriting recognition. However RNN performance in speech recognition has so far been disappointing, with better results returned by deep feedforward networks. This paper investigates \emph{deep recurrent neural networks}, which combine the multiple levels of representation that have proved so effective in deep networks with the flexible use of long range context that empowers RNNs. When trained end-to-end with suitable regularisation, we find that deep Long Short-term Memory RNNs achieve a test set error of the TIMIT phoneme recognition benchmark, which to our knowledge is the best recorded score.", \
    "Many real-world sequence learning tasks require the prediction of sequences of labels from noisy, unsegmented input data. In speech recognition, for example, an acoustic signal is transcribed into words or sub-word units. Recurrent neural networks (RNNs) are powerful sequence learners that would seem well suited to such tasks. However, because they require pre-segmented training data, and post-processing to transform their outputs into label sequences, their applicability has so far been limited. This paper presents a novel method for training RNNs to label unsegmented sequences directly, thereby solving both problems. An experiment on the TIMIT speech corpus demonstrates its advantages over both a baseline HMM and a hybrid HMM-RNN.", \
    "We present a simple technique that allows capsule models to detect adversarial images. In addition to being trained to classify images, the capsule model is trained to reconstruct the images from the pose parameters and identity of the correct top-level capsule. Adversarial images do not look like a typical member of the predicted class and they have much larger reconstruction errors when the reconstruction is produced from the top-level capsule for that class. We show that setting a threshold on the l2 distance between the input image and its reconstruction from the winning capsule is very effective at detecting adversarial images for three different datasets. The same technique works quite well for CNNs that have been trained to reconstruct the image from all or part of the last hidden layer before the softmax. We then explore a stronger, white-box attack that takes the reconstruction error into account. This attack is able to fool our detection technique but in order to make the model change its prediction to another class, the attack must typically make the adversarial image resemble images of the other class.", \
    "Convolutional Neural Networks (CNNs) are effective models for reducing spectral variations and modeling spectral correlations in acoustic features for automatic speech recognition (ASR). Hybrid speech recognition systems incorporating CNNs with Hidden Markov Models/Gaussian Mixture Models (HMMs/GMMs) have achieved the state-of-the-art in various benchmarks. Meanwhile, Connectionist Temporal Classification (CTC) with Recurrent Neural Networks (RNNs), which is proposed for labeling unsegmented sequences, makes it feasible to train an end-to-end speech recognition system instead of hybrid settings. However, RNNs are computationally expensive and sometimes difficult to train. In this paper, inspired by the advantages of both CNNs and the CTC approach, we propose an end-to-end speech framework for sequence labeling, by combining hierarchical CNNs with CTC directly without recurrent connections. By evaluating the approach on the TIMIT phoneme recognition task, we show that the proposed model is not only computationally efficient, but also competitive with the existing baseline systems. Moreover, we argue that CNNs have the capability to model temporal correlations with appropriate context information.", "hello"]
    arsim = ArticleSimilarity(student_summary=[summary])
    print arsim.similarity(articles[0])
    # test OverAllSimilarity class
    oas = OverAllSimilarity(student_summary=[summary])
    print oas.calculate_overall_similarity(articles)

if __name__ == "__main__":    
    main()