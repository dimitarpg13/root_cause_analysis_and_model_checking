# Causal Inference, Root Cause Analysis (RCA) and Model Checking via Probabilistic Temporal Logic (PTL)

Literature overview on the topic of Process Mining in general and Root Cause Analysis specifically:
Process Mining / RCA literature compendum:
https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/tree/main/literature

Personally, I am quite fascinated by the use of of special kind of logic for model checking - the Probabilistic Temporal Logic (PTL).
But you may ask yourself - why using PTL in RCA ?
Because it allows fairly complex queries to the underlying probabilistic model relevant for particular RCA scenarios to be generalized and expressed in mathematical (PTL) notation which can be implemented via graph algorithms in an elegant way.

The probabilistic model for RCA generally is built by a Markov Chain and is represented by a labeled directed graph, Kripke structure, Petri Net, etc. So the bottom line is that fairly complex RCA analysis queries to the probabilistic model based on the chosen set of events can be performed with generic graph algorithms which are already implemented efficiently in open source libraries.
PTL is an extension of  Computation Tree Logic (CTL). CTL is a superset of linear temporal logic and it is related to first order logic. Also note that CTL  is a  standard method for design/model verification in the analysis and design of VLSI ICs as well as analysis of  the correctness of parallel program execution.

A detailed and thorugh survey by Clarke et al on the most relevant logic systems for model verification can be found here:
[Clarke, E. M., Schlingloff, B. H. (2001). Model Checking](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/literature/ModelChecking/ModelChecking_ClarkeSchlingloff1999.pdf)

As quick intro into Temporal Logic can serve Clarke, Emerson, and Sistla's paper:
[Clarke, E.M., Emerson, E.A., Sistla, A.P. (1983). Automatic Verification Finite State Concurrent Systems Using Temporal Logic Specifications: A Practical Approach](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/literature/ModelChecking/AutomaticVerifictionOfFiniteStateConcurrentSystemUsingTemporalLogicSpecification.pdf)

An excellent tutorial for Probablistic Temporal Logic (PTL) is the Hanssen and Jonsson's paper:
[Hansson, H., Jonsson, B. (1994). A Logic about Reasoning about Time and Reliability](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/literature/ModelChecking/ALogicforReasoningaboutTimeandReliability_Hansson_Johnson_1994.pdf)

A refresher on first order logic which is the fundament of the logic systems for model verification can be found here:
[First-Order Logic, Open Logic Project](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/literature/ModelChecking/first-order-logic-OpenLogicProject.pdf)


## Selected Topics in Machine Learning
 
 * [Reinforcement Learning and Game Theory](https://github.com/dimitarpg13/reinforcement_learning_and_game_theory/blob/main/ReinforcementLearningAndGameTheoryResources.md)

 * [Offline Reinforcement and Self-Supervised Learning](https://github.com/dimitarpg13/self_supervised_learning/blob/main/SelfSupervisedLearningResources.md)

 * [NLP Concepts](https://github.com/dimitarpg13/nlp_concepts/blob/main/NLPResources.md)
 
 * [Transformers](https://github.com/dimitarpg13/transformers_intro/blob/main/TransformersResources.md)
 
 * [Large Language Models](https://github.com/dimitarpg13/large_language_models/blob/main/LargeLanguageModelsResources.md)
 
 * [Bayesian Networks](https://github.com/dimitarpg13/learning_bayesian_networks/blob/main/LearningBayesianNetworksResources.md)
 
 * [Probabilistic Machine Learning](https://github.com/dimitarpg13/probabilistic_machine_learning/blob/main/ProbabilisticMachineLearningResources.md)

 * [Statistical Learning, Kernel Methods, Kolomogorov-Arnold Networks](https://github.com/dimitarpg13/statistical_learning_and_kernel_methods/blob/main/Resources.md)

 * [Optimization, Classification, Regression](https://github.com/dimitarpg13/optimization_classification_regression/blob/main/Resources.md)
 
 * [Causal Inference, Root Cause Analysis and Model Checking](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/RootCauseAnalysisResources.md)

 * [Deep Learning and Neural Networks](https://github.com/dimitarpg13/deep_learning_and_neural_networks/blob/main/Resources.md)

 * [Deep Learning for solving Image Processing problems and Generative Tasks](https://github.com/dimitarpg13/deep_learning_for_image_processing/blob/main/Resources.md)

 * [Hypothesis Testing, Estimation of Treatment Effects and Generalized Synthetic Control](https://github.com/dimitarpg13/generalized_synthetic_control_for_testops/blob/main/Resources.md)
 
 * [Graphs and Dynamic Programming](https://github.com/dimitarpg13/graphs_and_dynamic_programming/blob/master/Resources.md)

 * [Dynamical Systems, State-Space Models, Chaos, Ergodicity](https://github.com/dimitarpg13/dynamical_systems_and_ergodicity/blob/main/Resources.md)

 * [Information Theory, Statistical Mechanics, Diffusion Models](https://github.com/dimitarpg13/information_theory_and_statistical_mechanics/blob/main/Resources.md)

 * [Queueing Networks, Queueing Theory, Reversible Stochastic Processes](https://github.com/dimitarpg13/queueing_theory/blob/main/Resources.md)

 * [Spectral Analysis, Optimization in Spectral Domain, Spectral Domain Modeling](https://github.com/dimitarpg13/spectral_analysis/blob/main/Resources.md)

 * [Computability, Automata, Logic Systems, Formal Grammars and Theory of Parsing](https://github.com/dimitarpg13/computability_and_logic_systems/blob/main/Resources.md)

 * [Thought Forming, Consciousness, Intelligent Machines, Inference, Logic Systems](https://github.com/dimitarpg13/aiconcepts/blob/master/Resources.md)

## Note

This repository uses git Large File Storage feature. In order to download locally the large files (> 1MB) which are maintained by git LFS you will need to install the Git extension for versioning large files: https://git-lfs.com/
