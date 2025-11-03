SHELL := /bin/bash

.PHONY: help promote promote-dry promote-only

help:
	@echo "Targets:";
	@echo "  promote        # Publish status: complete pages from content/ → docs/";
	@echo "  promote-dry    # Preview promotion without writing files";
	@echo "  promote-only   # Promote only selected files: make promote-only FILES='content/guide/core/quick-start.md ...'";

promote:
	python3 ops/promote.py

promote-dry:
	python3 ops/promote.py --dry-run

promote-only:
	@if [ -z "$(FILES)" ]; then \
		echo "Usage: make promote-only FILES='content/guide/core/quick-start.md content/guide/core/accuracy.md'"; \
		exit 1; \
	fi
	python3 ops/promote.py --only $(FILES)

