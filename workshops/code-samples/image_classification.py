"""
GDG WOW Pune - AI/ML Workshop April 2025
Image Classification with TensorFlow and Vertex AI

This sample code demonstrates how to build a simple image classification model
using TensorFlow and deploy it to Vertex AI.
"""

import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define paths and parameters
DATA_DIR = 'data/images'
IMG_HEIGHT, IMG_WIDTH = 150, 150
BATCH_SIZE = 32
EPOCHS = 10
MODEL_PATH = 'saved_models/image_classifier'

def build_model(num_classes):
    """Build a simple CNN model for image classification."""
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def prepare_data():
    """Prepare and augment image data."""
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )
    
    train_generator = train_datagen.flow_from_directory(
        DATA_DIR,
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )
    
    validation_generator = train_datagen.flow_from_directory(
        DATA_DIR,
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )
    
    return train_generator, validation_generator

def train_model():
    """Train the image classification model."""
    # Prepare data
    train_generator, validation_generator = prepare_data()
    num_classes = len(train_generator.class_indices)
    
    # Build and train model
    model = build_model(num_classes)
    
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE
    )
    
    # Save the model
    if not os.path.exists(os.path.dirname(MODEL_PATH)):
        os.makedirs(os.path.dirname(MODEL_PATH))
    
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    
    return history, model

def vertex_ai_deploy(project_id, model_path, endpoint_name):
    """
    Deploy the model to Vertex AI.
    Note: This is a placeholder function that would be implemented
    with the actual Vertex AI SDK code in the workshop.
    """
    print(f"Deploying model from {model_path} to Vertex AI endpoint {endpoint_name}")
    # In the actual workshop, we would include the vertex_ai import and deployment code
    
    # Example deployment code (commented out):
    # from google.cloud import aiplatform
    # 
    # aiplatform.init(project=project_id, location='us-central1')
    # model = aiplatform.Model.upload(
    #     display_name=endpoint_name,
    #     artifact_uri=model_path,
    #     serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-8:latest"
    # )
    # endpoint = model.deploy(
    #     machine_type="n1-standard-4",
    #     min_replica_count=1,
    #     max_replica_count=1
    # )
    
    print("Deployment placeholder - See workshop materials for full implementation")

if __name__ == "__main__":
    print("GDG WOW Pune - AI/ML Workshop April 2025")
    print("Image Classification with TensorFlow and Vertex AI")
    print("------------------------------------------------")
    print("Note: This sample code is for demonstration purposes.")
    print("See workshop materials for complete implementation details.")
    
    # Uncomment the following lines to run the training process
    # history, model = train_model()
    
    # Example deployment (would be done in the workshop with actual credentials)
    # vertex_ai_deploy(
    #     project_id="your-gcp-project-id",
    #     model_path=MODEL_PATH,
    #     endpoint_name="image-classifier-endpoint"
    # )
