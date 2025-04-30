# 📦 Docker Task: Power Simulation for Statistical Tests

Original writeup (first README.md commit) has been changed by AI to have nice structure, formatting and emojis.

---

## 🧪 1. `stat_tests_simulation.py`

This script calculates the power of three different statistical tests across various sample sizes using generated data.

- **Output**: `power_plot.png` (a graph showing power curves)
- The script is fully documented with inline comments.

---

## 📄 2. `requirements.txt`

- Contains only three essential libraries to keep the environment lightweight.
- Library versions are pinned for reproducibility and compatibility.

---

## 🐳 3. `Dockerfile`

The Dockerfile defines the build process using the `python:3.11-slim` base image for efficiency.

Steps:
1. Set the working directory to `/app`.
2. Copy `requirements.txt` and install dependencies.
3. Copy the remaining project files.
4. Set the default command to run `stat_tests_simulation.py`.

---

## 📁 4. Folder Structure

All project files are placed inside a single folder named `stats-project`:

```text
stats-project/
├── Dockerfile
├── requirements.txt
└── stat_tests_simulation.py
```

---

## 🔍 Step 5: Build Docker Image and Verify it

Moved to the project directory:

```bash
cd stats-project
```

Then ran:

```bash
docker run --rm stats-project .
```
This command builds the `stats-project` image and uses the `Dockerfile` found in the current folder.

Checked if the image was created successfully by running:

```bash
docker images
```

This lists all Docker images, including `stats-project`.

---

## 🚀 Step 6: Run the Docker Container

Executed the container with volume mounting:

```bash
docker run --rm -v "$PWD:/app" stats-project
```

Here, `"$PWD:/app"` mounts your current directory to the container’s `/app` folder, so you can edit files locally without rebuilding the image.

---

## 📊 Step 7: Check the Output

The Docker container runs and automatically stores the output graph in your local folder:

```
stats-project/
```

---

## Step 8: Image Publicly Available

Tagged my image:

```bash
docker tag stats-project:latest pijue/stats-project:latest
```
Pushed it to DockerHub:

```bash
docker push pijue/stats-project:latest
```

Image is available with the tag:
```
pijue/stats-project:latest
```

