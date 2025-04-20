#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Introduction to Machine Learning - Sample Code
For GDG WOW Pune AI/ML Workshops

This script demonstrates basic ML concepts using scikit-learn:
1. Data loading and exploration
2. Data preprocessing
3. Model training
4. Model evaluation
5. Visualization

Prerequisites:
- Python 3.8+
- scikit-learn
- pandas
- matplotlib
- seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

# Set the visual style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

def load_and_explore_data():
    """
    Load sample dataset and perform basic exploration
    """
    # Load the breast cancer dataset (binary classification)
    data = load_breast_cancer()
    
    # Create a DataFrame
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    
    print(f"Dataset shape: {df.shape}")
    print("\nFeatures:")
    for i, feature in enumerate(data.feature_names):
        print(f"  - {feature}")
    
    print(f"\nTarget names: {data.target_names}")
    print(f"Class distribution: {df['target'].value_counts()}")
    
    # Display basic statistics
    print("\nBasic statistics:")
    print(df.describe().T)
    
    # Visualize correlations
    plt.figure(figsize=(16, 12))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', linewidths=0.5)
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png')
    
    return df, data.feature_names, data.target_names

def preprocess_data(df):
    """
    Preprocess the data for model training
    """
    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test

def train_and_evaluate_models(X_train, X_test, y_train, y_test):
    """
    Train and evaluate different ML models
    """
    # Dictionary to store model performance
    results = {}
    
    # 1. Logistic Regression
    print("\nTraining Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train, y_train)
    
    # Evaluate
    y_pred_lr = lr_model.predict(X_test)
    accuracy_lr = accuracy_score(y_test, y_pred_lr)
    results['Logistic Regression'] = {
        'accuracy': accuracy_lr,
        'predictions': y_pred_lr,
        'model': lr_model
    }
    
    print(f"Logistic Regression Accuracy: {accuracy_lr:.4f}")
    print("\nClassification Report (Logistic Regression):")
    print(classification_report(y_test, y_pred_lr))
    
    # 2. Random Forest
    print("\nTraining Random Forest...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Evaluate
    y_pred_rf = rf_model.predict(X_test)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    results['Random Forest'] = {
        'accuracy': accuracy_rf,
        'predictions': y_pred_rf,
        'model': rf_model
    }
    
    print(f"Random Forest Accuracy: {accuracy_rf:.4f}")
    print("\nClassification Report (Random Forest):")
    print(classification_report(y_test, y_pred_rf))
    
    # Visualize confusion matrices
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Logistic Regression confusion matrix
    cm_lr = confusion_matrix(y_test, y_pred_lr)
    sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', ax=axes[0])
    axes[0].set_title('Logistic Regression Confusion Matrix')
    axes[0].set_xlabel('Predicted Label')
    axes[0].set_ylabel('True Label')
    
    # Random Forest confusion matrix
    cm_rf = confusion_matrix(y_test, y_pred_rf)
    sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', ax=axes[1])
    axes[1].set_title('Random Forest Confusion Matrix')
    axes[1].set_xlabel('Predicted Label')
    axes[1].set_ylabel('True Label')
    
    plt.tight_layout()
    plt.savefig('confusion_matrices.png')
    
    return results

def feature_importance_analysis(model, feature_names):
    """
    Analyze feature importance for Random Forest model
    """
    # Get feature importances
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    # Plot feature importances
    plt.figure(figsize=(12, 8))
    plt.title('Feature Importance')
    plt.bar(range(len(importances)), importances[indices], align='center')
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    
    print("\nTop 10 most important features:")
    for i in range(10):
        print(f"{i+1}. {feature_names[indices[i]]} ({importances[indices[i]]:.4f})")

def main():
    """
    Main function to run the ML workflow
    """
    print("=" * 80)
    print("GDG WOW Pune - Introduction to Machine Learning")
    print("=" * 80)
    
    # 1. Load and explore data
    df, feature_names, target_names = load_and_explore_data()
    
    # 2. Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(df)
    
    # 3. Train and evaluate models
    results = train_and_evaluate_models(X_train, X_test, y_train, y_test)
    
    # 4. Analyze feature importance
    rf_model = results['Random Forest']['model']
    feature_importance_analysis(rf_model, feature_names)
    
    print("\nAll visualizations have been saved to the current directory.")
    print("=" * 80)

if __name__ == "__main__":
    main()