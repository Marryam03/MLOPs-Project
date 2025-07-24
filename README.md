# MLOPs-Project
This project is an end-to-end MLOps pipeline for malware classification using machine learning. It includes data preprocessing, model training, API deployment with Flask, containerization with Docker, orchestration with Kubernetes, and CI/CD integration using Azure Pipelines.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Model Training](#model-training)
- [API Usage](#api-usage)
- [Dockerization](#dockerization)
- [Kubernetes Deployment](#kubernetes-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Data Preprocessing:** Cleans and prepares malware dataset for training.
- **Feature Selection:** Uses Random Forest feature importances to select relevant features.
- **Model Training:** Trains a Random Forest classifier with SMOTE for class balancing.
- **Model Serialization:** Saves the trained model as `SavedWeights.joblib`.
- **REST API:** Flask-based API for serving predictions.
- **Containerization:** Dockerfile for easy deployment.
- **Kubernetes Ready:** Deployment and service YAML for scalable orchestration.
- **CI/CD:** Automated build and deployment pipeline using Azure DevOps.

---

## Model Training:

- Loads and preprocesses the dataset.
- Performs feature selection to reduce dimensionality.
- Encodes labels using `LabelEncoder`.
- Applies SMOTE to handle class imbalance.
- Trains a Random Forest classifier.
- Evaluates the model and prints classification metrics.
- Saves the trained model as `SavedWeights.joblib`.

**Output:**
- Model Accuracy: ~91%
- Supports 15 malware/benign classes.

---

## API Usage

The Flask API (`app.py`) exposes a `/predict` endpoint:

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Input:** JSON with a `text` key containing a list of feature dictionaries.
- **Output:** JSON with predicted class labels.

**Example Request:**
```json
POST /predict
{
  "text": [
    {"feature1": value1, "feature2": value2, ...},
    ...
  ]
}
```

**Example Response:**
```json
{
  "answer": ["Adware", "Trojan", ...]
}
```

---

## Dockerization

Build and run the API in a Docker container:

```bash
# Build the Docker image
docker build -t mlopsproject:latest .

# Run the container
docker run -p 5000:5000 mlopsproject:latest
```

---

## Kubernetes Deployment

Deploy the application using Kubernetes:

1. **Build and push the Docker image** to your container registry (see CI/CD section).
2. **Apply the deployment and service:**
   ```bash
   kubectl apply -f deployment.yaml
   ```
3. The service is exposed as a LoadBalancer on port 80.

---

## CI/CD Pipeline

- **Azure Pipelines:** The `azure-pipelines.yml` file automates Docker image build and push to Azure Container Registry on every commit to the `main` branch.
- **Kubernetes Deployment:** The `ci-cd-pipeline.yaml` and `deployment.yaml` files define the deployment and service for Kubernetes.

---

## Requirements

- Python 3.8+
- Flask
- pandas
- scikit-learn==1.2.2
- joblib
- imbalanced-learn (for training, in notebook)
- Docker (for containerization)
- Kubernetes (for orchestration)
- Azure DevOps (for CI/CD)

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Setup Instructions

1. **Train the Model:**
   - Run `MLOPS_Project2.ipynb` to preprocess data and train the model.
   - Ensure `SavedWeights.joblib` is generated in the project root.

2. **Run the API Locally:**
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000/predict`.

3. **Containerize and Deploy:**
   - Build and run with Docker as shown above.
   - Deploy to Kubernetes using the provided YAML files.

4. **CI/CD:**
   - Configure Azure DevOps with your container registry credentials.
   - Push to `main` to trigger the pipeline.

