# Terraform Modules

## Structure

/root/terraform-projects/
│
├── us-payroll-app/       ← Parent / Root module
│   ├── main.tf
│   └── provider.tf
│
└── modules/
    └── payroll-app/      ← Child module

### Variables consumed by Child

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

&nbsp;

./us-payrolll-app/main.tf

```hcl
module "us_payroll" {
    source = "../modules/payroll-app"
    app_region  = "us-east-1"
    ami         = "ami-242das45ea156e"
}
```

> [!TIP]
> Variables are declared in the child module with a variables.tf file but with no defined value, it will pick it up from the parent module call.

---

### Variables consumed used from Child by Parent Module

```shell
mkdir /root/terraform-projects/modules/payroll-app
#app_server.tf dynamodb_table.tf s3_bucket.tf variables.tf outputs.tf
```

outputs.tf

```hcl
output "app_server_ip" {
  description = "Dirección IP privada de la instancia"
  value       = aws_instance.app_server.private_ip
}

output "bucket_arn" {
  description = "ARN del bucket S3 creado"
  value       = aws_s3_bucket.payroll_data.arn
}
```

&nbsp;

./us-payrolll-app/main.tf

```hcl
module "us_payroll" {
  source     = "../modules/payroll-app"
  app_region = "us-east-1"
  ami        = "ami-242das45ea156e"
}

# Ejemplo 1: Exponer el valor como un output del root module
output "payroll_server_private_ip" {
  value = module.us_payroll.app_server_ip
}

# Ejemplo 2: Usar el valor en otro recurso del parent
resource "aws_sns_topic" "alerts" {
  name = "alerts-${module.us_payroll.app_server_ip}"
}
```
