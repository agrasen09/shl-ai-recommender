# SHL Conversational Assessment Recommender — Approach Document

## Overview

The system is a conversational AI-based recommendation engine that helps recruiters and hiring managers identify suitable SHL assessments through natural language interaction.

The solution supports:
- clarification handling
- conversational refinement
- recommendation generation
- assessment comparison
- off-topic refusal

## Architecture

The system uses:
- FastAPI backend
- Gemini AI for conversational generation
- Lightweight retrieval engine
- SHL catalog scraping pipeline

## Retrieval Strategy

The SHL catalog is scraped and stored as structured JSON data.

Recommendations are generated using:
- keyword relevance scoring
- contextual query matching
- conversational intent handling

This lightweight retrieval strategy was selected to reduce deployment memory usage while maintaining strong conversational behavior and recommendation relevance.

## Prompt Design

Gemini AI is used to:
- generate conversational responses
- explain recommendations
- maintain professional tone

The prompt includes:
- user hiring requirements
- retrieved assessment names
- conversational context

## Evaluation Approach

The system was tested for:
- vague queries
- clarification handling
- recommendation quality
- off-topic refusal
- conversational refinement
- comparison behavior

## Challenges & Improvements

Initial deployment using FAISS and SentenceTransformers exceeded Render memory limits.

The architecture was optimized using lightweight retrieval while retaining Gemini AI conversational capabilities.

This improved:
- deployment reliability
- response speed
- production stability