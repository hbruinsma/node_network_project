from tqdm import tqdm
import time

# Test tqdm
for i in tqdm(range(10), desc="Testing tqdm"):
    time.sleep(0.5)  # Simulate work

print("Progress bar test completed!")
