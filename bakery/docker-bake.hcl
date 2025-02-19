group "default" {
    targets = ["backend", "frontend"]
}

target "backend" {
    context = "./backend"
    dockerfile = "Dockerfile"
    tags = ["myapp-backend:latest"]
}

target "frontend" {
    context = "./frontend"
    dockerfile = "Dockerfile"
    tags = ["myapp-frontend:latest"]
}