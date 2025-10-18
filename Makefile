# Makefile for Chennai Flood Prediction Project

# Directories
SRC_DIR = src
TEST_DIR = tests

# Python environment
PYTHON = python3
PIP = $(PYTHON) -m pip

# Files
REQUIREMENTS = requirements.txt

# Upgrade pip, install requirements
install:
	@echo "Upgrading pip..."
	$(PIP) install --upgrade pip
	@echo "Installing dependencies..."
	$(PIP) install -r $(REQUIREMENTS)

# Run fetch & preprocess
fetch:
	$(PYTHON) $(SRC_DIR)/fetch_data.py

preprocess:
	$(PYTHON) $(SRC_DIR)/preprocess.py

# Train the model
train:
	$(PYTHON) $(SRC_DIR)/train_model.py

# Run predictions
predict:
	$(PYTHON) $(SRC_DIR)/predict.py

# Lint code using pylint
lint:
	@echo "Running pylint..."
	$(PYTHON) -m pylint $(SRC_DIR)

# Format code using black
format:
	@echo "Running black..."
	@$(PYTHON) -m black $(SRC_DIR) $(TEST_DIR) || echo "Black finished with warnings"

# Run tests using pytest
test:
	@echo "Running tests..."
	@$(PYTHON) -m pytest -v --maxfail=1 --disable-warnings $(TEST_DIR)

# Run everything
all: install format lint fetch preprocess train test
