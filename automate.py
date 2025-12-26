import subprocess
import os
import make_data

# Configuration
results_path = "C:/Users/alexr/OneDrive/QAO-REU/constraint_gadgets_alex/alex/"
operators = ["equals", "geq", "leq"]
max_n_range = range(1, 6)  # Tests n from 1 to 5
layers_range = range(1, 3) # Tests 1 and 2 layers

run_single = False
run_two = True

# Single Constraint
if run_single:
    print("Running for a single constraint")
    for op in operators:
        for n in max_n_range:
            # Step 1: Generate Constraint Gadget
            print(f"--- Generating Gadget: {op}, n={n} ---")
            subprocess.run([
                "python", "run_single_constraint.py",
                "--corp", "constraint",
                "--max_n", str(n),
                "--op", op,
                "--results_dir", results_path
            ])
            
            for p in layers_range:
                # Step 2: Solve Problem with Gadget
                print(f"--- Running Problem: {op}, n={n}, p={p} ---")
                subprocess.run([
                    "python", "run_single_constraint.py",
                    "--corp", "problem",
                    "--max_n", str(n),
                    "--op", op,
                    "--n_layers", str(p),
                    "--results_dir", results_path
                ])

# Multiple Constraint
if run_two:
    print("Running for two constraints")
    print("--- Generating Constraint Data Files ---")
    data_path = os.path.join(results_path, "results/")
    make_data.make_two_constraints(result_dir=data_path)
    for support in [1, 2, 3]:
        print(f"--- Generating Gadgets: support={support} ---")
        subprocess.run([
            "python", "run_two_constraint.py",
            "--corp", "constraint",
            "--support", str(support),
            "--results_dir", results_path
        ])

        for p in layers_range:
            print(f"--- Running Problem: support={support}, p={p} ---")
            subprocess.run([
                "python", "run_two_constraint.py",
                "--corp", "problem",
                "--support", str(support),
                "--n_layers", str(p),
                "--results_dir", results_path
            ])

                
                
print("Full experiment suite complete.")