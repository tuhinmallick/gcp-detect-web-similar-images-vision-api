# Using GCP Vision API to Detect Similar Images in the Web

![](./vision-api-demo.gif)

Google Cloud Platform's Vision APIs can detect [web references](https://cloud.google.com/vision/docs/detecting-web) for an image, finding similar images from the web.

## Setup

We'll use [gradio](https://gradio.app/) for the user interface, The [GCP Vision AI API](https://cloud.google.com/vision) and [Cloud Run](https://cloud.google.com/run) to deploy our demo.

1. Build the docker image and push to GCP's container repository. Make sure to substitute the project id below with yours.

    ```bash
    docker build . -t gcr.io/<project_id>/vision-api-detect-web-entities:latest
    docker push gcr.io/<project_id>/vision-api-detect-web-entities:latest
    ```

1. Deploy the image to cloud run

    ```bash
    gcloud run deploy --port 80 vision-api-demo --image gcr.io/<project_id>/vision-api-detect-web-entities:latest --region us-central1
    ```

1. When this is deployed, you'll get a URL where you can access the webui. Make the url public by following [this link](https://cloud.google.com/run/docs/securing/managing-access#making_a_service_public). You might have organizational policies that don't allow public internet to access your instance. If that's the case, add Domain restricted sharing to `All`. Be aware this can create a security loophole. 

