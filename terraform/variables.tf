variable "aws_region" {
  default = "eu-central-1"
}

variable "db_password" {
  description = "Password for PostgreSQL"
  type        = string
  sensitive   = true
}