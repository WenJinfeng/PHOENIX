# PHOENIX: Misconfiguration Detection for AWS Serverless Computing

We provide the used dataset, code of our tool PHOENIX, and evaluation data.

!!!We provide new experiments and results in the directory **NewAddExperimentData**.

1. The LLM-related implementations: **Simple_LLM.py**, **Three_Few_shot_LLM.py**, and **LLM Results.xlsx**

2. The compared pattern mining algorithm (N Painting Growth algorithm) implementation: **AWSRuleMiningUsingN-Painting.ipynb**

3. The evaluation dataset and the detection results of our approach and AWS SAM CLI: **injected misconfiguration information-updatedResults.xlsx** and **realworld problem information-update.xlsx**


## Used dataset

The used dataset is saved in the directory "Dataset".

- The directory "configuration files-real" contains **733 real-world configuration files** with 701 configuration files from 658 serverless applications in AWS SAR and 32 configuration cases from GitHub.
    - The detailed information of these real-world configuration files is described in the file "real dataset info.xlsx".
    - They are used to conduct a study in Section 3 and learn the patterns of our tool PHOENIX.

- The directory "configuration files-office" contains sample configuration files provided in the official documentation.
    - The detailed information of these examples is partially described in the file "official dataset info.xlsx".
    - They are used to learn the patterns of our tool PHOENIX.



## Code of our tool PHOENIX

The required libraries in our tool are recorded in the file "requirement.txt". 

#### Data collection, data conversion, and pattern mining

- The dataset collection includes two scripts:
    - AWS SAR dataset: the code file "Get_sar.py" can collect relevant AWS serverless applications.
    - GitHub issue dataset: the code file "Get_github_issue.py" can collect relevant GitHub issues.
- The learned patterns are saved in the directory "Patterns".
- The code file "AWSupdate_data.ipynb" can learn the patterns about configuration resource types, configuration entries, and configuration entry values.
- The code file "AWSRuleMining.ipynb" can learn the patterns about coarse-grained and fine-grained configuration dependencies.
- The code file "GeneralMethod.py" contains some general method implementation.

#### Misconfiguration Detection

- The code file "approachAWS.ipynb" conducts misconfiguration detection for a tested configuration file of the serverless application.
- The learned patterns can be read only once, and then the tests are constantly carried out on the configuration file to be tested.



## Evaluation data


- Experimental evaluation 1 for 35 injected misconfigurations on 20 correct configuration files that are newly selected.
    - The directory "correct file" includes 20 correct configuration files, from EvaluationFile1.yaml to EvaluationFile20.yaml.
    - The specific links about 20 correct configuration files and corresponding injected strategies are provided in the file "injected misconfiguration information.xlsx"


- Experimental evaluation 2 for 70 real-world misconfigurations that are newly selected from GitHub. 
    - The specific links of these configuration problems are provided in the file "realworld problem information.xlsx".

