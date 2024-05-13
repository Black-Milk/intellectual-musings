# Iterative Adversarial Ablation

## Overview

We introduce a method designated as "Iterative Adversarial
Ablation." This method employs a construct known as a discriminator tree
ensemble to effectuate the selective exclusion of samples from a data
distribution. Through a process of iterative refinement, the method develops a
subsample that progressively approximates the characteristics of a specified
reference distribution. The ultimate objective is to achieve a subsample that is
virtually indistinguishable from the reference. To justify the application of
this procedure, certain assumptions regarding the data must be articulated and
acknowledged: both the evaluation dataset and the reference dataset are presumed
to originate from identical distributions. However, the evaluation dataset is
subjected to a biased sampling process, often the result of human intervention.
Conversely, the reference dataset is presumed to be devoid of such biases. This
differentiation is crucial for the applicability of the Iterative Adversarial
Ablation method, as it seeks to rectify these introduced discrepancies.

## Motivation

In the domain of machine learning, it is not uncommon for evaluation datasets to
be compromised by biases introduced through human intervention in the data
selection process. This bias may vitiate the validity of model evaluations,
particularly when the model in question has been trained on a dataset whose
distribution diverges markedly from that of the evaluation data—a condition
commonly referred to as data drift. To confront this challenge, the proposed
technique utilizes tree ensembles functioning as discriminators. These
discriminators are adeptly trained to discern distinctions between the samples
drawn from the evaluation dataset and those from the reference dataset, which is
generally constituted by the training data. Through an iterative
procedure, this technique "purifies" the evaluation dataset, thereby aligning it
more closely with the distributional characteristics of the training dataset.
This alignment is instrumental in fostering more accurate evaluations of the
model’s performance, tailored to reflect the conditions of its training
environment.

### Implementation

To be continued...



