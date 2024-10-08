# Certified Kubernetes Application Developer Prep

## Architecture
**Nodes** are the machines in the cluster.
Nodes are categorized as **workers** or **masters**.

**Worker nodes** include software to run containers managed by the Kubernetes control plane.

**Master nodes** run the **control plane**.

The **control plane** is a set of APIs and software that Kubernetes users interact with.

The APIs and software are referred to as **master components**. 

----

## Iterecting with K8s

<details>
<summary><b>Method 1: REST API</b></summary>

* **Direct interaction:** While possible, it's not common.
* **Necessity:** May be required if there's no Kubernetes client library for your programming language.
</details>

<details>
<summary><b>Method 2: Client Libraries</b></summary>

* **Abstraction:** Handles authentication, managing individual REST API requests and responses.
* **Official libraries:** Kubernetes maintains official client libraries for various programming languages.
* **Community-maintained libraries:** Available for languages without official libraries.
</details>

<details>
<summary><b>Method 3: kubectl</b></summary>

* **Command-line interface:** Issues high-level commands that are translated into REST API calls.
* **Local and remote clusters:** Works with both local and remote Kubernetes clusters.
* **Most common commands:**
  * Create: create new resources.
  * Delete: delete existing resources.
  * Apply: Set configuration to existing resources.
  * Get: List the existing resources.
  * Describe: Detailed info of a resource.
  * Logs: See the log of each resource.
</details>

<details>
<summary><b>Method 4: Web Dashboard</b></summary>

* **Graphical user interface:** Provides a visual way to interact with Kubernetes resources.
* **Accessibility:** User-friendly for those who prefer a visual interface.
</details>

---

### Pods

What's in a Pod Declaration?

#### Pod Declaration Components

* **Container image:** Specifies the image to be used for the container.
* **Container ports:** Defines the ports exposed by the container.
* **Container restart policy:** Determines how the container should be restarted if it fails.
* **Resource limits:** Sets limits on the resources (CPU, memory) that the container can use.

#### Manifest Files

* **Declare desired properties:** Manifests define the desired state of Kubernetes resources.
* **Describe all kinds of resources:** Manifests can describe various types of resources, including Pods, Deployments, Services, etc.
* **Resource-specific properties:** The `spec` section of a manifest contains properties specific to the resource type.

**Example of manifest file:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
  namespace: mynamespace
  labels:
    app: webserver
spec:
  containers:
  - name: mycontainer
    image: nginx:latest
    resources:
      requests:
        memory: "128Mi" # 128 Mi = 128 mebibytes
        cpu: "500m"     # 500m = 500 milliCPUs (1/2 CPU)
      limits:
        memory: "128Mi"
        cpu: "500m"
    ports:
      - containerPort: 80
```

If the requirements are met the QoS Class will be Guaranteed when you describe the pod.

#### Getting the status of the Pod

Get the status of your pods with aditional information
```sh
kubectl get pods -o wide
```
>Sample output
<img src="https://cdn.prod.website-files.com/64b7506ad75bbfcf43a51e90/65411cc00707e2a0ae8a2a2d_E2yi_WHKRBViatddnxALPIXAGNDAQ3i_EuOooW9xklKNQAkPlfs-Pr0WfMYUjcNii6Q-IQPUTkr8xp-zwkRMFLq9lMz51pNuuANZzc3veuxA5SyodL0t3LSYw-VsU3HhogHo4L1LHcsXJVwaoWa3_f4.png">

References:
* **Two Pods:** There are two Pods running in the cluster.
* **Name:** The name of each Pod is `nginx-deployment-cbdccf466-4h7dv` and `nginx-deployment-cbdccf466-c8wlb`.
* **Ready:** Both Pods are ready, meaning they are running and accepting connections.
* **Status:** Both Pods have a status of `Running`, indicating they are actively executing.
* **Restarts:** Neither Pod has been restarted.
* **Age:** Both Pods have been running for approximately 3 minutes and 46 seconds.
* **IP:** The IP address of each Pod is `10.0.0.10` and `10.0.0.11`, respectively.
* **NODE:** The Node where each Pod is currently running is `worker-node1` and `worker-node2`, respectively.
* **NOMINATED NODE:** Both Pods have no nominated Node, indicating that the scheduler has not yet selected a preferred Node for them.
* **READINESS GATES:** Both Pods have no readiness gates defined, meaning they are considered ready as soon as their containers are running.

----
### Services

* **Defines networking rules:** 
  * For accessing Pods in the cluster
  * And from the internet

* **Uses labels:**
  * To select a group of Pods

* **Has a fixed IP address**

* **Distributes requests:**
  * Across Pods in the group