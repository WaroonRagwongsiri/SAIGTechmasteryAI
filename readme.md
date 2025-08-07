# Prepare Virtual Environment
# Step 0
Linux	:	python3 -m venv .venv \
Window	:	python -m venv .venv

# Step 1
Linux	:	source .venv/bin/activate \
Window	:	./venv/Script/python

# Step 2 (make sure you are in venv)
pip install -r requirements.txt

# After Finish Virtual Environment
# Step 1
Linux	:	source .venv/bin/activate \
Window	:	./venv/Script/python

# Step 2 (Only if computer can't find venv)
jupyter notebook --no-browser --ip=0.0.0.0

# Step 3
Select kernel that you create