# Dynamic Deep Network Models

This repository contains code and examples for training Dynamic Deep Network (DDN) models that can adapt to evolving data distributions. 

## Background

Neural network models are typically trained on static datasets with fixed data distributions. In real-world scenarios, the underlying data distribution often changes over time due to various factors. When these distributional shifts occur, the performance of models trained on the original data can deteriorate.

DDN models offer a solution by enabling models to continuously learn and adapt from new data as it becomes available. This allows the models to track changes in the data distribution in a controlled manner.

## Approach

We use State Space Models (SSMs) based on the Extended Kalman Filter (EKF) for training DDN models, rather than standard training algorithms like gradient descent. 

With EKF, we obtain not only the model weights, but also the uncertainties over the weights. This allows finely controlling the adaptation rate of different parts of the model to new data by tweaking the prior uncertainties.

## Contents

This repo contains:

- Implementations of DDN training algorithms based on EKF  
- Examples and animations demonstrating DDN model adaptation on toy datasets with shifting distributions
- An application of DDN models for multiple sensor object tracking with changing dynamics

## More Details

See the [presentation](resources/Team_Presentation.pdf) for more details on the background, motivation, and technical approach for this project. 

## Authors

This project was developed by:

- [Abraham (Avi) Linzer](https://www.linkedin.com/in/abraham-linzer-318876231/)
- [Joseph Couzens](https://www.linkedin.com/in/josephcouzens/)
- [Michael Batushansky](https://www.linkedin.com/in/michael-batushansky-aa5986205)
- [Michael Kupferstein](https://www.linkedin.com/in/michael-kupferstein-50967124a/)
- [Tani Gross](https://www.linkedin.com/in/jonathan-gross-001189279/)

Under the mentorship of [Ramesh Natarajan](https://www.linkedin.com/in/ramesh-natarajan-07a05989/).
