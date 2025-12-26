This file is a merged representation of the entire codebase, combined into a single document by Repomix.
The content has been processed where security check has been disabled.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Security check has been disabled - content may contain sensitive information
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
alex/
  results/
    qubos.csv
results/
  cqaoa_hamiltonian_table_equals.tex
  cqaoa_hamiltonian_table_geq.tex
  cqaoa_hamiltonian_table_leq.tex
  qubos.csv
  two_constraints_support_1.txt
  two_constraints_support_2.txt
  two_constraints_support_3.txt
analyze_results.py
automate.py
constraint_qaoa.py
LICENSE
make_data.py
problem_qaoa.py
run_single_constraint.py
run_two_constraint.py
```

# Files

## File: alex/results/qubos.csv
```
(1, 0); -2*x_0; [[-2]]
(1, 1); -4*x_0; [[-4]]
(1, 2); ; [[0]]
(1, 3); 1*x_0; [[1]]
(1, 4); 3*x_0; [[3]]
(1, 5); 1*x_0; [[1]]
(1, 6); -1*x_0; [[-1]]
(1, 7); 4*x_0; [[4]]
(1, 8); ; [[0]]
(1, 9); 4*x_0; [[4]]
(2, 0); 2*x_0 + 2*x_0 x_1 + 3*x_1; [[2, 2], [0, 3]]
(2, 1); -4*x_0 + -3*x_0 x_1 + 4*x_1; [[-4, -3], [0, 4]]
(2, 2); -5*x_0 + -4*x_0 x_1 + 1*x_1; [[-5, -4], [0, 1]]
(2, 3); 2*x_0 + -1*x_0 x_1 + 1*x_1; [[2, -1], [0, 1]]
(2, 4); 3*x_0 + 2*x_0 x_1 + 3*x_1; [[3, 2], [0, 3]]
(2, 5); 3*x_0 + 1*x_0 x_1 + 4*x_1; [[3, 1], [0, 4]]
(2, 6); 2*x_0 + -1*x_0 x_1 + -5*x_1; [[2, -1], [0, -5]]
(2, 7); -2*x_0 + 2*x_0 x_1; [[-2, 2], [0, 0]]
(2, 8); -2*x_0 x_1; [[0, -2], [0, 0]]
(2, 9); -4*x_0 + -5*x_0 x_1 + -5*x_1; [[-4, -5], [0, -5]]
(3, 0); 4*x_0 + -5*x_0 x_1 + 4*x_0 x_2 + -2*x_1 + 3*x_1 x_2; [[4, -5, 4], [0, -2, 3], [0, 0, 0]]
(3, 1); -5*x_0 + -4*x_0 x_1 + -1*x_0 x_2 + -2*x_1 + 2*x_1 x_2 + -2*x_2; [[-5, -4, -1], [0, -2, 2], [0, 0, -2]]
(3, 2); 2*x_0 + -5*x_0 x_1 + -5*x_0 x_2 + 3*x_1 + -2*x_1 x_2 + -2*x_2; [[2, -5, -5], [0, 3, -2], [0, 0, -2]]
(3, 3); -2*x_0 x_1 + 1*x_0 x_2 + 2*x_1 + -4*x_1 x_2 + -4*x_2; [[0, -2, 1], [0, 2, -4], [0, 0, -4]]
(3, 4); -3*x_0 + -3*x_0 x_1 + -1*x_1 + 4*x_1 x_2; [[-3, -3, 0], [0, -1, 4], [0, 0, 0]]
(3, 5); 2*x_0 + 4*x_0 x_1 + 2*x_0 x_2 + -5*x_1 + 3*x_2; [[2, 4, 2], [0, -5, 0], [0, 0, 3]]
(3, 6); -5*x_0 + -5*x_0 x_1 + 2*x_0 x_2 + -3*x_1 + -4*x_1 x_2 + -1*x_2; [[-5, -5, 2], [0, -3, -4], [0, 0, -1]]
(3, 7); -1*x_0 + -2*x_0 x_1 + -3*x_0 x_2 + 2*x_1 + 4*x_1 x_2 + -2*x_2; [[-1, -2, -3], [0, 2, 4], [0, 0, -2]]
(3, 8); -4*x_0 + -4*x_0 x_2 + -3*x_1 + 2*x_1 x_2 + 4*x_2; [[-4, 0, -4], [0, -3, 2], [0, 0, 4]]
(3, 9); -3*x_0 + 4*x_0 x_1 + -3*x_0 x_2 + 1*x_1 + 3*x_1 x_2 + -1*x_2; [[-3, 4, -3], [0, 1, 3], [0, 0, -1]]
(4, 0); -1*x_0 + -3*x_0 x_1 + -2*x_0 x_2 + -1*x_0 x_3 + -1*x_1 x_2 + 4*x_1 x_3 + -3*x_2 x_3 + -5*x_3; [[-1, -3, -2, -1], [0, 0, -1, 4], [0, 0, 0, -3], [0, 0, 0, -5]]
(4, 1); -4*x_0 + 1*x_0 x_1 + 1*x_0 x_2 + 2*x_0 x_3 + -3*x_1 + 3*x_1 x_2 + 2*x_1 x_3 + -1*x_2 + -3*x_2 x_3 + -2*x_3; [[-4, 1, 1, 2], [0, -3, 3, 2], [0, 0, -1, -3], [0, 0, 0, -2]]
(4, 2); -1*x_0 + -1*x_0 x_1 + 2*x_0 x_2 + -1*x_1 + -3*x_1 x_2 + 4*x_1 x_3 + 2*x_2 + 4*x_2 x_3 + 3*x_3; [[-1, -1, 2, 0], [0, -1, -3, 4], [0, 0, 2, 4], [0, 0, 0, 3]]
(4, 3); 2*x_0 + 1*x_0 x_1 + 2*x_0 x_2 + 4*x_0 x_3 + -3*x_1 + 2*x_1 x_2 + 3*x_1 x_3 + 1*x_2 + -5*x_2 x_3 + 3*x_3; [[2, 1, 2, 4], [0, -3, 2, 3], [0, 0, 1, -5], [0, 0, 0, 3]]
(4, 4); -3*x_0 + 2*x_0 x_1 + -5*x_0 x_2 + -4*x_0 x_3 + 2*x_1 + 4*x_1 x_2 + -2*x_1 x_3 + -4*x_2 + -1*x_2 x_3 + -1*x_3; [[-3, 2, -5, -4], [0, 2, 4, -2], [0, 0, -4, -1], [0, 0, 0, -1]]
(4, 5); -3*x_0 + -1*x_0 x_1 + 2*x_0 x_2 + -1*x_1 + -5*x_1 x_2 + -2*x_1 x_3 + 4*x_2 + 3*x_2 x_3 + 4*x_3; [[-3, -1, 2, 0], [0, -1, -5, -2], [0, 0, 4, 3], [0, 0, 0, 4]]
(4, 6); 2*x_0 + 4*x_0 x_1 + -4*x_0 x_2 + -3*x_0 x_3 + 2*x_1 + 1*x_1 x_2 + -1*x_2 x_3 + -4*x_3; [[2, 4, -4, -3], [0, 2, 1, 0], [0, 0, 0, -1], [0, 0, 0, -4]]
(4, 7); -4*x_0 x_1 + -4*x_0 x_2 + 3*x_0 x_3 + -3*x_1 + 4*x_1 x_2 + -1*x_1 x_3 + 4*x_2 + -5*x_3; [[0, -4, -4, 3], [0, -3, 4, -1], [0, 0, 4, 0], [0, 0, 0, -5]]
(4, 8); 4*x_0 + 4*x_0 x_1 + 4*x_0 x_2 + 4*x_0 x_3 + -5*x_1 + -2*x_1 x_2 + 4*x_1 x_3 + -1*x_2 + -5*x_2 x_3 + -4*x_3; [[4, 4, 4, 4], [0, -5, -2, 4], [0, 0, -1, -5], [0, 0, 0, -4]]
(4, 9); -4*x_0 + 3*x_0 x_1 + -5*x_0 x_2 + 4*x_0 x_3 + 2*x_1 + -2*x_1 x_2 + -2*x_1 x_3 + 1*x_2 + 4*x_2 x_3 + -2*x_3; [[-4, 3, -5, 4], [0, 2, -2, -2], [0, 0, 1, 4], [0, 0, 0, -2]]
(5, 0); -4*x_0 x_1 + -5*x_0 x_2 + 3*x_0 x_3 + -5*x_0 x_4 + -5*x_1 + -5*x_1 x_2 + -1*x_1 x_3 + 1*x_1 x_4 + 4*x_2 + -5*x_2 x_4 + -5*x_3 + -5*x_3 x_4 + 4*x_4; [[0, -4, -5, 3, -5], [0, -5, -5, -1, 1], [0, 0, 4, 0, -5], [0, 0, 0, -5, -5], [0, 0, 0, 0, 4]]
(5, 1); -5*x_0 + 3*x_0 x_1 + -3*x_0 x_2 + 1*x_0 x_3 + 4*x_0 x_4 + 3*x_1 + -3*x_1 x_3 + 1*x_2 + 1*x_2 x_3 + 3*x_2 x_4 + -5*x_3 + 1*x_3 x_4 + 3*x_4; [[-5, 3, -3, 1, 4], [0, 3, 0, -3, 0], [0, 0, 1, 1, 3], [0, 0, 0, -5, 1], [0, 0, 0, 0, 3]]
(5, 2); -1*x_0 + 4*x_0 x_1 + 4*x_0 x_2 + -4*x_0 x_4 + -2*x_1 + 3*x_1 x_3 + 2*x_1 x_4 + 2*x_2 + -4*x_2 x_3 + -1*x_2 x_4 + -3*x_3 + -1*x_3 x_4 + 2*x_4; [[-1, 4, 4, 0, -4], [0, -2, 0, 3, 2], [0, 0, 2, -4, -1], [0, 0, 0, -3, -1], [0, 0, 0, 0, 2]]
(5, 3); -1*x_0 + 1*x_0 x_1 + -5*x_0 x_3 + 1*x_0 x_4 + 4*x_1 + -1*x_1 x_2 + 2*x_1 x_4 + -2*x_2 x_3 + 4*x_2 x_4 + 1*x_3 + 4*x_3 x_4 + 2*x_4; [[-1, 1, 0, -5, 1], [0, 4, -1, 0, 2], [0, 0, 0, -2, 4], [0, 0, 0, 1, 4], [0, 0, 0, 0, 2]]
(5, 4); 1*x_0 + -2*x_0 x_1 + 2*x_0 x_2 + -5*x_0 x_3 + -4*x_0 x_4 + -2*x_1 + 2*x_1 x_2 + -5*x_1 x_3 + -2*x_1 x_4 + -3*x_2 + 4*x_2 x_3 + -2*x_2 x_4 + 3*x_3 x_4 + 3*x_4; [[1, -2, 2, -5, -4], [0, -2, 2, -5, -2], [0, 0, -3, 4, -2], [0, 0, 0, 0, 3], [0, 0, 0, 0, 3]]
(5, 5); -3*x_0 + -2*x_0 x_1 + 3*x_0 x_2 + 3*x_0 x_3 + 1*x_0 x_4 + -5*x_1 + -4*x_1 x_2 + -1*x_1 x_3 + -2*x_1 x_4 + -2*x_2 + -1*x_2 x_3 + -4*x_2 x_4 + -2*x_3 + -1*x_4; [[-3, -2, 3, 3, 1], [0, -5, -4, -1, -2], [0, 0, -2, -1, -4], [0, 0, 0, -2, 0], [0, 0, 0, 0, -1]]
(5, 6); -1*x_0 + -1*x_0 x_2 + -4*x_0 x_3 + 1*x_0 x_4 + 3*x_1 x_2 + 1*x_1 x_3 + 1*x_1 x_4 + -3*x_2 + -4*x_2 x_3 + 1*x_2 x_4 + 1*x_3 + 1*x_3 x_4 + 3*x_4; [[-1, 0, -1, -4, 1], [0, 0, 3, 1, 1], [0, 0, -3, -4, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 3]]
(5, 7); -4*x_0 + 3*x_0 x_2 + 3*x_0 x_3 + 3*x_0 x_4 + -2*x_1 + -4*x_1 x_2 + 1*x_1 x_3 + 1*x_1 x_4 + 1*x_2 + -3*x_2 x_3 + 1*x_2 x_4 + 1*x_3 + -4*x_3 x_4 + 3*x_4; [[-4, 0, 3, 3, 3], [0, -2, -4, 1, 1], [0, 0, 1, -3, 1], [0, 0, 0, 1, -4], [0, 0, 0, 0, 3]]
(5, 8); 1*x_0 + 4*x_0 x_1 + -4*x_0 x_2 + -3*x_0 x_4 + 2*x_1 x_2 + 2*x_1 x_3 + -5*x_1 x_4 + -5*x_2 + 1*x_2 x_4 + -2*x_3 + -3*x_3 x_4 + -4*x_4; [[1, 4, -4, 0, -3], [0, 0, 2, 2, -5], [0, 0, -5, 0, 1], [0, 0, 0, -2, -3], [0, 0, 0, 0, -4]]
(5, 9); -4*x_0 + 3*x_0 x_1 + 1*x_0 x_2 + -3*x_0 x_3 + 3*x_0 x_4 + -2*x_1 + -2*x_1 x_2 + -4*x_1 x_3 + 4*x_1 x_4 + -1*x_2 + 1*x_2 x_3 + -3*x_3 + 2*x_3 x_4 + -2*x_4; [[-4, 3, 1, -3, 3], [0, -2, -2, -4, 4], [0, 0, -1, 1, 0], [0, 0, 0, -3, 2], [0, 0, 0, 0, -2]]
```

## File: results/cqaoa_hamiltonian_table_equals.tex
```
\begin{tabular}{|c|l|}
\hline
\textbf{Constraints} & \textbf{Hamiltonian} \\
\hline
$x_0 = 0$ & $ -  Z_0 Z_f$ \\
\hline
$x_0 = 1$ & $ Z_0 Z_f$ \\
\hline
$x_0 + x_1 = 0$ & $\frac{1}{2} Z_f - \frac{1}{2} Z_1 Z_f - \frac{1}{2} Z_0 Z_f - \frac{1}{2} Z_0 Z_1 Z_f$ \\
\hline
$x_0 + x_1 = 1$ & $ Z_0 Z_1 Z_f$ \\
\hline
$x_0 + x_1 = 2$ & $\frac{1}{2} Z_f + \frac{1}{2} Z_1 Z_f + \frac{1}{2} Z_0 Z_f - \frac{1}{2} Z_0 Z_1 Z_f$ \\
\hline
$x_0 + x_1 + x_2 = 0$ & $\frac{3}{4} Z_f - \frac{1}{4} Z_2 Z_f - \frac{1}{4} Z_1 Z_f - \frac{1}{4} Z_1 Z_2 Z_f - \frac{1}{4} Z_0 Z_f - \frac{1}{4} Z_0 Z_2 Z_f - \frac{1}{4} Z_0 Z_1 Z_f - \frac{1}{4} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 = 1$ & $\frac{1}{4} Z_f - \frac{1}{4} Z_2 Z_f - \frac{1}{4} Z_1 Z_f + \frac{1}{4} Z_1 Z_2 Z_f - \frac{1}{4} Z_0 Z_f + \frac{1}{4} Z_0 Z_2 Z_f + \frac{1}{4} Z_0 Z_1 Z_f + \frac{3}{4} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 = 2$ & $\frac{1}{4} Z_f + \frac{1}{4} Z_2 Z_f + \frac{1}{4} Z_1 Z_f + \frac{1}{4} Z_1 Z_2 Z_f + \frac{1}{4} Z_0 Z_f + \frac{1}{4} Z_0 Z_2 Z_f + \frac{1}{4} Z_0 Z_1 Z_f - \frac{3}{4} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 = 3$ & $\frac{3}{4} Z_f + \frac{1}{4} Z_2 Z_f + \frac{1}{4} Z_1 Z_f - \frac{1}{4} Z_1 Z_2 Z_f + \frac{1}{4} Z_0 Z_f - \frac{1}{4} Z_0 Z_2 Z_f - \frac{1}{4} Z_0 Z_1 Z_f + \frac{1}{4} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 = 0$ & $\frac{7}{8} Z_f - \frac{1}{8} Z_3 Z_f - \frac{1}{8} Z_2 Z_f - \frac{1}{8} Z_2 Z_3 Z_f - \frac{1}{8} Z_1 Z_f - \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_f - \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 = 1$ & $\frac{1}{2} Z_f - \frac{1}{4} Z_3 Z_f - \frac{1}{4} Z_2 Z_f - \frac{1}{4} Z_1 Z_f + \frac{1}{4} Z_1 Z_2 Z_3 Z_f - \frac{1}{4} Z_0 Z_f + \frac{1}{4} Z_0 Z_2 Z_3 Z_f + \frac{1}{4} Z_0 Z_1 Z_3 Z_f + \frac{1}{4} Z_0 Z_1 Z_2 Z_f + \frac{1}{2} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 = 2$ & $\frac{1}{4} Z_f + \frac{1}{4} Z_2 Z_3 Z_f + \frac{1}{4} Z_1 Z_3 Z_f + \frac{1}{4} Z_1 Z_2 Z_f + \frac{1}{4} Z_0 Z_3 Z_f + \frac{1}{4} Z_0 Z_2 Z_f + \frac{1}{4} Z_0 Z_1 Z_f - \frac{3}{4} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 = 3$ & $\frac{1}{2} Z_f + \frac{1}{4} Z_3 Z_f + \frac{1}{4} Z_2 Z_f + \frac{1}{4} Z_1 Z_f - \frac{1}{4} Z_1 Z_2 Z_3 Z_f + \frac{1}{4} Z_0 Z_f - \frac{1}{4} Z_0 Z_2 Z_3 Z_f - \frac{1}{4} Z_0 Z_1 Z_3 Z_f - \frac{1}{4} Z_0 Z_1 Z_2 Z_f + \frac{1}{2} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 = 4$ & $\frac{7}{8} Z_f + \frac{1}{8} Z_3 Z_f + \frac{1}{8} Z_2 Z_f - \frac{1}{8} Z_2 Z_3 Z_f + \frac{1}{8} Z_1 Z_f - \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_f + \frac{1}{8} Z_0 Z_f - \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 = 0$ & $\frac{15}{16} Z_f - \frac{1}{16} Z_4 Z_f - \frac{1}{16} Z_3 Z_f - \frac{1}{16} Z_3 Z_4 Z_f - \frac{1}{16} Z_2 Z_f - \frac{1}{16} Z_2 Z_4 Z_f - \frac{1}{16} Z_2 Z_3 Z_f - \frac{1}{16} Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_f - \frac{1}{16} Z_1 Z_4 Z_f - \frac{1}{16} Z_1 Z_3 Z_f - \frac{1}{16} Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_f - \frac{1}{16} Z_1 Z_2 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_3 Z_f - \frac{1}{16} Z_1 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_f - \frac{1}{16} Z_0 Z_4 Z_f - \frac{1}{16} Z_0 Z_3 Z_f - \frac{1}{16} Z_0 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_f - \frac{1}{16} Z_0 Z_2 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_3 Z_f - \frac{1}{16} Z_0 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_f - \frac{1}{16} Z_0 Z_1 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_3 Z_f - \frac{1}{16} Z_0 Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 = 1$ & $\frac{11}{16} Z_f - \frac{3}{16} Z_4 Z_f - \frac{3}{16} Z_3 Z_f - \frac{1}{16} Z_3 Z_4 Z_f - \frac{3}{16} Z_2 Z_f - \frac{1}{16} Z_2 Z_4 Z_f - \frac{1}{16} Z_2 Z_3 Z_f + \frac{1}{16} Z_2 Z_3 Z_4 Z_f - \frac{3}{16} Z_1 Z_f - \frac{1}{16} Z_1 Z_4 Z_f - \frac{1}{16} Z_1 Z_3 Z_f + \frac{1}{16} Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_f + \frac{1}{16} Z_1 Z_2 Z_4 Z_f + \frac{1}{16} Z_1 Z_2 Z_3 Z_f + \frac{3}{16} Z_1 Z_2 Z_3 Z_4 Z_f - \frac{3}{16} Z_0 Z_f - \frac{1}{16} Z_0 Z_4 Z_f - \frac{1}{16} Z_0 Z_3 Z_f + \frac{1}{16} Z_0 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_f + \frac{1}{16} Z_0 Z_2 Z_4 Z_f + \frac{1}{16} Z_0 Z_2 Z_3 Z_f + \frac{3}{16} Z_0 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_f + \frac{1}{16} Z_0 Z_1 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_3 Z_f + \frac{3}{16} Z_0 Z_1 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_f + \frac{3}{16} Z_0 Z_1 Z_2 Z_4 Z_f + \frac{3}{16} Z_0 Z_1 Z_2 Z_3 Z_f + \frac{5}{16} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 = 2$ & $\frac{3}{8} Z_f - \frac{1}{8} Z_4 Z_f - \frac{1}{8} Z_3 Z_f + \frac{1}{8} Z_3 Z_4 Z_f - \frac{1}{8} Z_2 Z_f + \frac{1}{8} Z_2 Z_4 Z_f + \frac{1}{8} Z_2 Z_3 Z_f + \frac{1}{8} Z_2 Z_3 Z_4 Z_f - \frac{1}{8} Z_1 Z_f + \frac{1}{8} Z_1 Z_4 Z_f + \frac{1}{8} Z_1 Z_3 Z_f + \frac{1}{8} Z_1 Z_3 Z_4 Z_f + \frac{1}{8} Z_1 Z_2 Z_f + \frac{1}{8} Z_1 Z_2 Z_4 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_4 Z_f - \frac{1}{8} Z_0 Z_f + \frac{1}{8} Z_0 Z_4 Z_f + \frac{1}{8} Z_0 Z_3 Z_f + \frac{1}{8} Z_0 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_2 Z_f + \frac{1}{8} Z_0 Z_2 Z_4 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_f + \frac{1}{8} Z_0 Z_1 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f - \frac{5}{8} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 = 3$ & $\frac{3}{8} Z_f + \frac{1}{8} Z_4 Z_f + \frac{1}{8} Z_3 Z_f + \frac{1}{8} Z_3 Z_4 Z_f + \frac{1}{8} Z_2 Z_f + \frac{1}{8} Z_2 Z_4 Z_f + \frac{1}{8} Z_2 Z_3 Z_f - \frac{1}{8} Z_2 Z_3 Z_4 Z_f + \frac{1}{8} Z_1 Z_f + \frac{1}{8} Z_1 Z_4 Z_f + \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_3 Z_4 Z_f + \frac{1}{8} Z_1 Z_2 Z_f - \frac{1}{8} Z_1 Z_2 Z_4 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_f + \frac{1}{8} Z_0 Z_4 Z_f + \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_2 Z_f - \frac{1}{8} Z_0 Z_2 Z_4 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_f - \frac{1}{8} Z_0 Z_1 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f + \frac{5}{8} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 = 4$ & $\frac{11}{16} Z_f + \frac{3}{16} Z_4 Z_f + \frac{3}{16} Z_3 Z_f - \frac{1}{16} Z_3 Z_4 Z_f + \frac{3}{16} Z_2 Z_f - \frac{1}{16} Z_2 Z_4 Z_f - \frac{1}{16} Z_2 Z_3 Z_f - \frac{1}{16} Z_2 Z_3 Z_4 Z_f + \frac{3}{16} Z_1 Z_f - \frac{1}{16} Z_1 Z_4 Z_f - \frac{1}{16} Z_1 Z_3 Z_f - \frac{1}{16} Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_f - \frac{1}{16} Z_1 Z_2 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_3 Z_f + \frac{3}{16} Z_1 Z_2 Z_3 Z_4 Z_f + \frac{3}{16} Z_0 Z_f - \frac{1}{16} Z_0 Z_4 Z_f - \frac{1}{16} Z_0 Z_3 Z_f - \frac{1}{16} Z_0 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_f - \frac{1}{16} Z_0 Z_2 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_3 Z_f + \frac{3}{16} Z_0 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_f - \frac{1}{16} Z_0 Z_1 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_3 Z_f + \frac{3}{16} Z_0 Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_f + \frac{3}{16} Z_0 Z_1 Z_2 Z_4 Z_f + \frac{3}{16} Z_0 Z_1 Z_2 Z_3 Z_f - \frac{5}{16} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 = 5$ & $\frac{15}{16} Z_f + \frac{1}{16} Z_4 Z_f + \frac{1}{16} Z_3 Z_f - \frac{1}{16} Z_3 Z_4 Z_f + \frac{1}{16} Z_2 Z_f - \frac{1}{16} Z_2 Z_4 Z_f - \frac{1}{16} Z_2 Z_3 Z_f + \frac{1}{16} Z_2 Z_3 Z_4 Z_f + \frac{1}{16} Z_1 Z_f - \frac{1}{16} Z_1 Z_4 Z_f - \frac{1}{16} Z_1 Z_3 Z_f + \frac{1}{16} Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_f + \frac{1}{16} Z_1 Z_2 Z_4 Z_f + \frac{1}{16} Z_1 Z_2 Z_3 Z_f - \frac{1}{16} Z_1 Z_2 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_f - \frac{1}{16} Z_0 Z_4 Z_f - \frac{1}{16} Z_0 Z_3 Z_f + \frac{1}{16} Z_0 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_f + \frac{1}{16} Z_0 Z_2 Z_4 Z_f + \frac{1}{16} Z_0 Z_2 Z_3 Z_f - \frac{1}{16} Z_0 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_f + \frac{1}{16} Z_0 Z_1 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_3 Z_f - \frac{1}{16} Z_0 Z_1 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 = 2$ & $ Z_f$ \\
\hline
$x_0 = 3$ & $ Z_f$ \\
\hline
$x_0 = 4$ & $ Z_f$ \\
\hline
$x_0 = 5$ & $ Z_f$ \\
\hline
$x_0 + x_1 = 3$ & $ Z_f$ \\
\hline
$x_0 + x_1 = 4$ & $ Z_f$ \\
\hline
$x_0 + x_1 = 5$ & $ Z_f$ \\
\hline
$x_0 + x_1 + x_2 = 4$ & $ Z_f$ \\
\hline
$x_0 + x_1 + x_2 = 5$ & $ Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 = 5$ & $ Z_f$ \\
\hline
\end{tabular}
```

## File: results/cqaoa_hamiltonian_table_geq.tex
```
\begin{tabular}{|c|l|}
\hline
\textbf{Constraints} & \textbf{Hamiltonian} \\
\hline
$x_0 \geq 0$ & $ -  Z_f$ \\
\hline
$x_0 \geq 1$ & $ Z_0 Z_f$ \\
\hline
$x_0 + x_1 \geq 0$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 \geq 1$ & $ - \frac{1}{2} Z_f + \frac{1}{2} Z_1 Z_f + \frac{1}{2} Z_0 Z_f + \frac{1}{2} Z_0 Z_1 Z_f$ \\
\hline
$x_0 + x_1 \geq 2$ & $\frac{1}{2} Z_f + \frac{1}{2} Z_1 Z_f + \frac{1}{2} Z_0 Z_f - \frac{1}{2} Z_0 Z_1 Z_f$ \\
\hline
$x_0 + x_1 + x_2 \geq 0$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 \geq 1$ & $ - \frac{3}{4} Z_f + \frac{1}{4} Z_2 Z_f + \frac{1}{4} Z_1 Z_f + \frac{1}{4} Z_1 Z_2 Z_f + \frac{1}{4} Z_0 Z_f + \frac{1}{4} Z_0 Z_2 Z_f + \frac{1}{4} Z_0 Z_1 Z_f + \frac{1}{4} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 \geq 2$ & $\frac{1}{2} Z_2 Z_f + \frac{1}{2} Z_1 Z_f + \frac{1}{2} Z_0 Z_f - \frac{1}{2} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 \geq 3$ & $\frac{3}{4} Z_f + \frac{1}{4} Z_2 Z_f + \frac{1}{4} Z_1 Z_f - \frac{1}{4} Z_1 Z_2 Z_f + \frac{1}{4} Z_0 Z_f - \frac{1}{4} Z_0 Z_2 Z_f - \frac{1}{4} Z_0 Z_1 Z_f + \frac{1}{4} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \geq 0$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \geq 1$ & $ - \frac{7}{8} Z_f + \frac{1}{8} Z_3 Z_f + \frac{1}{8} Z_2 Z_f + \frac{1}{8} Z_2 Z_3 Z_f + \frac{1}{8} Z_1 Z_f + \frac{1}{8} Z_1 Z_3 Z_f + \frac{1}{8} Z_1 Z_2 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_f + \frac{1}{8} Z_0 Z_f + \frac{1}{8} Z_0 Z_3 Z_f + \frac{1}{8} Z_0 Z_2 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \geq 2$ & $ - \frac{3}{8} Z_f + \frac{3}{8} Z_3 Z_f + \frac{3}{8} Z_2 Z_f + \frac{1}{8} Z_2 Z_3 Z_f + \frac{3}{8} Z_1 Z_f + \frac{1}{8} Z_1 Z_3 Z_f + \frac{1}{8} Z_1 Z_2 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_f + \frac{3}{8} Z_0 Z_f + \frac{1}{8} Z_0 Z_3 Z_f + \frac{1}{8} Z_0 Z_2 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{3}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \geq 3$ & $\frac{3}{8} Z_f + \frac{3}{8} Z_3 Z_f + \frac{3}{8} Z_2 Z_f - \frac{1}{8} Z_2 Z_3 Z_f + \frac{3}{8} Z_1 Z_f - \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_f + \frac{3}{8} Z_0 Z_f - \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_f + \frac{3}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \geq 4$ & $\frac{7}{8} Z_f + \frac{1}{8} Z_3 Z_f + \frac{1}{8} Z_2 Z_f - \frac{1}{8} Z_2 Z_3 Z_f + \frac{1}{8} Z_1 Z_f - \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_f + \frac{1}{8} Z_0 Z_f - \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \geq 0$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \geq 1$ & $ - \frac{15}{16} Z_f + \frac{1}{16} Z_4 Z_f + \frac{1}{16} Z_3 Z_f + \frac{1}{16} Z_3 Z_4 Z_f + \frac{1}{16} Z_2 Z_f + \frac{1}{16} Z_2 Z_4 Z_f + \frac{1}{16} Z_2 Z_3 Z_f + \frac{1}{16} Z_2 Z_3 Z_4 Z_f + \frac{1}{16} Z_1 Z_f + \frac{1}{16} Z_1 Z_4 Z_f + \frac{1}{16} Z_1 Z_3 Z_f + \frac{1}{16} Z_1 Z_3 Z_4 Z_f + \frac{1}{16} Z_1 Z_2 Z_f + \frac{1}{16} Z_1 Z_2 Z_4 Z_f + \frac{1}{16} Z_1 Z_2 Z_3 Z_f + \frac{1}{16} Z_1 Z_2 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_f + \frac{1}{16} Z_0 Z_4 Z_f + \frac{1}{16} Z_0 Z_3 Z_f + \frac{1}{16} Z_0 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_2 Z_f + \frac{1}{16} Z_0 Z_2 Z_4 Z_f + \frac{1}{16} Z_0 Z_2 Z_3 Z_f + \frac{1}{16} Z_0 Z_2 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_f + \frac{1}{16} Z_0 Z_1 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_3 Z_f + \frac{1}{16} Z_0 Z_1 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \geq 2$ & $ - \frac{5}{8} Z_f + \frac{1}{4} Z_4 Z_f + \frac{1}{4} Z_3 Z_f + \frac{1}{8} Z_3 Z_4 Z_f + \frac{1}{4} Z_2 Z_f + \frac{1}{8} Z_2 Z_4 Z_f + \frac{1}{8} Z_2 Z_3 Z_f + \frac{1}{4} Z_1 Z_f + \frac{1}{8} Z_1 Z_4 Z_f + \frac{1}{8} Z_1 Z_3 Z_f + \frac{1}{8} Z_1 Z_2 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_4 Z_f + \frac{1}{4} Z_0 Z_f + \frac{1}{8} Z_0 Z_4 Z_f + \frac{1}{8} Z_0 Z_3 Z_f + \frac{1}{8} Z_0 Z_2 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f - \frac{1}{4} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \geq 3$ & $\frac{3}{8} Z_4 Z_f + \frac{3}{8} Z_3 Z_f + \frac{3}{8} Z_2 Z_f - \frac{1}{8} Z_2 Z_3 Z_4 Z_f + \frac{3}{8} Z_1 Z_f - \frac{1}{8} Z_1 Z_3 Z_4 Z_f - \frac{1}{8} Z_1 Z_2 Z_4 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_f + \frac{3}{8} Z_0 Z_f - \frac{1}{8} Z_0 Z_3 Z_4 Z_f - \frac{1}{8} Z_0 Z_2 Z_4 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_f + \frac{3}{8} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \geq 4$ & $\frac{5}{8} Z_f + \frac{1}{4} Z_4 Z_f + \frac{1}{4} Z_3 Z_f - \frac{1}{8} Z_3 Z_4 Z_f + \frac{1}{4} Z_2 Z_f - \frac{1}{8} Z_2 Z_4 Z_f - \frac{1}{8} Z_2 Z_3 Z_f + \frac{1}{4} Z_1 Z_f - \frac{1}{8} Z_1 Z_4 Z_f - \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_4 Z_f + \frac{1}{4} Z_0 Z_f - \frac{1}{8} Z_0 Z_4 Z_f - \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f - \frac{1}{4} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \geq 5$ & $\frac{15}{16} Z_f + \frac{1}{16} Z_4 Z_f + \frac{1}{16} Z_3 Z_f - \frac{1}{16} Z_3 Z_4 Z_f + \frac{1}{16} Z_2 Z_f - \frac{1}{16} Z_2 Z_4 Z_f - \frac{1}{16} Z_2 Z_3 Z_f + \frac{1}{16} Z_2 Z_3 Z_4 Z_f + \frac{1}{16} Z_1 Z_f - \frac{1}{16} Z_1 Z_4 Z_f - \frac{1}{16} Z_1 Z_3 Z_f + \frac{1}{16} Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_f + \frac{1}{16} Z_1 Z_2 Z_4 Z_f + \frac{1}{16} Z_1 Z_2 Z_3 Z_f - \frac{1}{16} Z_1 Z_2 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_f - \frac{1}{16} Z_0 Z_4 Z_f - \frac{1}{16} Z_0 Z_3 Z_f + \frac{1}{16} Z_0 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_f + \frac{1}{16} Z_0 Z_2 Z_4 Z_f + \frac{1}{16} Z_0 Z_2 Z_3 Z_f - \frac{1}{16} Z_0 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_f + \frac{1}{16} Z_0 Z_1 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_3 Z_f - \frac{1}{16} Z_0 Z_1 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 \geq 2$ & $ Z_f$ \\
\hline
$x_0 \geq 3$ & $ Z_f$ \\
\hline
$x_0 \geq 4$ & $ Z_f$ \\
\hline
$x_0 \geq 5$ & $ Z_f$ \\
\hline
$x_0 + x_1 \geq 3$ & $ Z_f$ \\
\hline
$x_0 + x_1 \geq 4$ & $ Z_f$ \\
\hline
$x_0 + x_1 \geq 5$ & $ Z_f$ \\
\hline
$x_0 + x_1 + x_2 \geq 4$ & $ Z_f$ \\
\hline
$x_0 + x_1 + x_2 \geq 5$ & $ Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \geq 5$ & $ Z_f$ \\
\hline
\end{tabular}
```

## File: results/cqaoa_hamiltonian_table_leq.tex
```
\begin{tabular}{|c|l|}
\hline
\textbf{Constraints} & \textbf{Hamiltonian} \\
\hline
$x_0 \leq 0$ & $ -  Z_0 Z_f$ \\
\hline
$x_0 \leq 1$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 \leq 0$ & $\frac{1}{2} Z_f - \frac{1}{2} Z_1 Z_f - \frac{1}{2} Z_0 Z_f - \frac{1}{2} Z_0 Z_1 Z_f$ \\
\hline
$x_0 + x_1 \leq 1$ & $ - \frac{1}{2} Z_f - \frac{1}{2} Z_1 Z_f - \frac{1}{2} Z_0 Z_f + \frac{1}{2} Z_0 Z_1 Z_f$ \\
\hline
$x_0 + x_1 \leq 2$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 \leq 0$ & $\frac{3}{4} Z_f - \frac{1}{4} Z_2 Z_f - \frac{1}{4} Z_1 Z_f - \frac{1}{4} Z_1 Z_2 Z_f - \frac{1}{4} Z_0 Z_f - \frac{1}{4} Z_0 Z_2 Z_f - \frac{1}{4} Z_0 Z_1 Z_f - \frac{1}{4} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 \leq 1$ & $ - \frac{1}{2} Z_2 Z_f - \frac{1}{2} Z_1 Z_f - \frac{1}{2} Z_0 Z_f + \frac{1}{2} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 \leq 2$ & $ - \frac{3}{4} Z_f - \frac{1}{4} Z_2 Z_f - \frac{1}{4} Z_1 Z_f + \frac{1}{4} Z_1 Z_2 Z_f - \frac{1}{4} Z_0 Z_f + \frac{1}{4} Z_0 Z_2 Z_f + \frac{1}{4} Z_0 Z_1 Z_f - \frac{1}{4} Z_0 Z_1 Z_2 Z_f$ \\
\hline
$x_0 + x_1 + x_2 \leq 3$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \leq 0$ & $\frac{7}{8} Z_f - \frac{1}{8} Z_3 Z_f - \frac{1}{8} Z_2 Z_f - \frac{1}{8} Z_2 Z_3 Z_f - \frac{1}{8} Z_1 Z_f - \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_f - \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \leq 1$ & $\frac{3}{8} Z_f - \frac{3}{8} Z_3 Z_f - \frac{3}{8} Z_2 Z_f - \frac{1}{8} Z_2 Z_3 Z_f - \frac{3}{8} Z_1 Z_f - \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_f - \frac{3}{8} Z_0 Z_f - \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_f + \frac{3}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \leq 2$ & $ - \frac{3}{8} Z_f - \frac{3}{8} Z_3 Z_f - \frac{3}{8} Z_2 Z_f + \frac{1}{8} Z_2 Z_3 Z_f - \frac{3}{8} Z_1 Z_f + \frac{1}{8} Z_1 Z_3 Z_f + \frac{1}{8} Z_1 Z_2 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_f - \frac{3}{8} Z_0 Z_f + \frac{1}{8} Z_0 Z_3 Z_f + \frac{1}{8} Z_0 Z_2 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{3}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \leq 3$ & $ - \frac{7}{8} Z_f - \frac{1}{8} Z_3 Z_f - \frac{1}{8} Z_2 Z_f + \frac{1}{8} Z_2 Z_3 Z_f - \frac{1}{8} Z_1 Z_f + \frac{1}{8} Z_1 Z_3 Z_f + \frac{1}{8} Z_1 Z_2 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_f - \frac{1}{8} Z_0 Z_f + \frac{1}{8} Z_0 Z_3 Z_f + \frac{1}{8} Z_0 Z_2 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \leq 4$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \leq 0$ & $\frac{15}{16} Z_f - \frac{1}{16} Z_4 Z_f - \frac{1}{16} Z_3 Z_f - \frac{1}{16} Z_3 Z_4 Z_f - \frac{1}{16} Z_2 Z_f - \frac{1}{16} Z_2 Z_4 Z_f - \frac{1}{16} Z_2 Z_3 Z_f - \frac{1}{16} Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_f - \frac{1}{16} Z_1 Z_4 Z_f - \frac{1}{16} Z_1 Z_3 Z_f - \frac{1}{16} Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_f - \frac{1}{16} Z_1 Z_2 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_3 Z_f - \frac{1}{16} Z_1 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_f - \frac{1}{16} Z_0 Z_4 Z_f - \frac{1}{16} Z_0 Z_3 Z_f - \frac{1}{16} Z_0 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_f - \frac{1}{16} Z_0 Z_2 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_3 Z_f - \frac{1}{16} Z_0 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_f - \frac{1}{16} Z_0 Z_1 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_3 Z_f - \frac{1}{16} Z_0 Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \leq 1$ & $\frac{5}{8} Z_f - \frac{1}{4} Z_4 Z_f - \frac{1}{4} Z_3 Z_f - \frac{1}{8} Z_3 Z_4 Z_f - \frac{1}{4} Z_2 Z_f - \frac{1}{8} Z_2 Z_4 Z_f - \frac{1}{8} Z_2 Z_3 Z_f - \frac{1}{4} Z_1 Z_f - \frac{1}{8} Z_1 Z_4 Z_f - \frac{1}{8} Z_1 Z_3 Z_f - \frac{1}{8} Z_1 Z_2 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_4 Z_f - \frac{1}{4} Z_0 Z_f - \frac{1}{8} Z_0 Z_4 Z_f - \frac{1}{8} Z_0 Z_3 Z_f - \frac{1}{8} Z_0 Z_2 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f + \frac{1}{4} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \leq 2$ & $ - \frac{3}{8} Z_4 Z_f - \frac{3}{8} Z_3 Z_f - \frac{3}{8} Z_2 Z_f + \frac{1}{8} Z_2 Z_3 Z_4 Z_f - \frac{3}{8} Z_1 Z_f + \frac{1}{8} Z_1 Z_3 Z_4 Z_f + \frac{1}{8} Z_1 Z_2 Z_4 Z_f + \frac{1}{8} Z_1 Z_2 Z_3 Z_f - \frac{3}{8} Z_0 Z_f + \frac{1}{8} Z_0 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_2 Z_4 Z_f + \frac{1}{8} Z_0 Z_2 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_3 Z_f + \frac{1}{8} Z_0 Z_1 Z_2 Z_f - \frac{3}{8} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \leq 3$ & $ - \frac{5}{8} Z_f - \frac{1}{4} Z_4 Z_f - \frac{1}{4} Z_3 Z_f + \frac{1}{8} Z_3 Z_4 Z_f - \frac{1}{4} Z_2 Z_f + \frac{1}{8} Z_2 Z_4 Z_f + \frac{1}{8} Z_2 Z_3 Z_f - \frac{1}{4} Z_1 Z_f + \frac{1}{8} Z_1 Z_4 Z_f + \frac{1}{8} Z_1 Z_3 Z_f + \frac{1}{8} Z_1 Z_2 Z_f - \frac{1}{8} Z_1 Z_2 Z_3 Z_4 Z_f - \frac{1}{4} Z_0 Z_f + \frac{1}{8} Z_0 Z_4 Z_f + \frac{1}{8} Z_0 Z_3 Z_f + \frac{1}{8} Z_0 Z_2 Z_f - \frac{1}{8} Z_0 Z_2 Z_3 Z_4 Z_f + \frac{1}{8} Z_0 Z_1 Z_f - \frac{1}{8} Z_0 Z_1 Z_3 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_4 Z_f - \frac{1}{8} Z_0 Z_1 Z_2 Z_3 Z_f + \frac{1}{4} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \leq 4$ & $ - \frac{15}{16} Z_f - \frac{1}{16} Z_4 Z_f - \frac{1}{16} Z_3 Z_f + \frac{1}{16} Z_3 Z_4 Z_f - \frac{1}{16} Z_2 Z_f + \frac{1}{16} Z_2 Z_4 Z_f + \frac{1}{16} Z_2 Z_3 Z_f - \frac{1}{16} Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_1 Z_f + \frac{1}{16} Z_1 Z_4 Z_f + \frac{1}{16} Z_1 Z_3 Z_f - \frac{1}{16} Z_1 Z_3 Z_4 Z_f + \frac{1}{16} Z_1 Z_2 Z_f - \frac{1}{16} Z_1 Z_2 Z_4 Z_f - \frac{1}{16} Z_1 Z_2 Z_3 Z_f + \frac{1}{16} Z_1 Z_2 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_f + \frac{1}{16} Z_0 Z_4 Z_f + \frac{1}{16} Z_0 Z_3 Z_f - \frac{1}{16} Z_0 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_2 Z_f - \frac{1}{16} Z_0 Z_2 Z_4 Z_f - \frac{1}{16} Z_0 Z_2 Z_3 Z_f + \frac{1}{16} Z_0 Z_2 Z_3 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_f - \frac{1}{16} Z_0 Z_1 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_3 Z_f + \frac{1}{16} Z_0 Z_1 Z_3 Z_4 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_4 Z_f + \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_f - \frac{1}{16} Z_0 Z_1 Z_2 Z_3 Z_4 Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 + x_4 \leq 5$ & $ -  Z_f$ \\
\hline
$x_0 \leq 2$ & $ -  Z_f$ \\
\hline
$x_0 \leq 3$ & $ -  Z_f$ \\
\hline
$x_0 \leq 4$ & $ -  Z_f$ \\
\hline
$x_0 \leq 5$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 \leq 3$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 \leq 4$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 \leq 5$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 \leq 4$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 \leq 5$ & $ -  Z_f$ \\
\hline
$x_0 + x_1 + x_2 + x_3 \leq 5$ & $ -  Z_f$ \\
\hline
\end{tabular}
```

## File: results/qubos.csv
```
(1, 0); -2*x_0; [[-2]]
(1, 1); -4*x_0; [[-4]]
(1, 2); ; [[0]]
(1, 3); 1*x_0; [[1]]
(1, 4); 3*x_0; [[3]]
(1, 5); 1*x_0; [[1]]
(1, 6); -1*x_0; [[-1]]
(1, 7); 4*x_0; [[4]]
(1, 8); ; [[0]]
(1, 9); 4*x_0; [[4]]
(2, 0); 2*x_0 + 2*x_0 x_1 + 3*x_1; [[2, 2], [0, 3]]
(2, 1); -4*x_0 + -3*x_0 x_1 + 4*x_1; [[-4, -3], [0, 4]]
(2, 2); -5*x_0 + -4*x_0 x_1 + 1*x_1; [[-5, -4], [0, 1]]
(2, 3); 2*x_0 + -1*x_0 x_1 + 1*x_1; [[2, -1], [0, 1]]
(2, 4); 3*x_0 + 2*x_0 x_1 + 3*x_1; [[3, 2], [0, 3]]
(2, 5); 3*x_0 + 1*x_0 x_1 + 4*x_1; [[3, 1], [0, 4]]
(2, 6); 2*x_0 + -1*x_0 x_1 + -5*x_1; [[2, -1], [0, -5]]
(2, 7); -2*x_0 + 2*x_0 x_1; [[-2, 2], [0, 0]]
(2, 8); -2*x_0 x_1; [[0, -2], [0, 0]]
(2, 9); -4*x_0 + -5*x_0 x_1 + -5*x_1; [[-4, -5], [0, -5]]
(3, 0); 4*x_0 + -5*x_0 x_1 + 4*x_0 x_2 + -2*x_1 + 3*x_1 x_2; [[4, -5, 4], [0, -2, 3], [0, 0, 0]]
(3, 1); -5*x_0 + -4*x_0 x_1 + -1*x_0 x_2 + -2*x_1 + 2*x_1 x_2 + -2*x_2; [[-5, -4, -1], [0, -2, 2], [0, 0, -2]]
(3, 2); 2*x_0 + -5*x_0 x_1 + -5*x_0 x_2 + 3*x_1 + -2*x_1 x_2 + -2*x_2; [[2, -5, -5], [0, 3, -2], [0, 0, -2]]
(3, 3); -2*x_0 x_1 + 1*x_0 x_2 + 2*x_1 + -4*x_1 x_2 + -4*x_2; [[0, -2, 1], [0, 2, -4], [0, 0, -4]]
(3, 4); -3*x_0 + -3*x_0 x_1 + -1*x_1 + 4*x_1 x_2; [[-3, -3, 0], [0, -1, 4], [0, 0, 0]]
(3, 5); 2*x_0 + 4*x_0 x_1 + 2*x_0 x_2 + -5*x_1 + 3*x_2; [[2, 4, 2], [0, -5, 0], [0, 0, 3]]
(3, 6); -5*x_0 + -5*x_0 x_1 + 2*x_0 x_2 + -3*x_1 + -4*x_1 x_2 + -1*x_2; [[-5, -5, 2], [0, -3, -4], [0, 0, -1]]
(3, 7); -1*x_0 + -2*x_0 x_1 + -3*x_0 x_2 + 2*x_1 + 4*x_1 x_2 + -2*x_2; [[-1, -2, -3], [0, 2, 4], [0, 0, -2]]
(3, 8); -4*x_0 + -4*x_0 x_2 + -3*x_1 + 2*x_1 x_2 + 4*x_2; [[-4, 0, -4], [0, -3, 2], [0, 0, 4]]
(3, 9); -3*x_0 + 4*x_0 x_1 + -3*x_0 x_2 + 1*x_1 + 3*x_1 x_2 + -1*x_2; [[-3, 4, -3], [0, 1, 3], [0, 0, -1]]
(4, 0); -1*x_0 + -3*x_0 x_1 + -2*x_0 x_2 + -1*x_0 x_3 + -1*x_1 x_2 + 4*x_1 x_3 + -3*x_2 x_3 + -5*x_3; [[-1, -3, -2, -1], [0, 0, -1, 4], [0, 0, 0, -3], [0, 0, 0, -5]]
(4, 1); -4*x_0 + 1*x_0 x_1 + 1*x_0 x_2 + 2*x_0 x_3 + -3*x_1 + 3*x_1 x_2 + 2*x_1 x_3 + -1*x_2 + -3*x_2 x_3 + -2*x_3; [[-4, 1, 1, 2], [0, -3, 3, 2], [0, 0, -1, -3], [0, 0, 0, -2]]
(4, 2); -1*x_0 + -1*x_0 x_1 + 2*x_0 x_2 + -1*x_1 + -3*x_1 x_2 + 4*x_1 x_3 + 2*x_2 + 4*x_2 x_3 + 3*x_3; [[-1, -1, 2, 0], [0, -1, -3, 4], [0, 0, 2, 4], [0, 0, 0, 3]]
(4, 3); 2*x_0 + 1*x_0 x_1 + 2*x_0 x_2 + 4*x_0 x_3 + -3*x_1 + 2*x_1 x_2 + 3*x_1 x_3 + 1*x_2 + -5*x_2 x_3 + 3*x_3; [[2, 1, 2, 4], [0, -3, 2, 3], [0, 0, 1, -5], [0, 0, 0, 3]]
(4, 4); -3*x_0 + 2*x_0 x_1 + -5*x_0 x_2 + -4*x_0 x_3 + 2*x_1 + 4*x_1 x_2 + -2*x_1 x_3 + -4*x_2 + -1*x_2 x_3 + -1*x_3; [[-3, 2, -5, -4], [0, 2, 4, -2], [0, 0, -4, -1], [0, 0, 0, -1]]
(4, 5); -3*x_0 + -1*x_0 x_1 + 2*x_0 x_2 + -1*x_1 + -5*x_1 x_2 + -2*x_1 x_3 + 4*x_2 + 3*x_2 x_3 + 4*x_3; [[-3, -1, 2, 0], [0, -1, -5, -2], [0, 0, 4, 3], [0, 0, 0, 4]]
(4, 6); 2*x_0 + 4*x_0 x_1 + -4*x_0 x_2 + -3*x_0 x_3 + 2*x_1 + 1*x_1 x_2 + -1*x_2 x_3 + -4*x_3; [[2, 4, -4, -3], [0, 2, 1, 0], [0, 0, 0, -1], [0, 0, 0, -4]]
(4, 7); -4*x_0 x_1 + -4*x_0 x_2 + 3*x_0 x_3 + -3*x_1 + 4*x_1 x_2 + -1*x_1 x_3 + 4*x_2 + -5*x_3; [[0, -4, -4, 3], [0, -3, 4, -1], [0, 0, 4, 0], [0, 0, 0, -5]]
(4, 8); 4*x_0 + 4*x_0 x_1 + 4*x_0 x_2 + 4*x_0 x_3 + -5*x_1 + -2*x_1 x_2 + 4*x_1 x_3 + -1*x_2 + -5*x_2 x_3 + -4*x_3; [[4, 4, 4, 4], [0, -5, -2, 4], [0, 0, -1, -5], [0, 0, 0, -4]]
(4, 9); -4*x_0 + 3*x_0 x_1 + -5*x_0 x_2 + 4*x_0 x_3 + 2*x_1 + -2*x_1 x_2 + -2*x_1 x_3 + 1*x_2 + 4*x_2 x_3 + -2*x_3; [[-4, 3, -5, 4], [0, 2, -2, -2], [0, 0, 1, 4], [0, 0, 0, -2]]
(5, 0); -4*x_0 x_1 + -5*x_0 x_2 + 3*x_0 x_3 + -5*x_0 x_4 + -5*x_1 + -5*x_1 x_2 + -1*x_1 x_3 + 1*x_1 x_4 + 4*x_2 + -5*x_2 x_4 + -5*x_3 + -5*x_3 x_4 + 4*x_4; [[0, -4, -5, 3, -5], [0, -5, -5, -1, 1], [0, 0, 4, 0, -5], [0, 0, 0, -5, -5], [0, 0, 0, 0, 4]]
(5, 1); -5*x_0 + 3*x_0 x_1 + -3*x_0 x_2 + 1*x_0 x_3 + 4*x_0 x_4 + 3*x_1 + -3*x_1 x_3 + 1*x_2 + 1*x_2 x_3 + 3*x_2 x_4 + -5*x_3 + 1*x_3 x_4 + 3*x_4; [[-5, 3, -3, 1, 4], [0, 3, 0, -3, 0], [0, 0, 1, 1, 3], [0, 0, 0, -5, 1], [0, 0, 0, 0, 3]]
(5, 2); -1*x_0 + 4*x_0 x_1 + 4*x_0 x_2 + -4*x_0 x_4 + -2*x_1 + 3*x_1 x_3 + 2*x_1 x_4 + 2*x_2 + -4*x_2 x_3 + -1*x_2 x_4 + -3*x_3 + -1*x_3 x_4 + 2*x_4; [[-1, 4, 4, 0, -4], [0, -2, 0, 3, 2], [0, 0, 2, -4, -1], [0, 0, 0, -3, -1], [0, 0, 0, 0, 2]]
(5, 3); -1*x_0 + 1*x_0 x_1 + -5*x_0 x_3 + 1*x_0 x_4 + 4*x_1 + -1*x_1 x_2 + 2*x_1 x_4 + -2*x_2 x_3 + 4*x_2 x_4 + 1*x_3 + 4*x_3 x_4 + 2*x_4; [[-1, 1, 0, -5, 1], [0, 4, -1, 0, 2], [0, 0, 0, -2, 4], [0, 0, 0, 1, 4], [0, 0, 0, 0, 2]]
(5, 4); 1*x_0 + -2*x_0 x_1 + 2*x_0 x_2 + -5*x_0 x_3 + -4*x_0 x_4 + -2*x_1 + 2*x_1 x_2 + -5*x_1 x_3 + -2*x_1 x_4 + -3*x_2 + 4*x_2 x_3 + -2*x_2 x_4 + 3*x_3 x_4 + 3*x_4; [[1, -2, 2, -5, -4], [0, -2, 2, -5, -2], [0, 0, -3, 4, -2], [0, 0, 0, 0, 3], [0, 0, 0, 0, 3]]
(5, 5); -3*x_0 + -2*x_0 x_1 + 3*x_0 x_2 + 3*x_0 x_3 + 1*x_0 x_4 + -5*x_1 + -4*x_1 x_2 + -1*x_1 x_3 + -2*x_1 x_4 + -2*x_2 + -1*x_2 x_3 + -4*x_2 x_4 + -2*x_3 + -1*x_4; [[-3, -2, 3, 3, 1], [0, -5, -4, -1, -2], [0, 0, -2, -1, -4], [0, 0, 0, -2, 0], [0, 0, 0, 0, -1]]
(5, 6); -1*x_0 + -1*x_0 x_2 + -4*x_0 x_3 + 1*x_0 x_4 + 3*x_1 x_2 + 1*x_1 x_3 + 1*x_1 x_4 + -3*x_2 + -4*x_2 x_3 + 1*x_2 x_4 + 1*x_3 + 1*x_3 x_4 + 3*x_4; [[-1, 0, -1, -4, 1], [0, 0, 3, 1, 1], [0, 0, -3, -4, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 3]]
(5, 7); -4*x_0 + 3*x_0 x_2 + 3*x_0 x_3 + 3*x_0 x_4 + -2*x_1 + -4*x_1 x_2 + 1*x_1 x_3 + 1*x_1 x_4 + 1*x_2 + -3*x_2 x_3 + 1*x_2 x_4 + 1*x_3 + -4*x_3 x_4 + 3*x_4; [[-4, 0, 3, 3, 3], [0, -2, -4, 1, 1], [0, 0, 1, -3, 1], [0, 0, 0, 1, -4], [0, 0, 0, 0, 3]]
(5, 8); 1*x_0 + 4*x_0 x_1 + -4*x_0 x_2 + -3*x_0 x_4 + 2*x_1 x_2 + 2*x_1 x_3 + -5*x_1 x_4 + -5*x_2 + 1*x_2 x_4 + -2*x_3 + -3*x_3 x_4 + -4*x_4; [[1, 4, -4, 0, -3], [0, 0, 2, 2, -5], [0, 0, -5, 0, 1], [0, 0, 0, -2, -3], [0, 0, 0, 0, -4]]
(5, 9); -4*x_0 + 3*x_0 x_1 + 1*x_0 x_2 + -3*x_0 x_3 + 3*x_0 x_4 + -2*x_1 + -2*x_1 x_2 + -4*x_1 x_3 + 4*x_1 x_4 + -1*x_2 + 1*x_2 x_3 + -3*x_3 + 2*x_3 x_4 + -2*x_4; [[-4, 3, 1, -3, 3], [0, -2, -2, -4, 4], [0, 0, -1, 1, 0], [0, 0, 0, -3, 2], [0, 0, 0, 0, -2]]
```

## File: results/two_constraints_support_1.txt
```
['x_0 + x_1 + x_2 == 0', 'x_0 + x_3 + x_4 >= 2']
['x_0 + x_1 + x_2 >= 0', 'x_0 + x_3 + x_4 >= 1']
['x_0 + x_1 + x_2 <= 0', 'x_0 + x_3 + x_4 <= 1']
['x_0 + x_1 + x_2 <= 2', 'x_0 + x_3 + x_4 <= 2']
['x_0 + x_1 + x_2 >= 0', 'x_0 + x_3 + x_4 <= 2']
['x_0 + x_1 + x_2 >= 2', 'x_0 + x_3 + x_4 >= 3']
['x_0 + x_1 + x_2 <= 3', 'x_0 + x_3 + x_4 <= 1']
['x_0 + x_1 + x_2 == 1', 'x_0 + x_3 + x_4 <= 1']
['x_0 + x_1 + x_2 == 3', 'x_0 + x_3 + x_4 >= 3']
['x_0 + x_1 + x_2 == 1', 'x_0 + x_3 + x_4 == 2']
```

## File: results/two_constraints_support_2.txt
```
['x_0 + x_1 + x_2 + x_3 == 2', 'x_0 + x_3 + x_4 >= 0']
['x_0 + x_1 + x_2 + x_3 <= 0', 'x_0 + x_3 + x_4 == 0']
['x_0 + x_1 + x_2 + x_3 <= 4', 'x_0 + x_3 + x_4 <= 1']
['x_0 + x_1 + x_2 + x_3 >= 2', 'x_0 + x_3 + x_4 >= 0']
['x_0 + x_1 + x_2 + x_3 >= 2', 'x_0 + x_3 + x_4 <= 4']
['x_0 + x_1 + x_2 + x_3 <= 2', 'x_0 + x_3 + x_4 == 1']
['x_0 + x_1 + x_2 + x_3 >= 1', 'x_0 + x_3 + x_4 == 3']
['x_0 + x_1 + x_2 + x_3 == 1', 'x_0 + x_3 + x_4 >= 2']
['x_0 + x_1 + x_2 + x_3 == 4', 'x_0 + x_3 + x_4 >= 2']
['x_0 + x_1 + x_2 + x_3 <= 2', 'x_0 + x_3 + x_4 >= 0']
```

## File: results/two_constraints_support_3.txt
```
['x_0 + x_1 + x_2 + x_3 >= 4', 'x_0 + x_2 + x_3 + x_4 >= 4']
['x_0 + x_1 + x_2 + x_3 >= 1', 'x_0 + x_2 + x_3 + x_4 == 3']
['x_0 + x_1 + x_2 + x_3 <= 3', 'x_0 + x_2 + x_3 + x_4 >= 0']
['x_0 + x_1 + x_2 + x_3 <= 4', 'x_0 + x_2 + x_3 + x_4 <= 0']
['x_0 + x_1 + x_2 + x_3 >= 2', 'x_0 + x_2 + x_3 + x_4 == 2']
['x_0 + x_1 + x_2 + x_3 <= 1', 'x_0 + x_2 + x_3 + x_4 >= 1']
['x_0 + x_1 + x_2 + x_3 <= 1', 'x_0 + x_2 + x_3 + x_4 == 0']
['x_0 + x_1 + x_2 + x_3 >= 4', 'x_0 + x_2 + x_3 + x_4 >= 0']
['x_0 + x_1 + x_2 + x_3 >= 1', 'x_0 + x_2 + x_3 + x_4 <= 0']
['x_0 + x_1 + x_2 + x_3 >= 4', 'x_0 + x_2 + x_3 + x_4 >= 3']
```

## File: analyze_results.py
```python
import re
from matplotlib.patches import Patch
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')

#|%%--%%| <JT9SEL7RBJ|oRp6qeenrv>
r"""°°°
Single Constraint Data
°°°"""
#|%%--%%| <oRp6qeenrv|fQnYovfAXO>


ops = {'equals': '==', 'geq': '>=', 'leq': '<='}


def calculate_probability_optimal(counts: dict, outcomes: list):
    """
    Calculate the probability of getting the optimal solution from the counts.
    Args:
        counts (dict): The counts of the qubits.
        outcomes (list): The outcomes of the qubits.
    Returns:
        float: The probability of getting the optimal solution.
    """
    total_counts = sum(counts.values())
    tot_prob = 0
    for i, outcome in enumerate(outcomes):
        if outcome == -1:
            tot_prob += counts[list(counts.keys())[i]]
    return tot_prob / total_counts


def calculate_probability_optimal_qubo(counts: dict, optimal_x: list | None, n_c: int = 1, single_flag: bool = True):
    """
    Calculate the probability of getting the optimal solution from the counts.
    Args:
        counts (dict): The counts of the qubits.
        optimal_x (list): The optimal solution.
    Returns:
        float: The probability of getting the optimal solution.
    """
    if optimal_x is None:
        return -1
    if single_flag:
        n_c = 1
    total_counts = sum(counts.values())
    tot_prob = 0
    for i, outcome in enumerate(counts):
        if outcome[:-n_c] in optimal_x and outcome[-n_c:] == '0' * n_c:
            tot_prob += counts[outcome]
    return tot_prob / total_counts


def read_single_constraint_data(corp: str = '', results_dir: str = './alex/results/') -> pd.DataFrame:
    """
    Read the single constraint data from the results directory.
    Args:
        corp (str): The prefix of the file name.
        results_dir (str): The directory where the results are stored.
    Returns:
        pd.DataFrame: The single constraint data.
    """
    df = pd.DataFrame()
    for op in ops:
        if corp == '':
            #temp_df = pd.read_pickle(f'{results_dir}{corp}single_constraint_data_{op}.pkl')
            temp_df = pd.read_pickle(f'{results_dir}{corp}single_constraint_{op}.pkl')
            temp_df['problem'] = op
            temp_df['prob_opt'] = temp_df.apply(lambda x: calculate_probability_optimal(x['counts'], x['outcomes']), axis=1)
            temp_df['depth'] = temp_df['resources'].apply(lambda x: x.depth)
            temp_df['num_gates'] = temp_df['resources'].apply(lambda x: x.num_gates)
            temp_df['num_gates_2'] = temp_df['resources'].apply(lambda x: x.gate_sizes[2])
        elif corp == 'qubo_':
            temp_df = pd.read_pickle(f'{results_dir}{corp}single_constraint_{op}_1.pkl')
            # temp_df = pd.read_pickle(f'{results_dir}{corp}single_constraint_{op}_{}.pkl')
            temp_df['problem'] = op
            temp_df['constraints'] = temp_df['constraints'].apply(lambda x: [x])
            temp_df['prob_opt'] = temp_df.apply(lambda x: calculate_probability_optimal_qubo(x['counts'], x['optimal_x']), axis=1)
        # change 'AR' to float
        temp_df['AR'] = temp_df['AR'].apply(lambda x: np.float64(x))
        df = pd.concat([df, temp_df], ignore_index=True)
    return df


state_df = read_single_constraint_data()
qubo_df = read_single_constraint_data('qubo_')
#set the outcomes in qubo_df to the outcomes in state_df for the corresponding 'constraints'
qubo_df['outcomes'] = qubo_df['constraints'].apply(lambda x: state_df[state_df['constraints'].map(tuple) == tuple(x)]['outcomes'].values[0] if len(state_df[state_df['constraints'].map(tuple) == tuple(x)]) > 0 else None)
state_df = state_df[state_df['angle_strategy'] == 'ma-QAOA']
qubo_df = qubo_df[qubo_df['angle_strategy'] == 'ma-QAOA']


#|%%--%%| <fQnYovfAXO|DQ7E91yFUl>
r"""°°°
Plotting Functions for Single Constraint Data
°°°"""
#|%%--%%| <DQ7E91yFUl|4ADDj0liE4>


def plot_single_constraint_ar(df: pd.DataFrame, problem: str, hue='b', qubo: bool = False, moon: bool = True, confident: bool = False, save: bool = False, file: str | None = None) -> None:
    """
    Plot the approximation ratio vs number of variables for a given problem.
    Args:
        df (pd.DataFrame): The dataframe containing the data.
        problem (str): The problem to plot.
        hue (str): The column to use for the hue.
        qubo (bool): Whether to plot the qubo data or the state data.
        moon (bool): Whether to use the moon style or the dawn style.
        confident (bool): Whether to use the confident style or not.
        save (bool): Whether to save the plot or not.
        file (str): The name of the file to save the plot as.
    Returns:
        None
    """
    ops = {'equals': '=', 'geq': r'$\geq$', 'leq': r'$\leq$', 'less': '<', 'greater': '>'}
    plots_dir = 'alex/plots/'
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    if moon:
        plt.style.use('rose-pine-moon')
        colors = ['C0', 'C4', 'C2', 'C1', 'C3', 'C5']
    else:
        #plt.style.use('rose-pine-dawn')
        #colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
        plt.style.use("default")
        colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
    dff = df.copy()
    dff = dff[dff['problem'] == problem]
    dff['b'] = dff['constraints'].apply(lambda x: r'$b=$'+f'{x[0][-1]}')
    dff['constraints'] = dff['constraints'].map(tuple)
    fig = plt.figure(figsize=(15, 8))
    if qubo:
        ax = sns.boxplot(data=dff, x='n_x', y='AR', hue=hue, palette=colors)
    else:
        ax = sns.boxplot(data=dff, x='n_x', y='AR', hue=hue, palette=colors, fill=False, linewidth=5)

    if moon:
        plt.background = 'black'
        plt.xlabel('Number of variables: '+r'$n_x$', size=18)
        plt.ylabel('AR', size=18)
        plt.tick_params(axis='both', labelsize=18)
        plt.xticks([1, 2, 3, 4, 5])
        plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1), frameon=True, prop={'size': 12}, title=r'$\sum_{i=0}^{n_x - 1} x_i$' + f'{ops[problem]}' + r'$b$')  # , title='Number of Constraints/Layers')
        plt.title(f'{problem.capitalize()} Constraint Gadget vs AR', size=20)
        plt.tight_layout()
        if save:
            plt.savefig(f'{plots_dir}{problem}_AR_vs_n_x_moon.png')
        plt.show()
        plt.close()
    else:
        plt.background = 'white'
        plt.xlabel('Number of variables: '+r'$n_x$', size=20)
        plt.ylabel('AR', size=20)
        plt.xticks([0, 1, 2, 3, 4, 5])
        plt.tick_params(axis='both', labelsize=18)
        if qubo:
            # Build custom legend for hatch + color
            # legend_handles = []
            # seen = set()
            # for g in group_labels:
            #     hue = g.split('_')[0]
            #     layer = g.split('L')[1]
            #     label = r"$b=$" + f"{hue}"+r", $p=$" + f"{layer}"
            #     if label not in seen:
            #         legend_handles.append(Patch(facecolor=group_colors[g],
            #                                     hatch=group_to_hatch[g],
            #                                     edgecolor='black',
            #                                     label=label))
            #         seen.add(label)
            plt.title(f'QCBOs with {problem.capitalize()} Constraints vs Approximation Ratio', size=20)
            # plt.legend(handles=legend_handles, loc='upper right', bbox_to_anchor=(1.15, 1), frameon=True, prop={'size': 16}, title=r'$\sum_{i=0}^{n_x - 1} x_i$' + f'{ops[problem]}' + r'$b$', title_fontsize=18)  # , title='Number of Constraints/Layers')
            plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), frameon=True, prop={'size': 16}, title=r'$\sum_{i=0}^{n_x - 1} x_i$' + f'{ops[problem]}' + r'$b$', title_fontsize=18)  # , title='Number of Constraints/Layers')
        else:
            plt.title(f'{problem.capitalize()} Constraints vs Approximation Ratio', size=20)
            plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), frameon=True, prop={'size': 16}, title=r'$\sum_{i=0}^{n_x - 1} x_i$' + f'{ops[problem]}' + r'$b$', title_fontsize=18)  # , title='Number of Constraints/Layers')
        plt.tight_layout()
        ax.patch.set_facecolor('white')
        plt.rcParams['figure.facecolor'] = 'white'
        fig.patch.set_facecolor('white')
        if save:
            if file is not None:
                plt.savefig(f'{plots_dir}{file}_AR_dawn.png', facecolor='white')
            elif qubo:
                plt.savefig(f'{plots_dir}{problem}_qubo_AR_dawn.png', facecolor='white')
            else:
                plt.savefig(f'{plots_dir}{problem}_AR_dawn.png', facecolor='white')
        #plt.show()
        plt.close()


def plot_single_constraint_prob_opt(df: pd.DataFrame, problem: str, hue='b', qubo: bool = False, moon: bool = True, confident: bool = False, save: bool = False, file: str | None = None) -> None:
    """
    Plot the probability of optimal vs number of variables for a given problem.
    Args:
        df (pd.DataFrame): The dataframe containing the data.
        problem (str): The problem to plot.
        hue (str): The column to use for the hue.
        qubo (bool): Whether to plot the qubo data or the state data.
        moon (bool): Whether to use the moon style or the dawn style.
        confident (bool): Whether to use the confident style or not.
        save (bool): Whether to save the plot or not.
        file (str): The name of the file to save the plot as.
    Returns:
        None
    """
    ops = {'equals': '=', 'geq': r'$\geq$', 'leq': r'$\leq$', 'less': '<', 'greater': '>'}
    plots_dir = 'alex/plots/'
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    if moon:
        plt.style.use('rose-pine-moon')
        colors = ['C0', 'C4', 'C2', 'C1', 'C3', 'C5']
    else:
        #plt.style.use('rose-pine-dawn')
        #colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
        plt.style.use("default")
        colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
    dff = df.copy()
    dff = dff[dff['problem'] == problem]
    dff['b'] = dff['constraints'].apply(lambda x: r'$b=$'+f'{x[0][-1]}')
    dff['constraints'] = dff['constraints'].map(tuple)
    fig = plt.figure(figsize=(15, 8))
    if qubo:
        ax = sns.boxplot(data=dff, x='n_x', y='prob_opt', hue=hue, palette=colors)
    else:
        ax = sns.boxplot(data=dff, x='n_x', y='prob_opt', hue=hue, palette=colors, fill=False, linewidth=5)

    if moon:
        plt.background = 'black'
        plt.xlabel('Number of variables: '+r'$n_x$', size=18)
        plt.ylabel('AR', size=18)
        plt.xticks([1, 2, 3, 4, 5])
        plt.tick_params(axis='both', labelsize=18)
        plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1), frameon=True, prop={'size': 12}, title=r'$\sum_{i=0}^{n_x - 1} x_i$' + f'{ops[problem]}' + r'$b$')
        if qubo:
            plt.title(f'QCBOs with {problem.capitalize()} Constraints vs Probability of Optimal Solution', size=20)
        else:
            plt.title(f'{problem.capitalize()} Constraints vs Probability of Optimal Solution', size=20)
        plt.tight_layout()
        if save:
            if qubo:
                plt.savefig(f'{plots_dir}{problem}_qubo_prob_opt_vs_n_x_moon.png')
            else:
                plt.savefig(f'{plots_dir}{problem}_prob_opt_vs_n_x_moon.png')
        #plt.show()
        plt.close()
    else:
        plt.background = 'white'
        plt.xlabel('Number of variables: '+r'$n_x$', size=20)
        plt.ylabel('Probability of Optimal Solution', size=20)
        plt.xticks([0, 1, 2, 3, 4, 5])
        plt.tick_params(axis='both', labelsize=18)
        if qubo:
            # Build custom legend for hatch + color
            # legend_handles = []
            # seen = set()
            # for g in group_labels:
            #     hue = g.split('_')[0]
            #     layer = g.split('L')[1]
            #     label = r"$b=$" + f"{hue}"+r", $p=$" + f"{layer}"
            #     if label not in seen:
            #         legend_handles.append(Patch(facecolor=group_colors[g],
            #                                     hatch=group_to_hatch[g],
            #                                     edgecolor='black',
            #                                     label=label))
            #         seen.add(label)
            plt.title(f'QCBOs with {problem.capitalize()} Constraints vs Probability of Optimal Solution', size=20)
            # plt.legend(handles=legend_handles, loc='upper right', bbox_to_anchor=(1.15, 1), frameon=True, prop={'size': 16}, title=r'$\sum_{i=0}^{n_x - 1} x_i$' + f'{ops[problem]}' + r'$b$', title_fontsize=18)  # , title='Number of Constraints/Layers')
            plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), frameon=True, prop={'size': 16}, title=r'$\sum_{i=0}^{n_x - 1} x_i$' + f'{ops[problem]}' + r'$b$', title_fontsize=18)  # , title='Number of Constraints/Layers')
        else:
            plt.title(f'{problem.capitalize()} Constraints vs Probability of Optimal Solution', size=20)
            plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), frameon=True, prop={'size': 16}, title=r'$\sum_{i=0}^{n_x - 1} x_i$' + f'{ops[problem]}' + r'$b$', title_fontsize=18)  # , title='Number of Constraints/Layers')
        plt.tight_layout()
        ax.patch.set_facecolor('white')
        plt.rcParams['figure.facecolor'] = 'white'
        fig.patch.set_facecolor('white')
        if save:
            if file is not None:
                plt.savefig(f'{plots_dir}{file}_prob_opt_dawn.png', facecolor='white')
            elif qubo:
                plt.savefig(f'{plots_dir}{problem}_qubo_prob_opt_vs_n_x_dawn.png', facecolor='white')
            else:
                plt.savefig(f'{plots_dir}{problem}_prob_opt_vs_n_x_dawn.png', facecolor='white')

        #plt.show()
        plt.close()


def plot_single_constraint_counts(df: pd.DataFrame, constraint: list[str], problem: str, qubo: str | None = None, moon: bool = True, save: bool = False, file: str | None = None) -> None:
    """
    Plot the counts for a given constraint.
    Args:
        df (pd.DataFrame): The dataframe containing the data.
        constraint (list[str]): The constraint to plot.
        problem (str): The problem to plot.
        qubo (str | None): The qubo string to plot. If None, plot all qubo strings.
        moon (bool): Whether to use the moon style or the dawn style.
        save (bool): Whether to save the plot or not.
        file (str | None): The name of the file to save the plot as.
    Returns:
        None
    """
    plots_dir = 'alex/plots/'
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    if moon:
        plt.style.use('rose-pine-moon')
        colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
        outcome_color = 'C1'
    else:
        #plt.style.use('rose-pine-dawn')
        #colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
        plt.style.use("default")
        colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
    dff = df.copy()
    dff = dff[dff['constraints'].map(tuple) == tuple(constraint)]
    outcomes = dff['outcomes'].iloc[0]
    outcomes = [f'{i:0{dff["n_x"].iloc[0]+dff['n_c'].iloc[0]}b}' for i, o in enumerate(outcomes) if o == -1]
    if qubo is not None:
        dff = dff[dff['qubo_string'] == qubo]
        optimal = dff['optimal_x'].iloc[0]
        if optimal is not None:
            optimal = [f'{o}{'0'*dff["n_c"].iloc[0]}' for o in optimal]
    else:
        optimal = None
    dff['keys'] = dff['counts'].apply(lambda x: list(x.keys()))
    dff = dff.explode('keys')
    dff['values'] = dff.apply(lambda x: x['counts'][x['keys']], axis=1)

    fig = plt.figure(figsize=(15, 8), facecolor='white')
    # ax = sns.barplot(data=dff, x='keys', y='values', hue='type', palette=colors)
    ax = sns.barplot(data=dff, x='keys', y='values', hue='angle_strategy', palette=colors)
    labels = []
    colors = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        if optimal is not None and text in optimal:
            labels.append(r'$\mathbf{|'+text+r'\rangle}$')
            colors.append('blue')
        elif text in outcomes:
            labels.append(r'$|'+text+r'\rangle$')
            colors.append('blue')
        else:
            labels.append(r'$|'+text+r'\rangle$')
            colors.append('red')
    ax.set_xticklabels(labels, fontsize=18)
    for tick_label, color in zip(ax.get_xticklabels(), colors):
        tick_label.set_color(color)
    if moon:
        # plot vertical lines of indices of outcomes (in binary strings) that are 0
        plt.background = 'black'
        plt.xlabel('States', size=18)
        plt.ylabel('Counts', size=18)
        plt.tick_params(axis='both', labelsize=18)
        plt.tight_layout()
        if save:
            plt.savefig(f'{plots_dir}{problem}_prob_opt_vs_n_x_moon.png')
        #plt.show()
        plt.close()
    else:
        plt.xlabel('States: ' + r'$|'+' '.join([f'x_{i}' for i in range(dff["n_x"].iloc[0])]) + ' '.join([f'v_{i}' for i in range(dff['n_c'].iloc[0])]) + r' \rangle$', size=18)
        plt.ylabel('Counts', size=18)
        plt.tick_params(axis='both', labelsize=18)
        plt.xticks(rotation=90)
        plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), frameon=True, prop={'size': 18}, title='Constraint\nGadget', title_fontsize=18)

        def _latex_constraint(constraint):
            constraint = constraint.replace('<=', '\leq')
            constraint = constraint.replace('>=', '\geq')
            constraint = constraint.replace('==', '=')
            constraint = constraint.replace('*', '')
            return constraint

        qubo_title = ''
        if qubo is not None:
            qubo_title = r'QUBO: $' + _latex_constraint(qubo) + r'$' + '\n'
        plt.title(f'{qubo_title}' + r'Constraints $'+f'{', '.join([_latex_constraint(c) for c in constraint])}'+r'$ vs counts', size=20)
        ax.patch.set_facecolor('white')
        plt.rcParams['figure.facecolor'] = 'white'
        fig.patch.set_facecolor('white')
        plt.tight_layout()
        if save:
            if file is not None:
                plt.savefig(f'{plots_dir}{file}_counts_dawn.png', facecolor='white')
            elif qubo is None:
                plt.savefig(f'{plots_dir}alex_constr_vs_{df[df["constraints"].map(tuple) == tuple(constraint)].index[0]}_counts_dawn.png', facecolor='white')
            else:
                plt.savefig(f'{plots_dir}alex_qubo_vs_{df[df["constraints"].map(tuple) == tuple(constraint)].index[0]}_counts_dawn.png', facecolor='white')
        #plt.show()
        plt.close()


qubo_df = qubo_df[qubo_df['n_layers'] == 1]
for problem in ['equals', 'leq', 'geq']:
    plot_single_constraint_ar(state_df, problem, hue='b', qubo=False, moon=False, confident=False, save=True)
    plot_single_constraint_ar(qubo_df, problem, hue='b', qubo=True, moon=False, confident=False, save=True)
    plot_single_constraint_prob_opt(state_df, problem, hue='b', qubo=False, moon=False, confident=False, save=True)
    plot_single_constraint_prob_opt(qubo_df, problem, hue='b', qubo=True, moon=False, confident=False, save=True)

#|%%--%%| <4ADDj0liE4|O4Et9M9NAy>
r"""°°°
Two Constraint Data
°°°"""
#|%%--%%| <O4Et9M9NAy|qOL3rDxKxP>


def read_two_constraint_data(corp: str = '', results_dir: str = './alex/results/') -> pd.DataFrame:
    """
    Read the two constraint data from the results directory.
    This data is for n_layers = 1 of the GM-QAOA circuit.
    Args:
        corp (str): The prefix of the file name.
        results_dir (str): The directory where the results are stored.
    Returns:
        pd.DataFrame: The two constraint data.
    """
    df = pd.DataFrame()
    for support in [1, 2, 3]:
        for single in [True, False]:
            temp_df = pd.read_pickle(f'{results_dir}{corp}two_constraint_support_{support}_single_{single}.pkl')
            if corp == '':
                temp_df['prob_opt'] = temp_df.apply(lambda x: calculate_probability_optimal(x['counts'], x['outcomes']), axis=1)
                temp_df['depth'] = temp_df['resources'].apply(lambda x: x.depth)
                temp_df['num_gates'] = temp_df['resources'].apply(lambda x: x.num_gates)
                temp_df['num_gates_2'] = temp_df['resources'].apply(lambda x: x.gate_sizes[2])
            elif corp == 'qubo_':
                temp_df['constraints'] = temp_df['constraints'].apply(lambda x: [x])
                temp_df['prob_opt'] = temp_df.apply(lambda x: calculate_probability_optimal_qubo(x['counts'], x['optimal_x'], x['n_c'], x['single_flag']), axis=1)
            temp_df['support'] = support
            temp_df['AR'] = temp_df['AR'].astype(float)
            df = pd.concat([df, temp_df], ignore_index=True)
    return df


def read_two_constraint_data_2(corp='qubo_', results_dir: str = './alex/results/') -> pd.DataFrame:
    """
    Read the two constraint data from the results directory.
    This data is for n_layers = 2 of the GM-QAOA circuit.
    Args:
        corp (str): The prefix of the file name.
        results_dir (str): The directory where the results are stored.
    Returns:
        pd.DataFrame: The two constraint data.
    """
    df = pd.DataFrame()
    for support in [1, 2, 3]:
        for single in [True, False]:
            temp_df = pd.read_pickle(f'{results_dir}{corp}two_constraint_support_{support}_single_{single}_n_layers_2.pkl')
            if corp == '':
                temp_df['prob_opt'] = temp_df.apply(lambda x: calculate_probability_optimal(x['counts'], x['outcomes']), axis=1)
                temp_df['depth'] = temp_df['resources'].apply(lambda x: x.depth)
                temp_df['num_gates'] = temp_df['resources'].apply(lambda x: x.num_gates)
                temp_df['num_gates_2'] = temp_df['resources'].apply(lambda x: x.gate_sizes[2])
            elif corp == 'qubo_':
                temp_df['constraints'] = temp_df['constraints'].apply(lambda x: [x])
                temp_df['prob_opt'] = temp_df.apply(lambda x: calculate_probability_optimal_qubo(x['counts'], x['optimal_x'], x['n_c'], x['single_flag']), axis=1)
            temp_df['support'] = support
            temp_df['AR'] = temp_df['AR'].astype(float)
            df = pd.concat([df, temp_df], ignore_index=True)
    return df


two_state_df = read_two_constraint_data()
two_qubo_df = read_two_constraint_data('qubo_')
two_state_df = two_state_df[two_state_df['angle_strategy'] == 'ma-QAOA']
two_qubo_df = two_qubo_df[two_qubo_df['angle_strategy'] == 'ma-QAOA']
two_qubo_df_2 = read_two_constraint_data_2('qubo_')
two_qubo_df = pd.concat([two_qubo_df, two_qubo_df_2], ignore_index=True)


#|%%--%%| <qOL3rDxKxP|Dx2d0inCcb>
r"""°°°
Plotting Functions for Two Constraint Data
°°°"""
#|%%--%%| <Dx2d0inCcb|sFN4tWGzAb>


def plot_two_constraint_prob_opt(df: pd.DataFrame, hue='single_flag', qubo: bool = False, moon: bool = True, confident: bool = False, save: bool = False, file: str | None = None) -> None:
    """
    Plot the probability of optimal vs support of the constraints for two overlapping constraints.
    Args:
        df (pd.DataFrame): The dataframe containing the data.
        hue (str): The column to use for the hue.
        qubo (bool): Whether to plot the qubo data or the state data.
        moon (bool): Whether to use the moon style or the dawn style.
        confident (bool): Whether to use the confident style or not.
        save (bool): Whether to save the plot or not.
        file (str | None): The name of the file to save the plot as.
    Returns:
        None
    """
    plots_dir = 'alex/plots/'
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    if moon:
        plt.style.use('rose-pine-moon')
        colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
    else:
        plt.style.use('rose-pine-dawn')
        colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
    dff = df.copy()
    dff[hue] = dff[hue].astype(str)
    dff['constraints'] = dff['constraints'].map(tuple)
    dff['group'] = dff[hue].astype(str) + '_L' + dff['n_layers'].astype(str)
    group_labels = sorted(dff['group'].unique())
    hatch_map = {'1': '', '2': '//'}
    group_to_hatch = {g: hatch_map[g.split('L')[1]] for g in group_labels}
    base_colors = {'True': 'C0', "False": 'C5'}
    group_colors = {g: base_colors[g.split('_')[0]] for g in group_labels}
    hatches = np.repeat(['', '', '//', '//'], 3)

    fig = plt.figure(figsize=(15, 8))
    if qubo:
        ax = sns.boxplot(data=dff, x='support', y='prob_opt', hue='group', palette=group_colors)
        for bar, hatch in zip(ax.patches, hatches):
            bar.set_hatch(hatch)
            plt.draw()
    else:
        ax = sns.boxplot(data=dff, x='support', y='prob_opt', hue=hue, palette=colors)
    if moon:
        plt.background = 'black'
        plt.xlabel('Support of the Constraints', size=18)
        plt.ylabel('Probability of Optimal', size=18)
        plt.xticks([1, 2, 3])
        plt.tick_params(axis='both', labelsize=18)
        plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1), frameon=True, prop={'size': 12})  # , title=)  # , title='Number of Constraints/Layers')
        if qubo:
            plt.title('QCBOs with Two Overlapping Constraints vs Probability of Optimal Solution', size=20)
        else:
            plt.title('Two Overlapping Constraints vs Probability of Optimal Solution', size=20)
        plt.tight_layout()
        if save:
            if qubo:
                plt.savefig(f'{plots_dir}{hue}_qubo_prob_opt_vs_n_x_moon.png')
            else:
                plt.savefig(f'{plots_dir}{hue}_prob_opt_vs_n_x_moon.png')
        #plt.show()
        plt.close()
    else:
        plt.background = 'white'
        plt.xlabel('Support of the Constraints', size=18)
        plt.ylabel('Probability of Optimal', size=18)
        plt.xticks(ticks=[0, 1, 2, 3])
        plt.tick_params(axis='both', labelsize=14)

        if qubo:
            # Build custom legend for hatch + color
            legend_handles = []
            seen = set()
            for g in group_labels:
                hue = g.split('_')[0]
                layer = g.split('L')[1]
                label = f"{hue}"+r", $p=$" + f"{layer}"
                if label not in seen:
                    legend_handles.append(Patch(facecolor=group_colors[g],
                                                hatch=group_to_hatch[g],
                                                edgecolor='black',
                                                label=label))
                    seen.add(label)

            ax.legend(handles=legend_handles, title=r'(Single Flag, $p$ layers)', bbox_to_anchor=(.85, 1), loc='upper left', prop={'size': 14}, title_fontsize=16)
            plt.title('QCBOs with Two Overlapping Constraints vs Probability of Optimal Solution', size=20)
        else:
            plt.legend(loc='upper right', bbox_to_anchor=(.95, 1), frameon=True, prop={'size': 14}, title='Use of Single\nFlag Qubit', title_fontsize=14)
            plt.title('Two Overlapping Constraints vs Probability of Optimal Solution', size=20)
        plt.tight_layout()
        plt.rcParams['figure.facecolor'] = 'white'
        fig.patch.set_facecolor('white')
        ax.patch.set_facecolor('white')
        if save:
            if file is not None:
                plt.savefig(f'{plots_dir}{file}_prob_opt_dawn.png', facecolor='white')
            elif qubo:
                plt.savefig(f'{plots_dir}two_qubo_vs_support_prob_opt_dawn.png', facecolor='white')
            else:
                plt.savefig(f'{plots_dir}two_constr_vs_support_prob_opt_dawn.png', facecolor='white')

        #plt.show()
        plt.close()


def plot_two_constraint_ar(df: pd.DataFrame, hue='single_flag', qubo: bool = False, moon: bool = True, confident: bool = False, save: bool = False, file: str | None = None) -> None:
    """
    Plot the approximation ratio vs support of the constraints for two overlapping constraints.
    Args:
        df (pd.DataFrame): The dataframe containing the data.
        hue (str): The column to use for the hue.
        qubo (bool): Whether to plot the qubo data or the state data.
        moon (bool): Whether to use the moon style or the dawn style.
        confident (bool): Whether to use the confident style or not.
        save (bool): Whether to save the plot or not.
        file (str | None): The name of the file to save the plot as.
    Returns:
        None
    """
    plots_dir = 'alex/plots/'
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    if moon:
        plt.style.use('rose-pine-moon')
        colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
    else:
        #plt.style.use('rose-pine-dawn')
        #colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']
        plt.style.use("default")
        colors = ['C0', 'C5', 'C2', 'C1', 'C3', 'C4']

        
    dff = df.copy()
    dff[hue] = dff[hue].astype(str)
    dff['constraints'] = dff['constraints'].map(tuple)
    dff['group'] = dff['single_flag'].astype(str) + '_L' + dff['n_layers'].astype(str)
    group_labels = sorted(dff['group'].unique())
    hatch_map = {'1': '', '2': '//'}
    group_to_hatch = {g: hatch_map[g.split('L')[1]] for g in group_labels}
    base_colors = {'True': 'C0', "False": 'C5'}
    group_colors = {g: base_colors[g.split('_')[0]] for g in group_labels}
    hatches = np.repeat(['', '', '//', '//'], 3)

    fig = plt.figure(figsize=(15, 8))
    if qubo:
        ax = sns.boxplot(data=dff, x='support', y='AR', hue='group', palette=group_colors)
        for bar, hatch in zip(ax.patches, hatches):
            bar.set_hatch(hatch)
            plt.draw()
    else:
        ax = sns.boxplot(data=dff, x='support', y='AR', hue=hue, palette=colors)
    if moon:
        plt.background = 'black'
        plt.xlabel('Support of the Constraints', size=18)
        plt.ylabel('AR', size=18)
        plt.xticks([1, 2, 3])
        plt.tick_params(axis='both', labelsize=18)
        plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1), frameon=True, prop={'size': 12})
        if qubo:
            plt.title('QCBOs with Two Overlapping Constraints vs AR', size=20)
        else:
            plt.title('Two Overlapping Constraints vs AR', size=20)
        plt.tight_layout()
        if save:
            if qubo:
                plt.savefig(f'{plots_dir}{hue}_qubo_AR_vs_n_x_moon.png')
            else:
                plt.savefig(f'{plots_dir}{hue}_AR_vs_n_x_moon.png')
        plt.show()
        plt.close()
    else:
        plt.background = 'white'
        plt.xlabel('Support of the Constraints', size=18)
        plt.ylabel('AR', size=18)
        plt.xticks(ticks=[0, 1, 2, 3])
        plt.tick_params(axis='both', labelsize=14)

        if qubo:
            # Build custom legend for hatch + color
            legend_handles = []
            seen = set()
            for g in group_labels:
                hue = g.split('_')[0]
                layer = g.split('L')[1]
                label = f"{hue}"+r", $p=$" + f"{layer}"
                if label not in seen:
                    legend_handles.append(Patch(facecolor=group_colors[g],
                                                hatch=group_to_hatch[g],
                                                edgecolor='black',
                                                label=label))
                    seen.add(label)

            ax.legend(handles=legend_handles, title=r'(Single Flag, $p$ layers)', bbox_to_anchor=(.85, 1), loc='upper left', prop={'size': 14}, title_fontsize=16)
            plt.title('QCBOs with Two Overlapping Constraints vs Approximation Ratio', size=20)
        else:
            plt.legend(loc='upper right', bbox_to_anchor=(.95, 1), frameon=True, prop={'size': 14}, title='Use of Single\nFlag Qubit', title_fontsize=14)
            plt.title('Two Overlapping Constraints vs Approximation Ratio', size=20)
        plt.tight_layout()
        ax.patch.set_facecolor('white')
        plt.rcParams['figure.facecolor'] = 'white'
        fig.patch.set_facecolor('white')
        if save:
            if file is not None:
                plt.savefig(f'{plots_dir}{file}_AR_dawn.png', facecolor='white')
            elif qubo:
                plt.savefig(f'{plots_dir}two_qubo_vs_support_AR_dawn.png', facecolor='white')
            else:
                plt.savefig(f'{plots_dir}two_constr_vs_support_AR_dawn.png', facecolor='white')

        #plt.show()
        plt.close()


plot_two_constraint_prob_opt(two_state_df, hue='single_flag', qubo=False, moon=False, confident=False, save=True)
plot_two_constraint_ar(two_state_df, hue='single_flag', qubo=False, moon=False, confident=False, save=True)
plot_two_constraint_prob_opt(two_qubo_df, hue='single_flag', qubo=True, moon=False, confident=False, save=True)
plot_two_constraint_ar(two_qubo_df, hue='single_flag', qubo=True, moon=False, confident=True, save=True)

#|%%--%%| <sFN4tWGzAb|2p6LZG66oa>
r"""°°°
Hamiltonian LaTeX Table
°°°"""
#|%%--%%| <2p6LZG66oa|85lclkFh7q>

state_hams_eq = state_df[(state_df['problem'] == 'equals') & (state_df['angle_strategy'] == 'ma-QAOA')][['constraints', 'Hamiltonian']]


def write_hamiltonian_latex_table(df, file_name, results_dir='./alex/results/'):
    with open(f'{results_dir}{file_name}', 'w') as f:
        f.write('\\begin{tabular}{|c|l|}\n')
        f.write('\\hline\n')
        f.write('\\textbf{Constraints} & \\textbf{Hamiltonian} \\\\\n')
        f.write('\\hline\n')
        for i, row in df.iterrows():
            constraints = row['constraints']
            hamiltonian = row['Hamiltonian']
            flag_qubit = max(hamiltonian.wires)
            constraints_str = constraints[0]
            # remove ' and 1 * from the string, change == to =
            constraints_str = constraints_str.replace('\'', '').replace('1*', '')
            constraints_str = constraints_str.replace('==', '=')
            constraints_str = constraints_str.replace('>=', r'\geq')
            constraints_str = constraints_str.replace('<=', r'\leq')
            print(constraints_str)

            # convert Hamiltonian to LaTeX format, remove *, change (\d) to _\d using regex, remove @, and convert any decimal to its corresponding fraction using (float).as_integer_ratio() and formatting that as \frac{num}{den}
            ham_str = ''
            for i, t in enumerate(zip(hamiltonian.coeffs, hamiltonian.ops)):
                c = t[0]
                o = t[1]
                c = c.numpy().as_integer_ratio()
                if c[1] == 1 and np.abs(c[0]) != 1:
                    c_str = str(np.abs(c[0]))
                elif c[1] == 1 and np.abs(c[0]) == 1:
                    c_str = ''
                else:
                    c_str = f'\\frac{{{np.abs(c[0])}}}{{{c[1]}}}'
                if c[0] < 0:
                    c_str = ' - ' + c_str
                elif c[0] > 0 and i != 0:
                    c_str = ' + ' + c_str

                o_str = str(o)
                o_str = re.sub(r'\((\d)\)', r'_\1', o_str)
                # find max _\d and replace it with _f
                o_str = re.sub(f'_{flag_qubit}', '_f', o_str)
                o_str = o_str.replace(' @', '')

                ham_str += f'{c_str} {o_str}'
                print(ham_str)

            f.write(f'${constraints_str}$ & ${ham_str}$ \\\\\n')
            f.write('\\hline\n')
        f.write('\\end{tabular}\n')


ops = {'equals': '$=$', 'leq': r'$\leq$', 'less': '$<$', 'geq': r'$\geq$', 'greater': '$>$'}
for op in ops:
    op_df = state_df[(state_df['problem'] == op) & (state_df['angle_strategy'] == 'ma-QAOA')][['constraints', 'Hamiltonian']]
    write_hamiltonian_latex_table(op_df, f'cqaoa_hamiltonian_table_{op}.tex')
```

## File: automate.py
```python
import subprocess
import os

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
```

## File: constraint_qaoa.py
```python
import re
import pennylane as qml
from pennylane import numpy as np
import pandas as pd
import itertools as it
import time


class ConstraintQAOA:
    """
    A class to implement the Constraint QAOA or Constraint Gadget algorithm.
    This class constructs a QAOA circuit to handle constraints in optimization problems.
    The gadget takes a list of constraints, flag wires, and various parameters to set up the QAOA circuit.
    Attributes:
        constraints (list[str]): A list of constraint strings.
        flag_wires (list[int]): A list of wires to be used as flag qubits.
        angle_strategy (str): The strategy for angle optimization ("ma-QAOA" or "QAOA").
        decompose (bool): Whether to decompose the Hamiltonian into Pauli terms.
        single_flag (bool): Whether to use a single flag qubit for all constraints.
        n_layers (int): The number of QAOA layers.
        samples (int): The number of samples for measurement.
        learning_rate (float): The learning rate for the optimizer.
        steps (int): The number of optimization steps.
        num_restarts (int): The number of random restarts for optimization.
        pre_made (bool): Whether to use pre-made data for the Hamiltonian and angles.
        path (str): The path to the pre-made data file.
    """

    def __init__(
        self,
        constraints: list[str],
        flag_wires: list[int],
        angle_strategy: str = "ma-QAOA",
        decompose: bool = True,
        single_flag: bool = False,
        n_layers: int = 1,
        samples: int = 1000,
        learning_rate: float = 0.01,
        steps: int = 50,
        num_restarts: int = 100,
        pre_made: bool = False,
        path: str = None,
    ) -> None:

        self.constraints = constraints
        self.angle_strategy = angle_strategy
        self.decompose = decompose
        self.single_flag = single_flag
        self.n_layers = n_layers
        self.samples = samples
        self.learning_rate = learning_rate
        self.steps = steps
        self.num_restarts = num_restarts

        self.lhs, self.rhs, self.op = self.parse_constraint(self.constraints)
        self.var_wires = [[int(x) for x in re.findall(r"x_*(\d+)", c)] for c in self.lhs]
        self.n_x = len(list(set(w for ww in self.var_wires for w in ww)))
        self.n_c = len(self.constraints) if not single_flag else 1
        self.n = self.n_x + self.n_c
        self.flag_wires = flag_wires
        self.all_wires = list(set(w for ww in self.var_wires for w in ww)) + list(self.flag_wires)
        if pre_made:
            self.path = path
            self.get_pre_made_data()
        else:
            self.constraint_Ham = self.get_constraint_Hamiltonian()
        self.num_gamma = len(self.constraint_Ham.ops) if self.decompose else 1
        self.num_beta = len(self.all_wires)

    def get_pre_made_data(self) -> None:
        """
        Loads the pre-made data from the given path.

        Args:
            path (str): The path to the pre-made data.
        """
        df = pd.read_pickle(self.path)
        mapper = ConstraintMapper(df['constraints'].to_list())
        df = df[(df['n_layers'] == self.n_layers) & (df['angle_strategy'] == self.angle_strategy) & (df['constraints'].apply(lambda x: set(x) == set(mapper.map_constraints(self.constraints))))]
        if not df.empty:
            self.outcomes = df['outcomes'].iloc[0]
            self.constraint_Ham = df['Hamiltonian'].iloc[0].map_wires({i: w for i, w in enumerate(self.all_wires)})
            self.opt_angles = np.array(df['opt_angles'].iloc[0])
        else:
            print("No pre-made data found for the given constraints and parameters. Making new data.")
            self.constraint_Ham = self.get_constraint_Hamiltonian()

    def parse_constraint(self, constraint: str) -> tuple[str, int, str]:
        """
        Parses the constraint string and returns the left-hand side, right-hand side, and operator.
        Args:
            constraint (str): The constraint string to parse.

        Returns:
            tuple[str, int, str]: The left-hand side, right-hand side, and operator of the constraint.
        """
        operators = {'==': 'Equals', '<=': 'Leq', '>=': 'Geq', '=': 'Equals', '<': 'LT', '>': 'GT'}

        lhs, rhs, op = [], [], []
        for constraint in self.constraints:
            for temp_op in operators.keys():
                if temp_op in constraint:
                    temp_lhs, temp_rhs = constraint.split(temp_op)
                    lhs.append(temp_lhs)
                    rhs.append(temp_rhs)
                    op.append([temp_op, operators[temp_op]])
                    break
        return lhs, rhs, op

    def get_constraint_Hamiltonian(self) -> qml.Hamiltonian:
        """
        Creates the constraint Hamiltonian. If the constraint has been optimized before, it will load the Hamiltonian from a file. Otherwise, it will construct the Hamiltonian.
        """
        true_table, outcomes = self.generate_truth_table(False)
        diag = np.diag(outcomes, requires_grad=False)
        start = time.time()
        if self.decompose:
            hamiltonian = qml.pauli_decompose(diag, hide_identity=True, wire_order=self.all_wires)
        else:
            hamiltonian = qml.Hermitian(diag, wires=self.all_wires)
        end = time.time()
        total_time = end - start
        self.hamiltonian_time = total_time
        return hamiltonian

    def constraint_circuit(self, angles: np.ndarray) -> None:
        """
        Constructs the constraint QAOA circuit.

        Args:
            angles (np.ndarray): Parameters for the QAOA circuit.
        """
        if self.angle_strategy == "ma-QAOA":
            gammas = angles[:, :self.num_gamma]
            betas = angles[:, self.num_gamma:]
        else:
            gammas = np.array([angles[:, 0]] * self.num_gamma).T
            betas = np.array([angles[:, 1]] * self.num_beta).T

        for wire in self.all_wires:
            qml.Hadamard(wires=wire)

        for q in range(self.n_layers):
            # Cost unitary
            if self.decompose:
                idx = 0
                coeffs, ops = self.constraint_Ham.terms()
                for (w, op) in zip(coeffs, ops):
                    if re.search(r"^[I]+$", qml.pauli.pauli_word_to_string(op)):
                        continue
                    qml.MultiRZ(w * gammas[q][idx], wires=op.wires)
                    idx += 1
            else:
                hamiltonian = self.constraint_Ham
                qml.evolve(hamiltonian, coeff=gammas[q][0])

            # Mixing unitary
            for i, wire in enumerate(self.all_wires):
                qml.RX(betas[q][i], wires=wire)

    def opt_circuit(self) -> None:
        """
        Constructs the circuit using the optimal angles.
        """
        opt_angles = self.opt_angles

        self.constraint_circuit(opt_angles)

    def do_evolution_circuit(self, angles: np.ndarray) -> float:
        """
        Creates the quantum circuit and computes the expectation value of the cost Hamiltonian.

        Args:
            angles (np.ndarray): Parameters for the QAOA circuit.

        Returns:
            float: The expectation value after evolving the quantum circuit.
        """

        if self.decompose:
            dev = qml.device("default.qubit", wires=self.all_wires)
        else:
            dev = qml.device("default.qubit", wires=self.all_wires)

        @qml.qnode(dev)
        def circuit(angles):
            self.constraint_circuit(angles)
            hamiltonian = self.constraint_Ham
            return qml.expval(hamiltonian)

        return circuit(angles)

    def do_counts_circuit(self, probs=False, shots=1000) -> dict:
        """
        Creates the quantum circuit and returns the distribution of measurement outcomes.

        Args:
            probs (bool): Whether to return probabilities instead of counts.
            shots (int): The number of shots to use for sampling.

        Returns:
            dict: The distribution of measurement outcomes.
        """
        if self.decompose:
            dev = qml.device("default.qubit", wires=self.all_wires, shots=shots)
        else:
            dev = qml.device("default.qubit", wires=self.all_wires, shots=shots)

        @qml.qnode(dev)
        def circuit():
            self.opt_circuit()
            return qml.counts(all_outcomes=True)

        start = time.time()
        counts = circuit()
        end = time.time()
        total_time = end - start
        self.count_time = total_time

        return counts

    def get_circuit_resources(self, opt: bool = False) -> qml.resource.Resources:
        """
        Returns the resources required for the circuit.

        Args:
            opt (bool): Whether to use the optimal angles.

        Returns:
            qml.resource.Resources: The resources required for the circuit.
        """
        @qml.qnode(qml.device("default.qubit"))
        def qubo_cost_fn():
            if opt:
                self.opt_circuit()
            else:
                if self.angle_strategy == "ma-QAOA":
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, self.n_layers*(self.num_gamma + self.num_beta)).reshape(self.n_layers, self.num_gamma + self.num_beta)
                else:
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, 2*self.n_layers, requires_grad=True).reshape(self.n_layers, 2)
                self.constraint_circuit(init_angles)
            return qml.state()

        gate_resources = qml.specs(qml.compile(qubo_cost_fn, basis_set=["Hadamard", "CNOT"]))()['resources']
        if self.decompose:
            coeffs, ops = self.constraint_Ham.terms()
            est_shots = qml.resource.estimate_shots(coeffs)
            est_error = qml.resource.estimate_error(coeffs)
            group_ops, group_coeffs = qml.pauli.group_observables(ops, coeffs)
            group_shots = qml.resource.estimate_shots(group_coeffs)
            group_error = qml.resource.estimate_error(group_coeffs)
        else:
            est_shots = 0
            est_error = 0
            group_shots = 0
            group_error = 0
        return gate_resources, est_shots, est_error, group_shots, group_error

    def __convert_angles(self, angles: np.ndarray) -> np.ndarray:
        """
        Converts a list of angles into the MaQAOA format (where the gamma and beta values are repeated).

        Args:
            angles (np.ndarray): List of angles for the QAOA circuit.

        Returns:
            np.ndarray: Converted angles array in the MaQAOA format.
        """
        maqaoa_angles = []
        if self.n_layers == 1:
            # If there is only one layer, we can just repeat the angles
            for gamma, beta in angles:
                maqaoa_angles += [gamma] * self.num_gamma
                maqaoa_angles += [beta] * self.num_beta
            return np.array(maqaoa_angles).reshape(1, self.num_gamma + self.num_beta)
        else:
            for i in range(self.n_layers):
                for gamma, beta in angles[i]:
                    maqaoa_angles += [gamma] * self.num_gamma
                    maqaoa_angles += [beta] * self.num_beta
            return np.array(maqaoa_angles).reshape(self.n_layers, self.num_gamma + self.num_beta)

    def generate_truth_table(self, yesPrintTTable: bool = False) -> tuple[np.ndarray, np.ndarray]:
        """
        Generates the truth table for the constraint.

        Args:
            yesPrintTTable (bool): Whether to print the truth table.

        Returns:
            tuple[np.ndarray, np.ndarray]: The truth table and the outcomes.
        """
        start = time.time()
        # Prepare to store the truth table
        truth_table = []
        valid_bitstrings = set()

        # Create all possible bitstrings for original vars
        original_bitstrings = list(it.product([0, 1], repeat=self.n_x))

        for original_vars in original_bitstrings:
            # Check each constraint and create the corresponding ancilla bits
            ancillae = []
            # Create a dictionary to map the wire names to their indices
            wires_correct_index = {w: i for i, w in enumerate(self.all_wires)}
            for c in range(len(self.constraints)):
                # Evaluate the left-hand side of the constraint
                var_dict = {f'x_{x}': original_vars[wires_correct_index[x]] for x in self.var_wires[c]}
                eval_lhs = eval(self.lhs[c], {}, var_dict)

                # Check satisfaction based on the type of constraint
                is_satisfied = (eval(f'{eval_lhs} {self.op[c][0]} {self.rhs[c]}'))

                ancillae.append(0 if is_satisfied else 1)

            # Append the valid bitstring (original vars + ancillae) with outcome 0
            if self.single_flag:
                valid_bitstring = tuple(original_vars) + tuple([int(any(ancillae))])
            else:
                valid_bitstring = tuple(original_vars) + tuple(ancillae)
            valid_bitstrings.add(valid_bitstring)
            truth_table.append(list(valid_bitstring) + [-1])

        # Generate all possible bitstrings for total_vars
        all_bitstrings = list(it.product([0, 1], repeat=self.n))

        # Mark the remaining bitstrings with outcome 1
        for bitstring in all_bitstrings:
            if bitstring not in valid_bitstrings:
                invalid_bitstring = list(bitstring) + [1]
                truth_table.append(invalid_bitstring)

        # Sort the truth table based on the bitstrings
        truth_table.sort(key=lambda x: tuple(x[:-1]))

        if yesPrintTTable:
            print("Truth table (original_vars + ancillae + outcome):")
            for row in truth_table:
                print(row)

        # Separate outcomes from the truth table
        outcomes = [row[-1] for row in truth_table]
        end = time.time()
        total_time = end - start
        self.table_time = total_time
        self.outcomes = outcomes

        return np.array(truth_table), outcomes

    def optimize_angles(self, cost_fn, maximize: bool = False, starting_angles_from_qaoa: np.ndarray = None, prev_layer_angles: np.ndarray = None) -> tuple[float, np.ndarray]:
        """
            Optimize the angles for the QAOA circuit.

            Args:
                cost_fn (function): The cost function to optimize.
                maximize (bool): Whether to maximize the cost function.
                starting_angles_from_qaoa (np.ndarray): The starting angles for the optimization.
                prev_layer_angles (np.ndarray): The angles from the previous layer for layer-wise optimization.
            Returns:
                tuple[float, np.ndarray]: The optimal cost and the optimal angles.
        """
        conv_tol = 1e-6
        opt = qml.AdamOptimizer(stepsize=0.1)

        best_cost = float('inf')  # Initialize with infinity for comparison
        best_angles = None  # Store best angles for optimal cost

        if maximize:
            opt_mult = -1
        else:
            opt_mult = 1

        start = time.time()
        for restart in range(self.num_restarts):
            # In case we know a good starting point
            if starting_angles_from_qaoa is not None:
                init_angles = starting_angles_from_qaoa
                init_angles = self.__convert_angles(init_angles) if self.angle_strategy == "ma-QAOA" else init_angles
                # reshape angle to match multi-angle QAOA
            elif prev_layer_angles is not None:
                if self.angle_strategy == "ma-QAOA":
                    init_angles = np.concatenate((prev_layer_angles, np.random.uniform(-2*np.pi, 2*np.pi, self.n_layers*(self.num_gamma + self.num_beta - prev_layer_angles.shape[1]), requires_grad=True).reshape(self.n_layers, self.num_gamma + self.num_beta - prev_layer_angles.shape[1])), axis=1)
                else:
                    init_angles = np.concatenate((prev_layer_angles, np.random.uniform(-2*np.pi, 2*np.pi, 2*self.n_layers - prev_layer_angles.shape[1], requires_grad=True).reshape(self.n_layers, 2 - prev_layer_angles.shape[1])), axis=1)
            else:
                if self.angle_strategy == "ma-QAOA":
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, self.n_layers*(self.num_gamma + self.num_beta), requires_grad=True).reshape(self.n_layers, self.num_gamma + self.num_beta)
                else:
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, 2*self.n_layers, requires_grad=True).reshape(self.n_layers, 2)

            angles = init_angles

            # Bookkeeping
            new_cost = opt_mult * cost_fn(angles)

            for i in range(self.steps):
                angles, prev_cost = opt.step_and_cost(cost_fn, angles)

                new_cost = cost_fn(angles)

                conv_prev = np.abs(new_cost - prev_cost)

                # if the difference between the previous cost and the current cost is less than the convergence tolerance
                if conv_prev <= conv_tol:
                    break

            if new_cost < best_cost:
                best_cost = new_cost
                best_angles = angles

        end = time.time()
        total_time = end - start
        self.optimize_time = total_time
        self.opt_angles = best_angles

        return best_cost, best_angles


class ConstraintMapper:
    """
    A class to map a set of constraints to a pre-existing set of constraints in a dataframe.
    """

    def __init__(self, constraints_in_df):
        self.constraints_in_df = constraints_in_df

    def normalize_constraint(self, constraint: str) -> str:
        """
        Normalizes a constraint by removing spaces, sorting terms within the constraint, and standardizing the operator.
        Args:
            constraint (str): The constraint to normalize.
        Returns:
            str: The normalized constraint.
        """
        # Remove spaces and sort terms within the constraint
        constraint = re.sub(r'\s+', '', constraint)
        operator = re.search(r'(==|<=|>=|=|<|>)', constraint).group(0)
        lhs, rhs = constraint.split(operator)
        terms = sorted(re.split(r'(\+)', lhs))
        normalized_lhs = ' '.join(terms)
        return f"{normalized_lhs}{operator}{rhs}"

    def normalize_constraints(self, constraints: list[str]) -> list[str]:
        """
        Normalizes a list of constraints.
        Args:
            constraints (list[str]): The list of constraints to normalize.
        Returns:
            list[str]: The list of normalized constraints.
        """
        return [self.normalize_constraint(c) for c in constraints]

    def map_constraints(self, input_constraints: list[str]) -> list[str] | None:
        """
        Maps the input constraints to a set of constraints in the dataframe.
        Args:
            input_constraints (list[str]): The input constraints to map.
        Returns:
            list[str] | None: The mapped constraints if a match is found, otherwise None.
        """
        normalized_input = self.normalize_constraints(input_constraints)
        for constraints in self.constraints_in_df:
            normalized_constraints = self.normalize_constraints(constraints)
            if self.match_constraints(normalized_input, normalized_constraints):
                return constraints
        return None

    def match_constraints(self, input_constraints: list[str], df_constraints: list[str]) -> bool:
        """
        Checks if two sets of constraints match, allowing for permutations of variables and constraints.
        Args:
            input_constraints (list[str]): The input constraints to check.
            df_constraints (list[str]): The constraints from the dataframe to check against.
        Returns:
            bool: True if the constraints match, otherwise False.
        """
        input_vars = sorted(set(re.findall(r'x_\d+', ' '.join(input_constraints))))
        df_vars = sorted(set(re.findall(r'x_\d+', ' '.join(df_constraints))))

        if len(input_vars) != len(df_vars):
            return False

        # Generate all possible mappings of input_vars to df_vars
        for perm in it.permutations(df_vars):
            var_map = {input_var: perm[i] for i, input_var in enumerate(input_vars)}
            mapped_input_constraints = [
                re.sub(r'x_\d+', lambda m: var_map[m.group(0)], constraint)
                for constraint in input_constraints
            ]

            # Check all permutations of the constraints themselves
            for perm_constraints in it.permutations(mapped_input_constraints):
                if self.check_permutations(perm_constraints, df_constraints):
                    return True

        return False

    def check_permutations(self, perm_constraints: list[str], df_constraints: list[str]) -> bool:
        """
        Checks if two sets of constraints match, allowing for permutations of variables within each constraint.
        Args:
            perm_constraints (list[str]): The permuted input constraints to check.
            df_constraints (list[str]): The constraints from the dataframe to check against.
        Returns:
            bool: True if the constraints match, otherwise False.
        """
        # Check all permutations of variables within each constraint
        for perm_constraint in perm_constraints:
            perm_operator = re.search(r'(==|<=|>=|=|<|>)', perm_constraint).group(0)
            for df_constraint in df_constraints:
                df_operator = re.search(r'(==|<=|>=|=|<|>)', df_constraint).group(0)
                lhs_perm, rhs_perm = perm_constraint.split(perm_operator)
                lhs_perm = re.split(r'(\+)', lhs_perm)
                lhs_df, rhs_df = df_constraint.split(df_operator)
                lhs_df = re.split(r'(\+)', lhs_df)
                if sorted(lhs_perm) == sorted(lhs_df) and rhs_perm == rhs_df and perm_operator == df_operator:
                    return True
        return False
```

## File: LICENSE
```
MIT License

Copyright (c) 2025 Anthony Wilkie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: make_data.py
```python
from pennylane import numpy as np
import itertools as it
import os
import warnings
warnings.filterwarnings('ignore')


#|%%--%%| <r7FwNHU1N7|c49bRzGd27>
r"""°°°
Functions to create single linear constraints.
°°°"""
#|%%--%%| <c49bRzGd27|FGDZWJe8Bm>


def make_single_constraint(n: int, op: str, b: int, coeff: list = None) -> str:
    """
    Create a linear constraint of the form $\\sum_{i=1}^n a_i x_i op b$.
    Args:
        n (int): Number of variables.
        op (str): Operator for the constraint ('==', '>=', '<=', '<', '>').
        b (int): Right-hand side value of the constraint.
        coeff (list, optional): Coefficients for each variable. Defaults to None, which sets all coefficients to 1.
    Returns:
        str: A string representing the linear constraint.
    """
    if coeff is None:
        coeff = [1] * n
    # Create the constraint string
    constraint = " + ".join([f"{coeff[i]}*x_{i}" for i in range(n)]) + f" {op} {b}"
    return constraint


def make_two_constraint(support: int) -> list[str]:
    """
    Generate a random constraint with the specified support.
    Args:
        support (int): The support of the constraint (1, 2, or 3).
    Returns:
        list[str]: A list of two constraint strings.
    """
    lhs = {
        1: ['x_0 + x_1 + x_2', 'x_0 + x_3 + x_4'],
        2: ['x_0 + x_1 + x_2 + x_3', 'x_0 + x_3 + x_4'],
        3: ['x_0 + x_1 + x_2 + x_3', 'x_0 + x_2 + x_3 + x_4'],
    }

    ops = ['==', '<=', '>=']

    rhs = {1: range(4), 2: range(5), 3: range(5)}[support]
    lhss = lhs[support]
    opss = np.random.choice(ops, size=2, replace=True)
    rhss = np.random.choice(rhs, size=2, replace=True)
    constraints = [f"{lhss[i]} {opss[i]} {rhss[i]}" for i in range(2)]
    return constraints


def make_two_constraints(result_dir: str = 'alex/results/') -> None:
    """
    Generate constraints with specified support and at least one feasible solution.
    Then save them to a file in the specified directory.
    Args:
        result_dir (str): Directory to save the constraints file.
    """
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    # only generate constraints if the file doesn't already exist
    if not os.path.exists(f'{result_dir}two_constraints_support_1.txt'):
        for support in range(1, 4):
            constraints = {}
            num_constraints = 10
            feasible = False
            print('-'*40)
            print(f"Generating {num_constraints} constraints with support {support}")
            for i in range(num_constraints):
                print(f"Constraint {i+1}/{num_constraints}")
                while not feasible:
                    constraint = make_two_constraint(support)
                    print(constraint)
                    if constraint in constraints.values():
                        print("Duplicate constraint, regenerating...")
                        continue
                    feasible = check_feasibility(constraint)
                    print("Feasible:", feasible)
                constraints[i] = constraint
                feasible = False
                with open(f'{result_dir}two_constraints_support_{support}.txt', 'a') as f:
                    f.write(f"{constraint}\n")


def check_feasibility(constraints: list[str]) -> bool:
    """
    Check if there exists a feasible solution for the given constraints.
    Args:
        constraints (list[str]): A list of constraint strings.
    Returns:
        bool: True if there exists a feasible solution, False otherwise.
    """
    n_vars = 5
    all_bitstrings = it.product([0, 1], repeat=n_vars)
    for x in all_bitstrings:
        x_feasible = True
        var_dict = {f'x_{i}': x[i] for i in range(len(x))}
        for c in constraints:
            if not eval(c, var_dict):
                x_feasible = False
                break
        if x_feasible:
            return True
    return False


#|%%--%%| <FGDZWJe8Bm|aEkoiyklK3>
r"""°°°
Functions to create random QUBOs and read/write them to/from files.
°°°"""
#|%%--%%| <aEkoiyklK3|EG86IUpVs9>


def generate_random_qubo_string(n: int) -> [np.ndarray, str]:
    """
    Generate a random QUBO matrix and its corresponding string representation.
    Args:
        n (int): Size of the QUBO matrix (n x n).
    Returns:
        tuple:
            - np.ndarray: The generated QUBO matrix.
            - str: The string representation of the QUBO.
    """
    Q = np.random.randint(low=-5, high=5, size=(n, n))
    Q = np.triu(Q)  # Make the matrix upper triangular
    qubo_terms = []
    for i in range(len(Q)):
        for j in range(i, len(Q)):
            if Q[i, j] != 0:
                if i == j:
                    qubo_terms.append(f"{Q[i, j]}*x_{i}")
                else:
                    qubo_terms.append(f"{Q[i, j]}*x_{i} x_{j}")

    qubo_string = " + ".join(qubo_terms)
    return Q, qubo_string


def generate_n_qubos(num_qubo: int, min_n: int, max_n: int) -> dict:
    """
    Generate a dictionary of random QUBO matrices and their string representations for sizes ranging from min_n to max_n.
    Args:
        num_qubo (int): Number of QUBO matrices to generate for each size.
        min_n (int): Minimum size of the QUBO matrix.
        max_n (int): Maximum size of the QUBO matrix.
    Returns:
        dict: A dictionary where keys are sizes (n) and values are dictionaries containing QUBO matrices and their string representations.
    """
    qubos = {}
    for i in range(min_n, max_n+1):
        qubos[i] = {}
        for j in range(num_qubo):
            Q, qubo_string = generate_random_qubo_string(i)
            qubos[i][j] = {'Q': Q, 'qubo_string': qubo_string}
    return qubos


def write_qubos_to_file(qubos: dict, file_name: str, min_n: int, max_n: int, results_dir: str = 'alex/results/') -> None:
    """
    Write a dictionary of QUBO matrices and their string representations to a file.
    Args:
        qubos (dict): A dictionary where keys are sizes (n) and values are dictionaries containing QUBO matrices and their string representations.
        file_name (str): Name of the file to write the QUBOs to.
        min_n (int): Minimum size of the QUBO matrix.
        max_n (int): Maximum size of the QUBO matrix.
        results_dir (str, optional): Directory to save the file. Defaults to 'alex/results/'.
    """
    with open(f'{results_dir}{file_name}', 'w') as f:
        for i in range(min_n, max_n+1):
            for j in range(len(qubos[i])):
                f.write(f"({i}, {j}); {qubos[i][j]['qubo_string']}; {qubos[i][j]['Q'].tolist()}\n")


def read_qubos_from_file(file_name: str, results_dir: str = 'alex/results/') -> dict:
    """
    Read a file containing QUBO matrices and their string representations into a dictionary.
    Args:
        file_name (str): Name of the file to read the QUBOs from.
        results_dir (str, optional): Directory where the file is located. Defaults to './results/'.
    Returns:
        dict: A dictionary where keys are sizes (n) and values are dictionaries containing QUBO matrices and their string representations.
    """
    qubos = {}
    with open(f'{results_dir}{file_name}', 'r') as f:
        qubos = {}
        for i, line in enumerate(f):
            line = line.split(';')
            n_i = eval(line[0])
            n = n_i[0]
            if n not in qubos:
                qubos[n] = {}
            qubos[n][n_i[1]] = {}
            qubos[n][n_i[1]]['qubo_string'] = line[1]
            qubos[n][n_i[1]]['Q'] = np.array(eval(line[2]))
    return qubos


def get_optimal_x(qubo: np.ndarray, constraints: list) -> [float, list, float]:
    """
    Get the optimal solution for a given QUBO matrix and a list of constraints by brute force.
    Args:
        qubo (np.ndarray): The QUBO matrix.
        constraints (list): A list of constraint strings.
    Returns:
        tuple:
            - float: Minimum value of the objective function for feasible solutions.
            - list: List of optimal bitstrings (as strings) that achieve the minimum value.
            - float: Minimum value of the objective function across all solutions (feasible and infeasible).
    """
    all_bitstrings = it.product([0, 1], repeat=len(qubo))
    feasible = []
    infeasible = []
    for x in all_bitstrings:
        x_feasible = True
        var_dict = {f'x_{i}': x[i] for i in range(len(x))}
        for c in constraints:
            if not eval(c, var_dict):
                x_feasible = False
                break
        if x_feasible:
            feasible.append(x)
        else:
            infeasible.append(x)

    feas_vals = {}
    infeas_vals = {}

    # Calculate objective values for feasible solutions
    for x in feasible:
        feas_vals[''.join(map(str, x))] = np.dot(x, np.dot(qubo, x))

    # Calculate objective values for infeasible solutions
    for x in infeasible:
        infeas_vals[''.join(map(str, x))] = np.dot(x, np.dot(qubo, x))

    # Determine minimum values and optimal solutions if there are no feasible solutions
    if len(feas_vals) == 0:
        min_infeas_val = min(infeas_vals.values())
        return min_infeas_val, None, min_infeas_val

    # Determine minimum values and optimal solutions if there are feasible solutions
    if len(infeas_vals) == 0:
        min_feas_val = min(feas_vals.values())
        optimal_x = [k for k, v in feas_vals.items() if v == min_feas_val]
        return min_feas_val, optimal_x, min_feas_val

    # Determine minimum values and optimal solutions if there are both feasible and infeasible solutions
    min_feas_val = min(feas_vals.values())
    min_infeas_val = min(infeas_vals.values())
    optimal_x = [k for k, v in feas_vals.items() if v == min_feas_val]
    total_min_val = min(min_feas_val, min_infeas_val)

    return min_feas_val, optimal_x, total_min_val
```

## File: problem_qaoa.py
```python
import re
import time
import pennylane as qml
from pennylane import numpy as np
from typing import Tuple


class ProblemQAOA:
    """
    Class to takes in a QUBO matrix and constraint state preparation circuits (constraint gadgets) to solve a constrained optimization problem using QAOA.
    The default method for solving the QCBO problem is to use the Grover mixer and the ma-QAOA angle strategy.
    Attributes:
        qubo (np.ndarray): The QUBO matrix representing the objective function.
        state_prep (list[cq.ConstraintQAOA]): List of constraint state preparation circuits.
        angle_strategy (str): The angle strategy to use ('QAOA' or 'ma-QAOA').
        mixer (str): The mixer to use ('Grover' or 'X-Mixer').
        penalty (list[float]): List of penalty values for each constraint.
        n_layers (int): Number of QAOA layers.
        samples (int): Number of samples to draw from the quantum circuit.
        learning_rate (float): Learning rate for the optimizer.
        steps (int): Number of optimization steps.
        num_restarts (int): Number of random restarts for the optimizer.
        overlap_vars (list[tuple[int, int]]): List of tuples indicating which variables should be equal across different constraints.
        overlap_penalty (float): Penalty value for the overlap constraints.
    """

    def __init__(
        self,
        qubo: np.ndarray,
        state_prep,  # : list[cq.ConstraintQAOA],
        angle_strategy: str = "ma-QAOA",
        mixer: str = "Grover",
        penalty: list[float] = [20],
        n_layers: int = 1,
        samples: int = 1000,
        learning_rate: float = 0.01,
        steps: int = 50,
        num_restarts: int = 100,
        overlap_vars: list[tuple[int, int]] = None,
        overlap_penalty: float = None
    ) -> None:

        self.qubo = qubo
        self.state_prep = state_prep
        self.angle_strategy = self.__error_check_angle_strategy(angle_strategy)
        self.mixer = self.__error_check_mixer(mixer)
        self.n_layers = n_layers
        self.samples = samples
        self.learning_rate = learning_rate
        self.steps = steps
        self.num_restarts = num_restarts
        self.overlap_vars = overlap_vars
        self.overlap_penalty = overlap_penalty
        self.starting_angles_from_qaoa = None

        # self.opt_angles = self.get_opt_angles()
        self.n_x = qubo.shape[0]
        self.var_wires = list(range(self.n_x))
        self.flag_wires = [f for qaoa in state_prep for f in qaoa.flag_wires]
        self.penalty = penalty * len(self.flag_wires) if len(penalty) == 1 else penalty
        self.all_wires = list(self.var_wires) + list(self.flag_wires)
        self.qubo_Ham = self.get_qubo_Hamiltonian()
        self.problem_Ham = self.get_problem_Hamiltonian()
        self.num_gamma = self.__get_num_gamma()
        self.num_beta = len(self.all_wires) if self.mixer == "X-Mixer" else 1

    def solve_problem_qaoa(self, n_layers: int = 1) -> tuple[float, np.ndarray, np.ndarray, qml.resource.Resources, float]:
        """
        Runs the QAOA algorithm for the deterministic equivalent of a multi-stage stochastic optimization problem.

        Args:
            n_layers (int): number of QAOA layers to use.

        Returns:
            tuple:
                - float: final expectation value of objective.
                - np.ndarray: array of bit strings sampled from the QAOA circuit.
                - np.ndarray: the optimal parameters found by the optimizer.
                - qml.resource.Resources: gate count of the quantum circuit.
                - float: total time taken to run the algorithm.
        """

        def objective(params: np.ndarray) -> float:
            if self.angle_strategy == "QAOA":
                params = self.__convert_angles(params)
            return self.__do_evolution_circuit(params)

        ar, counts, params, gates, total_time = self.__optimize_circuit(self.n_layers, objective)

        return ar, counts, params, gates, total_time

    def get_problem_Hamiltonian(self) -> qml.Hamiltonian:
        """
        Returns the problem Hamiltonian for the QAOA circuit, which consists of the QUBO Hamiltonian and the constraint flag penalty Hamiltonian.
        The penalty Hamiltonian is of the form (penalty / 2) (I_flag - Z_flag).
        The resulting problem Hamiltonian is H = H_qubo + H_penalty.

        Returns:
            qml.Hamiltonian: The problem Hamiltonian for the QAOA circuit.
        """
        start = time.time()
        pen_coeff = []
        pen_obs = []
        for i, pen in enumerate(self.penalty):
            pen_coeff.append(pen / 2)
            pen_coeff.append(-pen / 2)
            pen_obs.append(qml.Identity(self.flag_wires[i]))
            pen_obs.append(qml.PauliZ(self.flag_wires[i]))

        penalty_ham = qml.Hamiltonian(pen_coeff, pen_obs)
        problem_ham = self.qubo_Ham + penalty_ham
        if self.overlap_vars is not None:
            problem_ham = self.get_overlap_Hamiltoinan(problem_ham)

        end = time.time()
        total_time = end - start
        self.hamiltonian_time = total_time
        return problem_ham

    def get_overlap_Hamiltoinan(self, prob_ham: qml.Hamiltonian) -> qml.Hamiltonian:
        """
        Returns the penalization of the overlap variables to make sure they are the same value, e.g. x_0 = x_1 is penalized as lambda (x_0 - x_1)^2.
        Args:
            prob_ham (qml.Hamiltonian): The problem Hamiltonian without the overlap penalty.
        Returns:
            qml.Hamiltonian: The problem Hamiltonian for the QAOA circuit.
        """
        def _single_overlap_Hamiltonian(wire1, wire2, penalty):
            coeff = [penalty / 2, -penalty / 2]
            obs = [qml.Identity(wire1), qml.PauliZ(wire1) @ qml.PauliZ(wire2)]
            return qml.Hamiltonian(coeff, obs)

        for i, (w1, w2) in enumerate(self.overlap_vars):
            prob_ham += _single_overlap_Hamiltonian(w1, w2, self.overlap_penalty[i])
        return prob_ham

    def get_qubo_Hamiltonian(self) -> qml.Hamiltonian:
        """
        Returns the QUBO Hamiltonian for the based on the QUBO matrix.

        Returns:
            qml.Hamiltonian: The QUBO Hamiltonian for the QAOA circuit.
        """
        qubits = self.var_wires
        nxx = self.n_x

        jj, hh, oo = self.__get_hvals(self.qubo)
        h_coeff = []
        h_obs = []

        for i in range(nxx):
            for j in range(i+1, nxx):
                if jj[i, j] != 0:
                    h_coeff.append(jj[i, j])
                    h_obs.append(qml.PauliZ(qubits[i]) @ qml.PauliZ(qubits[j]))
            if hh[i] != 0:
                h_coeff.append(hh[i])
                h_obs.append(qml.PauliZ(qubits[i]))

        if oo != 0:
            h_coeff.append(oo)
            h_obs.append(qml.Identity(qubits[0]))
        h_coeff = np.array(h_coeff)
        hamiltonian = qml.Hamiltonian(h_coeff, h_obs)
        return hamiltonian

    def __get_hvals(self, Qx: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float]:
        """
        Function to obtain the Ising coefficients from the QUBO coefficients.

        Args:
            Qx (str): The node identifier for which to calculate the Ising coefficients.

        Returns:
            Tuple[np.ndarray, np.ndarray, float]:
                - jmat (np.ndarray): The quadratic coefficients matrix.
                - hvec (np.ndarray): The linear coefficients vector.
                - offset (float): The offset for the Hamiltonian.
        """
        nvars = self.n_x
        jmat = np.zeros(shape=(nvars, nvars))
        hvec = np.zeros(nvars)
        quadratic = Qx
        linear = np.diag(quadratic)

        for i in range(nvars):
            # The coefficients for the linear terms
            hvec[i] = hvec[i] - (1/2 * linear[i]
                                 + 1/4 * sum([quadratic[k][i] for k in range(i)])
                                 + 1/4 * sum([quadratic[i][l] for l in range(i+1, nvars)]))

            for j in range(i+1, nvars):
                # The coefficients for the quadratic terms
                jmat[i][j] = jmat[i][j] + quadratic[i][j]/4

        # Correct the offset value
        offset = (np.sum(quadratic)/4 + np.sum(linear)/4)
        return jmat, hvec, offset

    def problem_circuit(self, angles: np.ndarray) -> None:
        """
        Constructs the problem QAOA circuit.

        Args:
            angles (np.ndarray): Parameters for the QAOA circuit.
        """
        if self.angle_strategy == "ma-QAOA":
            gammas = angles[:, :self.num_gamma]
            betas = angles[:, self.num_gamma:]
        else:
            gammas = np.array([angles[:, 0]] * self.num_gamma).T
            betas = np.array([angles[:, 1]] * self.num_beta).T

        for c in self.state_prep:
            c.opt_circuit()

        for q in range(self.n_layers):
            # Cost unitary
            idx = 0
            coeffs, ops = self.problem_Ham.terms()
            for (w, op) in zip(coeffs, ops):
                if re.search(r"^[I]+$", qml.pauli.pauli_word_to_string(op)):
                    continue
                qml.MultiRZ(w * gammas[q][idx], wires=op.wires)
                idx += 1

            # Mixing unitary
            if self.mixer == "Grover":
                for c in self.state_prep[::-1]:
                    qml.adjoint(c.opt_circuit)()
                for i in self.all_wires:
                    qml.PauliX(wires=i)
                qml.ctrl(qml.PhaseShift(betas[q][0]/np.pi, wires=self.all_wires[-1]), control=self.all_wires[:-1])
                for i in self.all_wires:
                    qml.PauliX(wires=i)
                for c in self.state_prep:
                    c.opt_circuit()

            elif self.mixer == "X-Mixer":
                for i, wire in enumerate(self.all_wires):
                    # Custom combination of gates
                    qml.RX(betas[q][i], wires=wire)

    def opt_circuit(self) -> None:
        """
        Constructs the circuit using the optimal angles.
        """
        opt_angles = self.opt_angles

        self.problem_circuit(opt_angles)

    def do_evolution_circuit(self, angles: np.ndarray) -> float:
        """
        Creates the quantum circuit and computes the expectation value of the cost Hamiltonian.

        Args:
            angles (np.ndarray): Parameters for the QAOA circuit.

        Returns:
            float: The expectation value after evolving the quantum circuit.
        """

        @qml.qnode(qml.device("lightning.qubit", wires=self.all_wires))
        def circuit(angles):
            self.problem_circuit(angles)
            return qml.expval(self.problem_Ham)

        return circuit(angles)

    def do_counts_circuit(self, angles=None, shots=1000) -> dict:
        """
        Creates the quantum circuit and returns the distribution of counts or probabilities.

        Args:
            angles (np.ndarray): Parameters for the QAOA circuit.
            shots (int): Number of shots to sample from the quantum circuit.

        Returns:
            dict: The distribution of counts or probabilities from the quantum circuit.
        """
        @qml.qnode(qml.device("lightning.qubit", wires=self.all_wires, shots=shots))
        def circuit():
            if angles is None:
                self.opt_circuit()
            else:
                self.problem_circuit(angles)
            return qml.counts(all_outcomes=True)

        start = time.time()
        counts = circuit()
        end = time.time()
        total_time = end - start
        self.count_time = total_time

        return counts

    def __convert_angles(self, angles: np.ndarray) -> np.ndarray:
        """
        Converts a list of angles into the MaQAOA format (where the gamma and beta values are repeated).

        Args:
            angles (np.ndarray): List of angles for the QAOA circuit.

        Returns:
            np.ndarray: Converted angles array in the MaQAOA format.
        """
        maqaoa_angles = []
        for gamma, beta in zip(angles[::2], angles[1::2]):
            maqaoa_angles += [gamma] * self.num_gamma
            maqaoa_angles += [beta] * self.num_beta
        return np.array(maqaoa_angles).reshape(-1, 2)

    def optimize_angles(self, cost_fn, maximize: bool = False, starting_angles_from_qaoa: np.ndarray = None, prev_layer_angles: np.ndarray = None) -> tuple[float, np.ndarray]:
        """
        Runs the optimization process for the QAOA algorithm to solve the stochastic optimization problem.

        Args:
            n_layers (int): Number of QAOA layers.
            objective (callable): The objective function to minimize.
            maximize (bool): Whether to maximize the objective
            starting_angles_from_qaoa (np.ndarray): Optional starting angles from a previous QAOA run.
            prev_layer_angles (np.ndarray): Optional angles from a previous layer to use as a starting point.

        Returns:
            tuple:
                - float: final expectation value of objective.
                - np.ndarray: the optimal parameters found by the optimizer.
        """
        conv_tol = 1e-6
        opt = qml.AdamOptimizer(stepsize=0.1)

        best_obj_fn = float('inf')  # Initialize with infinity for comparison
        best_params = None  # Store best angles for optimal cost

        if maximize:
            opt_mult = -1
        else:
            opt_mult = 1

        start = time.time()
        for restart in range(self.num_restarts):
            # In case we know a good starting point
            if self.starting_angles_from_qaoa is not None:
                init_angles = self.starting_angles_from_qaoa
                # reshape angle to match multi-angle QAOA
            elif prev_layer_angles is not None:
                if self.angle_strategy == "ma-QAOA":
                    init_angles = np.concatenate((prev_layer_angles.flatten(), np.random.uniform(-2*np.pi, 2*np.pi, (self.num_gamma + self.num_beta), requires_grad=True)), axis=0).reshape(self.n_layers, self.num_gamma + self.num_beta)
                else:
                    init_angles = np.concatenate((prev_layer_angles.flatten, np.random.uniform(-2*np.pi, 2*np.pi, (2), requires_grad=True)), axis=0).reshape(self.n_layers, 2)
            else:
                if self.angle_strategy == "ma-QAOA":
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, self.n_layers*(self.num_gamma + self.num_beta), requires_grad=True).reshape(self.n_layers, self.num_gamma + self.num_beta)
                else:
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, 2*self.n_layers, requires_grad=True).reshape(self.n_layers, 2)

            angles = init_angles

            # Bookkeeping
            new_cost = opt_mult * cost_fn(angles)

            for i in range(self.steps):
                angles, prev_cost = opt.step_and_cost(cost_fn, angles)

                new_cost = cost_fn(angles)

                conv_prev = np.abs(new_cost - prev_cost)

                # if the difference between the previous cost and the current cost is less than the convergence tolerance
                if conv_prev <= conv_tol:
                    break

            if new_cost < best_obj_fn:
                best_obj_fn = new_cost
                best_params = angles

        end = time.time()
        total_time = end - start
        self.optimize_time = total_time
        self.opt_angles = best_params.reshape(self.n_layers, self.num_gamma + self.num_beta)

        return best_obj_fn, best_params

    def prob_opt_x_sol_in_counts(self, counts: dict) -> float:
        """
        Calculate probability of measuring optimal x solution as they appear in counts.
        Args:
            counts (dict): The distribution of counts from the quantum circuit.
        Returns:
            float: Probability of measuring the optimal solution.
        """
        prob_opt = 0
        total_counts = sum(counts.values())  # Total counts from the dictionary
        for sol in self.optimal_x:
            # Convert binary string to integer
            sol_key = sol+'0'*(len(self.flag_wires))
            if sol_key in counts:
                prob_opt += counts[sol_key] / total_counts
        return prob_opt

    def optimize_angles_with_counts(self, starting_angles_from_qaoa: np.ndarray = None) -> tuple[float, np.ndarray]:
        """
        Optimizes the angles for the QAOA circuit by maximizing the probability of measuring the optimal solution.
        This is done by sampling the circuit by getting its counts an then calculating the probability of measuring the optimal solution.
        Args:
            starting_angles_from_qaoa (np.ndarray): Optional starting angles from a previous QAOA run.
        Returns:
            tuple:
                - float: final expectation value of objective.
                - np.ndarray: the optimal parameters found by the optimizer.
        """
        # set scipy optimizer
        conv_tol = 1e-6
        opt = qml.AdamOptimizer(stepsize=0.1)
        best_obj_fn = 0
        best_params = None

        def objective(params: np.ndarray) -> float:
            @qml.qnode(qml.device("lightning.qubit", wires=self.all_wires))
            def probs_circuit(params):
                self.problem_circuit(params)
                return qml.probs()
            probs = probs_circuit(params)
            prob_opt = np.sum([probs[int(s+'0'*(len(self.flag_wires)), 2)] for s in self.optimal_x])
            return -1 * prob_opt

        start = time.time()
        for restart in range(self.num_restarts):
            # In case we know a good starting point
            if self.starting_angles_from_qaoa is not None:
                init_angles = self.starting_angles_from_qaoa
                # reshape angle to match multi-angle QAOA
            else:
                if self.angle_strategy == "ma-QAOA":
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, self.n_layers*(self.num_gamma + self.num_beta), requires_grad=True).reshape(self.n_layers, self.num_gamma + self.num_beta)
                else:
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, 2*self.n_layers, requires_grad=True).reshape(self.n_layers, 2)

            angles = init_angles
            new_cost = objective(angles)

            for i in range(self.steps):
                angles, prev_cost = opt.step_and_cost(objective, angles)
                new_cost = objective(angles)
                conv_prev = np.abs(new_cost - prev_cost)

                # if the difference between the previous cost and the current cost is less than the convergence tolerance
                if conv_prev <= conv_tol:
                    break

            if new_cost < best_obj_fn:
                best_obj_fn = new_cost
                best_params = angles

        end = time.time()
        total_time = end - start
        self.optimize_time = total_time
        self.opt_angles = best_params
        print(best_params)
        return -1*best_obj_fn, best_params

    def __error_check_angle_strategy(self, angle_strategy: str) -> str:
        """
        Checks if the provided angle strategy is valid.

        Args:
            angle_strategy(str): The angle strategy to check.

        Returns:
            str: The valid angle strategy.

        Raises:
            ValueError: If the angle strategy is not 'QAOA' or 'ma-QAOA'.
        """
        if angle_strategy in ["QAOA", "ma-QAOA"]:
            return angle_strategy
        else:
            raise ValueError("Angle strategy must be either 'QAOA' or 'ma-QAOA'.")

    def __error_check_mixer(self, mixer: str) -> str:
        """
        Checks if the provided mixer is valid.

        Args:
            mixer(str): The mixer to check.

        Returns:
            str: The valid mixer.

        Raises:
            ValueError: If the mixer is not 'Grover' or 'X-Mixer'.
        """
        if mixer in ["Grover", "X-Mixer"]:
            return mixer
        else:
            raise ValueError("Mixer must be either 'Grover' or 'X-Mixer'.")

    def get_circuit_resources(self, opt: bool = False) -> qml.resource.Resources:
        """
        Returns the gate count of the quantum circuit.
        Args:
            opt (bool): Whether to use the optimal angles or random angles.
        Returns:
            qml.resource.Resources: The gate count of the quantum circuit.
        """
        @qml.qnode(qml.device("default.qubit"))
        def qubo_cost_fn():
            if opt:
                self.opt_circuit()
            else:
                if self.angle_strategy == "ma-QAOA":
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, self.n_layers*(self.num_gamma + self.num_beta), requires_grad=True).reshape(self.n_layers, self.num_gamma + self.num_beta)
                else:
                    init_angles = np.random.uniform(-2*np.pi, 2*np.pi, 2*self.n_layers, requires_grad=True).reshape(self.n_layers, 2)
                self.problem_circuit(init_angles)
            return qml.state()

        gate_resources = None
        coeffs, ops = self.problem_Ham.terms()
        est_shots = qml.resource.estimate_shots(coeffs)
        est_error = qml.resource.estimate_error(coeffs)
        group_ops, group_coeffs = qml.pauli.group_observables(ops, coeffs)
        group_shots = qml.resource.estimate_shots(group_coeffs)
        group_error = qml.resource.estimate_error(group_coeffs)
        return gate_resources, est_shots, est_error, group_shots, group_error

    def __get_num_gamma(self) -> int:
        """
        Returns the number of gamma parameters needed for the QAOA circuit.
        Returns:
            int: The number of gamma parameters needed for the QAOA circuit.
        """
        num_gamma = len(self.problem_Ham.ops)  # - 1
        num_gamma = num_gamma - len(self.flag_wires)
        if self.overlap_vars is not None:
            num_gamma -= len(self.overlap_vars)
        return num_gamma
```

## File: run_single_constraint.py
```python
import pennylane as qml
from pennylane import numpy as np
import pandas as pd
#import constraint_qaoa_server as cq
import constraint_qaoa as cq
import problem_qaoa as pq
import make_data as data
import argparse
import warnings
warnings.filterwarnings('ignore')

#|%%--%%| <35nAGOsdcG|bERad0UHYE>
r"""°°°
Functions to collect data from ConstraintQAOA and ProblemQAOA instances after optimization.
°°°"""
#|%%--%%| <bERad0UHYE|XS2msgKae8>


def collect_cqaoa_data(cqaoa: cq.ConstraintQAOA, combined: bool = False, single_flag: bool = False, decompose: bool = True) -> dict:
    """Collect data from a ConstraintQAOA instance after optimization.
    Args:
        cqaoa (cq.ConstraintQAOA): An instance of the ConstraintQAOA class.
        combined (bool, optional): Whether constraints were combined. Defaults to False.
        single_flag (bool, optional): Whether a single flag qubit was used. Defaults to False.
        decompose (bool, optional): Whether the Hamiltonian was decomposed. Defaults to True.
    Returns:
        dict: A dictionary containing various metrics and results from the CQAOA instance.
    """
    C_max = max(qml.eigvals(cqaoa.constraint_Ham))
    C_min = min(qml.eigvals(cqaoa.constraint_Ham))
    opt_cost, opt_angles = cqaoa.optimize_angles(cqaoa.do_evolution_circuit)
    resources, est_shots, est_error, group_est_shots, group_est_error = cqaoa.get_circuit_resources()
    counts = cqaoa.do_counts_circuit(shots=est_shots)
    cqaoa_dataset = {
        'constraints': [cqaoa.constraints],
        'n_x': [cqaoa.n_x],
        'n_c': [len(cqaoa.constraints)],
        'combined': [combined],
        'single_flag': [single_flag],
        'decompose': [decompose],
        'Hamiltonian': [cqaoa.constraint_Ham],
        'outcomes': [cqaoa.outcomes],
        'angle_strategy': [cqaoa.angle_strategy],
        'n_layers': [cqaoa.n_layers],
        'num_gamma': [cqaoa.num_gamma],
        'num_beta': [cqaoa.num_beta],
        'opt_angles': [opt_angles.tolist()],
        'opt_cost': [opt_cost],
        'counts': [counts],
        'resources': [resources],
        'est_shots': [est_shots],
        'est_error': [est_error],
        'group_est_shots': [group_est_shots],
        'group_est_error': [group_est_error],
        'hamiltonian_time': [cqaoa.hamiltonian_time],
        'optimize_time': [cqaoa.optimize_time],
        'counts_time': [cqaoa.count_time],
        'C_max': [C_max],
        'C_min': [C_min],
        'AR': [(opt_cost-C_max)/(C_min-C_max)],
    }
    return cqaoa_dataset


def collect_pqaoa_data(constraints: list, pqaoa: pq.ProblemQAOA, qubo_string: str, combined=False, overlap=False, single_flag=False, decompose=True, previous_angles=None, min_val=None) -> dict:
    """
    Collect data from a ProblemQAOA instance after optimization.
    Args:
        constraints (list): List of constraint strings used in the problem.
        pqaoa (pq.ProblemQAOA): An instance of the ProblemQAOA class.
        qubo_string (str): String representation of the QUBO used in the problem.
        combined (bool, optional): Whether constraints were combined. Defaults to False.
        overlap (bool, optional): Whether overlapping variables were used. Defaults to False.
        single_flag (bool, optional): Whether a single flag qubit was used. Defaults to False.
        decompose (bool, optional): Whether the Hamiltonian was decomposed. Defaults to True.
        previous_angles (np.ndarray, optional): Optimal angles from the previous layer for warm-starting. Defaults to None.
        min_val (float, optional): Minimum value of the objective function for feasible solutions. Defaults to None.
    Returns:
        dict: A dictionary containing various metrics and results from the PQAOA instance.
    """
    C_max = max(qml.eigvals(pqaoa.problem_Ham))
    C_min = min(qml.eigvals(pqaoa.problem_Ham))
    if pqaoa.n_layers == 1:
        opt_cost, opt_angles = pqaoa.optimize_angles(pqaoa.do_evolution_circuit)
    else:
        opt_cost, opt_angles = pqaoa.optimize_angles(pqaoa.do_evolution_circuit, prev_layer_angles=previous_angles)
    resources, est_shots, est_error, group_est_shots, group_est_error = pqaoa.get_circuit_resources()
    counts = pqaoa.do_counts_circuit(shots=10000)
    pqaoa_dataset = {
        'qubo_string': [qubo_string],
        'constraints': [constraints],
        'n_x': [pqaoa.n_x],
        'n_c': [constraints],
        'combined': [combined],
        'constraint_penalty': [pqaoa.penalty],
        'overlap': [overlap],
        'overlap_vars': [pqaoa.overlap_vars],
        'overlap_penalty': [pqaoa.overlap_penalty],
        'single_flag': [single_flag],
        'decompose': [decompose],
        'Hamiltonian': [pqaoa.problem_Ham],
        'outcomes': [None],
        'angle_strategy': [pqaoa.angle_strategy],
        'n_layers': [pqaoa.n_layers],
        'num_gamma': [pqaoa.num_gamma],
        'num_beta': [pqaoa.num_beta],
        'opt_angles': [opt_angles.tolist()],
        'opt_cost': [opt_cost],
        'counts': [counts],
        'resources': [resources],
        'est_shots': [est_shots],
        'est_error': [est_error],
        'group_est_shots': [group_est_shots],
        'group_est_error': [group_est_error],
        'hamiltonian_time': [pqaoa.hamiltonian_time],
        'optimize_time': [pqaoa.optimize_time],
        'counts_time': [pqaoa.count_time],
        'C_max': [C_max],
        'C_min': [C_min],
        'min_val': [min_val],
        'AR': [(opt_cost-C_max)/(min_val-C_max)],
        'optimal_x': [pqaoa.optimal_x],
    }
    return pqaoa_dataset


#|%%--%%| <XS2msgKae8|uK2BmHTCtH>
r"""°°°
Functions to run ConstraintQAOA and ProblemQAOA for a range of constraints and collect results.
°°°"""
#|%%--%%| <uK2BmHTCtH|ZROy2CM4Gt>


def run_cqaoa(max_n: int, op: str, result_dir='./alex/results/', result_file='single_constraint', combined=False, single_flag=False, decompose=True) -> None:
    r"""
    Run ConstraintQAOA for constraints of the form $\sum_{i=1}^n x_i \; op \; b$ for n in [1, max_n] and b in [0, n].
    Then writes results to pickle file.
    Args:
        max_n (int): Maximum number of variables in the constraint.
        op (str): Operator for the constraint ('==', '>=', '<=', '<', '>').
        result_dir (str, optional): Directory to save results. Defaults to './results/'.
        result_file (str, optional): Filename for saving results. Defaults to 'single_constraint'.
        combined (bool, optional): Whether to combine constraints. Defaults to False.
        single_flag (bool, optional): Whether to use a single flag qubit. Defaults to False.
        decompose (bool, optional): Whether to decompose the Hamiltonian. Defaults to True.
    Returns:
        None
    """
    df = pd.DataFrame(columns=['constraints', 'n_x', 'n_c', 'single_flag', 'decompose', 'outcomes', 'Hamiltonian', 'angle_strategy', 'n_layers', 'num_gamma', 'num_beta', 'opt_angles', 'opt_cost', 'counts', 'resources', 'est_shots', 'est_error', 'group_est_shots', 'group_est_error', 'optimize_time', 'table_time', 'hamiltonian_time', 'counts_time'])
    df.to_pickle(f'{result_dir}{result_file}.pkl')

    angle_strats = ['QAOA', 'ma-QAOA']
    for n in range(1, max_n+1):
        for b in range(n+1):
            constraint = data.make_single_constraint(n, op, b)
            for angsty in angle_strats:
                cqaoa = cq.ConstraintQAOA(
                    constraints=[constraint],
                    flag_wires=[n],
                    angle_strategy=angsty,
                    n_layers=1,
                    pre_made=False,
                    path=f'{result_dir}{result_file}.pkl',
                )

                cqaoa_dataset = collect_cqaoa_data(cqaoa, combined=combined, single_flag=single_flag, decompose=decompose)
                df = pd.concat([df, pd.DataFrame(cqaoa_dataset)], ignore_index=True)
                df.to_pickle(f'{result_dir}{result_file}.pkl')


def run_pqaoa(max_n: int, op: str, result_dir='./alex/results/', result_file='qubo_single_constraint', n_layers=1, combined=False, overlap=False, single_flag=False, decompose=True, constraint_result_file='single_constraint') -> None:
    r"""
    Run ProblemQAOA for QUBOs with constraints of the form $\sum_{i=1}^n x_i \; op \; b$ for n in [1, max_n] and b in [0, n].
    Then writes results to pickle file.
    Args:
        max_n (int): Maximum number of variables in the constraint.
        op (str): Operator for the constraint ('==', '>=', '<=', '<', '>').
        result_dir (str, optional): Directory to save results. Defaults to './results/'.
        result_file (str, optional): Filename for saving results. Defaults to 'qubo_single_constraint'.
        n_layers (int, optional): Number of QAOA layers. Defaults to 1.
        combined (bool, optional): Whether to combine constraints. Defaults to False.
        overlap (bool, optional): Whether to use overlapping variables. Defaults to False.
        single_flag (bool, optional): Whether to use a single flag qubit. Defaults to False.
        decompose (bool, optional): Whether to decompose the Hamiltonian. Defaults to True.
        constraint_result_file (str, optional): Filename of the constraint results to use. Defaults to 'single_constraint'.
    Returns:
        None
    """
    df = pd.DataFrame(columns=['qubo_string', 'constraints', 'n_x', 'n_c', 'combined', 'constraint_penalty', 'overlap', 'overlap_vars', 'overlap_penalty', 'single_flag', 'decompose', 'outcomes', 'Hamiltonian', 'angle_strategy', 'n_layers', 'num_gamma', 'num_beta', 'opt_angles', 'opt_cost', 'counts', 'resources', 'est_shots', 'est_error', 'group_est_shots', 'group_est_error', 'optimize_time', 'hamiltonian_time', 'counts_time', 'C_max', 'C_min', 'AR'])
    df.to_pickle(f'{result_dir}{result_file}.pkl')

    qubos = data.read_qubos_from_file('qubos.csv', results_dir=result_dir)

    qubo_opt_x = {}
    angle_strats = ['ma-QAOA']
    for p in range(1, n_layers+1):
        for n in range(1, max_n+1):
            for b in range(n+1):
                constraint = data.make_single_constraint(n, op, b)
                for q in qubos[n]:
                    min_val, optimal_x, total_min = data.get_optimal_x(qubos[n][q]['Q'], [constraint])
                    qubo_opt_x[(qubos[n][q]['qubo_string'], str(constraint))] = optimal_x
                    for angsty in angle_strats:
                        cqaoa = cq.ConstraintQAOA(
                            constraints=[constraint],
                            flag_wires=[n],
                            angle_strategy=angsty,
                            n_layers=1,
                            pre_made=True,
                            path=f'{result_dir}{constraint_result_file}.pkl',
                        )
                        pqaoa = pq.ProblemQAOA(
                            qubo=qubos[n][q]['Q'],
                            state_prep=[cqaoa],  # [cqaoa],
                            angle_strategy="ma-QAOA",
                            mixer="Grover",
                            penalty=[5+2 * np.abs(total_min)],
                            n_layers=p,
                            samples=10000,
                            learning_rate=0.01,
                            steps=100,
                            num_restarts=10,
                        )
                        pqaoa.optimal_x = optimal_x
                        if p == 1:
                            previous_angles = None
                        else:
                            previous_angles = np.array(df[(df['n_layers'] == p-1) & (df['qubo_string'] == qubos[n][q]['qubo_string']) & (df['constraints'].map(tuple) == tuple(constraint))]['opt_angles'].values[0])

                        pqaoa_dataset = collect_pqaoa_data(constraint, pqaoa, qubos[n][q]['qubo_string'], combined=False, overlap=False, single_flag=single_flag, decompose=decompose, previous_angles=previous_angles, min_val=min_val)
                        df = pd.concat([df, pd.DataFrame(pqaoa_dataset)], ignore_index=True)
                        df.to_pickle(f'{result_dir}{result_file}.pkl')


#|%%--%%| <ZROy2CM4Gt|IQyqOAodvj>
r"""°°°
Run either the constraint gadget creation or the QCBO problem solving based on command line arguments.
°°°"""
#|%%--%%| <IQyqOAodvj|31MMWsyyX4>


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the server code.')
    parser.add_argument('--max_n', type=int, default=5, help='Maximum number of variables')
    parser.add_argument('--op', type=str, default='equals', help='Operator for the constraint')
    parser.add_argument('--results_dir', type=str, default='./alex/results/', help='Directory to save results')
    parser.add_argument('--corp', type=str, default='constraint', help='Whether to make the constraint gadget or solve the qcbo problem')
    parser.add_argument('--n_layers', type=int, default=1, help='Number of layers for QAOA')
    args = parser.parse_args()
    ops = {'equals': '==', 'geq': '>=', 'leq': '<=', 'less': '<', 'greater': '>'}

    if args.corp == 'constraint':
        run_cqaoa(args.max_n, ops[args.op], result_dir='./alex/results/', result_file=f'single_constraint_{args.op}')
    elif args.corp == 'problem':
        run_pqaoa(args.max_n, ops[args.op], result_dir='./alex/results/', result_file=f'qubo_single_constraint_{args.op}_{args.n_layers}', n_layers=args.n_layers, combined=False, overlap=False, single_flag=False, decompose=True, constraint_result_file=f'single_constraint_{args.op}')
    else:
        raise ValueError('Invalid value for --corp. Must be "constraint" or "problem".')
```

## File: run_two_constraint.py
```python
import pennylane as qml
from pennylane import numpy as np
import pandas as pd
#import constraint_qaoa_server as cq
import constraint_qaoa as cq
import problem_qaoa as pq
import make_data as data
import argparse
import warnings
warnings.filterwarnings('ignore')


#|%%--%%| <wSV4bXABkH|AMcG012Cru>
r"""°°°
Functions to collect data from ConstraintQAOA and ProblemQAOA instances after optimization.
°°°"""
#|%%--%%| <AMcG012Cru|vvC4czw1MY>


def collect_cqaoa_data(cqaoa: cq.ConstraintQAOA, combined: bool = False, single_flag: bool = False, decompose: bool = True) -> dict:
    """
    Collect data from a ConstraintQAOA instance after optimization.
    Args:
        cqaoa (cq.ConstraintQAOA): An instance of the ConstraintQAOA class.
        combined (bool, optional): Whether to use combined constraints. Defaults to False.
        single_flag (bool, optional): Whether to use a single flag qubit. Defaults to False.
        decompose (bool, optional): Whether to decompose multi-qubit gates. Defaults to True.
    Returns:
        dict: A dictionary containing various metrics and results from the CQAOA instance.
    """
    C_max = max(qml.eigvals(cqaoa.constraint_Ham))
    C_min = min(qml.eigvals(cqaoa.constraint_Ham))
    opt_cost, opt_angles = cqaoa.optimize_angles(cqaoa.do_evolution_circuit)
    resources, est_shots, est_error, group_est_shots, group_est_error = cqaoa.get_circuit_resources()
    counts = cqaoa.do_counts_circuit(shots=est_shots)
    cqaoa_dataset = {
        'constraints': [cqaoa.constraints],
        'n_x': [cqaoa.n_x],
        'n_c': [2],
        'combined': [combined],
        'single_flag': [single_flag],
        'decompose': [decompose],
        'Hamiltonian': [cqaoa.constraint_Ham],
        'outcomes': [cqaoa.outcomes],
        'angle_strategy': [cqaoa.angle_strategy],
        'n_layers': [cqaoa.n_layers],
        'num_gamma': [cqaoa.num_gamma],
        'num_beta': [cqaoa.num_beta],
        'opt_angles': [opt_angles.tolist()],
        'opt_cost': [opt_cost],
        'counts': [counts],
        'resources': [resources],
        'est_shots': [est_shots],
        'est_error': [est_error],
        'group_est_shots': [group_est_shots],
        'group_est_error': [group_est_error],
        'hamiltonian_time': [cqaoa.hamiltonian_time],
        'optimize_time': [cqaoa.optimize_time],
        'counts_time': [cqaoa.count_time],
        'C_max': [C_max],
        'C_min': [C_min],
        'AR': [(opt_cost-C_max)/(C_min-C_max)],
    }
    return cqaoa_dataset


def collect_pqaoa_data(pqaoa: pq.ProblemQAOA, qubo_string: str, cqaoa: cq.ConstraintQAOA, min_val: float, combined: bool = False, overlap: bool = False, single_flag: bool = False, decompose: bool = True, support: int = 1) -> dict:
    """
    Collect data from a ProblemQAOA instance after optimization.
    Args:
        pqaoa (pq.ProblemQAOA): An instance of the ProblemQAOA class.
        qubo_string (str): String representation of the QUBO matrix.
        cqaoa (cq.ConstraintQAOA): The corresponding ConstraintQAOA instance used for state preparation.
        min_val (float): Minimum value of the objective function for feasible solutions.
        combined (bool, optional): Whether to use combined constraints. Defaults to False.
        overlap (bool, optional): Whether to use overlapping variables in constraints. Defaults to False.
        single_flag (bool, optional): Whether to use a single flag qubit. Defaults to False.
        decompose (bool, optional): Whether to decompose multi-qubit gates. Defaults to True.
        support (int, optional): Support of the constraints (1, 2, or 3). Defaults to 1.
    Returns:
        dict: A dictionary containing various metrics and results from the PQAOA instance.
    """
    C_max = max(qml.eigvals(pqaoa.problem_Ham))
    C_min = min(qml.eigvals(pqaoa.problem_Ham))

    if pqaoa.n_layers == 1:
        opt_cost, opt_angles = pqaoa.optimize_angles(pqaoa.do_evolution_circuit)
    elif pqaoa.n_layers == 2:
        previous_df = pd.read_pickle(f'alex/results/qubo_two_constraint_support_{support}_single_{single_flag}.pkl')
        previous_angles = np.array(previous_df[(previous_df['qubo_string'] == qubo_string) & (previous_df['constraints'].map(tuple) == tuple(cqaoa.constraints)) & (previous_df['angle_strategy'] == cqaoa.angle_strategy)]['opt_angles'].values[0])
        opt_cost, opt_angles = pqaoa.optimize_angles(pqaoa.do_evolution_circuit, prev_layer_angles=previous_angles)
    else:
        previous_df = pd.read_pickle(f'alex/results/qubo_two_constraint_support_{support}_single_{single_flag}_n_layers_{pqaoa.n_layers-1}.pkl')
        previous_angles = np.array(previous_df[(previous_df['qubo_string'] == qubo_string) & (previous_df['constraints'].map(tuple) == tuple(cqaoa.constraints)) & (previous_df['angle_strategy'] == cqaoa.angle_strategy)]['opt_angles'].values[0])
        opt_cost, opt_angles = pqaoa.optimize_angles(pqaoa.do_evolution_circuit, prev_layer_angles=previous_angles)

    opt_cost, opt_angles = pqaoa.optimize_angles(pqaoa.do_evolution_circuit)
    resources, est_shots, est_error, group_est_shots, group_est_error = pqaoa.get_circuit_resources()
    counts = pqaoa.do_counts_circuit(shots=10000)
    pqaoa_dataset = {
        'qubo_string': [qubo_string],
        'constraints': [cqaoa.constraints],
        'n_x': [pqaoa.n_x],
        'n_c': [2],
        'combined': [combined],
        'constraint_penalty': [pqaoa.penalty],
        'overlap': [overlap],
        'overlap_vars': [pqaoa.overlap_vars],
        'overlap_penalty': [pqaoa.overlap_penalty],
        'single_flag': [single_flag],
        'decompose': [decompose],
        'Hamiltonian': [pqaoa.problem_Ham],
        'outcomes': [cqaoa.outcomes],
        'angle_strategy': [cqaoa.angle_strategy],
        'n_layers': [pqaoa.n_layers],
        'num_gamma': [pqaoa.num_gamma],
        'num_beta': [pqaoa.num_beta],
        'opt_angles': [opt_angles.tolist()],
        'opt_cost': [opt_cost],
        'counts': [counts],
        'resources': [resources],
        'est_shots': [est_shots],
        'est_error': [est_error],
        'group_est_shots': [group_est_shots],
        'group_est_error': [group_est_error],
        'hamiltonian_time': [pqaoa.hamiltonian_time],
        'optimize_time': [pqaoa.optimize_time],
        'counts_time': [pqaoa.count_time],
        'C_max': [C_max],
        'C_min': [C_min],
        'min_val': [min_val],
        'AR': [(opt_cost-C_max)/(np.float64(min_val)-np.float64(C_max))],
        'optimal_x': [pqaoa.optimal_x],
    }
    return pqaoa_dataset


#|%%--%%| <vvC4czw1MY|QzKeZMU5aC>
r"""°°°
Functions to run ConstraintQAOA and ProblemQAOA for a range of constraints and collect results.
°°°"""
#|%%--%%| <QzKeZMU5aC|WNJGvQ0iTO>


def run_cqaoa(support: int, result_dir: str = 'alex/results/', result_file: str = 'two_constraint', combined: bool = False, single_flag: bool = False, decompose: bool = True) -> None:
    """
    Run ConstraintQAOA for a set of constraints and collect results.
    Args:
        support (int): Support of the constraints (1, 2, or 3).
        result_dir (str, optional): Directory to save results. Defaults to './results/'.
        result_file (str, optional): Filename to save results. Defaults to 'two_constraint'.
        combined (bool, optional): Whether to use combined constraints. Defaults to False.
        single_flag (bool, optional): Whether to use a single flag qubit. Defaults to False.
        decompose (bool, optional): Whether to decompose multi-qubit gates. Defaults to True.
    Returns:
        None
    """
    df = pd.DataFrame(columns=['constraints', 'n_x', 'n_c', 'single_flag', 'decompose', 'outcomes', 'Hamiltonian', 'angle_strategy', 'n_layers', 'num_gamma', 'num_beta', 'opt_angles', 'opt_cost', 'counts', 'resources', 'est_shots', 'est_error', 'group_est_shots', 'group_est_error', 'optimize_time', 'table_time', 'hamiltonian_time', 'counts_time'])
    df.to_pickle(f'{result_dir}{result_file}.pkl')

    if single_flag:
        flag_wires = [5]
    else:
        flag_wires = [5, 6]

    with open(f'{result_dir}two_constraints_support_{support}.txt', 'r') as f:
        constraints_list = f.readlines()
    angle_strats = ['QAOA', 'ma-QAOA']
    for constraint in constraints_list:
        for angsty in angle_strats:
            cqaoa = cq.ConstraintQAOA(
                constraints=eval(constraint),
                flag_wires=flag_wires,
                angle_strategy=angsty,
                n_layers=1,
                pre_made=False,
                single_flag=single_flag,
                path=f'{result_dir}{result_file}.pkl',
            )

            cqaoa_dataset = collect_cqaoa_data(cqaoa, combined=combined, single_flag=single_flag, decompose=decompose)
            df = pd.concat([df, pd.DataFrame(cqaoa_dataset)], ignore_index=True)
            df.to_pickle(f'{result_dir}{result_file}.pkl')


def run_pqaoa(support: int, result_dir: str = 'alex/results/', constraint_result_file: str = 'two_constraint', result_file: str = 'qubo_two_constraint', combined: bool = False, overlap: bool = False, single_flag: bool = False, decompose: bool = True, n_layers: int = 1) -> None:
    """
    Run ProblemQAOA for a set of QCBOs and constraints, using ConstraintQAOA for state preparation, and collect results.
    Args:
        support (int): Support of the constraints (1, 2, or 3).
        result_dir (str, optional): Directory to save results. Defaults to './results/'.
        constraint_result_file (str, optional): Filename of the ConstraintQAOA results. Defaults to 'two_constraint'.
        result_file (str, optional): Filename to save ProblemQAOA results. Defaults to 'qubo_two_constraint'.
        combined (bool, optional): Whether to use combined constraints. Defaults to False.
        overlap (bool, optional): Whether to use overlapping variables in constraints. Defaults to False.
        single_flag (bool, optional): Whether to use a single flag qubit. Defaults to False.
        decompose (bool, optional): Whether to decompose multi-qubit gates. Defaults to True.
        n_layers (int, optional): Number of layers for QAOA. Defaults to 1.
    Returns:
        None
    """
    df = pd.DataFrame(columns=['qubo_string', 'constraints', 'n_x', 'n_c', 'combined', 'constraint_penalty', 'overlap', 'overlap_vars', 'overlap_penalty', 'single_flag', 'decompose', 'outcomes', 'Hamiltonian', 'angle_strategy', 'n_layers', 'num_gamma', 'num_beta', 'opt_angles', 'opt_cost', 'counts', 'resources', 'est_shots', 'est_error', 'group_est_shots', 'group_est_error', 'optimize_time', 'hamiltonian_time', 'counts_time', 'C_max', 'C_min', 'AR'])
    df.to_pickle(f'{result_dir}{result_file}.pkl')

    qubos = data.read_qubos_from_file('qubos.csv', results_dir=result_dir)
    with open(f'{result_dir}two_constraints_support_{support}.txt', 'r') as f:
        constraints_list = f.readlines()

    if single_flag:
        flag_wires = [5]
    else:
        flag_wires = [5, 6]
    p = n_layers
    n = 5
    qubo_opt_x = {}
    angle_strats = ['ma-QAOA']
    for constraint in constraints_list:
        for q in qubos[n]:
            min_val, optimal_x, total_min = data.get_optimal_x(qubos[n][q]['Q'], eval(constraint))
            qubo_opt_x[(qubos[n][q]['qubo_string'], str(constraint))] = optimal_x
            for angsty in angle_strats:
                cqaoa = cq.ConstraintQAOA(
                    constraints=eval(constraint),
                    flag_wires=flag_wires,
                    angle_strategy=angsty,
                    n_layers=1,
                    single_flag=single_flag,
                    pre_made=True,
                    path=f'{result_dir}{constraint_result_file}.pkl',
                )
                pqaoa = pq.ProblemQAOA(
                    qubo=np.array(qubos[n][q]['Q'], requires_grad=False),
                    state_prep=[cqaoa],
                    angle_strategy="ma-QAOA",
                    mixer="Grover",
                    penalty=[5+2 * np.abs(total_min)],
                    n_layers=p,
                    samples=10000,
                    learning_rate=0.01,
                    steps=100,
                    num_restarts=10,
                )
                pqaoa.optimal_x = optimal_x

                pqaoa_dataset = collect_pqaoa_data(pqaoa, qubos[n][q]['qubo_string'], cqaoa, min_val, combined=combined, overlap=overlap, single_flag=single_flag, decompose=decompose, support=support)
                df = pd.concat([df, pd.DataFrame(pqaoa_dataset)], ignore_index=True)
                df.to_pickle(f'{result_dir}{result_file}.pkl')


#|%%--%%| <WNJGvQ0iTO|j9rbWJUvDw>
r"""°°°
Main function to run either CQAOA or PQAOA based on command line arguments.
°°°"""
#|%%--%%| <j9rbWJUvDw|N2OB3lvR24>

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the server code.')
    parser.add_argument('--results_dir', type=str, default='alex/results/', help='Directory to save results')
    parser.add_argument('--corp', type=str, default='constraint', help='Whether to make the constraint gadget or solve the qubo problem')
    parser.add_argument('--support', type=int, default=1, help='Support of the constraints (1, 2, or 3)')
    parser.add_argument('--single_flag', action='store_true', help='Use single flag qubit for constraints')
    parser.add_argument('--n_layers', type=int, default=1, help='Number of layers for QAOA')
    args = parser.parse_args()

    if args.corp == 'constraint':
        run_cqaoa(args.support, result_dir='alex/results/', result_file=f'two_constraint_support_{args.support}_single_{args.single_flag}', combined=False, single_flag=args.single_flag, decompose=True)
    elif args.corp == 'problem':
        run_pqaoa(args.support, result_dir='alex/results/', constraint_result_file=f'two_constraint_support_{args.support}_single_{args.single_flag}', result_file=f'qubo_two_constraint_support_{args.support}_single_{args.single_flag}_n_layers_{args.n_layers}', combined=False, overlap=False, single_flag=args.single_flag, decompose=True, n_layers=args.n_layers)
    else:
        raise ValueError('Invalid value for --corp. Must be "constraint" or "problem".')
```
