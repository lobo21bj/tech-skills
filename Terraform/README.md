# Terraform - Associate Exam Prep

## IaC Concepts

### Infrastructure as Code (IaC)

You write a configuration script to automate *creating, updating or destroying* cloud infrastructure.

- IaC is a blueprint of your infrastructure.
- IaC allows you to easily *share, version or inventory* your cloud infrastructure.

### Popular IaC tools

[![image.png](https://i.postimg.cc/2jHwZfS2/image.png)](https://postimg.cc/0rwmTFmw)

#### Declarative

- What you see is what you get. *Explicit*
- More verbose, but zero chance of mis-configuration.
- Uses scriptting language eg. JSON, YAML, XML.

ARM Templates → Azure
Azure Blueprints → Azure, manages relationship between services.
CloudFormation → AWS
Cloud Deployment Manager → Google Cloud
*Terraform* → Spports many cloud service providers (CSPs) and cloud services.

#### Imperative

- You say what you want, and the rest is filled in. *Implicit*
- Less verbose, you could end up with misconfiguration.
- Does more than declarative.
- Uses programming languages eg. Python, Ruby, JavaScripts.

AWS Cloud Development Kit (CDK) → AWS
Pulumi → AWS, Azure, GCP, K8

---

Terraform is declarative but the Terraform language features imperative-like functionality.

HCL-ish (Terraform Language) supports:

- Loops (For Each)
- Dynamic Blocks
- Locals
- Complex Data Structure
  - Maps, Collections

### Infrastructure Lifecycle

**What is infrastructure lifecycle?**
A number of clearly defined and distinct work phases which are used by DevOps Engineers to *plan, design, build, test, deliver, maintain and retire* cloud infrastructure.

Day 0 → Plan and Design
Day 1 → Develop and Iterate
Day 2 → Go live and maintain

#### Benefits of the IaC

- **Reliability**: IaC makes changes idempotent, consistent, repeatable and predictable.

> [!NOTE]
> **Idempotent**
> No matter how many times you run IaC, you will always end up with the same state that is expected.

- **Manageability**: Enable mutation via code. Revised, with minimal changes.

- **Sensibility**: Avoid financial and reputational losses to even loss of life when considering government and military dependencies on infrastructure.

#### Non-Idempontent vs Idempontent

[![idempontent.png](https://i.postimg.cc/L84WQHy9/idempontent.png)](https://postimg.cc/CztJzVTX)

#### Provisioning vs Deployment vs Orchestration

##### Provisioning

To prepare a server with systems, data and software, and make it ready for network operation. Using Configuration Management tools like Puppet, Ansible, Chef, Bash scripts, PowerShell or Cloud-Init you can provision a server.
**When you launch a cloud service and configure it you are "provisioning"**

##### Deployment

Deployment is the act of delivering a version of your application to run a provisioned server.
Deployment could be performed via AWS CodePipeline, Harness, Jenkins, Github Actions, CircleCl.

##### Orchestration

Orchestration is the act of coordinating multiple systems or services. Is a common term when working with microservices, Containers and Kubernetes. Orchestration could be Kubernetes, Salt, Fabric.

---

#### Configuration Drift

Configuration Drift is when provisioned infrastrcture has an unexpected configuration change due to:

- team members manually adjusting configuration options.
- malicious actors.
- side affects from APIs, SDK or CLIs.

[![configdrift.png](https://i.postimg.cc/76QPhsfV/configdrift.png)](https://postimg.cc/VrnPHF9r)

##### How to detect configuration drift?

- A compliance tool that can detect misconfiguration eg. AWS Config, Azure Policies, GCP Security Health Analytics.
- Built-in support for drift detection eg. AWS CloudFormation Drift Detection.
- Storing the expected state eg. Terraform state files.

##### How to correct configuration drift?

- A compliance tool that can remediate misconfiguration eg. AWS Config.
- Terragorm refresh and plan commands.
- Manually correcting the configuration (not recommended).
- Tearing down and setting up the infrastructure again.

##### How to prevent configuration drift?

- **Immutable infrastructure**, always create and destroy, never reuse, Blue-Green deployment strategy.
  - Servers are never modified after they are deployed.
    - Baking AMI images or containers via AWS Image Builder or HashiCorp Packer, or a build server eg. GCP Cloud Run.
- Using GitOps to version control our IaC, and peer review every single via Pull Requests change to infrastructure.
&nbsp;

**Mutable Infrastructure**: A Virtual Machine is deployed and then configured via Ansible, Puppet or CLoud Init.
*Develop → Deploy → Configure*
&nbsp;

**Immutable infrastructure**: A Virtual Machine is lanched and provisioned, then it's turned into a Virtual Image, stored in an image repo, and that image is used to deploy VM instances.
*Develop → Configure → Deploy*

&nbsp;

---

#### What is GitOps?

**GitOps** is when you take infrastructure as Code (IaC) and you use a git repository to introduce a formal process to review and accept changes to infrastructure code, once that code is accepted, it automatically triggers a deploy.

[![gitops.png](https://i.postimg.cc/cJ0fBHTR/gitops.png)](https://postimg.cc/0zX689Tj)

&nbsp;

---

### What is Terraform?

Terraform is an open-source and cloud-agnostic IaC tool.
Terraform uses *declarative* configuration files.
The configuration files are writtend in HashiCorp Configuration Language (*HCL*).

```hcl
resource "aws_instance" "iac_in_action" {
    ami                 = var.ami_id
    instance_type       = var.instance_type
    availability_zone   = var.availability_zone

    //dynamically retrieve SSH Key Name
    key_name = aws_key_pair.iac_in_action.key_name

    //dynamically set Security Group ID (firewal)
    vpc_security_group_ids = [aws_security_group.iac_in_action.id]

    tags ={
        Name = "Terraform-managed EC2 Instance for IaC in Action"
    }
}

resource "aws_s3_bucket" "finance" {
    bucket  = "finance-21092020"
    tags    = {
        Description = "Finance and Payroll"
    }   
}

resource "aws_iam_user" "admin-user" {
    name = "lucy"
    tags = {
        Description= "Team Leader"
    }
}
```

#### Features of Terraform

- Installable modules.
- Plan and predict changes.
- Dependency graphing.
- State management.
- Provision infrastructure in familiar languages (via AWS CDK).
- Terraform Registry (+1000 providers).

#### What is Terraform Cloud?

Terraform Cloud is a Software as a Service (SaaS) offering for:

- Remote state stroge.
- Version control integrations.
- Flexible workflows.
- Collaborate on infrastructure changes in a single unified web portal [TerraformCloud](https://www.terraform.io/cloud).

&nbsp;

---

## Terraform Basics

### Terraform Lifecycle

[![terraformlifecycle.png](https://i.postimg.cc/1X7gxGk2/terraformlifecycle.png)](https://postimg.cc/ctY1wn4B)

### Change Automation

**What is change management?**: A standard approach to apply change, and resolving conflicts brought about by change. In the context of IaC, Change Management is the procedure that will be followed when resources are modify and applied via configuration script.

**What is a Change Automation?**: A way of automatically creating a consistent, systematic and predictable way of managing change request via controls and policies.

Terraform uses Change Automation in the form of *Executions Plans* and *Resources Graphs* to apply and review complex **changesets**

> [!NOTE]
> ChangeSet is a collection of commits that represent changes made to a versioning repository.

&nbsp;

#### Execution Plans

An **Execution Plan** is a **manual review** of what will add, change or destroy before you apply changes eg. terraform apply.

[![executionplan.png](https://i.postimg.cc/FsfbrzTM/executionplan.png)](https://postimg.cc/56VQp4dg)

### Terraform Parts

**Terraform Core**
Uses remote procedure calls (RPC) to communicate with Terraform Plugins.

**Terraform Plugins**
Expose an implementation for a specific service or provisioner.

[![tfparts.png](https://i.postimg.cc/C5rWj58Q/tfparts.png)](https://postimg.cc/sGS6zVwY)

&nbsp;

---

### Terraform Best Practices

[TF Best practices](https://www.terraform-best-practices.com/)

---

## Terraform Provisioners

Terraform Provisioners intall software, edit files, and provision machines created with Terraform.

### Cloud-Init

- Cloud-init: Is an industry standard for cross-platform cloud instance initializations. When you launch a VM on a Cloud Service Provider (CSP) you'll provide a YAML or Bash script in a user data window.

- Packer is an automated image-builder service. You provide a configuration file to create and provision the machine image and the image is the delivered to a repo for use.

> [!CAUTION]
> Provisioners should only be used as a last resort. For most common situations are better alternatives. As they could do something what won´t be reflected in the terraform state. Better use cloud-init.

Create your own Cloud-Init script

```yaml
users:
  - default
  - name: terraform
    gecos: terraform
    primary_group: hashicorp
    groups: users, admin
    ssh_import_id:
    lock_passwd: false
    ssh_authorized_keys:
      - # Paste your created SSH key here
package_upgrade: yes
package_update: yes
packages:
  - httpd
runcmd:
  - sudo service httpd start
  - sudo service httpd enable
```

Define the template

```hcl
data "template_file" "user_data" {
    template = file("../scripts/add-ssh-web-app.yaml")
}

resource "aws_instance "web" {
    ami                         = data.aws_ami.ubuntu.id
    instance_type               = "t2.micro"
    subnet_id                   = aws_subnet.subnet_public.id
    vpc_security_group_ids      = true
    user_data                   = data.template_file.user_data.rendered

    tags = {
        Name = "Learn-CloudInit"
    }
}
```

Reference it in the userdata for the VM.

---

### Local-exec

**Local-exec** allows you to execute local commands after a resource is provisioned.
The machine that is executing Terraform eg. terraform apply is where the command will execute.

Examples:

```hcl
resource "aws_instance" "web" {
    #...

    provisioner "local-exec" {
        command = "echo ${self.private_ip} >> private_ips.txt"
    }
}
```

```hcl
resource "null_resource" "example2" {
    provisioner "local-exec" {
        command = "Get-Date > completed.txt"
        interpreter = ["PowerShell", "-Command"]
    }
}
```

```hcl
resource "aws_instance" "web" {
    #...

    provisioner "local-exec" {
        command = "echo $KEY $SECRET >> credentials.yml"

        environment = {
            KEY = "JLmdsaasd65325dasd"
            SECRET = "dasfasGDFG432654"
        }
    }
}
```

---

### Remote-exec

**Remote-exec** allows you to execute commands on a target resource after a resource is provisioned.

Examples:

```hcl
resource "aws_instance" "web" {
    #...

    provisioner "remote-exec" {
        inline = [
            "puppet apply",
            "consul join ${aws_instance.web.private_ip}",
        ]
    }
}
```

```hcl
resource "aws_instance" "web" {
    #...

    provisioner "remote-exec" {
        scripts = [
            "./setup-users.sh",
            "/home/andrew/Desktop/bootstrap"
        ]
    }
}
```

---

### File

**file provisioner** is used to copy files or directories from our local machine to the newly created resource.

Examples:

```hcl
resource "aws_instance" "web" {
    #...

    # Copies the myapp.conf file to /etc/myapp.conf
    provisioner "file" {
        source      = "conf/myapp.conf"
        destination = "/etc/myapp.conf"
    }

    # Copies the string in content into /tmp/file.log
    provisioner "file" {
        content     =ami used: ${self.ami}"
        destination = "/tmp/file.log"
    }

    # Copies the configs.d folder to /etc/configs.d
    provisioner "file" {
        source      = "conf/configs.d"
        destination = "/etc"
    }

    # Copies all files and folders in apps/appl to D:/IIS/webappl
    provisioner "file" {
        source      = "apps/appl/"
        destination = "D:/IIS/webappl"
    }
}
```

---

### Connection

A connection block tells a provisioner or resource how to establish a connection.

Example:

```hcl
# Copies all the files as root using SSH - linux
 provisioner "file" {
    source      = "conf/myapp.conf"
    destination = "/etc/myapp.conf"

    connection {
        type        = "ssh"
        user        = "root"
        password    = "${var.root_password}"
        host        = "${var.host}"
    }
}

# Copies all the files as Administrator using winrm - Windows
 provisioner "file" {
    source      = "conf/myapp.conf"
    destination = "C:/App/myapp.conf"

    connection {
        type        = "winrm"
        user        = "Administrator"
        password    = "${var.admin_password}"
        host        = "${var.host}"
    }
}
```

---

### Null Resources

**null_resource** is a placeholder for resources that have no specific association to a provider resources.

Examples:

```hcl
resource "aws_instance" "cluster" {
    count = 3

    #...
}

resource "null_resource" "cluster" {
    # Changes to any instance of the cluster requires re-provisioning
    triggers = {
        cluster_instance_ids = "${join(",", aws_instance.cluster.*.id)}"
    }

    # Bootstrap script can run on any instance of the cluster
    # so we just choose the first in this case
    connection {
        host = "${element(aws_instance.cluster.*.public_ip, 0)}"
    }

    provisioner "remote-exec" {
        # Bootstrap script called with private_ip of each node in the cluster
        inline = [
            "bootstrap-cluster.sh ${join(" ", aws_instance.cluster.*.private_ip)}",
        ]
    }
}
```

**Triggers** is a map of values which should cause above set of provisioners to rerun.

---

### Terraform Data

Similar to null_resources but does not require or the configuration of a provider.

example:
[![tfdata-nullrsrc.png](https://i.postimg.cc/zvYjXqmT/tfdata-nullrsrc.png)](https://postimg.cc/wyFJw8jB)

&nbsp;

---

## Terraform Providers

Providers are Terraform Plugins that allow you to interactive with:

- Cloud Service Providers (CSPs): AWS, Azure, GCP.
- Software as a Service (SaaS) Providers eg. Github, Angolia, Stripe.
- Other APIs eg. Kubernetes, Postgres

Providers are required for your Terraform Configuration file to work.

Providers come in three tiers:

- Official
- Verified
- Community

**terraform init** will download the necessary provider plugins listed in a Terraform configuration file.

### Terraform Registry

Terraform registry is a website portal to browse, download or publish available Providers or Modules.

### Terraform Cloud - Private Registry

**Terraform Cloud** allows you to publish private modules for your organization within the Terraform Cloud Private Registry.

When creating a module you need to connect to a Version Control System (VCS) and choose a repository. (GitHub).

### Terraform Providers Command

*terraform providers* will list the providers used.

### Terraform Provider Configuration

Set an alternative provider

```hcl
provider "aws" {
    alias   = "west"
    region  = "us-west-2"
}
```

How to reference an alias provider

```hcl
provider "aws_instance" "foo" {
    provider = aws.west
    #...
}
```

How to set alias provider for a parent module

```hcl
terraform {
    required_providers {
        mycloud = {
            source  = "mycorp/mycloud"
            version = "~> 1.0"
            configuration_aliases = { mycloud.alternate }
        }
    }
}
```

How to set alias provider for a child module

```hcl
module "aws_vpc" {
    source      = "./aws_vpc"
    providers   = {
        aws = aws.west
    }
}
```

&nbsp;

---

## Terraform Modules

A module is a group of configuration files that provide common configuration functionality.

- Enforces best practices
- Reduce the amount of code
- Reduce time to develop scripts

Example:
**AWS VPC Module**: Using a module you can use a shorthand Domain Specific Language (DSL) that will reduce the amount of work.

```hcl
module "vpc" {
    source = "terraform-aws-modules/vpc/aws"

    name = "my-vpc"
    cidr = "10.0.0.0/16"

    azs             = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
    private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
    public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

    enable_nat_gateway = true
    enable_vpn_gateway = true

    tags = {
        Terraform = "true"
        Environment = "dev"
    }
}
```

[![image.png](https://i.postimg.cc/sDm0gGnf/image.png)](https://postimg.cc/XpZg2qSt)

---

## Terraform Files

Terraform files contain the configuration information about providers and resources.
Terraform files end in the extension of **.tf** or either **.tf.json** and are written in *Terraform Language*-

**Terraform Language** consists of only a few basic elements:

- Blocks: containers for other content, represent an object
  - block type: can have zero or more labels and a body
  - block label: name of a block
- Arguments: assign a value to a name
  - They appear within blocks
- Expressions: represent a value, either literally or by referencing and combinig other values.
  - The appear as values for arguments, or within other expressions.

```hcl
resource "aws_vpc" "main" {
    cidr_block = var.base_cidr_block
}

<BLOCK_TYPE> "<BLOCK_LABEL>" "<BLOCK_LABEL>" {
    # block body
    <IDENTIFIER> = <EXPRESSION> #Argument
}
```

[![image.png](https://i.postimg.cc/y65LGHCY/image.png)](https://postimg.cc/6TrV7FQD)

&nbsp;

Terraform also supports JSON which is useful when generating portions of a configuration programmatically. Files to be named as **.tf.json**

```json
{
    "resource": {
        "aws_instance": {
            "example": {
                "instance_type": "t2.micro",
                "ami": "ami-abc123"
            }
        }
    }
}
```

&nbsp;

### Files Convention

Filename        | Purpose
------------    | -------------
main.tf         | Main configuration file containing resource definition
variables.tf    | Contains variable declarations
outputs.tf      | Contains outputs from resources
provider.tf     | Contains Provider definitions

&nbsp;

---

## Terraform Settings

The special terraform configuration block type is used to configure some behaviors or Terraform itself.

We can specify:

- **required_version**: The expected version of Terraform.
- **required_providers**: The providers that will be pull during an terraform init.
- **experiments**: Experimental language features, that the community can try and provide feedback.
- **provider_meta**: Module-specific information for providers.

---

## Terraform Stages

[![image.png](https://i.postimg.cc/HsXF4x8G/image.png)](https://postimg.cc/HVWSTTt3)

### terraform init

[![image.png](https://i.postimg.cc/zvnpWyt6/image.png)](https://postimg.cc/2LS4NSf7)

### terraform plan

[![image.png](https://i.postimg.cc/QxQnKyv3/image.png)](https://postimg.cc/kB5ykfn1)

### terraform apply

[![image.png](https://i.postimg.cc/rsWZJnm3/image.png)](https://postimg.cc/tnqzRzFN)

### terraform show

[![image.png](https://i.postimg.cc/m2y8gFFV/image.png)](https://postimg.cc/F71jPzpJ)

**.tfstate** file is a blueprint of the existing infrastructure.

&nbsp;

---

## Terraform Variables

Can be exported in **variables.tf** file.

```hcl
variable "filename"{
    default = "/root/pets.txt"
    type = string
    description = "the path of local file"
}
variable "content" {
    default = "I love pets!"
    type = string
    descripttion "the content of the file"
}
variable "password_change" {
    default = true
    type = bool # Optional as it is true
}
```

Variable can be called from **main.tf** as below:

```hcl
resource "local_file" "pet" {
    filename = var.filename
    content = var.content
}
```

Also can be a list / map

```hcl
variable file-content {
    type    = map
    default = {
        "statement1" = "We love pets!"
        "statement2" = "We lovel animals!"
    }
}
```

can be called in main.tf as:

```hcl
resource "local_file" "my-pet" {
    filename = "/root/pets.txt"
    content = var.file-content["statement2"]
}
```

Another example

```hcl
variable "prefix" {
    default = ["Mr", "Mrs", "Sir"]
    type = list(string)
}
```

More:

```hcl
variable "cats" {
    default = {
        "color" = "brown"
        "name" = "bella"
    }
    type = map(string)
}

variable "pet_count" {
    default = {
        "dogs" = 3
        "cats" = 1
        "goldfish" = 2
    }
    type = map(number)
}
```

Example for an object:

```hcl
variable "bella" {
    type = object({
        name = string
        color = string
        age = number
        food = list(string)
        favorite_pet = bool
    })
    
    default = {
        name = "bella"
        collor = "brown"
        age = 7
        food = ["fish", "chicken", "turkey"]
        favorite_pet = true
    }
}
```

### Environmental Variables

Examples:

```shell
export TF_VAR_filename="/root/pets.txt"
export TF_VAR_content="We love pets!"
export TF_VAR_prefix="Mrs"
terraform apply
```

or create a separate file terraform.tfvars

```hcl
filename = "/root/pets.txt"
content = "We love pets!"
prefix = "Mrs"
```

```shell
terraform apply
```

> [!IMPORTANT]
> variables declared in **.auto.tfvars** will be automatically lodaded.

---

### Variable Definition Precedence

| Prioridad | Fuente | Ejemplo |
| ---: | --- | --- |
| **1** | `-var` | `terraform plan -var="env=prod"` |
| **2** | `-var-file` | `terraform plan -var-file="prod.tfvars"` |
| **3** | `*.auto.tfvars` | `prod.auto.tfvars` |
| **4** | `terraform.tfvars` | `terraform.tfvars` |
| **5** | Variables de entorno `TF_VAR_*` | `TF_VAR_env=prod` |
| **6** | `default` de la variable | `default = "dev"` |

&nbsp;

---

### Output Variables

Example:

```hcl
resource "local_file" "pet" {
    filename = var.filename
    content = "My favorite pet is ${random_pet.my-pet.id}"
}

resource "random_pet" "my-pet" {
    prefix = var.prefix
    separator = var.separator
    length = var.length
}

output "pet-name" {
    value           = random_pet.my-pet.id
    description     = "Record the value of pet ID generated by the random_pet resource"
}
```

Use below command to show the output variables

```shell
terraform output <output_variable>
```

&nbsp;

---

## Terraform State

After *terraform apply* is triggered a file terraform.tfstate gets created. Is a JSON file that maps real world resources with the resource definition in the config files.

If *terraform apply* is executed and there are no changes in the config. Nothing will do. Otherwise will destroy the existing resource ID and create the changed resource with a new ID.

[![image.png](https://i.postimg.cc/HLyxDDQz/image.png)](https://postimg.cc/SXmqCP1Y)

&nbsp;

### Purpose of State

- **Tracking metadata**: When you have resources dependent on others and you want to know which should get destroyed first.

```hcl
resource "local_file" "pet" {
    filename = "/root/pet.txt"
    content = "My favorite pet is ${random_pet.my-pet.id}!"
}

resource "random_pet" "my-pet" {
    length = 1
}

resource "local_file" "cat" {
    filename = "/root/cat.txt"
    content = "I like cats too!"
}
```

[![image.png](https://i.postimg.cc/DyR3VWBT/image.png)](https://postimg.cc/1f0jw3kC)

Now if pet files gets removed from config

[![image.png](https://i.postimg.cc/m2H6HmNv/image.png)](https://postimg.cc/6yB0sLPc)

The local_file pet will be destroyed first followed by the random_file.

[![image.png](https://i.postimg.cc/NjYqfhqy/image.png)](https://postimg.cc/2VHX2K5m)

&nbsp;

- **Performance**: Terraform reconciles state using the tfstate file as record of truth. It stores a cached attributes for all the resources in the state. Does not check the actual state of the resources and does not refresh the state of them.

&nbsp;

- **Collaboration**: tfstate file can be stored in a remote server using: AWS S3, Google Cloud Storage, HashiCorp Consul or Terraform Cloud.

&nbsp;

### Terraform State Considerations

- It's not recommended to save them in version control repos as GitHub. As they contain sensitive information better store them in AWS S3 or Terraform Cloud.

- Never modify it manually!

&nbsp;

---

## Working with Terraform

### Terraform Commands

- **terraform validate**: Help you to check the syntax fo files without running terraform plan.

- **terraform fmt**: Formats your file in a cannnical format. The output are the files that were updated. (indentation).

- **terraform show**: Displays the terraform current state.

- **terraform providers**: Lists the used providers. If you add mirror commands you can save it in a different file.

- **terraform output**: Gives you the list of variables with their values.

- **terraform refresh**: terraform apply -refresh-only is like a sync command which updates state file only.

- **terraform graph**: Generates a graphic representation of the resources. To be used with graphviz pkg. *terraform grap | dot -Tsvg > graph.svg*

&nbsp;

---

### Mutable vs Immutable infrastructure

**IMMUTABLE**
Resources are not getting updated, instead, destroy the old and creates a new resource with the updated config.

---

### Lifecycle rules

Whether you want to create the new resource or destroy the old first.
Cam ne configured in the main.tf file as below:

```hcl
resource "local_file" "pet" {
    filename = "/root/pets.txt"
    content = "We love pets!"
    file_permission = "0700"

    lifecycle {
        create_before_destroy = true
    }
}
```

Another flag is **prevent_destroy** if you want to hold any destruction action.

> ![CAUTION]
> If you use terraform destroy resource can be destroyed still.

**ignore_changes** flag to ignore atrributes and don´t generate new resources if these are modified. Example:

```hcl
resource "aws_instance" "webserver" {
    ami             = "ami-0addee64275fa214"
    instance_type   = "t2.micro"
    tags = {
        Name = "ProjectA-Webserver"
    }
    
    lifecycle {
        ignore_changes = all
    }

    # OR
    lifecycle {
        ignore_changes = [
            Name, ami
        ]
    }
}
```

---

### Datasources

By adding the data block in the configuration files. You can add them in the tfstate file. Example:

```hcl
resource "local_file" "pet" {
    filename = "/root/pets.txt"
    content = "We love pets!"
}

data "local_file" "dog" {
    filename = "/root/dog.txt"
}
```

Another example:

```hcl
output "os-version" {
  value = data.local_file.os.content
}
data "local_file" "os" {
  filename = "/etc/os-release"
}
```

&nbsp;

---

### Meta-Arguments

Such as depends_on or lifecycle.

- **count**: If you want to create multiple resources: Example:

main.tf

```hcl
resource "local_file" "pet" {
    filename = var.filename[count.index]

    count = length(var.filename) # or count = 3
}
```

variables.tf

```hcl
variable "filename" {
    default = [
        "/root/pets.txt",
        "/root/dogs.txt",
        "/root/cats.txt",
        "/root/cows.txt",
        "/root/ducks.txt"
    ]
}
```

&nbsp;

- **for_each**: Only works for a map or a set value. Example:

main.tf

```hcl
resource "local_file" "pet" {
    filename = each.value
    for_each = toset(var.filename)
}

output "pets" {
    value = local_file.pet
}
```

variables.tf

```hcl
type = list(string) # or type = set(string)
variable "filename" {
    default = [
        "/root/pets.txt",
        "/root/dogs.txt",
        "/root/cats.txt",
        "/root/cows.txt",
        "/root/ducks.txt"
    ]
}
```

count creates the output as a list but for_each as a map

[![image.png](https://i.postimg.cc/G29Nn211/image.png)](https://postimg.cc/YGK81t9X)

&nbsp;

---

### Version Constraints

```hcl
terraform {
    required_providers {
        local = {
            source = "hashicorp/local"
            varsion = "~> 1.2.0"
        }
    }
}

resource "local_file" "pet" {
    filename = each.value
    for_each = toset(var.filename)
}

```

&nbsp;

---

## Terraform with AWS

[AWS Management Console](https://aws.amazon.com/console)

### Introduction to IAM

**Requirements**:

- Access key ID
- Secret Access Key

**IAM Policy**: Gives access to user, is created in JSON format as below for AdministratorAccess.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

**IAM Group**: Collection of users, permissions can be assigned to a group or specific user.

**Roles**: Is to give permissions to another service / AWS accoount. You can attach policies into them.

&nbsp;

### Programmatic Access

In AWS CLI *aws configure* to fill:

**AWS Access Key ID**: AKAI44EXAMPLE
**AWS Secret Access Key**: jdasdjasdhasjkasbdj
**Default Region**: us-east-2
**Default output format**: json

They will be stored in hidden files:

.aws/config/config
.aws/config/credentials

```aws
aws iam create-user --user-name lucy
```

```aws
aws --endpoint http://aws:4566 iam attach-user-policy --user-name mary --policy-arn arn:aws:iam::aws:po
licy/AdministratorAccess
```

```aws
aws --endpoint http://aws:4566 iam attach-group-policy --group-name project-sapphire-developers --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess
```

&nbsp;

### AWS IAM with Terraform

main.tf

```hcl
provider "aws" {
    region = "us-west-2"
    access_key = "ASDADSADAS"
    secret_key = "sdasd821das"
}

resource "aws_iam_user" "admin-user" {
    name = "lucy"
    tags = {
        Description = "Technical Team Leader"
    }
}
```

Check .aws/credentials and .aws/config and export as env variables

```shell
export AWS_ACCESS_KEY_ID=ASDADSADAS
export AWS_SECRET_ACCESS_KEY_ID=sdasd821das
export AWS_REGION=us-west-2
```

and remove the aws provider section from main.tf

```hcl
resource "aws_iam_user" "admin-user" {
    name = "lucy"
    tags = {
        Description = "Technical Team Leader"
    }
}

resource "aws_iam_plicy" "adminUser" { # option 1
    name = "AdminUsers"
    policy = <<EOF
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
    }
    EOF
}

resource "aws_iam_plicy" "adminUser" { # option 2
    name = "AdminUsers"
    policy = file("admin-policy.json")
}

resource "aws_iam_user_policy_attachment "lucy-admin-access" {
    user = aws_iam_user.admin-user.name
    plicy_arn = aws_iam_policy.adminUser.arn
}
```

&nbsp;

---

### AWS S3 (Simple Storage Service)

Requires:

- Unique Bucket Name (DNS Compliant Name)
- Files size between 0 to 5 TB.
- Example: "<https://all-pets.us-west-1.amazonaws.com>"
- Bucket policy (By default owner only can access it)

[![image.png](https://i.postimg.cc/yxxdKvJp/image.png)](https://postimg.cc/1VxPc0rD)

[![image.png](https://i.postimg.cc/ZnXTSZzg/image.png)](https://postimg.cc/Wq6RGB36)

&nbsp;

### AWS S3 with Terraform

```hcl
resource "aws_s3_bucket" "finance" {
    bucket = "finance-21092020"
    tags = {
        Description = "Finance and Payroll"
    }
}

resource "aws_s3_bucket_object" "finance-2020" {
    content    = "/root/finance/finance-2020.doc"
    key        " "finance-2020.doc"
    bucket     = aws_s3_bucket.finance.id
}

data "aws_iam_group" "finance-data" {
    group_name = "finance-analysts"
}

resource "aws_s3_bucket_policy" "finance-policy" {
    bucket = aws_s3_bucket.finance.id
    policy = <<EOF
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "*",
                "Effect": "Allow",
                "Resource": "arn:aws:s3:::${aws_s3_bucket.finance.id}/*",
                "Principal": {
                    "AWS": [
                        "${data.aws_iam_group.finance-data.arn}"
                    ]
                }
            }
        ]
    }
    EOF
}
```

[![image.png](https://i.postimg.cc/y8pz4shx/image.png)](https://postimg.cc/Xr5P9Mz6)

Another example

```hcl
resource "aws_iam_user" "cloud" {
     name = split(":",var.cloud_users)[count.index]
     count = length(split(":",var.cloud_users))
  
}
resource "aws_s3_bucket" "sonic_media" {
     bucket = var.bucket
  
}
resource "aws_s3_bucket_object" "upload_sonic_media" {
     key = substr(each.value, 7, -1)
     source = each.value
     for_each = var.media
     bucket = aws_s3_bucket.sonic_media.id
}
```

&nbsp;

---

### AWS Dynamo DB

main.tf

```hcl
resource "aws_dynamodb_table" "cars" {
    name        = "cars"
    hash_key    = "VIN" # Primary Key
    billing_mode = "PAY_PER_REQUEST"  # PROVISIONED by default
    attribute {
        name = "VIN"
        type = "S"
    }
}

resource "aws_dynamodb_table_item" "car-items" {
    table_name = awsdynamodb_table.cars.name
    hash_key   = awsdynamodb_table.cars.hash_key
    item       = <<EOF
    {
        "Manufacturer: {"S": "Toyota"},
        "Make": {"S": "Corolla"},
        "Year": {"N": "2004"},
        "VIN": {"S": "4Y1SL65848Z411439"},
    }
    EOF
}
```

&nbsp;

---

## Remote State

Only one member should operate based on the config used.

[![image.png](https://i.postimg.cc/BQMcSqS6/image.png)](https://postimg.cc/Vd0b4PbQ)

[![image.png](https://i.postimg.cc/MpnRzV37/image.png)](https://postimg.cc/HrCj2cgn)

### Best practice

[![image.png](https://i.postimg.cc/PxQvS4NP/image.png)](https://postimg.cc/TLhPwnV6)

To implment it we should code the main.tf as below:

main.tf

```hcl
resource "local_file" "pet" {
    filename = each.value
    for_each = toset(var.filename)
}

```

terraform.tf

```hcl
terraform {
    backend "s3" {
        bucket          = "kodekloud-terraform-state-bucket01"
        key             = "finance/terraform.tfstate"
        region          = "us-west-1"
        dynamodb_table  = "state-locking"
    }
}
```

> [!CUATION]
> terraform init is required to set this up. And delete the local tfstate file. It will we saved in memory from backend storage.

&nbsp;

---

## Terraform State Commnads

```shell
terraform state <subcommand> aws_s3_bucket.finance
```

Whereas subcommand could be: list, mv, pull, rm, show

Example of pull remote state lockign.

```shell
terraform state pull | jq '.resources[] | select (.name == "state-locking-db")|.instances [].attributes.hash_key
```

*"LockID"*:

With terraform rm resource will be removed from management but not from real world.

&nbsp;

---

## AWS EC2 with Terraform

main.tf

```hcl
resource "aws_instance" "webserver" {
    ami             = "ami-0eaeaav214587"
    instance_type   = "t2.micro"
    tags = {
        Name        = "webserver"
        Description = "An Ngnix WebServer on Ubuntu"
    }
    user_data = <<-EOF
        #!/bin/bash
        sudo apt update
        sudo apt install nginx -y
        systemctl enable nginx
        systemctl start ngix
        EOF
    
    key_name = aws_key_pair.web.id
    vpc_security_group_ids = [ aws_security_group.ssh-access.id ]
}

resource "aws_key_pair" "web" {
    public_key = file ("/root/.ssh/web.pub")
}

resource "aws_security_group" "ssh-access" {
    name        = "ssh-access"
    description = "Allow SSH access from Internet"
    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

output publicip {
    value   = aws_instance.webserver.public_ip
}
```

provider.tf

```hcl
provider "aws" {
    region = "us-east-1"
}
```

&nbsp;

---

## Terraform Provisioners 2

**remote-exec**:

```hcl
resource "aws_instance" "webserver" {
    ami             = "ami-0eaeaav214587"
    instance_type   = "t2.micro"
    tags = {
        Name        = "webserver"
        Description = "An Ngnix WebServer on Ubuntu"
    }
    provisioner "remote-exec" {
        inline = [  "sudo apt update",
                    "sudo apt install nginx -y",
                    "systemctl enable nginx",
                    "systemctl start ngix",
                 ]
    }      
    
    key_name = aws_key_pair.web.id
    vpc_security_group_ids = [ aws_security_group.ssh-access.id ]
}
```

&nbsp;

***local-exec** (Creation time provisioner):

```hcl
resource "aws_instance" "webserver" {
    ami             = "ami-0eaeaav214587"
    instance_type   = "t2.micro"


    provisioner "local-exec" {
        command = "echo ${aws_instance.webserver.public_ip} >> /tmp/ips.txt"
    }
}
```

&nbsp;

**Destroy time provisioner**:

```hcl
resource "aws_instance" "webserver" {
    ami             = "ami-0eaeaav214587"
    instance_type   = "t2.micro"


    provisioner "local-exec" {
        command = "echo ${aws_instance.webserver.public_ip} >> /tmp/ips.txt"
    }

    provisioner "local-exec" {
        when    = destroy
        command = "echo ${aws_instance.webserver.public_ip} Destroyed! > /tmp/instance_state.txt"
    }
}
```

**Failure behavior**:

```hcl
resource "aws_instance" "webserver" {
    ami             = "ami-0eaeaav214587"
    instance_type   = "t2.micro"


    provisioner "local-exec" {
        on_failure = continue
        command = "echo ${aws_instance.webserver.public_ip} > /temp/ips.txt"
    }

    provisioner "local-exec" {
        when    = destroy
        command = "echo ${aws_instance.webserver.public_ip} Destroyed! > /tmp/instance_state.txt"
    }
}
```

&nbsp;

---

## Terraform Taint

When the resource creation fails, terraform marks it as **tainted**.
It will try to recreate it every time an apply is ran.

```shell
terraform taint aws_instance.web_server
```

To mark it for recreation.

```shell
terraform untaint aws_instance.web_server
```

&nbsp;

---

## Terraform Debugging

```shell
export TF_LOG=<log_level>
export TF_LOG_PATH=/tmp/terraform.log
```

Log levels:

- INFO
- WARNING
- ERROR
- DEBUG
- TRACE

```shell
unset TF_LOG_PATH
```

&nbsp;

---

## Terraform Import

**Data Source**:

```hcl
data "aws_instance" "newserver" {
    instance_id = "i-021s5daer1er5e640"
}

output nweserver {
    value   = data.aws_instance.newserver.public_ip
}
```

Retrieve data from a resource not created by terraform.

**Import**: Only updates the tfstate.

```shell
# terraform import <resource_type>.<resource_name> <attribute>
terraform import aws_instance.webserver-2 i-021s5daer1er5e640
```

So we need to update the config with the resource trying to be imported.

```hcl
resource "aws_instance" "newserver-2" {
    # (resource arguments)
}
```

Now the import will succeed.

To retrieve details from aws ec2 instance:

```shell
terraform show -json | jq '.values.root_module.resources[] | select(.type == "aws_instance" and .name == "jade-mw")'
```

&nbsp;

---

## Terraform modules 2

How to import a module

[![image.png](https://i.postimg.cc/2SHJzHnf/image.png)](https://postimg.cc/dhyn6jWW)

Create our own module

```shell
mkdir /root/terraform-projects/modules/payroll-app
#app_server.tf dynamodb_table.tf s3_bucket.tf variables.tf
```

app_server.tf

```hcl
resource "aws_instance" "app_server" {
    ami             = var.ami
    instance_tpe    = "t2.medium"
    tags = {
        Name = "${var.app_region}-app-server"
    }
    depends_on = [ aws_dynammodb_table.payroll_db,
                   aws_s3_bucket.payroll_data
                 ]
}
```

s3_bucket.tf

```hcl
resource "aws_s3_bucket" "payroll_data" {
    bucket = "${var.app_region}-${var.bucket}"
}
```

dynamodb_table.tf

```hcl
resource "aws_dynamodb_table" "payroll_db" {
    name            = "user_data"
    billing_mode    = "PAY_PER_REQUEST"
    hash_key        = "EmployeeID"

    attribute {
        name = "EmployeeID"
        type = "N"
    }
}
```

variables.tf

```hcl
variable "app_region" {
    type = string
}
variable "bucket" {
    default = "flexit-payroll-alpha-222001c"
}
variable "ami" {
    type = string
}
```

[![image.png](https://i.postimg.cc/k4Py981T/image.png)](https://postimg.cc/7CXznCyz)

[![image.png](https://i.postimg.cc/gcS6H8ym/image.png)](https://postimg.cc/w3Nv6tbG)

./us-payrolll-app/main.tf

```hcl
module "us_payroll" {
    source = "../modules/payroll-app"
    app_region  = "us-east-1"
    ami         = "ami-242das45ea156e"
}
```

./uk-payrolll-app/main.tf

```hcl
module "uk_payroll" {
    source = "../modules/payroll-app"
    app_region  = "eu-west-1"
    ami         = "ami-242das12ea156f"
}
```

> [!IMPORTANT]
> us_payroll and uk_payroll modules are parents of payroll-app as they call the child module.

## Functions

```shell
terraform console
```

To test function or interpolate variables.

length()
toset()
file()
ceil()
floor()
keys()
values()
lookup()
split()
join()

&nbsp;

---

## Terraform Workspaces (OSS)

[![image.png](https://i.postimg.cc/bY9nJ7Dv/image.png)](https://postimg.cc/4nny2F1C)

We can create multiple projects from the same config.

```shell
terraform workspace new ProjectA
```

To see created workspaces

```shell
terraform workspace list
```

variables.tf

```hcl
variable region {
    default = "ca-central-1"
}
variable instance_type {
    default = "t2.micro"
}
variable ami {
    type = map
    default = {
        "ProjectA" = "ami-0dasdas54a6s",
        "ProjectB" = "ami-0das5dsa36ds"
    }
}
```

main.tf

```hcl
resource "aws_instance" "project" {
    ami             = lookup(var.ami, terraform.workspace)
    instance_type   = var.instance_tpye
    tags = {
        Name = terraform.workspace
    }
}
```

To switch between workspaces

```shell
terraform workspace select ProjectA
```

Stores the state file in **terraform.tfstate.d** where you will have a new folder for each workspace.

&nbsp;

---

## HCP Terraform

### HCP Terraform Types

- **Remote Mode**: Runs execute on HCP Terraform's disposable virtual machines. Enables advanced features like VCS integration, policy enforcement (Sentinel), and cost estimation.
- **Local Mode**: Runs execute on your local machine via the CLI. State is stored in HCP Terraform, but remote execution and cloud variable evaluation are disabled.
- **Agent Mode**: Runs execute on private, on-premises, or isolated infrastructure via lightweight HCP Terraform agents.

### HCP Terraform Workflows

- **VCS-driven workflow**: Es el flujo nativo de GitOps. Conectas el workspace directamente a un repositorio (GitHub, GitLab, etc.). Cada vez que haces un Push o abres un Pull Request, HCP Terraform detecta el cambio automáticamente y lanza el plan o apply.
- **CLI-driven workflow**: Utiliza tu terminal local con los comandos estándar de Terraform (terraform plan, terraform apply). Al añadir el bloque cloud {} a tu código, la CLI intercepta el comando, sube tus archivos locales a HCP Terraform y ejecuta el proceso de forma remota en la nube de HashiCorp.
- **API-driven workflow**: Pensado para integraciones avanzadas y automatización total. No se conecta a Git ni requiere que uses la CLI de forma interactiva. Empaqueta el código en un archivo .tar.gz y lo envía programáticamente mediante llamadas REST a la API de HCP Terraform, ideal para pipelines personalizados de CI/CD (como Jenkins o GitLab CI sin integración nativa).
