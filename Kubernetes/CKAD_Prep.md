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

Kubernetes provides multiple deployment strategies for managing updates to applications. The goal is to update applications with minimal downtime or disruptions. Below are the four common deployment strategies supported in Kubernetes.




<details>
<summary><b>1. RollingUpdate (Default)</b> </summary>

The default deployment strategy for Kubernetes Deployments. It allows you to incrementally replace old pods with new ones while maintaining the application’s availability.

##### Key Parameters:
- **maxUnavailable**: Maximum number of pods that can be unavailable during the update. Default is 25%.
- **maxSurge**: Maximum number of extra pods that can be created during the update. Default is 25%.

##### Example:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    spec:
      containers:
        - name: my-app-container
          image: my-app:2.0
```

##### Benefits:
- Ensures application availability during updates.
- Gradual rollout allows monitoring for issues.

##### Drawbacks:
- May take longer depending on the number of replicas and settings of `maxUnavailable` and `maxSurge`.
</details>

<details>
<summary><b>2. Recreate</b></summary>

In the `Recreate` strategy, all old pods are terminated before new pods are created. This means there will be downtime during the deployment process.

##### Example:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  strategy:
    type: Recreate
  template:
    spec:
      containers:
        - name: my-app-container
          image: my-app:2.0
```

#### Benefits:
- Ensures that only the new version is running, with no overlap between versions.

#### Drawbacks:
- Downtime is guaranteed while the old pods are terminated and new ones are spun up.
</details>

<details>
<summary><b>3. Blue-Green</b></summary>

In a Blue-Green deployment, two environments (blue and green) are maintained. The "blue" environment runs the current version, and the "green" environment is the new version. Once the new version is verified, traffic is switched to the "green" environment.

##### Steps:
1. Deploy the new version to the green environment (without impacting blue).
2. Once verified, switch traffic to the green environment.
3. Optionally, keep the blue environment as a backup until confident.

##### Example (simplified workflow):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-green
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: my-app-container
          image: my-app:2.0
```

##### Benefits:
- Zero downtime during the switch.
- Quick rollback by switching traffic back to the blue environment.

##### Drawbacks:
- Requires double the resources (both environments running simultaneously).
- Switching traffic can introduce complexity.
</details>

<details>
<summary><b>4. Canary</b></summary>

Canary deployments involve releasing the new version to a small subset of users first (a "canary" group). Based on feedback and performance, the new version is gradually rolled out to the rest of the users.

##### Steps:
1. Deploy the new version to a small percentage of the user base.
2. Monitor the new version for issues.
3. Gradually increase the percentage of users directed to the new version until 100%.

##### Example (simplified workflow):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-canary
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0
      maxSurge: 1
  template:
    spec:
      containers:
        - name: my-app-container
          image: my-app:2.0
```
> [!NOTE]
> In this example, the new canary version could start with 10% of the traffic and gradually increase.

#### Benefits:
- Safer and incremental rollout, allowing testing with a subset of users.
- Easier to catch issues early before a full rollout.

#### Drawbacks:
- Slightly more complex to configure and monitor.
- Requires constant monitoring during the gradual rollout.
</details>

&nbsp;

#### Conclusion

When choosing a deployment strategy in Kubernetes, consider your application's availability requirements and resource constraints. Here's a quick summary:

- **RollingUpdate**: Default and gradual rollout. Ideal for applications requiring high availability.
- **Recreate**: Full downtime but simple. Suitable for non-critical applications.
- **Blue-Green**: Zero downtime but resource-intensive. Best for large-scale, mission-critical applications.
- **Canary**: Safe, incremental rollout. Suitable for applications where testing with a subset of users is beneficial.

---

### Probes

Kubernetes provides mechanisms to check the health and status of containers running inside Pods. These mechanisms are called **Probes**. A probe can be used to determine the readiness or liveness of a container and help ensure high availability and efficient resource utilization in your cluster.

##### Types of Probes

1. **Liveness Probe**:
    - Checks if the application running in the container is still alive.
    - If the liveness probe fails, the container is killed and restarted according to the `restartPolicy`.
  
2. **Readiness Probe**:
    - Checks if the application is ready to start serving traffic.
    - If the readiness probe fails, the Pod is temporarily removed from the Service’s load balancer, but the container is not restarted.
  
3. **Startup Probe**:
    - Checks whether the application within a container has started.
    - Useful for slow-starting containers.
    - After the startup probe succeeds, Kubernetes switches to using the liveness probe.

&nbsp;

##### Probe Types by Mechanism

Kubernetes provides three types of mechanisms to perform probes:

1. **HTTP Probe**:
    - Kubernetes sends an HTTP GET request to the container. If the response has a status code greater than or equal to 200 and less than 400, the probe is considered successful.

    ```yaml
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 3
      periodSeconds: 3
    ```

2. **TCP Socket Probe**:
    - Kubernetes tries to establish a TCP connection on the specified port of the container. If the connection can be established, the probe is considered successful.

    ```yaml
    livenessProbe:
      tcpSocket:
        port: 3306
      initialDelaySeconds: 5
      periodSeconds: 10
    ```

3. **Exec Probe**:
    - Kubernetes executes a command inside the container. If the command exits with a status code of 0, the probe is successful.

    ```yaml
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 5
      periodSeconds: 5
    ```

#### Key Probe Parameters

- `initialDelaySeconds`: The number of seconds after the container starts before the first probe is initiated.
- `periodSeconds`: How often (in seconds) to perform the probe.
- `timeoutSeconds`: Number of seconds after which the probe times out if no response is received.
- `failureThreshold`: When a probe fails, Kubernetes will try `failureThreshold` times before considering the container to have failed.
- `successThreshold`: Minimum consecutive successes for the probe to be considered successful after it fails.

#### Example 
data-tier deployment
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
apiVersion: apps/v1 # apps API group
kind: Deployment
metadata:
  name: data-tier
  labels:
    app: microservices
    tier: data
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: data
  template:
    metadata:
      labels:
        app: microservices
        tier: data
    spec: # Pod spec
      containers:
      - name: redis
        image: redis:latest
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 6379
            name: redis
        livenessProbe:
          tcpSocket:
            port: redis # named port
          initialDelaySeconds: 15
        readinessProbe:
          exec:
            command:
            - redis-cli
            - ping
          initialDelaySeconds: 5
```
&nbsp;

app-tier deployment
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
  replicas: 1
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
            name: server
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
          - name: DEBUG
            value: express:*
        livenessProbe:
          httpGet:
            path: /probe/liveness
            port: server
          initialDelaySeconds: 5
        readinessProbe:
          httpGet:
            path: /probe/readiness
            port: server
          initialDelaySeconds: 3
```

---

### Init Containers

Init Containers allow you to perform tasks before main application containers have an opportunity to start.
It's useful for checking preconditions and preparing dependencies.
They run every time a Pod is created and use their own image.

##### Usage

Inside app-tier deployment at the containers level
```yaml
initContainers:
        - name: await-redis
          image: lrakai/microservices:server-v1
          env:
          - name: REDIS_URL
            value: redis://$(DATA_TIER_SERVICE_HOST):$(DATA_TIER_SERVICE_PORT_REDIS)
          command:
            - npm
            - run-script
            - await-redis
```
If we check the status of the Pod once is initialized..

```sh
kubectl -n probes describe pods
```

<img src="https://i.postimg.cc/GpT2rz8X/image.png">

---

### Volumes

Kubernetes Volumes provide a way for containers to store and share data beyond their ephemeral lifecycle. While the container's file system is temporary, a volume allows data to persist as long as the Pod is running, and in some cases, even beyond that.

#### Why Use Volumes?

- **Persistent Data**: Containers' file systems are ephemeral. When a container crashes or restarts, all data inside it is lost. Volumes provide a mechanism to store data that needs to persist.
- **Data Sharing**: Multiple containers within the same Pod can share the same volume, allowing them to access the same files or directories.
- **Integration with External Storage**: Volumes can be connected to external storage systems, allowing you to use cloud providers, NFS, or other storage solutions.

#### Volume Types

Kubernetes supports various types of volumes, each suited to different use cases:

<details>
<summary><b>1. emptyDir</b></summary>

- **Purpose**: Temporary storage for the lifetime of the Pod.
- **Use Case**: For data sharing between containers in the same Pod, scratch space, or temporary storage.
- **Lifecycle**: Data is deleted when the Pod is deleted.

Example:
```yaml
volumes:
  - name: cache-volume
    emptyDir: {}
```
</details>

<details>
<summary><b>2. hostPath</b></summary>

- **Purpose**: Mounts a file or directory from the host node's filesystem into the Pod.
- **Use Case**: Accessing specific files or directories on the host machine.
- **Security Warning**: Can compromise security since it gives containers access to the host machine's filesystem.

Example:
```yaml
volumes:
  - name: host-volume
    hostPath:
      path: /data
```
</details>

<details>
<summary><b>3. persistentVolumeClaim (PVC)</b></summary>

- **Purpose**: Claims persistent storage resources.
- **Use Case**: Allows users to dynamically request storage based on predefined `PersistentVolumes` (PVs) or through a storage class.
- **Lifecycle**: Data can persist beyond the lifecycle of the Pod.

Example:
```yaml
volumes:
  - name: my-pvc-volume
    persistentVolumeClaim:
      claimName: my-pvc
```
</details>

<details>
<summary><b>4. configMap</b></summary>

- **Purpose**: Mounts configuration data from a `ConfigMap` into the Pod.
- **Use Case**: Inject configuration settings or files into containers.
- **Lifecycle**: Data is managed externally in the `ConfigMap`.

Example:
```yaml
volumes:
  - name: config-volume
    configMap:
      name: my-config
```
</details>

<details>
<summary><b>5. secret</b></summary>

- **Purpose**: Mounts sensitive data like passwords, tokens, or keys stored in a Kubernetes `Secret`.
- **Use Case**: Securely provide credentials or sensitive data to containers.
- **Lifecycle**: Managed externally in a `Secret`.

Example:
```yaml
volumes:
  - name: secret-volume
    secret:
      secretName: my-secret
```
</details>

<details>
<summary><b>6. nfs</b></summary>

- **Purpose**: Mounts an NFS (Network File System) share.
- **Use Case**: Sharing data between different Pods or across nodes in a cluster.
- **Lifecycle**: Managed externally and accessible to any node in the cluster.

Example:
```yaml
volumes:
  - name: nfs-volume
    nfs:
      server: nfs-server.example.com
      path: /data
```
</details>

&nbsp;

#### Volume Mounts

Once volumes are defined in a Pod spec, they must be mounted inside the container. Each volume can be mounted to one or more containers in the Pod.

Example:
```yaml
containers:
- name: app-container
  image: nginx
  volumeMounts:
  - mountPath: /usr/share/nginx/html
    name: cache-volume
```

In this example:
- `volumeMounts` specifies where the volume is mounted inside the container.
- `mountPath` is the path inside the container where the volume will be accessible.
- `name` references the defined volume (`cache-volume` in this case).

#### Volume Lifecycle

- **Pod Lifetime**: A volume is tied to the lifecycle of a Pod, unless it is backed by an external storage system (e.g., Persistent Volumes, NFS).
- **Ephemeral or Persistent**: Volumes like `emptyDir` are ephemeral and exist only for the duration of the Pod. Others, like `persistentVolumeClaim`, are backed by persistent storage and can outlive a Pod's lifecycle.

#### Persistent Volumes and Claims

To decouple storage from Pods, Kubernetes uses **Persistent Volumes (PVs)** and **Persistent Volume Claims (PVCs)**:
- **PersistentVolume (PV)**: A cluster-level resource that represents physical storage, such as cloud storage, NFS, or a local disk.
- **PersistentVolumeClaim (PVC)**: A request for storage made by a Pod. The PVC binds to a PV that matches the requested storage requirements.

##### Example of Persistent Volume and Persistent Volume Claim

**PersistentVolume (PV):**
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  nfs:
    server: nfs-server.example.com
    path: /data
```

**PersistentVolumeClaim (PVC):**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```
> [!NOTE]
> The **PersistentVolume (PV)** provides 10Gi of storage.
> The **PersistentVolumeClaim (PVC)** requests 5Gi of storage and will bind to an appropriate PV (such as `my-pv`).

&nbsp;

#### Access Modes

Different types of volumes support different access modes, specifying how volumes can be mounted:
- **ReadWriteOnce (RWO)**: The volume can be mounted as read-write by a single node.
- **ReadOnlyMany (ROX)**: The volume can be mounted as read-only by many nodes.
- **ReadWriteMany (RWX)**: The volume can be mounted as read-write by many nodes.

Summarized example: in **data-tier** deployment:

<img src="https://i.postimg.cc/jjQwt9NR/image.png">

```yaml
xxx
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: data-tier-volume
spec:
  capacity:
    storage: 1Gi # 1 gibibyte
  accessModes:
    - ReadWriteOnce
  awsElasticBlockStore: 
    volumeID: INSERT_VOLUME_ID # replace with actual ID
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-tier-volume-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 128Mi # 128 mebibytes 
---
apiVersion: apps/v1 # apps API group
kind: Deployment
metadata:
  name: data-tier
  labels:
    app: microservices
    tier: data
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: data
  template:
    metadata:
      labels:
        app: microservices
        tier: data
    spec: # Pod spec
      containers:
      - name: redis
        image: redis:latest
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 6379
            name: redis
        livenessProbe:
          tcpSocket:
            port: redis # named port
          initialDelaySeconds: 15
        readinessProbe:
          exec:
            command:
            - redis-cli
            - ping
          initialDelaySeconds: 5
        volumeMounts:
          - mountPath: /data
            name: data-tier-volume
      volumes:
      - name: data-tier-volume
        persistentVolumeClaim:
          claimName: data-tier-volume-claim
```

---

### ConfigMap and Secrets

In Kubernetes, **ConfigMaps** and **Secrets** are used to manage configuration data and sensitive information, respectively. They allow you to decouple configuration artifacts from container images, providing flexibility in how your applications are configured.


#### ConfigMaps and Secrets

* **Separate configuration from Pod specs:** Results in easier to manage and more portable manifests.
* **Both are similar but Secrets are specifically for sensitive data:** There are specialized types of Secrets for storing Docker registry credentials and TLS certificates.
* **We will focus on the generic Secrets.**

#### Using ConfigMaps and Secrets

- Data stored in key-value pairs.**
- Pods must reference ConfigMaps or Secrets to use their data.**
- References can be made by mounting Volumes or setting environment variables.

**ConfigMap Example:**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
data:
  my-key: my-value
```

**Secrets Example:**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  my-secret-key: base64encodedvalue
```

**Pod Manifest Example:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-app
    env:
    - name: MY_CONFIG_VALUE
      valueFrom:
        configMapKeyRef:
          name: my-configmap
          key: my-key
    - name: MY_SECRET_VALUE
      valueFrom:
        secretKeyRef:
          name: my-secret
          key: my-secret-key
```

---

### Kubernetes Ecosystem

You'll find below a set of useful tools that compatible with Kubernetes.

<details>
<summary><b>Helm:</b> The Package Manager for Kubernetes</summary>

**What is Helm?**

* A tool for packaging and deploying Kubernetes applications.
* Manages a collection of Kubernetes resources as a single unit.
* Simplifies the process of installing, upgrading, and managing complex applications.

**Key Components:**

* **Charts:** Templates that define a set of Kubernetes resources.
* **Helm Client:** Interacts with the Helm server to manage charts.
* **Tiller:** A server-side component that deploys charts to Kubernetes.

**Benefits of Using Helm:**

* **Simplified Deployment:** Packages complex applications into a single unit.
* **Version Control:** Tracks changes to charts and their dependencies.
* **Reusable Components:** Creates reusable building blocks for applications.
* **Community-Driven:** Benefits from a large and active community.

**Basic Helm Commands:**

* **helm init:** Initializes Helm and installs Tiller.
* **helm search:** Searches for charts in the official Helm repository.
* **helm repo add:** Adds a custom chart repository.
* **helm install:** Installs a chart to Kubernetes.
* **helm upgrade:** Upgrades an existing chart.
* **helm delete:** Deletes an installed chart.

**Example:**

```bash
helm repo add stable https://charts.helm.sh/stable
helm install my-nginx stable/nginx
```
> [!NOTE]
> This command installs the Nginx chart from the stable repository with the name "my-nginx".

**Additional Features:**

- **Values Files:** Customize chart values during installation.
- **Hooks:** Execute scripts before or after chart installation.
- **Plugins:** Extend Helm's functionality with custom plugins.

Helm is a powerful tool for managing Kubernetes applications. It simplifies the deployment and management of complex applications, making Kubernetes more accessible to developers and operations teams.
</details>

<details>
<summary><b>Kustomize:</b> A Tool for Customizing Kubernetes Manifests</summary>

**What is Kustomize?**

- A tool for customizing Kubernetes YAML manifests.
- Helps manage the complexity of your applications.
- Works by using a `kustomization.yaml` file that declares customization rules.
- Original manifests remain untouched and usable.

**Key Features:**

- **Generating ConfigMaps and Secrets from files:** Creates ConfigMaps and Secrets based on the contents of files.
- **Configuring common fields across multiple resources:** Sets common labels, annotations, or other fields for multiple resources.
- **Applying patches to any field in a manifest:** Modifies specific fields in a manifest without directly editing the original file.
- **Using overlays to customize base groups of resources:** Creates overlays to customize specific parts of a base set of resources.

**Using Kustomize:**

- Kustomize is directly integrated with `kubectl`.
- Include the `--kustomize` or `-k` option to `kubectl create` or `kubectl apply` commands.

**Example:**

```yaml
# kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- deployment.yaml
- service.yaml
patchesStrategicMerge:
- patch.yaml
configMapGenerator:
- name: my-configmap
  envVarPrefix: MY_CONFIG
  literals:
  - MY_VAR=my-value
```

This `kustomization.yaml` file:

- Specifies the base resources (deployment.yaml and service.yaml).
- Applies a strategic merge patch from patch.yaml.
- Generates a ConfigMap named "my-configmap" with an environment variable prefix "MY_CONFIG" and a literal value "MY_VAR=my-value".

By running `kubectl apply -k .`, Kustomize will apply the customized resources to your Kubernetes cluster.

Kustomize is a valuable tool for managing and customizing Kubernetes applications, especially when dealing with complex deployments or requiring frequent changes.
</details>

<details>
<summary><b>Prometheus:</b> A Monitoring and Alerting System</summary>

**What is Prometheus?**

- An open-source monitoring and alerting system.
- A server for pulling in and storing time series metric data.
- Inspired by an internal monitoring tool at Google called borgmon.
- De facto standard solution for monitoring Kubernetes.

**Prometheus + Kubernetes:**

- Kubernetes components supply all their own metrics in PromQL format.
- Many more metrics than Metrics Server.
- Adapter available to autoscale using metrics in Prometheus rather than CPU utilization.
- Commonly paired with Grafana for visualizations.
- Define alert rules and send notifications.
- Easily installed via Helm chart.

**Key Points:**

- Prometheus is a powerful tool for monitoring Kubernetes applications.
- It provides a rich set of metrics and alerting capabilities.
- It integrates seamlessly with Kubernetes components.
- It's often used in conjunction with Grafana for visualization and alerting.

</details>

<details>
<summary><b>Kubeflow:</b> A Machine Learning Platform</summary>

**What is Kubeflow?**

- A platform for deploying machine learning workflows on Kubernetes.
- Simplifies the process of building, training, and serving machine learning models.
- Provides a complete machine learning stack.
- Leverages Kubernetes for deployment, scaling, and portability.

**Key Features:**

- **Machine Learning Pipelines:** Defines and executes machine learning workflows.
- **TensorFlow Integration:** Seamlessly integrates with TensorFlow for model training and serving.
- **Distributed Training:** Scales machine learning models across multiple nodes.
- **Model Serving:** Deploys trained models as REST APIs or gRPC services.
- **Experiment Tracking:** Tracks and compares different machine learning experiments.

**Benefits of Using Kubeflow:**

- **Simplified Deployment:** Manages the complexity of deploying machine learning pipelines.
- **Scalability:** Automatically scales resources based on workload.
- **Portability:** Deploys machine learning models on any Kubernetes cluster.
- **Integration:** Provides a comprehensive set of tools and integrations.

Kubeflow is a valuable tool for data scientists and machine learning engineers who want to leverage Kubernetes to build and deploy scalable machine learning applications.

</details>

<details>
<summary><b>Knative:</b> A Platform for Serverless Workloads</summary>

**What is Knative?**

* A platform for building, deploying, and managing serverless workloads on Kubernetes.
* Provides a consistent and portable way to run serverless applications.
* Can be deployed anywhere with Kubernetes, avoiding vendor lock-in.
* Supported by Google, IBM, and SAP.

**Key Features:**

* **Serverless Functions:** Create and deploy event-driven functions without managing infrastructure.
* **Custom Runtimes:** Use your preferred programming language or framework.
* **Horizontal Autoscaling:** Automatically scales resources based on demand.
* **Service Binding:** Connect services to event sources and triggers.

**Benefits of Using Knative:**

* **Simplified Development:** Focus on writing code without worrying about infrastructure.
* **Scalability:** Automatically scales to handle varying workloads.
* **Portability:** Deploy applications on any Kubernetes environment.
* **Community Support:** Backed by a strong community and industry leaders.

Knative is a powerful tool for building and deploying serverless applications on Kubernetes. It provides a flexible and scalable platform for modern application development.

</details>