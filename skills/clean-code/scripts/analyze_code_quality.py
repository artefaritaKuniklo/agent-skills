#!/usr/bin/env python3
"""
Code Quality Analyzer - Detects common code smells and quality issues

This script analyzes Python code files and reports potential clean code violations
based on Robert C. Martin's "Clean Code" principles.

Usage:
    python analyze_code_quality.py <file_path>
    python analyze_code_quality.py <directory_path>

Example:
    python analyze_code_quality.py my_module.py
    python analyze_code_quality.py src/
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict


class CodeQualityAnalyzer:
    """Analyzes Python code for common quality issues and smells."""
    
    def __init__(self):
        self.issues = []
        self.file_path = None
        self.lines = []
    
    def analyze_file(self, file_path: str) -> List[Dict]:
        """Analyze a single Python file."""
        self.file_path = file_path
        self.issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.lines = f.readlines()
        except Exception as e:
            return [{"type": "ERROR", "message": f"Could not read file: {e}"}]
        
        self._check_line_length()
        self._check_function_length()
        self._check_magic_numbers()
        self._check_naming_conventions()
        self._check_function_parameters()
        self._check_too_many_returns()
        self._check_duplicate_code_patterns()
        
        return self.issues
    
    def _check_line_length(self):
        """Check for lines that are too long."""
        for line_num, line in enumerate(self.lines, 1):
            if len(line.rstrip()) > 120:
                self.issues.append({
                    "type": "FORMATTING",
                    "line": line_num,
                    "message": f"Line too long ({len(line.rstrip())} chars, max 120)",
                    "severity": "INFO"
                })
    
    def _check_function_length(self):
        """Check for functions that are too long."""
        current_function = None
        function_start = 0
        indent_level = 0
        in_function = False
        
        for line_num, line in enumerate(self.lines, 1):
            stripped = line.strip()
            
            if stripped.startswith('def ') or stripped.startswith('async def '):
                if in_function and current_function:
                    length = line_num - function_start
                    if length > 30:
                        self.issues.append({
                            "type": "FUNCTION_LENGTH",
                            "line": function_start,
                            "message": f"Function '{current_function}' is too long ({length} lines, max 30)",
                            "severity": "WARNING"
                        })
                
                match = re.match(r'(async\s+)?def\s+(\w+)', stripped)
                if match:
                    current_function = match.group(2)
                    function_start = line_num
                    in_function = True
    
    def _check_magic_numbers(self):
        """Check for magic numbers without explanation."""
        magic_number_pattern = r'\b\d+\b(?!["])'
        
        for line_num, line in enumerate(self.lines, 1):
            # Skip comments and strings
            if '#' in line:
                line = line[:line.index('#')]
            
            # Common false positives to skip
            if any(skip in line for skip in ['range(', 'sleep(', 'version', 'port']):
                continue
            
            matches = re.findall(magic_number_pattern, line)
            for match in matches:
                # Skip 0, 1, -1 as they're common
                if match not in ['0', '1', '-1', '2']:
                    self.issues.append({
                        "type": "MAGIC_NUMBER",
                        "line": line_num,
                        "message": f"Magic number '{match}' found. Consider extracting to named constant.",
                        "severity": "INFO"
                    })
                    break  # Report once per line
    
    def _check_naming_conventions(self):
        """Check for naming convention violations."""
        for line_num, line in enumerate(self.lines, 1):
            stripped = line.strip()
            
            # Check for SINGLE LETTER variable names (except in loops)
            if '=' in stripped and 'for ' not in stripped:
                var_match = re.search(r'\b([a-z])\s*=', stripped)
                if var_match and var_match.group(1) not in ['i', 'j', 'k', 'x', 'y', 'z']:
                    self.issues.append({
                        "type": "NAMING",
                        "line": line_num,
                        "message": f"Single-letter variable name '{var_match.group(1)}' is not descriptive",
                        "severity": "WARNING"
                    })
            
            # Check for Uppercase variable names (should be lowercase)
            var_match = re.search(r'\b([A-Z]{2,}[a-z])\s*=', stripped)
            if var_match and not stripped.startswith('class'):
                name = var_match.group(1)
                if name.isupper() or (name[0].isupper() and '_' not in name):
                    self.issues.append({
                        "type": "NAMING",
                        "line": line_num,
                        "message": f"Variable '{name}' should use snake_case",
                        "severity": "INFO"
                    })
    
    def _check_function_parameters(self):
        """Check for functions with too many parameters."""
        for line_num, line in enumerate(self.lines, 1):
            if 'def ' in line:
                # Extract parameters
                match = re.search(r'def\s+\w+\((.*?)\)', line)
                if match:
                    params = [p.strip().split('=')[0] for p in match.group(1).split(',')]
                    params = [p.strip() for p in params if p.strip() and p.strip() != 'self']
                    
                    if len(params) > 3:
                        self.issues.append({
                            "type": "FUNCTION_PARAMETERS",
                            "line": line_num,
                            "message": f"Function has {len(params)} parameters (max 3). Consider grouping in an object.",
                            "severity": "WARNING"
                        })
    
    def _check_too_many_returns(self):
        """Check for functions with too many return statements."""
        current_function = None
        function_line = 0
        indent_level = 0
        return_count = 0
        
        for line_num, line in enumerate(self.lines, 1):
            stripped = line.strip()
            
            if stripped.startswith('def '):
                if current_function and return_count > 3:
                    self.issues.append({
                        "type": "MULTIPLE_RETURNS",
                        "line": function_line,
                        "message": f"Function '{current_function}' has {return_count} return statements (max 1-2)",
                        "severity": "INFO"
                    })
                
                current_function = stripped.split('(')[0].replace('def ', '')
                function_line = line_num
                return_count = 0
                indent_level = len(line) - len(line.lstrip())
            
            elif current_function and stripped.startswith('return '):
                return_count += 1
    
    def _check_duplicate_code_patterns(self):
        """Check for potential duplicate code patterns."""
        # Simple heuristic: look for similar line patterns
        seen_patterns = {}
        
        for line_num, line in enumerate(self.lines, 1):
            stripped = line.strip()
            
            # Create a pattern by removing variable names
            pattern = re.sub(r'\w+', 'VAR', stripped)
            
            # Skip short lines and common patterns
            if len(stripped) < 30 or not pattern or '=' not in pattern:
                continue
            
            if pattern in seen_patterns:
                prev_line = seen_patterns[pattern]
                if line_num - prev_line > 3:  # Only report if not adjacent
                    self.issues.append({
                        "type": "DUPLICATE_PATTERN",
                        "line": line_num,
                        "message": f"Similar code pattern found. Consider extracting to shared function.",
                        "severity": "INFO"
                    })
            else:
                seen_patterns[pattern] = line_num


def analyze_directory(directory_path: str) -> Dict[str, List]:
    """Analyze all Python files in a directory."""
    analyzer = CodeQualityAnalyzer()
    results = {}
    
    for root, dirs, files in os.walk(directory_path):
        # Skip common directories
        dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'venv', '.venv']]
        
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                issues = analyzer.analyze_file(file_path)
                if issues:
                    results[file_path] = issues
    
    return results


def print_report(results: Dict[str, List]):
    """Print a formatted report of issues."""
    if not results:
        print("✅ No code quality issues found!")
        return
    
    total_issues = sum(len(issues) for issues in results.values())
    print(f"\n📋 Code Quality Report")
    print(f"{'=' * 60}")
    print(f"Total issues found: {total_issues}\n")
    
    for file_path, issues in results.items():
        print(f"📄 {file_path}")
        print(f"{'-' * 60}")
        
        for issue in issues:
            line = issue.get('line', 'N/A')
            severity = issue.get('severity', 'INFO')
            issue_type = issue.get('type', 'UNKNOWN')
            message = issue.get('message', '')
            
            icon = '⚠️' if severity == 'WARNING' else 'ℹ️'
            print(f"  {icon} Line {line}: [{issue_type}] {message}")
        
        print()


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python analyze_code_quality.py <file_or_directory>")
        print("Example: python analyze_code_quality.py my_module.py")
        print("         python analyze_code_quality.py src/")
        sys.exit(1)
    
    path = sys.argv[1]
    analyzer = CodeQualityAnalyzer()
    
    if os.path.isfile(path):
        issues = analyzer.analyze_file(path)
        results = {path: issues} if issues else {}
    elif os.path.isdir(path):
        results = analyze_directory(path)
    else:
        print(f"Error: Path '{path}' not found")
        sys.exit(1)
    
    print_report(results)
    
    # Exit with error code if issues found
    total_warnings = sum(1 for issues in results.values() 
                        for issue in issues if issue.get('severity') == 'WARNING')
    sys.exit(1 if total_warnings > 0 else 0)


if __name__ == "__main__":
    main()
