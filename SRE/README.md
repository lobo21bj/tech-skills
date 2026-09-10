# SRE

This section contains my personal notes in the path to become SRE.

## Introduction

SRE stands for Site Reliability Engineer. It's a role created by Google in 2003.
Is a discipline that incorporates aspects of software engineering and applies them to infrastucture and operations problems.

- The goal is to create ultra-scalabale and highly reliable distributed software systems.
- SREs spend 50% of their time doing ops related work such as issue resolution, on-call, and manual interventions.
- SREs spend 50% of their time on development tasks such as new features, scaling or automation.
- Monitoring, alerting and automation are a large part of SRE.

### Principles

- Scalability
- Availability
- Incident Response
- Automation

Difference between SRE and DevOps ([Video](https://www.youtube.com/watch?v=uTEL8Ff1Zvk))

Before (**DevOps**):
Developers were concerned in releasing code.
Operators, in reliability.

DevOps is a culture and practices to reduce this friction.

- Reduce Organization Silos
- Accept Failure as Normal
- Implement Gradual Change
- Leverage Tooling & Automation
- Measure Everything

Now (**SRE**):

It's a way of accomplish DevOps philosophy.
**class SRE implements DevOps**. And this is how above items are responded from an SRE standpoint.

- Share ownership.
- SLOs & Blameless PMs.
- Reduce costs of failure (Canaries).
- Automate this year's job away.
- Measure toil and reliability.

---

## Chapter 1: Tenets of SRE

SRE team is responsible of the *availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of their services.

1. **Ensuring a durable Focus on Engineering**
50% of SRE's time should be dedicated on engineering and the remaining 50%, in operations with a suggested number of events of 2 in a 12 hs on-call shift. So they can get enough time for the blame-free postmortems analysis where the monitoring gaps and root causes are identified and assign actions to correct the problems.

2. **Pursuing Maximum Change Velocity Without Violating a Service's SLO**
Structural conflict is between pace of innovation and product stability. It's resolved with the introduction of an *error budget*. Reliability/availability target can´t be 100%. Developers use this error budget getting the maximum feature velocity as part of innovation.

    $$
    \text {Error Budget} = (1 - \text {Availability Target})
    $$

3. **Monitoring**
Monitoring shouldn´t fire notification to users to take action, there are three kinds of monitoring output:
    I. **Alerts** → Needs immediate reponse from the user.
    II **Tickets** → Needs non-immediate action from user.
    III **Logging** → No need to look for this but it's recorded for diagnostic or forensic purposes.

4. **Emergency Response**
Reliability is a function of mean time to failure (**MTTF**) and mean time to repair (**MTTR**), which is bring the system back to health.

5. **Change Management**
Use automation for:

    - Implementing progressive rollouts.
    - Quickly and accurately detecting problems.
    - Rolling back changes safely when problems arise.

6. **Demand Forecasting and Capacity Planning**
Organic demand → More users/traffic.
Inorganic demand → Business driven changes.
Do regular load testing.

7. **Provisioning**
It's a combination of change management and capacity planning. It's important do it only when it's necessary, as capacity is expensive.

8. **Efficiency and Performance**
Resource use is a function of: load, capacity and software efficiency. Job of SRE is to predict demand, provision capacity and can modify the software.

## Chapter 2: Prodction Environment from SRE viewpoint

### Hardware

Machine: It's a piece of hardware
Server: Software that implements a service

Borg?

---

## Chapter 3: Embracing Risk

Goal is to explicitly align the risk taken by a given service with the risk the business is willing to bear.

### Measuring Service Risk

Focus is on *unplanned downtime*.

#### Time-based availability

$$
availability = \frac{uptime}{uptime + downtime}
$$

#### Aggregate availability

$$
availability = \frac{\text {successful requests}}{\text {total requests}}
$$
&nbsp;

### Types of Failures

By Cost

- Proposed improvement in availability target: 99.9% → 99.99%
- Proposed increase in availability: 0.09%
- Service revenue: $1M
- Value of improved availability: $1M * 0.0009 = $900

Error budget

- Product managment defines an SLO. How much uptime the service should have by quarter.
- The actual uptime is measured by the monitoring system.
- The difference between these two is the budget.
- As long as the uptime measured is above the SLOW, new releases can be pushed.

---

## Chapter 4: Service Level Objectives

### SLI

Quantitative measure of some aspect of the level of service that is provided.

- **User-facing serving systems**: Availability, latency and throughput.
- **Storage systems**: Latency, Availability and Durability.
- **Big data systems**: Throughput, end-to-end latency.
- **All systems**: Correctness.

> [!TIP]
>
> - Use percentiles rather mean or median to avoid missing the outliers.
> - SLI specification should contain: aggregation intervals/regions, measurement frequency, how data is acquired, which requests are included and/or data-access latency (Time to last byte).

### SLO

For maximum clarity, SLOs should specify how they're measured and the conditions under which they're valid.

Example:

- 99% (averaged over 1 minute) of Get RPC calls will complete in less than 100 ms (measured across all the backend servers).
*Removing redundancy...*
- 99% of Get RPC calls will complete in less than 100 ms.
- 95% of throughput clients' Set RPC calls will complete in < 1s,
- 99% of latency clients' Set RPC calls with payloads < 1kB will complete in < 10 ms.

Suggestions:

- Don´t pick a target based on current performance.
- Keep it simple.
- Avoid absolutes.
- Have as few SLOs as possible.
- Perfection can wait.

### SLA

Is the consequence of missing an SLO. It ends up in a court case. Needs to be set up with product and legal team. Are difficult to modify or delete.

---

1. **Operations is a software problem**
The basic tenet of SRE is that doing operations well is a software problem. SRE should therefore use software engineering approaches to solve that problem. Software engineering as a discipline focuses on designing and building rather than operating and maintaining.
2. **Service Levels**
A *Service Level Objective* (SLO) is an availability target for a product of service (this is never 100%). In SRE, services are managed to the SLO.
&nbsp;
**SLI: Service Level Indicator**
An Indicator of the level of service your are providing. e.g. http request success rate 99%.
**SLO: Service Level Objective**
Specifies a target level for the reliability of your service e.g. what the success rate should be 98%.
**SLA: Service Level Agreement**
A business contract that comes into effect when your users are so unhappy you have to compensate them in some fashion.
&nbsp;
3. **Toil**
Any manual, mandated operation task is bad. If a task can be automated then it should be automated. Tasks can provide the *wisdowm of production* that will inform better system design and behavior. SREs must have time to make tomorrow better than today.
4. **Automation**
Automate what is currently done manually. Decide what and how to automate it.
Take an engineering-based approach to problems rather than just toiling at them over and over. This should dominate what an SRE does. Don´t automate a bad process. Fix that first!. The time we save by doing this will go into engineering better products and services.
5. **Reduce The Cost of Failure**
LAte problem (defect) discovery is expensive so SRE looks for ways to avoid this. Look to improve the *MTTR (Mean Time To Repair)*.
Smaller changes help with this, Canary deployments.
SREs embrace the DevOps/Lean concept of smaller batch size. Canary deployments reduce the risk of introducing a new software version in production by slowly rolling out the change to a small subset of users before rolling it out to everyone (like a canary in a mine). **FAILURE IS AN OPPORTUNITY TO IMPROVE**
6. **Shared Ownership**
SREs share skill sets with product develpment teams. Boundaries between "App Dev" and "PM" (DevOps) should be removed. In SRE we encourage more engineers to have experience of production deployments, not less. No one team or individual should become the Ops team.

## Source

Site Reliability Engineer [Book](https://learning.oreilly.com/library/view/site-reliability-engineering/9781491929117/)
<img src="https://rukminim2.flixcart.com/image/480/640/kjd6nww0-0/book/s/c/q/site-reliability-engineering-original-imafyxhgpdgzpnh8.jpeg?q=90" style="width:25%;">
