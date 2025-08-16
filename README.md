# Social Media Sentiment Analysis on Public Topics Using Turkish BERT Models

A research project focused on analyzing public sentiment in Turkish social media content using NLP and deep learning techniques. The study explores how public opinion trends are shaped around sensitive or widely discussed topics through publicly available data.

> 🔍 **Note**: This project uses only publicly accessible social media data for academic research purposes. No private or identifiable user information was collected. All analysis is anonymized and conducted ethically.

---

## 🎯 Project Overview

- Analyzed Turkish tweets using NLP and hybrid machine learning/deep learning approaches.
- Explored sentiment classification of social discourse around a highly discussed topic (anonymized).
- Compared performance of multiple pre-trained Turkish BERT models and fine-tuned variants.
- Implemented a hybrid modeling approach combining deep learning outputs with classical ML classifiers.

---

## 🛠 Technologies Used

- **Programming**: Python 3.10  
- **Platform**: Google Colab  
- **Web Scraping**: Selenium WebDriver (for public data collection)  
- **Data Processing**: Pandas, NumPy, Regex, urlextract  
- **NLP Models**: Hugging Face Transformers (Turkish BERT variants), PyTorch  
- **Machine Learning**: Scikit-learn (Random Forest, SVM, k-NN)  
- **Visualization**: Matplotlib, WordCloud  
- **Model Training**: GPU-accelerated training via Torch  

---

## 🗂 Data Collection & Preprocessing

- **Source**: Publicly available social media posts (X.com / Twitter)  
- **Keyword Filter**: Topic-specific term (anonymized)  
- **Preprocessing Steps**:
  - Removed duplicate entries
  - Filtered tweets with fewer than 3 words
  - Replaced URLs, @mentions, and emojis with placeholders
  - Removed stop words (preserving contextually meaningful tokens)

---

## 🔍 Model Evaluation & Results

### ✅ Best Performing Models
| Model | Accuracy | Macro F1 |
|------|----------|----------|
| `akoksal/bounti` | 72.0% | 0.700 |
| `VRLLab/TurkishBERTweet` | 75.0% | 0.697 |

> ⚠️ *Fine-tuned model achieved optimal results at 75% accuracy with 0.697 F1 score.*

### 🔁 Hybrid Approach
- Fine-tuned BERT outputs used as input features for Random Forest.
- **Hybrid model accuracy**: **83.51%**
- Outperformed standalone deep learning and traditional ML models.

### 📊 Confidence Threshold Analysis
| Threshold | Accuracy | F1 Score | Coverage |
|---------|----------|----------|----------|
| 0.50    | 71.43%   | 0.665    | 98.0%    |
| 0.65 (Optimal) | 75.00% | 0.697 | 88.0% |
| 0.95    | 78.57%   | 0.661    | 56.0%    |

---

## 📈 Visualizations
- Positive/neutral/negative sentiment distribution
- Monthly sentiment trend lines
- Word clouds (pre/post-cleaning)
- Top engaging posts and users (anonymized)
- Average engagement per post (likes, retweets, comments)

---

## ✅ Validation
- 50 manually labeled tweets used for testing
- Final model performance:
  - **Accuracy**: 75%
  - **Macro F1 Score**: 0.697

---

## 🎯 Research Goals
- Develop a custom Turkish sentiment classifier for public discourse
- Expand data augmentation techniques
- Publish findings in an open-access academic paper
- Share code and dataset responsibly under research license

---

## 📚 References
- `akoksal/bounti` – Hugging Face  
- `VRLLab/TurkishBERTweet` – Hugging Face  
- Scikit-learn, PyTorch, Pandas  
- Academic papers on Turkish NLP and sentiment analysis

---


---

## 📝 License & Ethical Note
This project is for **academic and research purposes only**.  
No personal, political, or sensitive data was collected.  
All results are anonymized and presented for educational use.  
