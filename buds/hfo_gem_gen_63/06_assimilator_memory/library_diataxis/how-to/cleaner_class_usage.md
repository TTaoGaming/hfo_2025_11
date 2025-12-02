---
holon:
  id: d399fcb2-235f-4039-a086-78b29d35f3c0
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/cleaner.py
hexagon:
  ontos: owner
  logos: diataxis
---

# How to Use the Cleaner Class (Gen 63)

The `Cleaner` class is designed to ensure that the system remains clean and consistent by refreshing memory and checking the integrity of critical files. This article will guide you through the steps required to utilize this class effectively.

## Prerequisites
- Python 3.x installed
- Appropriate directory structure with required files

## Step-by-Step Instructions

### Step 1: Import Necessary Modules
Begin by importing the required modules. The Cleaner class relies on `os`, `sys`, and `logging` along with a custom `Assimilator` class.

```python
import os
import sys
import logging
from typing import List
from src.assimilator import Assimilator
```

### Step 2: Set Up Logging
Configure logging to track the operations performed by the Cleaner class.

```python
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Cleaner")
```

### Step 3: Initialize the Cleaner
Create an instance of the `Cleaner` class. This step sets up the `Assimilator` object and the base path for file operations.

```python
cleaner = Cleaner()
```

### Step 4: Refresh Memory
Call the `refresh_memory` method to re-ingest the brain and source directories. This ensures that memory is up-to-date.

```python
cleaner.refresh_memory()
```

### Step 5: Check Integrity
Invoke the `check_integrity` method to verify the presence of critical files necessary for system integrity.

```python
cleaner.check_integrity()
```

### Example Usage
Here is a complete example of how to use the Cleaner class in a Python script:

```python
if __name__ == "__main__":
    cleaner = Cleaner()
    cleaner.refresh_memory()
    cleaner.check_integrity()
```

## Conclusion
By following these steps, you can effectively utilize the `Cleaner` class to maintain system hygiene by refreshing memory and checking for critical files. This process ensures the optimal functioning of the system.