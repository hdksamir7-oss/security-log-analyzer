# 🛡️ Security Log Analyzer

A Python tool that analyzes SSH authentication logs to detect suspicious login attempts and potential brute-force attacks.

## Problem
Servers exposed to the internet are constantly targeted by automated login attempts. Manually reviewing logs to spot attack patterns is slow and error-prone.

## Solution
This script parses authentication log files, identifies failed login attempts, and flags IP addresses with repeated failures — a common sign of brute-force attacks.

## Features
- Parses SSH authentication logs
- Counts failed login attempts per IP address
- Flags suspicious IPs (2+ failed attempts)
- Simple, readable, dependency-free Python code

## Installation
`bash
git clone https://github.com/hdksamir7-oss/security-log-analyzer.git
cd security-log-analyzer
