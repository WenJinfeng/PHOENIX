# SCOMD: Misconfiguration Detection for AWS Serverless Computing

We provide the used dataset, code of our tool SCOMD, and evaluation data.


## Used dataset

The used dataset is saved in the directory "Dataset".

- The directory "configuration files-real" contains **733 real-world configuration files** with 701 configuration files from 658 serverless applications in AWS SAR and 32 configuration cases from GitHub.
    - The detailed information of these real-world configuration files are described in the file "real dataset info.xlsx".
    - They are used to conduct a study in Section 3 and learn the patterns of our tool SCOME.

- The directory "configuration files-office" contains sample configuration files provided in the official documentation.
    - The detailed information of these examples are partially described in the file "official dataset info.xlsx".
    - They are used to learn the patterns of our tool SCOME.



## Code of our tool SCOME

The required libaries in our tool are recoreded in the file "requirement.txt". 

#### Data collection, data convertion, and pattern mining

- The learned patterns is saved in the directory "Patterns".
- The code file "AWSupdate_data.ipynb" can learn the patterns about configuration resource types, configuration entries, and configuration entry values.
- The code file "AWSRuleMining.ipynb" can learn the patterns about coarse-grained and fine-grained configuration denpendencies.
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

