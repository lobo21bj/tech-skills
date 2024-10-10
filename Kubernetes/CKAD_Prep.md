# Certified Kubernetes Application Developer Prep
<p align="center">
<img src="https://images.credly.com/images/cc8adc83-1dc6-4d57-8e20-22171247e052/blob" width=300 >
</p>

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

Another example of ClusterIP service implementation
<img src="https://i.postimg.cc/d0VrVSBq/image.png">

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

<img src="https://i.postimg.cc/rFh8LnKG/image.png">
&nbsp;

<img src="https://i.postimg.cc/HkcC1pGH/image.png">
&nbsp;

<img src="https://i.postimg.cc/5tdDcLqq/image.png">

> [!WARNING]
> It's not recommended to use NodePort for external connections!

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
kubectl create -f 3.1-namespace.yaml
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
kubectl create -f 3.2-multi_container.yaml -n microservice
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
kubectl describe -n microservice pod app
```
<img src="https://i.postimg.cc/jdzGJm8b/image.png">
&nbsp;

To check the logs associated to each container
```sh
kubectl logs -n microservice app counter --tail 10       # last 10 lines of counter container
```
```sh
kubectl logs -n microservice app poller -f               # interactive of poller container
```
---

### Service Discovery
&nbsp;

**What are Kubernetes Services?**

In a Kubernetes cluster, Services act as a layer of abstraction between pods and their clients. They provide a stable network endpoint for a set of pods, regardless of individual pod IP address changes.

**Why Services?**

* **Supports multi-pod design:** Services allow you to scale applications horizontally by adding more pods without affecting clients.
* **Provides static endpoint:** Each Service has a fixed IP address and port, making it easy for clients to connect.
* **Handles Pod IP changes:** When pods are added, removed, or replaced, Services automatically update their internal routing table to ensure clients can always reach the correct pods.
* **Load balancing:** Services can distribute traffic across multiple pods based on various load balancing algorithms.
&nbsp;

**Service Discovery Mechanisms**

Kubernetes offers two primary mechanisms for service discovery:

#### Environment Variables
* **Automatic injection:** Services automatically inject their IP address and port into containers as environment variables.
* **Naming conventions:** Environment variables follow specific naming conventions based on the service name, making it easy for applications to access them.

#### DNS
* **Automatic creation:** Kubernetes creates DNS records for Services in the cluster's DNS.
* **Container configuration:** Containers are automatically configured to use the cluster's DNS, allowing them to resolve service names to IP addresses.

**Visual Representation**

<img src="https://i.postimg.cc/htVTnbPM/image.png">
&nbsp;

**Key Points**
* Services are essential for building scalable and resilient applications in Kubernetes.
* They provide a stable network endpoint for a set of pods.
* Services use environment variables and DNS for service discovery.
* Understanding Services is crucial for effective Kubernetes development and operations.


**Creating the tiers**

We can create multiple resources in one unique manifest yaml file by separating them with "---"
```sh
kubectl create -f 4.2-data_tier.yaml -n service-discovery
```

4.2-data_tier.yaml content
```yaml
apiVersion: v1
kind: Service
metadata:
  name: data-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 6379
    protocol: TCP # default 
    name: redis # optional when only 1 port
  selector:
    tier: data 
  type: ClusterIP # default
---
apiVersion: v1
kind: Pod
metadata:
  name: data-tier
  labels:
    app: microservices
    tier: data
spec:
  containers:
    - name: redis
      image: redis:latest
      imagePullPolicy: IfNotPresent
      ports:
        - containerPort: 6379
```
&nbsp;

To describe the newly created tier
```sh
kubectl describe -n service-discovery service data-tier
```
> It has a public IP and it points to pod endpoint.
<img src="https://i.postimg.cc/vT1xN5Nr/image.png">
&nbsp;

Moving on lets create the app tier
```sh
kubectl create -f 4.3-app_tier.yaml -n service-discovery
```

4.3-app_tier.yaml content
```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 8080
  selector:
    tier: app
---
apiVersion: v1
kind: Pod
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  containers:
    - name: server
      image: lrakai/microservices:server-v1
      ports:
        - containerPort: 8080
      env:
        - name: REDIS_URL
          # Environment variable service discovery
          # Naming pattern:
          #   IP address: <all_caps_service_name>_SERVICE_HOST
          #   Port: <all_caps_service_name>_SERVICE_PORT
          #   Named Port: <all_caps_service_name>_SERVICE_PORT_<all_caps_port_name>
          value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
          # In multi-container example value was
          # value: redis://localhost:6379 
```

The app gets the host and port of data tier via environment variables
```
$(DATA_TIER_SERVICE_HOST) & $(DATA_TIER_SERVICE_PORT_REDIS)
```
&nbsp;

Creating the support tier
```sh
kubectl create -f 4.4-support_tier.yaml -n service-discovery
```

4.4-support_tier.yaml content
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: support-tier
  labels:
    app: microservices
    tier: support
spec:
  containers:

    - name: counter
      image: lrakai/microservices:counter-v1
      env:
        - name: API_URL
          # DNS for service discovery
          # Naming pattern:
          #   IP address: <service_name>.<service_namespace>
          #   Port: needs to be extracted from SRV DNS record
          value: http://app-tier.service-discovery:8080

    - name: poller
      image: lrakai/microservices:poller-v1
      env:
        - name: API_URL
          # omit namespace to only search in the same namespace
          value: http://app-tier:$(APP_TIER_SERVICE_PORT)
```
> It uses DNS. If it will be used in the same namespace only, you can ommit the service-discovery.
&nbsp;

**Final state**
```sh
kubectl get pods -n service-discovery
```
<img src="https://i.postimg.cc/tRLzHgNq/image.png">

&nbsp;

App is up and running...

```sh
kubectl logs -n service-discovery support-tier poller -f
```
<img src="https://i.postimg.cc/R0V7TJ4R/image.png">
&nbsp;

#### MultiPort configuration

<img src="https://i.postimg.cc/FF3dN44y/image.png">

>each port can have a name defined for easier configuration
<img src="https://i.postimg.cc/vB9BYWpY/image.png">


---

### Deployments

**Deployment** is a template to create Pods. It's used to create replicas, which are copies of a pod.
The **Deployment Controller** is a master component responsible for converging the actual state of the system to the desired state. 

- **Replicas:** A Deployment manages multiple instances (replicas) of a Pod.
- **Desired State:** It defines the target configuration for the application.
- **Deployment Controller:** Ensures that the actual state aligns with the desired state.

**Example:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-image:latest
```
> [!NOTE]
> This deployment creates 3 replicas of a Pöd with the label "app=my-app"

> [!WARNING]
> API Grouping: Kubernetes groups its resources into different API groups for better organization and scalability.
> The core API group is represented as v1, which includes core resources like Pod, Service, ConfigMap, etc.
> The apps API group includes resources related to applications, such as Deployment, DaemonSet, StatefulSet, etc.

&nbsp;

The deployment is app and running:
```sh
kubectl get -n deployments deployments
```
<img src="https://i.postimg.cc/2S4kq4G3/image.png">

&nbsp;

```sh
kubectl get -n deployments pods
```
<img src="https://i.postimg.cc/7LwxSft9/image.png">

&nbsp;

If we want to apply horizontal scalling and scale up the app-tier & support-tier deployment to 5 replicas:
```sh
kubectl scale -n deployments deployments app-tier support-tier --replicas=5
```

<img src="https://i.postimg.cc/3RbYM98f/image.png">

&nbsp;

We can also validate that app-tier service now has 5 endpoints:

```sh
kubectl describe -n deployments service app-tier
```

<img src="https://i.postimg.cc/brD8qbdy/image.png">

---

### Autoscaling

**Autoscaling Deployments** in Kubernetes allow you to automatically scale the number of replicas of a Deployment based on resource utilization, such as CPU or custom metrics.

**Key features:**

- **Automatic Scaling:** Adjusts the number of replicas to match demand.
- **CPU Utilization:** Scales based on the percentage of CPU used by the Pods.
- **Custom Metrics:** Can use other metrics like memory usage, network traffic, or application-specific data.
- **Target CPU:** Defines the desired CPU utilization level.
- **Min/Max Replicas:** Sets limits on the minimum and maximum number of replicas.

In order to use autoscalling **Metrics** are required.
- Autoscalling depends on metrics being collected.
- **Metrics Server** is one solution for collecting metrics.
- Several manifest files are used to deploy **Metrics Server** ([Repos]([Metrics](https://github.com/kubernets-sigs/metrics-server)))

To install **Metrics Server**:

```sh
kubectl apply -f metrics-server/
```

&nbsp;

Once deployed we see the status of the running pods

```sh
kubectl top pods -n deployments
```
<img src="https://i.postimg.cc/66rxf9R1/image.png">

&nbsp;

We can also specify resource request of 20m of CPU. in *6.1-app_tier_cpu_request.yaml*.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-tier
  labels:
    app: microservices
spec:
  ports:
  - port: 8080
  selector:
    tier: app
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  replicas: 5
  selector:
    matchLabels:
      tier: app
  template:
    metadata:
      labels:
        app: microservices
        tier: app
    spec:
      containers:
      - name: server
        image: lrakai/microservices:server-v1
        ports:
          - containerPort: 8080
        resources:
          requests:
            cpu: 20m # 20 milliCPU / 0.02 CPU
        env:
          - name: REDIS_URL
            # Environment variable service discovery
            # Naming pattern:
            #   IP address: <all_caps_service_name>_SERVICE_HOST
            #   Port: <all_caps_service_name>_SERVICE_PORT
            #   Named Port: <all_caps_service_name>_SERVICE_PORT_<all_caps_port_name>
            value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
            # In multi-container example value was
            # value: redis://localhost:6379 
```

```sh
kubectl create -f 6.1-app_tier_cpu_request.yaml -n deployments
```
> ![CUATION]
> Fails cause the resources already exists

```sh
kubectl apply -f 6.1-app_tier_cpu_request.yaml -n deployments
```
<img src="https://i.postimg.cc/BbsyVKD7/image.png">

&nbsp;

#### HorizontalPodAutoscaler component
6.2-autoscale.yaml content:
```yaml
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: app-tier
  labels:
    app: microservices
    tier: app
spec:
  maxReplicas: 5
  minReplicas: 1
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app-tier
  targetCPUUtilizationPercentage: 70
```

```sh
kubectl create -f 6.2-autoscale.yaml -n deployments
```

Once done, we can check the status in real time by running below, it will keep updating every 1 s.

```sh
watch -n 1 kubectl get -n deployments deployment
```

By checking the

```sh
kubectl api-resources
```

we see that *hpa* is the alias of HorizontalPodAutoscaler resource.

To see full desciption of the resource including a list of events
```sh
kubectl describe -n deployments hpa
```
<img src="https://i.postimg.cc/wxVbB3DH/image.png">

&nbsp;

To see the actual status of the hpa
```sh
kubectl get -n deployments hpa
```
<img src="https://i.postimg.cc/xT1pNYPm/image.png">

&nbsp;

If you want edit an apply it you can go with:

```sh
kubectl edit -n deployments hpa
```

---

### Rolling Updates and Rollbacks