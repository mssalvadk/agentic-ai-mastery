import yaml
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import BaseEstimator, TransformerMixin

class TextCleaner(BaseEstimator, TransformerMixin):
    """Custom transformer for Agentic input cleaning."""
    def fit(self, X, y=None): return self
    def transform(self, X):
        return [text.lower().strip() for text in X]

def build_pipeline(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Implementing a reusable, modular Scikit-learn structure
    pipeline = Pipeline([
        ('cleaner', TextCleaner()),
        ('tfidf', TfidfVectorizer(max_features=config['pipeline']['preprocessing']['max_length'])),
        ('clf', RandomForestClassifier(n_estimators=100))
    ])
    
    return pipeline

if __name__ == "__main__":
    model_pipeline = build_pipeline('../config/pipeline_config.yaml')
    print(f"Successfully initialized: {model_pipeline}")