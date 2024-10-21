
# Capstone Project - Azure ML Engineer

In this project, I will experiment with a classification task, using 'accuracy' as primary metric, with both auto ML and hyperparameter tuning. The best model from two experiments will be compared and I will deploy the one with higher accuracy. In this repo:
- `heart.csv` is the dataset
- `automl.ipynb` and `hyperparameter_tuning.ipynb` are the two notebooks where I run the two experiments
- `train.py` and `conda_dependencies.yml` are the training script and environment dependecies for hyperdrive config
- `cond_env.yml` is the experiment environment
- `scoring.py` is downloaded after I deploy to put in inference config

## Dataset

### Overview
This is the Heart Failure Prediction Dataset taken from Kaggle [link here](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction). It consists of 11 features and 1 target (HeartDisease: 1,0)

### Task
The task is Classification, with the HeartDisease target: 1 is patient having heart disease and 0 is not having. As there are relatively few features, I will use all 11 of them. Description of the features as taken from Kaggle:

| **Feature**      | **Description**                                                                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Age               | age of the patient [years]                                                                                                                           |
| Sex               | sex of the patient [M: Male, F: Female]                                                                                                              |
| ChestPainType     | chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]                                                  |
| RestingBP         | resting blood pressure [mm Hg]                                                                                                                       |
| Cholesterol       | serum cholesterol [mm/dl]                                                                                                                            |
| FastingBS         | fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]                                                                                      |
| RestingECG        | resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria] |
| MaxHR             | maximum heart rate achieved [Numeric value between 60 and 202]                                                                                        |
| ExerciseAngina    | exercise-induced angina [Y: Yes, N: No]                                                                                                              |
| Oldpeak           | oldpeak = ST [Numeric value measured in depression]                                                                                                   |
| ST_Slope          | the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]                                                             |
| HeartDisease      | output class [1: heart disease, 0: Normal]                                                                                                           |

### Access
I first uploaded the dataset to github, then copy the raw URL. This URL is then used  to access the dataset using URL, with `Dataset.Tabular`. I also registered dataset to workspace for so both AutoML and Hyperdrive notebooks can access the same data.

## Automated ML

Settings:

- **Experiment Timeout**: Max of 30 minutes, so the process completes in a reasonable timeframe.
- **Concurrent Iterations**: Up to 5 iterations run concurrently to speed up training.
- **Primary Metric**: Accuracy, to match with the logistic regression hyperdrive config later.
- **Early Stopping**: Enabled to halt training if further iterations are unlikely to improve model performance.

Config:
- **Task**: Classification
- **Dataset**: Only train 80% of dataset to match setting of hyperdrive (`test_size` = 0.2).
- **Label**: column "HeartDisease"
- **Featurization**: Feature engineering is automatically handled by the system (`featurization` = 'auto').
- **Logging**: Debug logs are stored in "automl_errors.log"

### Results
The best model from the automated ML run is Voting Ensemble, with accuracy 0.877.

<img width="369" alt="Screenshot 2024-10-21 at 18 33 45" src="https://github.com/user-attachments/assets/6c7a626b-62f7-4b93-8b13-415282c909f2">

Screenshot of the `RunDetails` widget:
<img width="836" alt="Screenshot 2024-10-21 at 18 35 51" src="https://github.com/user-attachments/assets/a9a570b7-91bd-4939-8b57-0f6917a5af4b">

Screenshot of run id of best model:
<img width="973" alt="Screenshot 2024-10-21 at 18 28 51" src="https://github.com/user-attachments/assets/a95346d7-9a95-408a-9282-a9f938118b4f">


## Hyperparameter Tuning

I used a simple model: logistic regression, tuning two parameters:
-  `C`: Inverse of regularization strength. Smaller values cause stronger regularization. I pass continuous random value ranged 0.5 to 1.0 discrete.
-  `max_iter`: Maximum number of iterations to converge. I pass discrete values: 16,32,64,128


### Results
Tuning with the above parameter ranges give the highest accuracy of 0.859. The parameter values to get this result is `C=0.843` and `max_iter=128`. I could have improved it with larger ranges, or try add another parameter for tuning as well.
<img width="1005" alt="Screenshot 2024-10-21 at 18 40 09" src="https://github.com/user-attachments/assets/f528728d-591b-446c-aa19-877db30e2e17">

Screenshot of `RunDetails` widget
<img width="946" alt="Screenshot 2024-10-21 at 18 39 06" src="https://github.com/user-attachments/assets/a69a390a-61ba-456b-89e3-726682adf69b">

Screenshot of best model's run ID and parameters
<img width="964" alt="Screenshot 2024-10-21 at 18 41 37" src="https://github.com/user-attachments/assets/be650309-a911-4950-bbd7-956c411f7055">

## Model Deployment
The deployed model is the model from the best run of automl, deployed with authentication insights and authentication enabled

Screenshot showing model endpoint with deployment status Completed, operation status Healthy and endpoint URI:
<img width="645" alt="image" src="https://github.com/user-attachments/assets/cd22de46-37ba-4253-bb99-1b36ff29d92e">

To deploy the model, get the scoring URI and the key. Use key for header authorization and send request to the URI.
Sample input to query the endpoint:
```json
{"data":
  [{"Age": 58, "Sex": "M", "ChestPainType": "ASY", "RestingBP": 120, "Cholesterol": 0, "FastingBS": false, "RestingECG": "LVH", "MaxHR": 106, "ExerciseAngina": true, "Oldpeak": 1.5, "ST_Slope": "Down"},
  {"Age": 47, "Sex": "M", "ChestPainType": "NAP", "RestingBP": 140, "Cholesterol": 193, "FastingBS": false, "RestingECG": "Normal", "MaxHR": 145, "ExerciseAngina": true, "Oldpeak": 1.0, "ST_Slope": "Flat"}]}
```
For this, the expected response should be:
```json
{"result": [true, true]}
```

Sample code to send request to endpoint:
<img width="983" alt="image" src="https://github.com/user-attachments/assets/f8e1978c-ff15-4856-ab93-7bf5725de7ef">


## Screen Recording
[Youtube Screencast](https://www.youtube.com/watch?v=9Qop1wjSyBw)
