variable "credentials_file" {
  description = "Path to the Google Cloud credentials JSON file."
  type        = string
  default     = "./keys/credentials.json"
}

variable "loaction" {
  description = "Location of all instance and products."
  type        = string
  default     = "us-west2"
}
