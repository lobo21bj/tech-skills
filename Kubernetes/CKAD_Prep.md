# Certified Kubernetes Application Developer Prep
<img src="https://www.globalitsuccess.com/images/product/Certified-Kubernetes-Application-Developer-small-new.webp" width=300 align="center" >

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

<img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1628000314071/HlHf3l2NI.png?auto=compress,format&format=webp">

&nbsp;

**Example of manifest file for creation:** 
```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: webserver
  name: webserver
spec:
  ports:
  - port: 80
  selector:
    app: webserver
  type: NodePort
```
&nbsp;
Get the status of your services
```sh
kubectl get service
```
>Sample output
<img src="https://i.postimg.cc/5tVxRcrn/kubectl-services.jpg">

* kubernetes is the 
* **NAME:** is the service unique name.
* **TYPE:** Service type.
* **CLUSTER-IP:** Would be the private IP address.
* **EXTERNAL-IP:** Will show the public IP address if applies.
* **PORT:** A port will automatically be assigned if it's not defined.
* **AGE:** Since when the services are running.

Get more full description of your service

```sh
kubectl describe service webserver
```
>Sample Output
<img src="https://i.postimg.cc/4y7k3wMY/image.png">
When Endpoints will list each Pod IP of the selected group (selector: app=webserver) along with the container port.

&nbsp;

Try it out:
Get the IP of the node
```sh
kubectl describe nodes | grep -i address -A 1
```
>Output
<img src="https://i.postimg.cc/5N51QKyz/image.png">

Test the webserver by running below command
```sh
curl 192.168.64.2:32337
```

#### Types
| Characteristic | ClusterIP | NodePort | LoadBalancer | ExternalName | Headless | Accessibility | Use case |
|---|---|---|---|---|---|---|---|
| Interface with external service discovery systems | Yes | Yes | Yes | Yes | Yes | External | Advanced custom networking that avoids automatic Kubernetes proxying |
| Client connection type | Stable cluster-internal IP address or DNS name | Port on Node IP address | IP address of external load balancer | Stable cluster-internal IP address or DNS name | Stable-cluster internal IP address or DNS name that also enables DNS resolution of the Pod IPs behind the Service | Internal | Internal communications between workloads |
| External dependencies | None | Free port on each Node | A Load Balancer component (typically billable by your cloud provider) | None | None | External | Accessing workloads outside the cluster, for one-off or development use |
| Suitable for | Internal communications between workloads | Accessing workloads outside the cluster, for one-off or development use | Serving publicly accessible web apps and APIs in production | Decoupling your workloads from direct dependencies on external service URLs | Internal communications between workloads | External | Expose Pods to other Pods in your cluster |
| Expose Pods to other Pods in your cluster | Yes | No | No | No | Yes | Internal | Expose Pods to other Pods in your cluster |
| Expose Pods on a specific Port of each Node | No | Yes | No | No | No | External | Expose Pods on a specific Port of each Node |
| Expose Pods using a cloud load balancer resource | No | No | Yes | No | No | External | Expose Pods using a cloud load balancer resource |
| Configure a cluster DNS CNAME record that resolves to a specified address | No | No | No | Yes | No | External | Configure a cluster DNS CNAME record that resolves to a specified address |

---

### Multi-Container Pods

Refers to multiple containers within the same pod.

<img src="https://i.postimg.cc/650MKXjy/image.png">
&nbsp;

#### Namespace
- Separate resources according to users, environments or applications.
- Role based access control (RBAC) to secure access per Namespace.
- Using Namespaces is a best practice.

It can be created with below command
```sh
Kubectl create -f 3.1-namespace.yaml
```

where 3.1-namespace.yaml contents is:
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: microservice
  labels:
    app: counter
```
&nbsp;

The multi-container Pod is created with this command. It's associated to aforementioned namespace.
```sh
Kubectl create -f 3.2-multi_container.yaml -n microservice
```
And the yaml content is
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: redis
      image: redis:latest
      imagePullPolicy: IfNotPresent
      ports:
        - containerPort: 6379
    
    - name: server
      image: lrakai/microservices:server-v1
      ports:
        - containerPort: 8080
      env:
        - name: REDIS_URL
          value: redis://localhost:6379

    - name: counter
      image: lrakai/microservices:counter-v1
      env:
        - name: API_URL
          value: http://localhost:8080

    - name: poller
      image: lrakai/microservices:poller-v1
      env:
        - name: API_URL
          value: http://localhost:8080
```
> [!NOTE]
> Redis is an open source data structure server. It belongs to the class of NoSQL databases known as key/value stores.

&nbsp;

Command to check event logs related to pod **app** in **microservice** namespace
```sh
Kubectl describe -n microservice pod app
```
<img src="https://i.postimg.cc/jdzGJm8b/image.png">
&nbsp;

To check the logs associated to each container
```sh
Kubectl logs -n microservice app counter --tail 10       # last 10 lines of counter container
```
```sh
Kubectl logs -n microservice app poller -f               # interactive of poller container
```