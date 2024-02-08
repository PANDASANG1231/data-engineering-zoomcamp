provider "google" {
  credentials = file(var.credentials_file)
  project     = "brave-computer-390518"
  region      = var.loaction
}

resource "google_storage_bucket" "demo_storage_bucket_wenjia" {
  name          = "demo_storage_bucket_wenjia"
  location      = var.loaction
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "demo_dataset_wenjia" {
  dataset_id = "demo_dataset_wenjia"
  location   = var.loaction
}

