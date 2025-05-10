import sys
import os

print("Python executable:", sys.executable)
print("\nPython version:", sys.version)
print("\nPython search paths:")
for path in sys.path:
    print(f"  {path}")

# Try to import kirin and catch the error
try:
    import kirin
except ImportError as e:
    print("\nError details:")
    print(f"  {str(e)}")
    print("\nFull error info:")
    import traceback
    traceback.print_exc() 