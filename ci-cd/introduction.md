# Introduction
CI/CD = Continuoys Integration / Continuous Deployment or Delivery
Gitlab will execute the pipeline that we configured. 
![CI CD](/ci-cd/imgs/ci_cd.png "CI/CD")<br/>

# GitLab Architecture
There is a GitLab instance or Server that has multiple jobs. Each job is executed by a runner. The runners are the agents that run the CI/CD jobs and the GitLab Server assigns pipeline jobs to available Runners.
![GitLab Arch](/ci-cd/imgs/gitlab_arch.png "Gitlab Arch")<br/>

Executing tests is a core part of the CI/CD pipeline.
Before running tests, the app needs dependencies.

## How do we create the pipeline?
The configuration is scripted in the **.gitlab.yml** YAML file.

The tasks such as: run tests, build images, deploy are configured as what are called jobs.

You can define arbitrry names for your jobs. Each job must contain the script clause where we list the commands that should be executed for that job.

 // to be successful make must be available and it mys execute pip and python so they need to be avaialble. 

But where and on which environment is the job executed? pipeline jobs are executed in GitLab runners. And gitlab runners can be installed on different environments such as different OS, and the simplest executor is the `shell` executer. The gitlab runner can be also run in docker containers, where only docker itself needs to be installed and each job runs in a separate and isolated container. Containers runs on a certain Docker image. Depending on the image you use you will have different tools available inside the container. We can specify the image used for the runner using the attribute image for the job, so we specify python and we use a specific version using a tag for the docker image.
The attribute `before_script` are used to install the things and the dependencies before the script runs.

In .gitlab-ci.yml:
```

run_tests:         //name of the job
    image: python:3.9-slim-buster
    before_script: //commands to run before the script
    - apt-get update && apt-get install make
    script:        // what the job should do
    - make test   // needs to be avaibaled

build_image: // build a docker image from the py application
    variables: 
    IMAGE_NAME: repo_name
    IMAGE_TAG: python_app-1.0 
    before_script:
    - docker login -u $REGISTRY blabla
    script: 
    - docker build -t repo_name:python_app-1.0 . 
    - docker push $IMAGE_NAME:$IMAGE_TAG 

```
After committing the changes in the file, gitlab will automatically detect the file and execute the pipeline. 

You can define variables at the job level but also extract them and make them avaible for all the jobs. You use the `$` to access the defined variables.

## Define stages
We want to define in which order the jobs should run. To force the order we use stages by grouping jobs that belong together.

run_test and build_image should be in two different stages. 
```
stages:
    - test
    - build

run_tests: 
    - test
    ...

build_image:
    - build
    ...


```

# Definitions
- Runner: a runner is a service running on a computer and it executes a job.
# Useful Readings