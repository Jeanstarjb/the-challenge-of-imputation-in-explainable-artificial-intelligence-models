# The Challenge of Imputation in Explainable Artificial Intelligence Models

This repository contains the implementation of experiments and methods discussed in the research paper "[The Challenge of Imputation in Explainable Artificial Intelligence Models](https://arxiv.org/pdf/1907.12669v1)" by Muhammad Aurangzeb Ahmad, Carly Eckert, and Ankur Teredesai. The paper investigates the impact of data imputation on the fidelity of explanations produced by Explainable Artificial Intelligence (XAI) models and suggests ways to address scenarios where imputation could lead to unsafe outcomes.

---

## Table of Contents

- [Overview](#overview)
- [Core Concept](#core-concept)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Experiments](#experiments)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Explainable AI (XAI) models are increasingly used in critical applications requiring transparency and accountability, such as healthcare and finance. However, the fidelity of these models' explanations can be adversely affected by missing data in real-world datasets. The common practice of imputing missing values may introduce counterfactual scenarios—situations that do not align with real-world possibilities. This can lead to misleading explanations and potentially unsafe decisions.

This repository provides a Python/PyTorch-based implementation to reproduce the findings of the paper. The code demonstrates the challenges posed by data imputation in XAI and explores mitigation strategies.

---

## Core Concept

The paper highlights the following key points:

1. **Explainable AI and Data Fidelity:**
   - XAI models rely on the fidelity of input data to provide accurate and meaningful explanations.
   - Missing data in real-world scenarios is often handled using imputation techniques such as mean, median, or model-based imputation.

2. **Imputation Challenges:**
   - Imputed values may create counterfactual scenarios, leading to incorrect or misleading explanations.
   - Acting on these imprecise explanations can have severe consequences, especially in high-stakes applications.

3. **Proposed Methodology:**
   - The paper explores synthetic and real-world datasets to demonstrate how imputation affects explanation fidelity.
   - It outlines best practices and mitigation strategies to minimize risks associated with imputation in XAI models.

By providing a practical implementation, this repository allows researchers and practitioners to better understand and address the imputation-related challenges in XAI systems.

---

## Repository Structure

The repository is organized as follows:

```
.
├── data/
│   ├── sample_dataset.csv         # Example dataset with missing values
│   └── synthetic_dataset.csv      # Synthetic dataset for experiments
├── models/
│   ├── xai_model.py               # Implementation of an explainable AI model
│   └── imputation_methods.py      # Common imputation techniques (mean, median, etc.)
├── notebooks/
│   ├── exploratory_analysis.ipynb # Jupyter Notebook for data exploration
│   └── experiments.ipynb          # Notebook to reproduce paper's experiments
├── results/
│   └── output_analysis/           # Saved outputs and visualizations
├── utils/
│   └── data_preprocessing.py      # Helper functions for handling missing data
├── main.py                        # Entry point for running the experiments
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## Installation

To run the code, follow these steps:

1. Clone this repository:
   ```
   git clone https://github.com/your-username/xai-imputation-challenge.git
   cd xai-imputation-challenge
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Code
1. Prepare the dataset:
   - Place your dataset in the `data/` directory (e.g., `data/sample_dataset.csv`).
   - Ensure the dataset contains missing values for imputation experiments.

2. Run the experiments:
   ```
   python main.py
   ```

3. View the results:
   - Output files and visualizations will be saved in the `results/output_analysis/` directory.

### Jupyter Notebooks
For a step-by-step walkthrough of the experiments, open the Jupyter Notebooks provided in the `notebooks/` directory:
   ```
   jupyter notebook notebooks/exploratory_analysis.ipynb
   jupyter notebook notebooks/experiments.ipynb
   ```

---

## Experiments

The following experiments are included in this repository:

1. **Exploratory Data Analysis:**
   - Analyze the structure of datasets with missing values.
   - Visualize the distribution of missing data.

2. **Imputation Techniques:**
   - Implement common imputation methods (mean, median, mode, k-NN, etc.).
   - Evaluate their impact on data distribution and downstream XAI model performance.

3. **Impact on Explainability:**
   - Compare explanations generated by XAI models with and without imputation.
   - Measure the fidelity of explanations and identify counterfactual scenarios.

4. **Mitigation Strategies:**
   - Explore techniques to minimize the adverse effects of imputation on explanation fidelity.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```
   git commit -m "Add your descriptive commit message"
   ```
4. Push to the branch:
   ```
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.