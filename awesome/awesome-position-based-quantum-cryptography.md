# Position-Based Quantum Cryptography

> 来源：[Renaller/awesome-position-based-quantum-cryptography](https://github.com/Renaller/awesome-position-based-quantum-cryptography)

[![GitHub stars](https://img.shields.io/github/stars/Renaller/awesome-position-based-quantum-cryptography?style=flat)](https://github.com/Renaller/awesome-position-based-quantum-cryptography/stargazers)

# Awesome Position-Based Quantum Cryptography [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
This is a curated list of papers on position-based quantum cryptography (PBQC). The goal is to build a categorised community-driven always up-to-date literature overview of this growing field.

QPV = Quantum Position Verification

QPA = Quantum Position-based Authentication

PB-QKD = Position-based Quantum Key Distribution

## Contents

- [Classical Impossibility](#classical-impossibility)
- [First Protocols](#first-protocols)
- [Protocols without quantum communication](#protocols-without-quantum-communication)
- [Universal Attacks on QPV](#universal-attacks-on-qpv)
- [Ways Around the Universal Attacks on QPV](#ways-around-the-universal-attacks-on-qpv)
- [Conjectured Exponential Lower Bound](#conjectured-exponential-lower-bound)
- [Quantum Position-based Authentication](#quantum-position-based-authentication)
- [Towards Understanding NLQC](#towards-understanding-nlqc)
- [Towards Practicality](#towards-practicality)
- [Experiments](#experiments)

## Classical Impossibility

- N. Chandran, V. Goyal, R. Moriarty, and R. Ostrovsky: [Position-based cryptography (2009)](https://doi.org/10.1007/978-3-642-03356-8_23) - Establishes classical impossibility of position-based cryptography in the vanilla model. Explores possibility in the bounded-storage model.

## First Protocols

- A. Kent, W. Munro, T. Spiller, and R. Beausoleil: [Tagging systems (2006)](https://patents.google.com/patent/US20060022832A1/en) - Introduces QPV under the name of 'quantum tagging'.
- R. A. Malaney: [Location-dependent communications using
quantum entanglement (2010)](https://doi.org/10.1103/PhysRevA.81.042319) - Introduces QPV in the academic literature, but incorrectly claims unconditional security. Studies QPV based on Bell states.
- R. A. Malaney: [Quantum location verification in noisy channels (2010)](https://doi.org/10.1109/GLOCOM.2010.5684009) - Studies QPV based on Bell states, GHZ states and entanglement swapping. Studies the effect of noise/decoherence.
- A. Kent, W. J. Munro, and T. P. Spiller: [Quantum tagging: Authenticating location via quantum information and relativistic signalling constraints (2011)](https://doi.org/10.1103/PhysRevA.84.012326) - Introduces a rooster of different QPV protocols like BB84 QPV, $f$-routing, $f$-BB84 QPV and variations of them. Mentions entanglement-based attacks on some of them.

### BB84 QPV and Generalisations

- H. Buhrman, N. Chandran, S. Fehr, R. Gelles, V. Goyal, R. Ostrovsky, and C. Schaffner: [Position-based quantum cryptography: Impossibility and constructions (2011)](https://doi.org/10.1137/130913687) - Shows security against unentangled attacks.
- M. Tomamichel, S. Fehr, J. Kaniewski and S. Wehner: [A monogamy-of-entanglement game with applications to device-independent quantum cryptography (2013)](https://doi.org/10.1088/1367-2630/15/10/103002) - Shows a tight upper bound for unentangled attacks, parallel repetition and a linear lower bound for the repeated protocol.
- K. Chakraborty and A. Leverrier: [Practical position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.92.052304) - Considers the case where the two input bases are related by a unitary $U$.
- J. Ribeiro and F. Grosshans: [A tight lower bound for the BB84-states quantum-position-verification protocol (2015)](https://arxiv.org/abs/1504.07171) - Gives essentially tight lower bound for attacks with classical communication.
- B. Qi and G. Siopsis: [Loss-tolerant position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.91.042337) - Generalises BB84 QPV to more input bases and notes better loss tolerance properties because of it. Also discusses using decoy states and continuous variables for BB84 QPV.
- F. Speelman: [Position-based quantum cryptography and catalytic computation (2016)](https://eprints.illc.uva.nl/id/eprint/2138/) - Chapter 5 independently generalises BB84 QPV to more input bases. Chapter 4 provides an efficient attack on the protocol based on interleaved unitaries.
- A. Olivo, U. Chabaud, A. Chailloux, and F. Grosshans: [Breaking simple quantum position verification protocols with little entanglement (2020)](https://arxiv.org/abs/2007.15808) - Considers the case when the input bases are related by different angles and shows dimension-dependent attacks depending on the angle. Notably, they show the angle $\pi/6$ (outside the Clifford hierarchy) can be attacked with a 6-dimensional resource state.
- L. Escolà-Farràs and F. Speelman: [Single-qubit loss-tolerant quantum position verification protocol secure against entangled attackers (2023)](https://doi.org/10.1103/PhysRevLett.131.140802) - Tightly characterises the secure region of the protocol depending on the loss and error rates.
- R. Allerstorfer, L. Escolà-Farràs, A. A. Ray, B. Škorić, F. Speelman, and P. Verduyn Lunel: [Security of a continuous-variable based quantum position verification protocol (2023)](https://arxiv.org/abs/2308.04166) - Generalises the protocol to continuous variable inputs and shows security against unentangled attacks depending on loss and noise rates.
- C. A. Miller and Y. Alnawakhtha: [Perfect cheating is impossible for single-qubit position verification (2026)](https://doi.org/10.1103/4pcn-d1yj) - Considers a generalisation where the input qubits are eigenstates of a $\mathbb{C}^2$ projector chosen uniformly at random. Shows that no finite-dimensional resource state can perfectly attack this protocol.
- L. Escolà-Farràs and F. Speelman: [Lossy-and-Constrained Extended Non-Local Games with Applications to Quantum Cryptography (2025)](https://doi.org/10.22331/q-2025-04-18-1712) - Improved analyis of the BB84 protocol under loss compared to "Single-qubit loss-tolerant quantum position verification protocol secure against entangled attackers" (2023) by the same authors, introduces SDP hierarchies to compute bounds on lossy-and-constrained extended non-local games
- L. Escolà-Farràs, F. Speelman: [Sharp error tolerance of the monogamy-of-entanglement game (2026)](https://doi.org/10.48550/arXiv.2611.09504) - Improved loss tolerance of f-measure in the random oracle model and in the plain model under parallel repetition, enabled by an improved analysis of the monogamy-of-entanglement game  

### $f$-route

- H. Buhrman, S. Fehr, C. Schaffner, and Florian Speelman: [The garden-hose model (2013)](https://doi.org/10.1145/2422436.2422455) - Studies attacks on $f$-routing and introduces garden-hose complexity to connect attacks on $f$-routing to complexity theory. Provides many first results regarding that connection, for example that any $f \in \mathsf{L}$ (with pre-processing) can be attacked efficiently.
- A. Bluhm, M. Christandl, and F. Speelman: [A single-qubit position verification protocol that is secure against multi-qubit attacks (2022)](https://doi.org/10.1038/s41567-022-01577-0) - Shows a robust linear lower bound on the dimension of the attack resource state.
- J. Cree and A. May: [Code-routing: A new attack on position verification (2023)](https://doi.org/10.22331/q-2023-08-09-1079) - Provides a new attack on $f$-routing, connecting attacks to secret-sharing schemes and span programs, and showing that any $f \in \mathsf{Mod}_p\mathsf{L}$ (with pre-processing), for $p$ prime, can be attacked efficiently.
- R. Allerstorfer, H. Buhrman, A. May, F. Speelman, and P. Verduyn Lunel: [Relating non-local quantum computation to information theoretic cryptography (2023)](https://doi.org/10.22331/q-2024-06-27-1387) - Connects $f$-routing to topics in classical cryptography, in particular conditional disclosure of secrets. Shows a sub-exponential upper bound for attacks for any $f$ and finds an $f$ that is believed to be outside of $\mathsf{P}$ (with pre-processing), but efficiently attacked.
- V. R. Asadi, E. Culf, and A. May: [Rank lower bounds on non-local quantum computation (2024)](https://arxiv.org/abs/2402.18647) - Provides a lower bound in terms of the Schmidt-rank of the resource state for perfect attacks. Gives linear lower bounds for some concrete functions.
- V. Asadi, R. Cleve, E. Culf, and A. May: [Linear gate bounds against natural functions for position-verification (2025)](https://doi.org/10.22331/q-2025-01-21-1604) - Provides a robust linear lower bound on the number of quantum gates/measurements needed to attack the inner product function.
- L. Escolà-Farràs, L. Colisson Palais, F. Speelman: [A quantum cloning game with applications to quantum position verification (2025)](https://doi.org/10.4230/LIPIcs.TQC.2025.2) - Proves security of the $f$-route protocol in the random oracle model by analyzing a quantum cloning game.

### $f$-measure

- D. Unruh: [Quantum position verification in the random oracle model (2014)](https://doi.org/10.1007/978-3-662-44381-1_1) - Considers QPV in higher dimensions carefully and shows unconditional security in the random oracle model.
- A. Bluhm, M. Christandl, and F. Speelman: [A single-qubit position verification protocol that is secure against multi-qubit attacks (2022)](https://doi.org/10.1038/s41567-022-01577-0) - Shows a robust linear lower bound on the dimension of the attack resource state.
- L. Escolà-Farràs and F. Speelman: [Single-qubit loss-tolerant quantum position verification protocol secure against entangled attackers (2023)](https://doi.org/10.1103/PhysRevLett.131.140802) - Tightly characterises the secure region of the protocol depending on the loss and error rates.
- R. Allerstorfer, A. Bluhm, H. Buhrman, M. Christand, L. Escolà-Farràs, F. Speelman, and P. Verduyn Lunel: [Making existing quantum position verification protocols secure against arbitrary transmission loss (2025)](https://doi.org/10.1103/szwj-s7r6) - Introduces an extra commitment step into QPV and shows that for a class of protocols, involving $f$-BB84 QPV, this makes the transmission loss irrelevant for security. Argues $f$-BB84 is a practical QPV protocol.
- R. Allerstorfer, L. Escolà-Farràs, A. A. Ray, B. Skoric, and F. Speelman: [Continuous-variable quantum position verification secure against entangled attackers (2024)](https://doi.org/10.1103/PhysRevA.110.062605) - Generalises $f$-BB84 QPV to continuous-variable inputs and shows analogous security statements as for finite-dimensional inputs.
- A. May and P. Verduyn Lunel [Quantum gate lower bounds for loss-tolerant position verification](https://arxiv.org/abs/2608.16495) -  Proves nearly-linear quantum gate lower for $f$-measure, even when allowing the attacker to declare a transmission loss of up to 50%. Proof is analytic, improved analysis of the monogamy-of-entanglement game.

#### Bounds for concrete functions

- V. R. Asadi, E. Culf, and A. May: [Rank lower bounds on non-local quantum computation (2024)](https://arxiv.org/abs/2402.18647) - Provides a lower bound in terms of the Schmidt-rank of the resource state for perfect attacks. Gives linear lower bounds for some concrete functions.
- V. Asadi, R. Cleve, E. Culf, and A. May: [Linear gate bounds against natural functions for position-verification (2025)](https://doi.org/10.22331/q-2025-01-21-1604) - Provides a robust linear lower bound on the number of quantum gates/measurements needed to attack the inner product function.
- K. Bogner: [Robust logarithmic entanglement lower bound for $f$-routing (2026)](https://doi.org/10.48550/arXiv.2608.05775) -  Proves robust logarithmic lower bound for $f$-route with the binary inner product function
- A. Hasegawa and R. Mataraarachchi: [New lower bounds for CDS and $f$-routing (2026)](https://doi.org/10.48550/arXiv.2609.24291) - Gives linear lower bounds for perfect attacks for the inner product function.
- O. Renard and N. Spooner: [Computational Bounds for $f$-Routing (2026)](https://doi.org/10.48550/arXiv.2609.40278) - Proves unconditional resource lower bounds for concrete $f$ in the case of uniform attackers under computational assumptions 

### Bell QPV

- R. A. Malaney: [Location-dependent communications using
quantum entanglement (2010)](https://doi.org/10.1103/PhysRevA.81.042319) - Studies QPV based on Bell states. Claimed unconditional security, which later turned out to be false.
- R. A. Malaney: [Quantum location verification in noisy channels (2010)](https://doi.org/10.1109/GLOCOM.2010.5684009) - Studies QPV based on Bell states, GHZ states and entanglement swapping. Studies the effect of noise/decoherence.
- H.-K. Lau and H.-K. Lo: [Insecurity of position-based
quantum cryptography protocols against entanglement attacks (2011)](https://doi.org/10.1103/PhysRevA.83.012322) - Proves insecurity of QPV protocols that were previously claimed secure and studies general principle underlying entanglement attacks. Studies variations of QPV protocols based on Bell/GHZ states and shows that using eigenstates other than Pauli $X$, $Y$, $Z$ leads to protocols that need >1 EPR pair to be attacked.
- C. C. W. Lim, F. Xu, G. Siopsis, E. Chitambar, P. G. Evans, and B. Qi: [Loss-tolerant quantum secure positioning with weak laser sources (2016)](https://doi.org/10.1103/PhysRevA.94.032315) - Studies a version of the protocol with separable inputs. Proves full loss tolerance and studies practical implementation based on decoy states.
- R. Allerstorfer, H. Buhrman, F. Speelman, P. Verduyn Lunel: [On the role of quantum communication and loss in attacks on quantum position verification (2022)](https://arxiv.org/abs/2208.04341) - Proves a 3/4 upper bound on the success probability of unentangled attacks.
- R. Allerstorfer, M. Christandl, D. Grinko, I. Nechita, M. Ozols, D. Rochette, and P. Verduyn Lunel: [Monogamy of highly symmetric states (2025)](https://doi.org/10.1007/s00220-025-05483-3) - The results in this paper imply a $\ln(2) \approx 0.69$ upper bound on the success probability of unentangled attacks.

### Other protocols

- K. Chakraborty and A. Leverrier: [Practical position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.92.052304) - Provides a protocol based on interleaved unitaries, conjecturing security. The protocol was broken efficiently later.
- F. Gao, B. Liu & QY. Wen: [Quantum position verification in bounded-attack-frequency model (2016)](https://doi.org/10.1007/s11433-016-0234-0) - Considers BB84 QPV with non-simultaneous arrival times of input information at the prover (the basis being encoded in which side arrived first). Discusses the general port-based attack in this setting. 
- S. Das and G. Siopsis: [Practically secure quantum position verification (2021)](https://doi.org/10.1088/1367-2630/ac0755) - Gives an overview over the existing protocols at the time and mixes elements of them to obtain different variations of those protocols.
- R. Allerstorfer, H. Buhrman, F. Speelman, and P. Verduyn Lunel: [Towards practical and error-robust quantum position verification (2021)](https://arxiv.org/abs/2106.12911) - Defines a new protocol based on the SWAP test and studies it theoretically and practically.
- R. Allerstorfer, A. Bluhm, H. Buhrman, M. Christandl, L. Escolà-Farràs, F. Speelman, and P. Verduyn Lunel: [Making existing quantum position verification protocols secure against arbitrary transmission loss (2025)](https://doi.org/10.1103/szwj-s7r6) - Introduces an extra commitment step into QPV and shows that for a class of protocols this makes the transmission loss irrelevant for security.
- G. A. Kavuri, Y. Zhang, A. R. Gookin, S. Patra, J. C. Bienfang, H. Fu, Y. Alnawakhtha, D. V. Reddy, M. D. Mazurek, C. Abellán, W. Amaya, M. W. Mitchell, S. W. Nam, C. A. Miller, R. P. Mirin, M. J. Stevens, S. Glancy, E. Knill, L. K. Shalm: [Quantum Position Verification with Remote Untrusted Devices (2026)](https://doi.org/10.48550/arXiv.2601.16892) - Introduces and proves device-independent security of a Bell-test based QPV protocol which resembles $f$-measure, implements the protocol in an experiment
- J. Cai, R. Fleur, B. Tissot, W. Löffler, T. B. Propp: [High-Fidelity Remote Graph State Preparation for Blind Quantum Computation (2026)](https://doi.org/10.48550/arXiv.2610.06247) - Proposes a QPV protocol based on remote graph state preparation.
- W. Y. Kon, N. Bigagli, A. Conrad, T. Shields, F. Kaleoglu, I. W. Primaatmaja, A. Craddock, RJ Pisani, M. Flament, J. Seeber, O. Amer, C. Lim, X. Ling, R. Otter, K. Chakraborty, and M. Namazi: [Loss-Tolerant Quantum Position Verification for Metropolitan Area Networks (2026)](https://doi.org/10.48550/arXiv.2609.23234) - Introduces a QPV protocol that is fully loss-tolerant as long as all information travels at the speed of light and that has the prover prepare the quantum state. The protocol is secure in the random oracle model. It is demonstrated experimentally with off-the-shelf hardware. 

## Protocols without quantum communication

- J. Liu, Q. Liu, and L. Qian: [Beating classical impossibility of position verification (2022)](https://doi.org/10.4230/LIPIcs.ITCS.2022.100) - Constructs the first QPV protocol with only classical input and output information from the assumption that LWE is quantum-hard. Shows unconditional security in the random oracle model.
- F. Kaleoglu, M. Liu, D. Cui, O. Amer, M. Pistoia, C. Lim, and Kaushik Chakraborty: [On the equivalence between classically verifiable position verification and certified randomness (2026)](https://doi.org/10.1038/s41467-026-70628-4) - Presents a compiler that converts any single-device certified randomness protocol to classically verifiable position verification protocol which is secure in the random oracle model.
- W. Y. Kon, F. Kaleoglu, and K. Chakraborty: [Classical Verifier Position Verification from Non-Local Games (2026)](https://doi.org/10.48550/arXiv.2609.38441) - Provides a compiler that converts any complete-support non-local game with the required quantum advantage to a multi-prover classically verifiable position verification protocol.

## Universal Attacks on QPV

- H. Buhrman, N. Chandran, S. Fehr, R. Gelles, V. Goyal, R. Ostrovsky, and C. Schaffner: [Position-based quantum cryptography: Impossibility and constructions (2011)](https://doi.org/10.1137/130913687) - Rigorously defines QPV and provides an general attack on all such QPV protocols using a doubly exponential amount of pre-shared EPR pairs in the number of input qubits. 
- S. Beigi and R. König: [Simplified instantaneous non-local quantum computation with applications to position-based cryptography (2011)](https://doi.org/10.1088/1367-2630/13/9/093036) - Provides a general attack on QPV based on port-based teleportation, using an exponential amount of pre-shared EPR pairs in the number of input qubits. Also provides a QPV protocol with a provably linear lower bound.
- F. Speelman: [Instantaneous non-local computation of low T-depth quantum circuits (2016)](https://doi.org/10.4230/LIPIcs.TQC.2016.9) - Provides a general attack on QPV using an exponential amount of pre-shared EPR pairs in the number of T-gates or T-depth based on the circuit decomposition of the task unitary into Clifford+T gates.
- K. Dolev and S. Cree: [Non-local computation of quantum circuits with small light cones (2022)](https://arxiv.org/abs/2203.10106) - Provides a general attack on QPV based on the geometric structure of a circuit decomposition of the task unitary. Is more efficient for certain classes of unitaries than previous general attacks.

### Attacks on classes of unitaries

- K. Chakraborty and A. Leverrier: [Practical position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.92.052304) - Shows efficient attacks for certain classes, like the second level of the Clifford hierarchy.
- A. Gonzales and E. Chitambar: [Bounds on instantaneous non-local quantum computation (2020)](https://doi.org/10.1109/TIT.2019.2950190) - Shows that any 2-qubit unitary can be attacked up to error $\varepsilon$ using $\log(1/\varepsilon)$ EPR pairs and that any hermitian bipartite binary controlled unitary can be attacked with 1 EPR pair. Shows logarithmic lower bound on entanglement entropy for general bipartite binary controlled unitary.

## Ways Around the Universal Attacks on QPV

- A. Kent: [Quantum tagging for tags containing secret classical data (2011)](https://doi.org/10.1103/PhysRevA.84.022335) - Considers QPV in the setting when the verifiers and the prover pre-share a secret. Shows that then QPV is unconditionally secure by indefinitely expanding the secret using QKD.
- D. Unruh: [Quantum position verification in the random oracle model (2014)](https://doi.org/10.1007/978-3-662-44381-1_1) - Shows unconditional security of $f$-BB84 QPV in the random oracle model.
- J. Liu, Q. Liu, and L. Qian: [Beating classical impossibility of position verification (2022)](https://doi.org/10.4230/LIPIcs.ITCS.2022.100) - Constructs a QPV protocol with only classical input and output information from the assumption that LWE is quantum-hard. Shows unconditional security in the random oracle model.
- A. Behera, V. Goyal: [Breaking the Bounded Entanglement Barrier for Quantum Position Verification (2026)](https://doi.org/10.48550/arXiv.2609.39234) - Introduces a model, in which the verifiers' messages are sent at a time drawn uniformly at random from a continuous time interval and proves security against LOCC adversaries. Also considers a model with discretized time where security depends on how accurately time can be measured
- O. Renard and N. Spooner: [Computational Bounds for $f$-Routing (2026)](https://doi.org/10.48550/arXiv.2609.40278) - Proves unconditional resource lower bounds for concrete $f$ in the case of uniform attackers under computational assumptions

## Conjectured Exponential Lower Bound

- M. Junge, A. M. Kubicki, C. Palazuelos, and D. Pérez-García: [Geometry of Banach spaces: A new route towards position based cryptography (2021)](https://doi.org/10.1007/s00220-022-04407-9) - Provides a new protocol based on applying a phase unitary depending on the classical input information. Shows an exponential lower bound (i.e., exponential in the quantum resources of the honest parties) under a regularity assumption on the attack, and an exponential lower bound conditioned on an, as yet, unresolved Banach space geometry conjecture.
- I.M. Moreno-Cuadrado, C. Palazuelos, and D. Perez-Garcia: [Exponential lower bounds for low-degree strategies in position-based quantum cryptography (2026)](https://doi.org/10.48550/arXiv.2609.35592) - Proposes a variant of the phase unitary protocol that needs less resources for the honest parties, proves exponential lower bounds  (i.e., exponential in all resources of the honest parties) against low-degree strategies. As in the preceding paper, there is also an exponential lower bound conditioned on an unresolved Banach space geometry conjecture.

## Quantum Position-based Authentication

- H. Buhrman, N. Chandran, S. Fehr, R. Gelles, V. Goyal, R. Ostrovsky, and C. Schaffner: [Position-based quantum cryptography: Impossibility and constructions (2011)](https://doi.org/10.1137/130913687) - Provides a generic, but inefficient, construction to go from QPV to QPA to PB-QKD.
- D. Unruh: [Quantum position verification in the random oracle model (2014)](https://doi.org/10.1007/978-3-662-44381-1_1) - Provides more efficient extensions to QPA and PB-QKD in the random oracle model for $f$-BB84 QPV. 
- W. Y. Kon, I. W. Primaatmaja, K. Chakraborty, and C. Lim: [Efficient multi-basis quantum position verification secure against generalized adversaries (2026)](https://doi.org/10.1038/s41534-026-01325-9) - Improved analysis of how to use QPV to provide the authentication within QKD.
 
## Towards Understanding NLQC

- A. Kent: [Quantum tasks in Minkowski space (2012)](https://doi.org/10.1088/0264-9381/29/22/224013) - Considers more general quantum tasks than QPV.
- A. Broadbent: [Popescu-Rohrlich correlations imply efficient instantaneous nonlocal quantum computation (2016)](https://doi.org/10.1103/PhysRevA.94.022318) - Shows that if attackers share PR boxes, then any unitary can be attacked using only linear entanglement and a linear number of PR box uses.
- K. Dolev: [Constraining the doability of relativistic quantum tasks (2019)](https://arxiv.org/abs/1909.05403) - Generalises the port-based attack to more general quantum tasks and spacetime circuits. Finds that the coarse causal structure of the task is the relevant property determining whether the task is doable non-locally.
- R. Allerstorfer, H. Buhrman, F. Speelman, and P. Verduyn Lunel: [On the role of quantum communication and loss in attacks on quantum position verification (2022)](https://doi.org/10.48550/arXiv.2208.04341) - Shows that any QPV protocol that can be broken unentangled with quantum communication, but is secure against classical communication attacks, can be transformed into one that is secure against quantum communication attacks. Also notes that if the signal loss is high enough any QPV protocol can be attacked efficiently by a trivial teleportation attack.
- A. May: [Complexity and entanglement in non-local computation and holography (2022)](https://doi.org/10.22331/q-2022-11-28-864) - Notes that the necessary attack resource requirements are controlled by the entangled part of the task unitary. Shows that for tasks where one side is classical input information, a doubly-logarithmic (later improved to logarithmic) lower bound and exponential upper bound (in terms of any complexity measure of your choice of the entangled part of the task unitary) hold for attacks.
- R. Allerstorfer, H. Buhrman, A. May, F. Speelman, and P. Verduyn Lunel: [Relating non-local quantum computation to information theoretic cryptography (2023)](https://doi.org/10.22331/q-2024-06-27-1387) - Connects NLQC to some protocols in classical cryptography via $f$-routing.
- I. George, R. Allerstorfer, P. Verduyn Lunel, and E. Chitambar: [Orthogonality Broadcasting and Quantum Position Verification (2025)](https://doi.org/10.1088/1367-2630/add87c) - Studies the difference between unentangled quantum and classical attacks on state discrimination QPV protocols and proves several results on that, for example that there is a separable state ensemble that can be perfectly discriminated with quantum communication, but not without.
- H. Apel, T. Cubitt, P. Hayden, T. Kohler, and D. Pérez-García : [Security of position-based quantum cryptography limits Hamiltonian simulation via holography (2024)](https://doi.org/10.1007/JHEP08(2024)152) - Connects QPV to Hamiltonian simulation. Shows that if a superlinear lower bound can be shown for QPV attacks, then there are new fundamental lower bounds for resources required for one Hamiltonian to simulate another.
- A. Bluhm, S. Höfer, A. May, M. Stasiuk, P. Verduyn Lunel, and H. Yuen: [A complexity theory for non-local quantum computation (2026)](https://doi.org/10.22331/q-2026-07-01-2152) - Finds relations between a wide range of different NLQC tasks, including showing that $f$-route and $f$-measure are equivalent, with a constant-overhead reduction between them.
- A. Bluhm, S. Höfer, A. May, F. Speelman, and P. Verduyn Lunel: [Equivalence of non-local computation tasks beyond Clifford operations (2026)](https://doi.org/10.48550/arXiv.2606.26354) - Extends the equivalence between $f$-routing and $f$-measure (in the Hadamard basis) to $f$-measure with arbitrary bases, the controlled application of any Clifford unitary, and the controlled application of any unitary of the form $U=C_1 D C_0$ with $D$ an arbitrary diagonal unitary and $C_0$, $C_1$ Clifford circuits.
- M. Folkertsma, D. Grinko, G. Muuss, and F. Speelman: [Perfect non-local quantum computation is impossible(2026)](https://doi.org/10.48550/arXiv.2609.40228) - Proves that perfect NLQC is impossible.

### Connection to holography

- A. May: [Quantum tasks in holography (2019)](https://doi.org/10.1007/JHEP10(2019)233) - Connects QPV to the AdS/CFT conjecture by noting that a QPV protocol in the bulk must have an equivalent protocol in the boundary. The boundary implementation turns out to be a valid attack on the bulk QPV protocol, implementing it non-locally.
- A. May, G. Penington, and J. Sorce: [Holographic scattering requires a connected entanglement wedge (2020)](https://doi.org/10.1007/JHEP08(2020)132) - Furthers the connection between QPV and holography and estimates the mutual information between the relevant boundary regions. Results based on the conjecture could yield efficient attacks on all QPV protocols due to the results in this paper.
- K. Dolev and S. Cree: [Holography as a resource for non-local quantum computation (2022)](https://arxiv.org/abs/2210.13500) - Discusses and fills a loophole in the paper one above. Costructs an attacked based on simulating a holographic CFT and argues that, based on some assumptions, any polynomially complex unitary can be efficiently attacked.


## Towards Practicality

- B. Qi and G. Siopsis: [Loss-tolerant position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.91.042337) - Generalises BB84 QPV to more input bases and notes better loss tolerance properties because of it. Also discusses using decoy states and continuous variables for BB84 QPV.
- C. C. W. Lim, F. Xu, G. Siopsis, E. Chitambar, P. G. Evans, and B. Qi: [Loss-tolerant quantum secure positioning with weak laser sources (2016)](https://doi.org/10.1103/PhysRevA.94.032315) - Studies Bell QPV with separable inputs. Proves full loss tolerance and studies practical implementation based on decoy states.
- R. Allerstorfer, H. Buhrman, F. Speelman, and P. Verduyn Lunel: [Towards practical and error-robust quantum position verification (2021)](https://arxiv.org/abs/2106.12911) - Defines a new protocol based on the SWAP test and studies it theoretically and practically. Argues that this protocol has practically versatile and robust properties.
- L. Escolà-Farràs and F. Speelman: [Single-qubit loss-tolerant quantum position verification protocol secure against entangled attackers (2023)](https://doi.org/10.1103/PhysRevLett.131.140802) - Tightly characterises the secure region of BB84 QPV and $f$-BB84 QPV depending on the loss and error rates.
- R. Allerstorfer, L. Escolà-Farràs, A. A. Ray, B. Škorić, F. Speelman, and P. Verduyn Lunel: [Security of a continuous-variable based quantum position verification protocol (2023)](https://arxiv.org/abs/2308.04166) - Generalises BB84 QPV to continuous variable inputs and shows security against unentangled attacks depending on loss and noise rates.
- R. Allerstorfer, A. Bluhm, H. Buhrman, M. Christandl, L. Escolà-Farràs, F. Speelman, and P. Verduyn Lunel: [Making existing quantum position verification protocols secure against arbitrary transmission loss (2025)](https://doi.org/10.1103/szwj-s7r6) - Introduces an extra commitment step into QPV and shows that for a class of protocols, involving $f$-BB84 QPV, this makes the transmission loss irrelevant for security. Argues $f$-BB84 is a practical QPV protocol.
- G. Cowperthwaite, A. Kent, D. Pitalua-Garcia: [Towards practical quantum position verification (2023)](https://arxiv.org/abs/2309.10070) - Delves into some technical hardware details of a practical QPV implementation.
- R. Allerstorfer, L. Escolà-Farràs, A. A. Ray, B. Skoric, F. Speelman: [Continuous-variable quantum position verification secure against entangled attackers (2024)](https://doi.org/10.1103/PhysRevA.110.062605) - Generalises $f$-BB84 QPV to continuous-variable inputs and shows analogous security statements as for finite-dimensional inputs.

### Security under parallel repetition

- M. Tomamichel, S. Fehr, J. Kaniewski and S. Wehner: [A monogamy-of-entanglement game with applications to device-independent quantum cryptography (2013)](https://doi.org/10.1088/1367-2630/15/10/103002) - Shows a tight upper bound for unentangled attacks, parallel repetition and a linear lower bound for the repeated protocol.
- L. Escolà-Farràs and F. Speelman: [Quantum position verification in one shot: parallel repetition of the $f$-BB84 and $f$-routing protocols (2025)](https://doi.org/10.48550/arXiv.2503.09544)- Proves security of $f$-route and $f$-measure under parallel repetition for random functions $f$.
- L. Escolà-Farràs, B. Škorić, and F. Speelman: [Arbitrarily Loss-Tolerant Quantum Position Verification in a Single Execution (2026)](https://doi.org/10.48550/arXiv.2606.25037) - Proves security of the $f$-measure protocol with commitment step (which is the version of the protocol that is fully loss tolerant) under parallel repetition.

### QPV beyond one dimension
- H. Buhrman, N. Chandran, S. Fehr, R. Gelles, V. Goyal, R. Ostrovsky, and C. Schaffner: [Position-based quantum cryptography: Impossibility and constructions (2011)](https://doi.org/10.1137/130913687) - Shows security against unentangled attacks, mentions extensions to higher dimensions.
- D. Unruh: [Quantum position verification in the random oracle model (2014)](https://doi.org/10.1007/978-3-662-44381-1_1) - Considers QPV in higher dimensions carefully and shows unconditional security in the random oracle model.
- Z. Zhang; F. Speelman; and P. Grosso: [Enhancing Position Verification in Multi-Node Quantum Networks (2025)](https://doi.org/10.1109/INFOCOM55648.2025.11044770) - Extension of QPV to 2D networks in a restricted attack model.

### Additional Features
- U. Girish, G. Gluch, S. Goldwasser, T. Malkin, L. Orshansky and H. Yuen: [Private Proofs of When and Where (2026)](https://doi.org/10.1007/978-3-032-35409-9_14) - Introduces zero-knowledge position verification and constructs such protocols from secure position verification and post-quantum one-way functions.
- J. Bartusek, Z. Huang, L. Orshansky, and H. Yuen: [How To Track Qubits Through Space and Time (Or: Sailing in a Quantum Boat) (2026)](https://doi.org/10.48550/arXiv.2605.30732) - Introduces a stronger notions of position verification called quantum localization, which requires that there is a specified, unclonable state at the verified spacetime point-and that this state can be found nowhere else. Security of such schemes in proven in the classical oracle model.

### Applications

- Y. Wang, G. Smith, A. May: [Secure quantum ranging (2025)](https://doi.org/10.48550/arXiv.2505.04776) -  Proposes a secure quantum ranging protocol that combines quantum ranging with quantum position verification.
- Z. Guo, F. Kitagawa, and X. Liang: [I Prove, Therefore I Am: Spatiotemporal Multi-Party Computation (2026)](https://doi.org/10.48550/arXiv.2609.26448) - Uses prover’s ability to pass position verification as the definition of its physical presence at the asserted position.

## Experiments

- K. Kanneworff, M. Poortvliet, D. Bouwmeester, R. Allerstorfer, P. Verduyn Lunel, F. Speelman, H. Buhrman, P. Steindl and W. Löffler: [Towards experimental demonstration of quantum position verification using single photons (2025)](https://doi.org/10.1088/2058-9565/adf2da) - A first demonstration experiment of QPV using the SWAP protocol, with single photons from a single semiconductor quantum dot in an optical microcavity.
- G.-J. Fan-Yuan, Y.-G. Shan, C. Zhang, Y.-L. Wang, Y.-X. Fan, W.-X. Xie, D.-Y. He, S. Wang, Z.-Q. Yin, W. Chen, S.-N. Fu, G.-C. Guo, and Z.-F. Han: [Relativistic position verification with coherent states (2026)](https://doi.org/10.1038/s41567-026-03439-5) -  Experimental implementation of the $f$-measure protocol using phase-randomized weak coherent states
- G. A. Kavuri, Y. Zhang, A. R. Gookin, S. Patra, J. C. Bienfang, H. Fu, Y. Alnawakhtha, D. V. Reddy, M. D. Mazurek, C. Abellán, W. Amaya, M. W. Mitchell, S. W. Nam, C. A. Miller, R. P. Mirin, M. J. Stevens, S. Glancy, E. Knill, L. K. Shalm: [Quantum Position Verification with Remote Untrusted Devices (2026)](https://doi.org/10.48550/arXiv.2601.16892) - Introduces and proves device-independent security of a Bell-test based QPV protocol which resembles $f$-measure, implements the protocol in an experiment
- W. Y. Kon, N. Bigagli, A. Conrad, T. Shields, F. Kaleoglu, I. W. Primaatmaja, A. Craddock, RJ Pisani, M. Flament, J. Seeber, O. Amer, C. Lim, X. Ling, R. Otter, K. Chakraborty, and M. Namazi: [Loss-Tolerant Quantum Position Verification for Metropolitan Area Networks (2026)](https://doi.org/10.48550/arXiv.2609.23234) - Introduces a QPV protocol that is fully loss-tolerant as long as all information travels at the speed of light and that has the prover prepare the quantum state. The protocol is secure in the random oracle model. It is demonstrated experimentally with off-the-shelf hardware. 
