.PHONY: help
help:
	@echo "Available commands"
	@echo " - install         : Installs all requirements"
	@echo " - record          : Start the recording process"
	@echo " - animation       : Generate and save animation"
	@echo " - preview         : Open a preview after generating animation"

.PHONY: install
install:
	poetry install

.PHONY: record
record: install
	poetry run termtosvg --template=material.svg --screen-geometry=91x38 readme.svg

.PHONY: animation
animation: install
	poetry run \
	termtosvg \
	--template=material.svg \
	--screen-geometry=91x38 \
	--command='poetry run python readme.py' \
	readme.svg

.PHONY: preview
preview: animation
	open readme.svg
