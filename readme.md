# Prepare Virtual Environment
# Step 0
Window	:	python -m venv .venv
Linux	:	python3 -m venv .venv

# Step 1
source .venv/bin/activate

# Step 2 (make sure you are in venv)
pip install pandas numpy matplotlib seaborn scikit-learn torch torchvision torchaudio opencv-python pillow tqdm jupyter notebook ipywidgets

# After Finish Virtual Environment
# Step 1
source .venv/bin/activate

# Step 2
jupyter notebook --no-browser --ip=0.0.0.0