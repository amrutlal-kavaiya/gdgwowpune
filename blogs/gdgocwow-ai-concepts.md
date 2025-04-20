# GDG OC WOW Pune: Demystifying Modern AI Concepts

## Introduction

The Google Developer Group Organizing Committee Women of Wonders (GDG OC WOW) Pune recently hosted an insightful technical session on advanced AI concepts. This blog summarizes key topics discussed for those who couldn't attend.

## Key AI Concepts Explored

### Foundation Models & Context Windows

**Model Context:** The "memory" of AI models that allows them to maintain coherence across conversations. Modern models like GPT-4 and Claude 3 can handle 128K+ tokens of context.

**Tokens:** The basic units that AI models process text with—typically 4 characters in English, allowing models to understand language piece by piece.

### Embedding & Retrieval Systems

**Embeddings:** Dense vector representations of text that capture semantic meaning, enabling machines to understand similarities between concepts.

**VectorDB:** Specialized databases optimized for storing and querying vector embeddings, essential for efficient information retrieval.

**RAG (Retrieval-Augmented Generation):** A technique combining retrieval systems with generative AI to ground responses in accurate information.

### Sampling & Output Control

**Temperature:** A parameter controlling randomness in AI responses—higher values (0.7-1.0) increase creativity while lower values (0.1-0.3) enhance predictability.

**Top-K/Top-P:** Sampling methods that filter token probability distributions, with Top-K selecting from the K most likely tokens and Top-P (nucleus sampling) choosing from the smallest set of tokens whose cumulative probability exceeds P.

### System Architecture

**MCP (Model Context Protocol):** Framework standardizing how AI models handle context, enabling consistent behavior across different implementations.

**Host-Client-Server Model:** The infrastructure powering modern AI applications, where servers host the models, clients provide interfaces, and the host manages computation resources.

## Conclusion

Understanding these concepts is essential for anyone working with modern AI systems. The GDG OC WOW Pune continues to bridge knowledge gaps in emerging technologies, making complex concepts accessible to all.

*This blog was contributed to the GDG WOW Pune community repository as part of our commitment to knowledge sharing.*