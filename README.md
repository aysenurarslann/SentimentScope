# 📊 Sentiment Analysis Project on Social Media Texts

## 🎯 Project Overview
This **academic research project** aims to reveal public sentiment patterns by analyzing social media posts from X platform (formerly Twitter) regarding a specific social topic. Within the framework of **ethical research principles and data privacy standards**, Turkish tweet data was analyzed using natural language processing (NLP) and deep learning methods. Additionally, a hybrid approach combining classical machine learning and deep learning models was tested.

## 🧰 Technologies Used
- Python 3.10
- Google Colab
- Selenium WebDriver – Tweet collection
- Pandas, NumPy – Data processing
- Regex, urlextract – Preprocessing
- Transformers (Hugging Face) – Deep learning models
- Scikit-learn – Machine learning algorithms
- Torch – GPU-supported model training
- Matplotlib, WordCloud – Visualization

## 🗂 Data Collection and Preprocessing
- **Source**: X.com (Twitter) - **For academic research purposes**, publicly available data
- **Method**: Keyword-based collection
- **Ethical Compliance**: Personal data protection and privacy principles were observed
- **Data Processing**: Sufficient amount of tweets were analyzed for research validity

### Applied Cleaning Steps:
- Removal of duplicate tweets
- Filtering tweets with less than 3 words
- Conversion of URLs, mentions, and emojis
- Stopword removal (excluding context determiners)

## 🔍 Modeling and Analysis

### 🎓 Tested Models
| Model Name | Status |
|------------|--------|
| savasy/bert-base-turkish-sentiment-cased | ❌ |
| anilguven/bert_tr_turkish_tweet | ❌ |
| akoksal/bounti | ✅ |
| VRLLab/TurkishBERTweet | ✅ (Main model) |

VRLLab/TurkishBERTweet is a specialized model trained on 894 million tweets, designed for Turkish social media language.

### ⚙️ Fine-Tuning and Data Augmentation
| Stage | Accuracy | Macro F1 | Weighted F1 |
|-------|----------|----------|-------------|
| Base Bounti Model | 68.00% | 0.636 | 0.635 |
| Fine-Tuned Bounti (90 tweets) | 72.00% | 0.700 | 0.690 |
| Fine-Tuned + Augmentation (382 tweets) | 70.00% | 0.642 | 0.650 |

Training data was expanded from 90 tweets to 382 samples through data augmentation.

### 🔒 Confidence Threshold Analysis
| Confidence Threshold | Accuracy | F1 Score | Coverage |
|---------------------|----------|----------|----------|
| 0.50 | 71.43% | 0.665 | 98.00% |
| 0.65 (Optimal) | 75.00% | 0.697 | 88.00% |
| 0.95 | 78.57% | 0.661 | 56.00% |

### 🤖 Classical Machine Learning Models
**For academic evaluation**, manually labeled dataset was used.
Feature Extraction: TF-IDF

| Model | Accuracy | F1 Score (Positive / Neutral / Negative) |
|-------|----------|------------------------------------------|
| Random Forest | 83.61% | 0.74 / 0.61 / 0.90 |
| SVM | 81.88% | 0.75 / 0.49 / 0.89 |
| k-NN | 30.09% | Poor performance |

### 🔁 Hybrid Model Approach
Fine-tuned model outputs were used as input for machine learning models. Random Forest achieved the highest success with 83.51% accuracy in the hybrid approach.

## 📈 Visualizations
- Positive/negative/neutral distribution charts
- Monthly sentiment change lines
- Word clouds (before/after)
- Most interactive tweets and users
- Average likes, comments, retweets per tweet analysis

## ✅ Validation
Performance evaluation was conducted with manually labeled test data according to **academic standards**.
- **Accuracy**: 75%
- **Macro F1 Score**: 0.697

## 🏁 Project Status
### ✔️ Completed
- Comprehensive tweet collection
- NLP preprocessing and visualization
- Testing different models
- Hybrid modeling
- Performance comparisons

### 🎯 Future Goals
- Training custom Turkish sentiment classification model
- Enriching data augmentation methods
- Academic publication preparation

## 📚 References
- VRLLab/TurkishBERTweet
- akoksal/bounti
- scikit-learn



## 📝 License and Usage
This project is **for academic research and educational purposes**. It was conducted in accordance with **ethical research standards** and **data privacy principles**. No personal data was stored or shared. Proper academic citation is required for usage.
