
# Capstone Project - Azure ML Engineer

*TODO:* Write a short introduction to your project.

## Dataset

### Overview
This is the Heart Failure Prediction Dataset taken from Kaggle [link here](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction). It consists of 11 features and 1 target (HeartDisease: 1,0)

### Task
The task is Classification, with the HeartDisease target: 1 is patient having heart disease and 0 is not having. As there are relatively few features, I will use all 11 of them.

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
I uploaded the dataset to github and access the dataset using URL. I access using Dataset.Tabular and register dataset to workspace.

## Automated ML

Settings:

- **Experiment Timeout**: Max of 30 minutes, so the process completes in a reasonable timeframe.
- **Concurrent Iterations**: Up to 5 iterations are allowed to run concurrently to speed up training.
- **Primary Metric**: Accuracy, to match with the logistic regression hyperdrive config later.
- **Early Stopping**: Enabled to halt training if further iterations are unlikely to improve model performance.

Config:
- **Task**: Classification
- **Dataset**: Only train 80% of dataset to match setting of hyperdrive (`test_size` = 0.2).
- **Label**: column "HeartDisease"
- **Featurization**: Feature engineering is automatically handled by the system (`featurization` = 'auto').
- **Logging**: Debug logs are stored in "automl_errors.log"

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?
<img width="369" alt="Screenshot 2024-10-21 at 18 33 45" src="https://github.com/user-attachments/assets/6c7a626b-62f7-4b93-8b13-415282c909f2">

<img width="956" alt="Screenshot 2024-10-21 at 18 29 54" src="https://github.com/user-attachments/assets/70ba0314-24d9-4e4b-a80e-56a566f4399e">

<img width="973" alt="Screenshot 2024-10-21 at 18 28 51" src="https://github.com/user-attachments/assets/a95346d7-9a95-408a-9282-a9f938118b4f">

<img width="836" alt="Screenshot 2024-10-21 at 18 35 51" src="https://github.com/user-attachments/assets/a9a570b7-91bd-4939-8b57-0f6917a5af4b">

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search
<img width="946" alt="Screenshot 2024-10-21 at 18 39 06" src="https://github.com/user-attachments/assets/a69a390a-61ba-456b-89e3-726682adf69b">
<img width="1005" alt="Screenshot 2024-10-21 at 18 40 09" src="https://github.com/user-attachments/assets/f528728d-591b-446c-aa19-877db30e2e17">
<img width="964" alt="Screenshot 2024-10-21 at 18 41 37" src="https://github.com/user-attachments/assets/be650309-a911-4950-bbd7-956c411f7055">


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response
