name: Home Designer CI

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Build and test
      run: |
        docker build -t home-designer .
        docker run home-designer python -m unittest discover

    - name: Push Docker image to Docker Hub
      if: success()
      uses: docker/build-push-action@v2
      with:
        context: .
        push: true
        tags: |
          latest
          ${{ github.sha }}

  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
    - name: Deploy to production
      if: github.ref == 'refs/heads/main' && github.event_name == 'push'
      run: |
        # Add deployment steps here
        echo "Deploying to production..."
