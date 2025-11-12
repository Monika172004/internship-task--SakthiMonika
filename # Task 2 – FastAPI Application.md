# Task 2 – FastAPI Application

This project implements Task 2 of the internship assignment using **FastAPI**.

## Overview
The API exposes two endpoints:

### 1. POST `/api/price-gap-pair`
Uses the function from Task 1 to find a pair of indices `(i, j)` where  
`abs(nums[i] - nums[j]) == k`.

**Example request:**
```json
{"nums": [4, 1, 6, 3, 8], "k": 2}
