# Root Cause Analysis (RCA) and Model Checking via Probabilistic Temporal Logic (PTL)

Literature overview on the topic of Process Mining in general and Root Cause Analysis specifically:
Process Mining / RCA literature compendum:
https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/tree/main/literature

Personally, I am quite fascinated by the use of of special kind of logic for model checking - the Probabilistic Temporal Logic (PTL).
But you may ask yourself - why using PTL in RCA ?
Because it allows fairly complex queries to the underlying probabilistic model relevant for particular RCA scenarios to be generalized and expressed in mathematical (PTL) notation which can be implemented via graph algorithms in an elegant way.

The probabilistic model for RCA generally is built by a Markov Chain and is represented by a labeled directed graph, Kripke structure, etc. So the bottom line is that fairly complex RCA analysis queries to the probabilistic model based on the chosen set of events can be performed with generic graph algorithms which are already implemented efficiently in open source libraries.
PTL is an extension of  Computation Tree Logic (CTL). CTL is a superset of linear temporal logic and it is related to first order logic. Also note that CTL  is a  standard method for design/model verification in the analysis and design of VLSI ICs as well as analysis of  the correctness of parallel program execution.

A detailed and thorugh survey by Clarke et al on the most relevant logic systems for model verification can be found here:
[Clarke, E. M., Schlingloff, B. H. (2001). Model Checking](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/literature/ModelChecking/ModelChecking_ClarkeSchlingloff1999.pdf)

As quick intro into Temporal Logic can serve Clarke, Emerson, and Sistla's paper:
[Clarke, E.M., Emerson, E.A., Sistla, A.P. (1983). Automatic Verification Finite State Concurrent Systems Using Temporal Logic Specifications: A Practical Approach](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/literature/ModelChecking/AutomaticVerifictionOfFiniteStateConcurrentSystemUsingTemporalLogicSpecification.pdf)

An excellent tutorial for Probablistic Temporal Logic (PTL) is the Hanssen and Jonsson's paper:
[Hansson, H., Jonsson, B. (1994). A Logic about Reasoning about Time and Reliability](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/literature/ModelChecking/ALogicforReasoningaboutTimeandReliability_Hansson_Johnson_1994.pdf)

A refresher on first order logic which is the fundament of the logic systems for model verification can be found here:
[First-Order Logic, Open Logic Project](https://github.com/dimitarpg13/root_cause_analysis_and_model_checking/blob/main/literature/ModelChecking/first-order-logic-OpenLogicProject.pdf)
