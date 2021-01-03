---
layout: post
title: Getting Started with Reinforcement Learning
---

## Getting Started with Reinforcement Learning
               -> Agent ->
              -           -
     s_t,r_t -             - a_t
              -           -
                <- Env  <- 


### Model Free vs Model Based 
If Agent has access to the model of the environment (a function which can predict state transition and rewards) falls under model based family. The main advantage is agent can see what action to take and can plan ahead to decide which transitions to make. AlphaZero is model based. This type of models have better sample efficiency over methods that don't have a model. 


If Agent does not have access to model of the environment, then agent has to learn the model purely from experience. This is quite challenging as agent interaction with environment can be biased. Usually agent performs well with respect to learned environment but performs sub-optimally in real environment. These family of models does not gain from sample efficiency but are easier to implement and tune.


### What's important in Model Free RL
There are two main approaches to train an agent with model-free RL 
1. Poicy Optimization : Optimize directly by gradient ascent and each update used data collected while acting according to current version of policy. Therefore called On Policy optimization. Examples of on-policy optimization methods are A2C / A3C, PPO.
2. Q-Learning : Learns approximator Q(s,a) for optimal action-value function Q^*(s,a). Uses bellman equation and each update uses data collectd at any point during training irrespective of the policy (how agent was choosing to explore the environment).Examples of off-policy are DQN, C51.
```latex
    a(s) = arg max Q_{\theta}(s,a)
                a
```

### Comparision between on-policy and off-policy 
The primary strength of policy optimization methods is that they are principled, in the sense that you directly optimize for the thing you want. This tends to make them stable and reliable. By contrast, Q-learning methods only indirectly optimize for agent performance, by training Q_{\theta} to satisfy a self-consistency equation. There are many failure modes for this kind of learning, so it tends to be less stable. But, Q-learning methods gain the advantage of being substantially more sample efficient when they do work, because they can reuse data more effectively than policy optimization techniques.

### Algorithms between Policy Optimization and Q-Learning 
there exist a range of algorithms that live in between the two extremes. Algorithms that live on this spectrum are able to carefully trade-off between the strengths and weaknesses of either side. Examples include

DDPG, an algorithm which concurrently learns a deterministic policy and a Q-function by using each to improve the other,
and SAC, a variant which uses stochastic policies, entropy regularization, and a few other tricks to stabilize learning and score higher than DDPG on standard benchmarks.



### What's important in Model Based RL
There are many ways of using models.

1. Pure Planning : The most basic approach never explicitly represents the policy, and instead, uses pure planning techniques like model-predictive control (MPC) to select actions. In MPC, each time the agent observes the environment, it computes a plan which is optimal with respect to the model, where the plan describes all actions to take over some fixed window of time after the present. (Future rewards beyond the horizon may be considered by the planning algorithm through the use of a learned value function.) The agent then executes the first action of the plan, and immediately discards the rest of it. It computes a new plan each time it prepares to interact with the environment, to avoid using an action from a plan with a shorter-than-desired planning horizon.


2.Expert Iteration. A straightforward follow-on to pure planning involves using and learning an explicit representation of the policy, \pi_{\theta}(a|s). The agent uses a planning algorithm (like Monte Carlo Tree Search) in the model, generating candidate actions for the plan by sampling from its current policy. The planning algorithm produces an action which is better than what the policy alone would have produced, hence it is an “expert” relative to the policy. The policy is afterwards updated to produce an action more like the planning algorithm’s output.

The ExIt algorithm uses this approach to train deep neural networks to play Hex.
AlphaZero is another example of this approach.

Data Augmentation for Model-Free Methods. Use a model-free RL algorithm to train a policy or Q-function, but either 1) augment real experiences with fictitious ones in updating the agent, or 2) use only fictitous experience for updating the agent.

See MBVE for an example of augmenting real experiences with fictitious ones.
See World Models for an example of using purely fictitious experience to train the agent, which they call “training in the dream.”
Embedding Planning Loops into Policies. Another approach embeds the planning procedure directly into a policy as a subroutine—so that complete plans become side information for the policy—while training the output of the policy with any standard model-free algorithm. The key concept is that in this framework, the policy can learn to choose how and when to use the plans. This makes model bias less of a problem, because if the model is bad for planning in some states, the policy can simply learn to ignore it.
