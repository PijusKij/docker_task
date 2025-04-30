# docker_task
1. stat_tests_simulation.py was developed, which calculates the power of three different tests for different samples with generated data. Output is the graph called power_plot.png. Code is explained in more detail in code file.
2. requirements.txt has been developed, as it is not computationally complex code, only 3 libraries were needed for the code. Library version was specified too.
3. Dockerfile has beent created. It uses python:3.11-slim version for faster building and deployment. Working directory is set to /app in the container. I copied the requirements.txt file from local machine to the /app directory and installed all libraries specified. Copied rest of the files from the local machine and ran the stat_tests_simulation.py.
4. All files were put into a single folder stats-project in my local machine - for the purpose of copying only them to the container.
5. moved to my stats-project folder in terminal and ran docker run --rm stats-project . - docker builds the stats-project image and looks for the Dockerfile in the folder.
6. docker images was run to ensure that the image i wanted has been created
7. docker run --rm -v "$PWD:/app" stats-project - running the container, "$PWD:/app" was used so that i could locally change files without the need to create new image.
8. docket container runs and output graph is automatically stored in my local folder "stats-project".
